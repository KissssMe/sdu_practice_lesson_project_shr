import random
import base64
from gmssl import sm3, func
from gmssl import sm2, sm4
from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
import math

p = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF
a = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC
b = 0x28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93
n = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123
x = 0x32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7
y = 0xBC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0

def epoint_mod(a, n):
    return float('inf') if math.isinf(a) else a % n

def epoint_modmult(a, b, n):
    if b == 0:
        result = float('inf')
    elif a == 0:
        result = 0
    else:
        t = bin(n - 2).replace('0b', '')
        y = 1
        i = 0
        while i < len(t):
            y = (y ** 2) % n
            if t[i] == '1':
                y = (y * b) % n
            i += 1
        result = (y * a) % n
    return result

def epoint_add(point_p, point_q, a_value, p_value):
    if math.isinf(point_p[0]) and ~math.isinf(point_q[0]):
        result_point = point_q
    elif ~math.isinf(point_p[0]) and math.isinf(point_q[0]):
        result_point = point_p
    elif math.isinf(point_p[0]) and math.isinf(point_q[0]):
        result_point = [float('inf'), float('inf')]
    else:
        if point_p != point_q:
            l = epoint_modmult(point_q[1] - point_p[1], point_q[0] - point_p[0], p_value)
        else:
            l = epoint_modmult(3 * point_p[0] ** 2 + a_value, 2 * point_p[1], p_value)
        X = epoint_mod(l ** 2 - point_p[0] - point_q[0], p_value)
        Y = epoint_mod(l * (point_p[0] - X) - point_p[1], p_value)
        result_point = [X, Y]
    return result_point

def epoint_mult(k_value, P, a_value, p_value):
    tmp = bin(k_value).replace('0b', '')
    l = len(tmp) - 1
    point_Z = P
    if l > 0:
        k_value = k_value - 2 ** l
        while l > 0:
            point_Z = epoint_add(point_Z, point_Z, a_value, p_value)
            l -= 1
        if k_value > 0:
            point_Z = epoint_add(point_Z, epoint_mult(k_value, P, a_value, p_value), a_value, p_value)
    return point_Z

def generate_key(a, p, n, G):
    value_d = random.randint(1, n - 2)
    created_k = epoint_mult(value_d, G, a, p)
    return value_d, created_k

def encrypt_msg(msg, key):
    lgth = 16
    n = len(msg)
    num = lgth - (n % lgth) if n % lgth != 0 else 0
    msg += ('\0' * num)
    msg = str.encode(msg)
    key = str.encode(key)
    print("Message：\n", base64.b16encode(msg))
    print("\nKey：\n", base64.b16encode(key))

    sm4_obj = CryptSM4()
    sm4_obj.set_key(key, SM4_ENCRYPT)
    encrypted_msg = sm4_obj.crypt_ecb(msg)

    encrypted_key = sm2_crypt.encrypt(key)
    print("\nEncrypted message：\n", base64.b16encode(encrypted_msg))
    print("\nEncrypted key：\n",base64.b16encode(encrypted_key))
    return encrypted_msg, encrypted_key

def decrypt_msg(encrypted_msg, encrypted_key):
    decrypted_key = sm2_crypt.decrypt(encrypted_key)
    sm4_obj = CryptSM4()
    sm4_obj.set_key(decrypted_key, SM4_DECRYPT)
    decrypted_msg = sm4_obj.crypt_ecb(encrypted_msg)

    print("\nDecrypted key：\n", base64.b16encode(decrypted_key))
    print("\nDecrypted message：\n", base64.b16encode(decrypted_msg))

if __name__ == '__main__':
    g = [x, y]
    d, k = generate_key(a, p, n, g)
    sk = hex(d)[2:]
    pk = hex(k[0])[2:] + hex(k[1])[2:]
    sm2_crypt = sm2.CryptSM2(public_key=pk, private_key=sk)
    msg = "Hello, I'm baekhunee!"
    key = hex(random.randint(2 ** 127, 2 ** 128))[2:]
    r1, r2 = encrypt_msg(msg, key)
    decrypt_msg(r1, r2)