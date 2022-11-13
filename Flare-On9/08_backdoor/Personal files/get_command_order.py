c_command_order = [250, 242, 240, 235, 243, 249, 247, 245, 238, 232, 253, 244, 237, 251, 234, 233, 236, 246, 241, 255, 252]

def get_ip(command: int) -> str:
    ip = ["43", ".", "0", ".", "0", ".", "0"]
    for index, letter in enumerate(str(command)):
        # Only write to index 2 and onwards and only at the bytes locations
        ip[(index+2)+(index*1)] = str(ord(letter))
    
    return "".join(ip)

for command_encoded in c_command_order:
    command = command_encoded ^ 248
    print(str(command) + "(" + get_ip(command) + ")", end=", ")

# New line
print("")