from _libs_ import *

msg = b"some important message"
chang = b"some NOT important message"

scrt_key = b"super_secret_key"

#create hmac
hmac1 = hmac.new(scrt_key, msg, hashlib.sha256).hexdigest()
hmac2 = hmac.new(scrt_key, chang, hashlib.sha256).hexdigest()

os.system("cls")
print(f"hmac1 : {hmac1}")
print("hmac2 :", hmac2) 
