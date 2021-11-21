from Crypto.Cipher import AES
from base64 import b64decode
key = 'thisisatestkey=='.encode('utf-8')
aes = AES.new(key, AES.MODE_ECB)
test = b64decode('9YuQ2dk8CSaCe7DTAmaqAA==')
unpad = lambda date: date[0:-ord(date[-1])]
ans = aes.decrypt(test).decode("utf-8")
print(unpad(ans))
 
