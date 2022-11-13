filename = "states_and_truefalse.txt"

with open(filename) as fd:
    content = fd.readlines()

new_content = list()

i = 0

while i < len(content):
    try:
        new_content.append(content[i])
        if content[i+1] == "True\n":
            new_content.append(content[i+1])
            # Skip "True" in the next line
            i += 1
        else:
            new_content.append("False\n")
        i += 1
    except IndexError:
        # Means we are at the last case's state which we don't need to add True/False for it anyway
        break

 
# print(new_content)    # For checking and debugging the output
with open("new_" + filename, "w") as fd:
    fd.writelines(new_content)