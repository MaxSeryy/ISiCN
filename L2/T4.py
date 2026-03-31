from _libs_ import *

#AES
k = Fernet.generate_key()
cipher = Fernet(k)

msg = b"some important doc"

enc = cipher.encrypt(msg)

dec = cipher.decrypt(enc)

os.system("cls")
print("key :", k)
print("encrypted:", enc)
print("decrypted: ", dec)