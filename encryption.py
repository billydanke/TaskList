from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64

def passwordAuthenticate(password):
    password = str(password).encode()

    salt = b"\x85Enz\xa1\xf2'\xe82\t\x04\x94\xd8~\x92u"
    checkToken = b'gAAAAABjUK6IUWF12KE73vxDwBlcgrM1YfFcTNQrZntzZUy8lY6jGB4QtlY-UfanzxlOo2YEFDeaNKvkOznGAZBuXI8Kht_Psw=='

    kdf = Scrypt(salt,32,2**14,8,1)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)

    checkSource = None
    try:
        checkSource = f.decrypt(checkToken)
    except:
        pass
    
    if(password == checkSource):
        return True
    else:
        return False