import shutil
import os
import stat

bashscript = 'bedrockupdate'
path = '/bedrock/bin/bedrockupdate'

def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 100) >> 2
    os.chmod(path, mode)

try:
    shutil.copy2(bashscript, path)
    make_executable(path)
    print("Installed bedrockupdate")
except PermissionError:
    print("ERROR, must run as root")
