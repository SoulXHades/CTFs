# Ref: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# Value of e used by the randomware
a = 0x10001
# ϕ(n). Change this
m = 0xcdfe7076154d4e876f3187d3cc97da8181a5daafc06c0ea90a6b574e1e8adadb57e82fd92254866b7f0736d78d5c01b3f92735c0a8415dbd17440ceaf86491e70318ec9fdc3dc487c73d84dc131d9ac54f68495c12e44cfd2dd7706313e5207c1a21e09ed231cd91b34170b51bd1611bb0b9173e3d73d0c52955beeb35383244
print(hex(modinv(a, m)))