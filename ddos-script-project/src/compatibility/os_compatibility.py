import platform

def get_os_compatibility():
    os_name = platform.system()

    if os_name == "Windows":
        return "Windows compatibility achieved."
    elif os_name == "Linux":
        return "Linux compatibility achieved."
    elif os_name == "Darwin":
        return "macOS compatibility achieved."
    else:
        return "Operating system not supported."

print(get_os_compatibility())