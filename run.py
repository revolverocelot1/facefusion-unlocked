#!/usr/bin/env python3 only
import os
from facefusion import core
os.chdir(f"/home/xlab-app-center")
os.system(f"git clone -b https://github.com/revolverocelot1/facefusion-unlocked/tree/master /home/xlab-app-center/facefusion-unlocked")
os.chdir(f"/home/xlab-app-center/facefusion-unlocked")
os.system(f"git lfs install")
os.system(f"git pull")
os.system(f"git reset --hard")
# Path to the core.py file
file_path = '/home/xlab-app-center/facefusion-unlocked/facefusion/uis/layouts/default.py'

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Replace the line with the updated version
updated_content = content.replace("ui.launch(show_api = False)", "ui.launch(show_api = False, share=True, enable_queue=True)")

# Write the updated content back to the file
with open(file_path, 'w') as file:
    file.write(updated_content)
if __name__ == '__main__':
    core.run()
