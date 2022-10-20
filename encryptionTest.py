from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64

password = input("Enter Password: ").encode()

salt = b"\x85Enz\xa1\xf2'\xe82\t\x04\x94\xd8~\x92u"
kdf = Scrypt(salt,32,2**14,8,1)

key = base64.urlsafe_b64encode(kdf.derive(password))

f = Fernet(key)

print("key: " + key.decode())

message = input("Enter Message: ").encode()
token = f.encrypt(message)

print("Saved encrypted prompt")

file = open("data.txt",'a')
file.write(token.decode() + "\n")
file.close()