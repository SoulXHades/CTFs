# RSA decryption: https://www.mandiant.com/resources/blog/cryptography-blackmatter-ransomware
# Chacha20 Algorithm: https://xilinx.github.io/Vitis_Libraries/security/2019.2/guide_L1/internals/chacha20.html
# Chacha20 Python library: https://pycryptodome.readthedocs.io/en/latest/src/cipher/chacha20.html

from Crypto.Cipher import ChaCha20
from base64 import b64decode

# Convert large hex number to list of numbers like what we see in hexeditors
def get_list_of_num(value: int):
    list_of_num = list()

    while value != 0:
        list_of_num.append(value % 0xFF)
        value = value >> 8


# Get list_of_random_numbers's value
encrypted_value = 0x5a04e95cd0e9bf0c8cdda2cbb0f50e7db8c89af791b4e88fd657237c1be4e6599bc4c80fd81bdb007e43743020a245d5f87df1c23c4d129b659f90ece2a5c22df1b60273741bf3694dd809d2c485030afdc6268431b2287c597239a8e922eb31174efcae47ea47104bc901cea0abb2cc9ef974d974f135ab1f4899946428184c
n = 0xdc425c720400e05a92eeb68d0313c84a978cbcf47474cbd9635eb353af864ea46221546a0f4d09aaa0885113e31db53b565c169c3606a241b569912a9bf95c91afbc04528431fdcee6044781fbc8629b06f99a11b99c05836e47638bbd07a232c658129aeb094ddaf4c3ad34563ee926a87123bc669f71eb6097e77c188b9bc9
d = 0x10001

decrypted_value = (encrypted_value ** d) % n
print("Decrypted value: " + hex(decrypted_value))
decrypted_value = decrypted_value.to_bytes(48, "little")    # 48 bytes as 32bytes=key, 4bytes=counter, 12bytes=nonce


# key = [ord(char) for char in "expand 32-byte k"].extend(get_list_of_num(decrypted_value))
encrypted_flag = b64decode("f4r6Y2WcXvaeucPcE+iyMTqP422UhjQhRitv6K0wjSp56Op7ZgnY0FgCPZcUa/KqYIUGSE2XDnHqggY1ukv8UY8G5K1pK+YlWw==")
key = decrypted_value[:32]
counter = decrypted_value[32:36]
print("Counter: " + str(int.from_bytes(counter, "little")))   # Just to check if counter has any values
nonce = decrypted_value[36:]
cipher = ChaCha20.new(key=key, nonce=nonce)
plaintext_flag = cipher.decrypt(encrypted_flag)
print(plaintext_flag.decode())
