import os 
import shutil
import sys

current_dir= os.path.abspath(os.path.dirname(__file__))
print(os.path.join(os.path.join(current_dir,"extensions"),"prompt-gallery"), os.path.join(sys.argv[1],"extensions"))
print(os.path.join(current_dir,"scripts"), os.path.join(sys.argv[1],"scripts"))
shutil.copytree(os.path.join(os.path.join(current_dir,"extensions"),"prompt-gallery"), os.path.join(os.path.join(sys.argv[1],"extensions"),"prompt-gallery"))
shutil.copy(os.path.join(os.path.join(current_dir,"scripts"),"prompt_gallery.py"), os.path.join(sys.argv[1],"scripts"))