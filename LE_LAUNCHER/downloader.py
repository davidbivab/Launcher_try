import json
import shutil
import subprocess
import requests
from urllib import parse
from zipfile import ZipFile
import os
import minecraft_launcher_lib
import re

base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources?'
public_key = "https://disk.yandex.ru/d/NJd_3w5FmFfWmQ"
final_url = base_url + parse.urlencode(dict(public_key=public_key))
response = requests.get(final_url)
def modpack_download():
    with open("launcher_options.json") as json_file:
        version = json.load(json_file)['version']
    for i in dict.get(dict.get(response.json(), "_embedded"), "items"):
        if dict.get(i, 'name') == version:
            with open('MOD_PACK.zip', 'wb') as file:
                file.write(requests.get(dict.get(i, 'file')).content)


def get_jsons():
    for i in dict.get(dict.get(response.json(), "_embedded"), "items"):
        if dict.get(i, 'name') == "launcher_options.json":
            with open('launcher_options.json', 'wb') as file:
                file.write(requests.get(dict.get(i, 'file')).content)
    if not os.path.exists('client_options.json'):
        for i in dict.get(dict.get(response.json(), "_embedded"), "items"):
            if dict.get(i, 'name') == 'standart_client_options.json':
                with open('client_options.json', 'wb') as file:
                    file.write(requests.get(dict.get(i, 'file')).content)

def get_modpack_version():
    with open("launcher_options.json") as json_file:
        version = json.load(json_file)['version']
    return version


def mod_pack_get():
    with ZipFile('MOD_PACK.zip', 'r') as archive:
        if os.path.exists("minecraft/mods"):
            shutil.rmtree("minecraft/mods")
        archive.extractall(path='./minecraft')
def game_check():
    if not os.path.exists('minecraft'):
        with open("launcher_options.json") as json_file:
            mc_version = json.load(json_file)['minecraft_version']
            minecraft_launcher_lib.forge.install_forge_version(mc_version, './minecraft')
    else:
        dir_list = os.listdir("minecraft/versions")
        with open("launcher_options.json") as json_file:
            in_json = json.load(json_file)['minecraft_version']
            to_find = re.sub(r"([0-9]+\.[0-9]+)-", r"\1-forge-", in_json)
            for versions in dir_list:
                print(versions)
                if versions == to_find:
                    return True

def game_get():
    with open("launcher_options.json") as json_file:
        if game_check() != True:
            in_json = json.load(json_file)['minecraft_version']
            minecraft_launcher_lib.forge.install_forge_version(in_json, './minecraft')
    if not os.path.exists('minecraft'):

        with open("launcher_options.json") as json_file:
            mc_version = json.load(json_file)['minecraft_version']
            minecraft_launcher_lib.forge.install_forge_version(mc_version, './minecraft')
def game_start():
    with open("launcher_options.json") as json_file:
        mc_version = json.load(json_file)['minecraft_version']
        mc_forge_version = re.sub(r'(\d+\.\d+\.\d+)-', r'\1-forge-', mc_version)
    with open('client_options.json') as json_file:
        optionss = json.load(json_file)
    DETACHED_PROCESS = 0x00000008
    # , creationflags = DETACHED_PROCESS
    subprocess.run(minecraft_launcher_lib.command.get_minecraft_command(mc_forge_version, 'minecraft', optionss), creationflags = DETACHED_PROCESS)


get_jsons()
