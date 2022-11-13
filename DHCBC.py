from Crypto.Util.number import isPrime, bytes_to_long,long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from functools import reduce
import random
import os
import math
g = 2
p = 11926291779462340019
A = 4341348937901765624
B = 1490295258673393701
IV ='60abd7a2ce17b5573c4ae03e0901f6ee'
Message='3365b3ea715e187df147ef583f6d20a02e7ddbaf8009ddfc851fcfb971b50ec4dd9a2264cbff1ad8051944a129a74500a51a2bb71536b85f5a8eedfa49c8dfc042936740de6dfa3caf1a541f30789c040ff5ae2fbb0eb7cd7d07de29bd213ba8317a6933d7dd78558d04829a06073ca3cd9e5b594a643fa733c7bccc0d38310852fbf4d4ede7d564ac2dd97ab26240d63af26b97becc21540b4ff757f9c9132f552b82df5f1c3c267775f4cfb0be91f5c41ade30ce849f21720d52f8c6fe950a5a4729877291a6420d1b30b094cf815d55981608f67558c9da07cb6a25d6a9b8'
b= 7185406284652169511
shared_secret = int(pow(A,b,(p)))

print(long_to_bytes(shared_secret))
key = shared_secret.to_bytes(16,'little')
print(shared_secret)
print(key)
iv=bytes.fromhex(IV)
ct=bytes.fromhex(Message)
cipher = AES.new(key,AES.MODE_CBC,iv)
plaintext = cipher.decrypt(ct)
plaintext=(unpad(plaintext,AES.block_size))
print(plaintext)
