import os
if os.name == "nt": os.system("cls")
else: os.system("clear")
print("Archiescript v1.0\n")

value = 0
cmd = input(">> ")
l = []
for i in cmd: l.append(i)

text = []
for c in l:
    if c == "+": value += 1
    elif c == "-": value -= 1
    elif c == ".": print(''.join(text))
    elif c == '#':
        text.append(chr(0x60+value))
        value = 0
    elif c == '@':
        text.append(chr(0x40+value))
        value = 0
    elif c == ";": quit()
    elif c == "*": text.append(" ")
    elif c == "!": value = 0
    elif c == "&": text.append(str(value))
