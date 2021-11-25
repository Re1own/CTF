from Crypto.Cipher import AES
import base64
import zlib

def decode(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decryptByts = base64.b64decode(data)
    msg = cipher.decrypt(decryptByts)
    msgstr = str(msg, encoding="utf-8")
    paddingLen = ord(msgstr[len(msgstr)-1])
    return msgstr[0: len(msgstr) - paddingLen]
endata = open('misc2.png', 'rb').read()
pngdata = b''
for m in range(0, len(endata), 16):
    pngdata += endata[m:m + 16][::-1]
open('tmp.png', 'wb').write(pngdata)
