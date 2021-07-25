# Like and subscribe!
# https://www.youtube.com/watch?v=-lefbawmaFk
import os
import hashlib
 
print("Kiolesis Studio Code | Developer Tools")
print("")
print("Hashowanie wartości w SHA256")
zmiennahash = input(":")
 
print(hashlib.sha256(zmiennahash.encode('utf-8')).hexdigest())
os.system("pause>>nul")
os.system("exit")
