#function for copying a lot of files

import os
import shutil

def copylott(src, dst):
    for i in os.listdir(src):
        shutil.copy2(src + i, dst)


source = ''
destination = ''
copylott(source, destination)
