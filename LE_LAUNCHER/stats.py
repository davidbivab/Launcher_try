import psutil
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}"
        bytes /= factor


def get_mem():
    svmem = psutil.virtual_memory()
    return round(float(get_size(svmem.total)))

