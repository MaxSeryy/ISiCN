from _libs_ import *

passwd = b"idk"

# hash obj
hash1 = hashlib.sha256(passwd).hexdigest()
os.system("cls")
print("hash1:", hash1)

chng = b"idk1"
hash2 = hashlib.sha256(chng).hexdigest()
print("hash2:", hash2) 