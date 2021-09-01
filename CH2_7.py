chisla = eval(input())

if len(chisla)==3:
    if chisla[2] - chisla[1] == chisla[1] - chisla[0]:
        print('является')
    else:
        print('Не является')