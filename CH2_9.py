try:
    ch1 = input()
    ch2 = input()
    s = "1ый больше" if int(ch1)>int(ch2) else "2ой больше"
    print(s)
except:
    print("Ничего страшного")