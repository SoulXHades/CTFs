import inspect

for frameinfo in inspect.stack():
    print(frameinfo.frame)


def crypt(word, salt):
    print(word)
    print(salt)

def ARC4(anything):
    print(anything)
    return GG()

class GG:
    def __init__(self) -> None:
        pass

    def encrypt(self, anything):
        print(anything)