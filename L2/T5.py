from _libs_ import *

pr = rsa.generate_private_key(public_exponent=65537, key_size=2048)
pb = pr.public_key()
    
msg = b"some important message"

#encrypt pb
ciphertext = pb.encrypt(
    msg,
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
#decrypt pr
plaintext = pr.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

os.system("cls")
print("ciphertext: ", ciphertext[0:20], "...")
print("plaintext:  ", plaintext) 