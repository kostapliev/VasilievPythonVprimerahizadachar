text = input("   ")
text_sh = []
consonants = "bcdfghjklmnpqrstvwxyz"
vowels = 'aeiou'
cons_l = list(consonants)
vowe_l = list(vowels)

for i in text:
    if i in cons_l:
        ind = cons_l.index(i)
        try:
            l = cons_l[ind+1]
        except IndexError:
            l = cons_l[0]
        text_sh.append(l)
    elif i in vowe_l:
        ind = vowe_l.index(i)
        try:
            l = vowe_l[ind+1]
        except IndexError:
            l = vowe_l[0]
        text_sh.append(l)
    else:
        pass

print("".join(text_sh))
