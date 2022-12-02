import os 
import shutil
import json
import launch


if not launch.is_installed("pyyaml"):
    launch.run_pip("install pyyaml", "requirements for Prompt Gallery")

current_dir= os.path.abspath(os.path.dirname(__file__))
trg = os.path.join(os.path.join(os.path.join(current_dir, os.path.pardir), os.path.pardir), "scripts/prompt_gallery.py")
shutil.copyfile(os.path.join(os.path.join(current_dir,"paste_this_to_webui_scripts_folder"),"prompt_gallery.py"), trg)
name = os.path.basename(current_dir)
with open(os.path.join(current_dir, os.path.join(os.path.join(current_dir, os.path.pardir), "prompt_gallery_name.json")), 'w') as fd:
    json.dump({'name': name}, fd)
