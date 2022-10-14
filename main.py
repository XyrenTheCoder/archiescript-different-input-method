import string

def encode(text):
    arr = []
    for i in " ".join(text):
        if i not in list(string.ascii_letters + string.digits + " "): return f"Invalid character at position {text.index(i)}"
        if i == " ": arr.append("*")
        elif i.isupper(): arr.append(f"{(int(hex(ord(i)), 16) - int('0x40', 16))*'+'}@")
        elif i.islower(): arr.append(f"{(int(hex(ord(i)), 16) - int('0x60', 16))*'+'}#")
        elif i.isdigit:
            var = "+"*int(i) + "%~"
            arr.append(var)
    arr.append(".;")
    return print(''.join(arr))

def decode(text):
    value = 0
    arr = []
    out = str()
    for i in text:
        if i == "+": value += 1
        elif i == ".": out += ''.join(arr)
        elif i == "#":
            arr.append(chr(0x60+value))
            value = 0
        elif i == "@":
            arr.append(chr(0x40+value))
            value = 0
        elif i == ";": break
        elif i == "*": arr.append(" ")
        elif i == "~": value = 0
        elif i == "%": arr.append(str(value))
    return print(''.join(arr))

def main():
    global a
    a = input("input <encode/decode> <text>: ")
    return a

while True:
    main()
    b = a.split()
    if b[0] == "encode": encode(b[1:])
    elif b[0] == "decode": decode(b[1])
    else: print("usage: <encode/decode> <text>")
