text = input()

text_sh = list()

for i in text:
    if ord(i)==65:
        text_sh.append(chr(ord("Z")-1))
    elif ord(i) == 66:
        text_sh.append("Z")
    else:
        text_sh.append(chr(ord(i)+2))

print("".join(text_sh))
