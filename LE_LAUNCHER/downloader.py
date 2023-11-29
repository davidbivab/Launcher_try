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


# download_url = response.json()['href']
#
# download_response = requests.get(download_url)
# # with open('downloaded_file.zip', 'wb') as f:
# #     f.write(download_response.content)
# print(json.dumps(response.json(),sort_keys=True,indent=4))
def modpack_download(version):
    for i in dict.get(dict.get(response.json(), "_embedded"), "items"):
        if dict.get(i, 'name') == version:
            with open('MOD_PACK.zip', 'wb') as file:
                file.write(requests.get(dict.get(i, 'file')).content)


def get_jsons():
    for i in dict.get(dict.get(response.json(), "_embedded"), "items"):
        if dict.get(i, 'name') == "launcher_options.json":
            with open('launcher_options.json', 'wb') as file:
                file.write(requests.get(dict.get(i, 'file')).content)
        if os.path.exists('client_options.json'):
            pass
        else:
            if dict.get(i, 'name') == 'standart_client_options.json':
                with open('client_options.json', 'wb') as file:
                    file.write(requests.get(dict.get(i, 'file')).content)


def get_modpack_version():
    #    for i in dict.get(dict.get(response.json(), "_embedded"), "items"):
    #        if dict.get(i, 'name') == "launcher_options.json":
    #            checkable_version = requests.get(dict.get(i, 'file')).json()['version']

    with open("launcher_options.json") as json_file:
        version = json.load(json_file)['version']
    return version


def mod_pack_get():
    modpack_download(get_modpack_version())
    with ZipFile('MOD_PACK.zip', 'r') as archive:
        for file in archive.namelist():
            match = re.findall(r'(\w+)\/', file)
            if match == []:
                continue
            if os.path.exists(f"minecraft/{match[0]}"):
                shutil.rmtree(f"minecraft/{match[0]}")
        archive.extractall(path='./minecraft')


def game_get():
    if not os.path.exists('minecraft'):
        with open("launcher_options.json") as json_file:
            mc_version = json.load(json_file)['minecraft_version']
            minecraft_launcher_lib.forge.install_forge_version(mc_version, './minecraft')
    else:
        pass


def game_start():
    with open("launcher_options.json") as json_file:
        mc_version = json.load(json_file)['minecraft_version']
        mc_forge_version = re.sub(r'(\d+\.\d+\.\d+)-', r'\1-forge-', mc_version)


    with open('client_options.json') as json_file:
        optionss = json.load(json_file)

    subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(mc_forge_version, 'minecraft', optionss))


get_jsons()
