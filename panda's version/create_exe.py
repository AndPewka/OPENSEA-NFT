import os

import shutil



print("Create exe")
os.remove("main.exe")
#os.remove("card_rates.txt")


os.system("pyinstaller --onefile main.py")

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'build')
shutil.rmtree(path)


path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '__pycache__')
shutil.rmtree(path)

os.replace("dist/main.exe","main.exe")
os.rmdir("dist")
os.remove("main.spec")


print("exe was done")

