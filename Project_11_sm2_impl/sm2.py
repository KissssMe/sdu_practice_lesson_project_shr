import random
import hashlib
import binascii

# sm2的一些参数
p = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF
a = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC
b = 0x28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93
Gx = 0x32C4AE2C1F1981195F9904466A39C9948FE30BBFF2660BE1715A4589334C74C7
Gy = 0xBC3736A2F4F6779C59BDCEE36B692153D0A9877CC62A474002DF32E52139F0A0
n = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123

# 转换为大整数
G = (Gx, Gy)
a, b = a % p, b % p

def ec_double(x1, y1):
    lam = (3 * x1 * x1 + a) * invert(2 * y1, p) % p
    x3 = (lam * lam - 2 * x1) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def ec_add(x1, y1, x2, y2):
    lam = (y2 - y1) * invert(x2 - x1, p) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

def invert(x, p):  # modular inverse
    return pow(x, p - 2, p)

def ec_multiply(g, n):  # 模运算，点运算
    if n == 0:
        return (0, 0)
    elif n == 1:
        return g
    else:
        Q = ec_double(*g)
        for i in range(n.bit_length() - 1, 0, -1):
            Q = ec_double(*Q)
            if n & (1 << i) != 0:
                Q = ec_add(*Q, *g)
        return Q

# 明文进行hash处理
def message_digest(message):
    return hashlib.sha256(message.encode()).hexdigest()

def sm2_encrypt(message, key_on_curve):
    m = message_digest(message)
    k = random.randint(1, n - 1)
    C1 = ec_multiply(G, k)
    C2 = (int(m, 16) + key_on_curve[0] * k) % n
    return (C1, C2)

def sm2_decrypt(cipher, private_key):
    C1, C2 = cipher
    x, y = ec_multiply(C1, private_key)
    m = (C2 - x) % n
    return m

private_key = random.randint(1, n-1)
public_key = ec_multiply(G, private_key)
print("Public Key: ", public_key)
print("Private Key: ", private_key)
message = 'Hello, SM2'
cipher = sm2_encrypt(message, public_key)
print("Cipher: ", cipher)
m = sm2_decrypt(cipher, private_key)
print("Message: ", hex(m))