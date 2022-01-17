from gen import *
from load import *
import os

username = os.environ.get("USERNAME")

mode = 0
print("""write mode:
1) gen cards
2) load cards
    """)
mode = int(input("write mode -->"))
os.system("cls")

if mode == 1:
    print("Gereration cards")
    gen()
elif mode == 2:
    print("Load cards")
    load()
else:
    print("Error! Choose wrong mode !")