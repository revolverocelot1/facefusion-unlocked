#!/usr/bin/env python3 only
import os
from facefusion import core
# Path to the core.py file
file_path = '/home/xlab-app-center/facefusion/uis/layouts/default.py'

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
