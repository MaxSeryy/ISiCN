from _libs_ import *

passwd = b"idk"

#random salt
salt = os.urandom(16)
#add salt to pswd
sp = hashlib.sha256(salt + passwd).hexdigest()

salt2 = os.urandom(16)
sp2 = hashlib.sha256(salt2 + passwd).hexdigest()

os.system("cls")
print("salt1:        ", salt)
print("salted hash1: ", sp)
print("salt2:        ", salt2)
print("salted hash2: ", sp2) 