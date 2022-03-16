B = "{0:{2}{1}s}"
for k in range(7):
    print(B.format("*", k, ">"), end="")
    if (k==4):
        print("*"*(2*(7-k)), end="")
    else:
        print(" "*(2*(7-k)), end="")
    print(B.format("*", k, "<"))
    
line = ""

B = "{0:{2}{1}s}"
for k in range(7):
    line+= B.format("*", k, ">")
    if (k==4):
        line+="*"*(2*(7-k))
    else:
        line+=" "*(2*(7-k))
    line+=B.format("*", k, "<")
    line+="\n"

print(line[::-1])
