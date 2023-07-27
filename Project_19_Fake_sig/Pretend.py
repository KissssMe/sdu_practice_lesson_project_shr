from ECDSA import *
import math
import random

def Check_Coprime(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def Calc_GCD(a, m):
    if Check_Coprime(a, m) != 1 and Check_Coprime(a, m) != -1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    if u1 > 0:
        return u1 % m
    else:
        return (u1 + m) % m

def Add_CurvePoints(m, n):
    if (m == 0):
        return n
    if (n == 0):
        return m
    res = []
    if (m != n):
        if (Check_Coprime(m[0] - n[0], p) != 1 and Check_Coprime(m[0] - n[0], p) != -1):
            return 0
        else:
            k = ((m[1] - n[1]) * Calc_GCD(m[0] - n[0], p)) % p
    else:
        k = ((3 * (m[0] ** 2) + a) * Calc_GCD(2 * m[1], p)) % p
    x = (k ** 2 - m[0] - n[0]) % p
    y = (k * (m[0] - x) - m[1]) % p
    res.append(x)
    res.append(y)
    return res

def Multiply_CurvePoints(n, l):
    if n == 0:
        return 0
    if n == 1:
        return l
    t = l
    while (n >= 2):
        t = Add_CurvePoints(t, l)
        n = n - 1
    return t

a = 2
b = 2
p = 17
msg = 'im Satoshi'
msg_1 = "i will pretend"
BasePoint = [5, 1]
element_in_group = 19
random_val = 2
k = 5
Public_Key = Multiply_CurvePoints(k, BasePoint)

def Sign_ECDSA(msg, element_in_group, BasePoint, k, random_val):
    e = hash(msg)
    Calculated_Point = Multiply_CurvePoints(random_val, BasePoint)
    r = Calculated_Point[0] % element_in_group
    s = (Calc_GCD(random_val, element_in_group) * (e + k * r)) % element_in_group
    return r, s

def ECDSA_Verification(msg, element_in_group, BasePoint, r, s, Public_Key):
    e = hash(msg)
    w = Calc_GCD(s, element_in_group)
    v1 = (e * w) % element_in_group
    v2 = (r * w) % element_in_group
    w = Add_CurvePoints(Multiply_CurvePoints(v1, BasePoint), Multiply_CurvePoints(v2, Public_Key))
    if (w == 0):
        print('Verification Failed')
        return False
    else:
        if (w[0] % element_in_group == r):
            print('Verification Successful')
            return True
        else:
            print('Verification Failed')
            return False

def Impersonation(r, s, element_in_group, BasePoint, Public_Key):
    u = random.randrange(1, element_in_group - 1)
    v = random.randrange(1, element_in_group - 1)
    r1 = Add_CurvePoints(Multiply_CurvePoints(u, BasePoint), Multiply_CurvePoints(v, Public_Key))[0]
    e1 = (r1 * u * Calc_GCD(v, element_in_group)) % element_in_group
    s1 = (r1 * Calc_GCD(v, element_in_group)) % element_in_group
    ECDSA_Verification(e1, element_in_group, BasePoint, r1, s1, Public_Key)


print("1. Testing sign and verify algorithm:")
r,s = Sign_ECDSA(msg, element_in_group, BasePoint, k, random_val)
print("Signature: ",r,s)
print("Verifying Signature:")
ECDSA_Verification(msg, element_in_group, BasePoint, r, s, Public_Key)

print("6. Testing Impersonation of Satoshi:")
print("Impersonation test result:")
Impersonation(r, s, element_in_group, BasePoint, Public_Key)
