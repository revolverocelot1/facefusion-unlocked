import os
os.chdir(f"/home/xlab-app-center")
os.system(f"git clone -b https://github.com/spliffm/facefusion-nsfw /home/xlab-app-center/facefusion-nsfw")
os.chdir(f"/home/xlab-app-center/facefusion-nsfw")
os.system(f"git lfs install")
os.system(f"git pull")
os.system(f"git reset --hard")
