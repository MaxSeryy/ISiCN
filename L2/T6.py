from _libs_ import *

hn = "example.com"
port = 443

context = ssl.create_default_context()
with socket.create_connection((hn, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hn) as ssock:

        os.system("cls")
        print(f"TLS version: {ssock.version()}")
        print(f"Subject: {ssock.getpeercert()['subject']}")
        print(f"Issuer: {ssock.getpeercert()['issuer']}")
        print(f"Valid from: {ssock.getpeercert()['notBefore']}")
        print(f"Valid to: {ssock.getpeercert()['notAfter']}") 