#molecon
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
import hashlib
import base64
import random
import os

steps = [2, ...]
steps.reverse()
ct = ' ... '
print(bytes.fromhex(ct))
ct = bytes.fromhex(ct)

def rot13(x: bytes) -> bytes:
    return x.translate(bytes.maketrans(
        bytes([i for i in range(256)]),
        bytes([(i - 13) % 256 for i in range(256)])
    ))


def RSA(x: bytes) -> bytes:
    e = 65537
    x = bytes_to_long(x)
    random.seed(bytes_to_long(b'ptm{'))
    p = getPrime(1024, randfunc=random.randbytes)
    q = getPrime(1024, randfunc=random.randbytes)
    N = p * q
    phi = (p-1)*(q-1)
    d = pow(e,-1,phi)
    m = pow(x,d,N)
    return m

possible_methods = [
    base64.b64decode,
    lambda x: x[::-1],
    RSA,
    rot13
]


flag = ct
for step in steps:
    flag = possible_methods[step](flag)

print(long_to_bytes(flag))
