#n - размерность матрицы n x n
#mat - результирующая матрица
#st - текущее значение-счетчик для записи в матрицу
#m - коеффициент, используемый для заполнения верхней
#матрицы последующих витков, т.к. одномерные матрицы
#следующих витков имеют меньше значений
n = int(input())
mat = [[0]*n for i in range(n)]
st, m = 1, 0
# Заранее присваиваю значение центральному элементу
# матрицы
mat[n//2][n//2]=n*n
for v in range(n//2):
#Заполнение верхней горизонтальной матрицы
    for i in range(n-m):
        mat[v][i+v] = st
        st+=1
        for ig in mat:
            print(*ig)

#Заполнение правой вертикальной матрицы    
    for i in range(v+1, n-v):
        mat[i][-v-1] = st
        st+=1
        for ig in mat:
            print(*ig)
#Заполнение нижней горизонтальной матрицы
    for i in range(v+1, n-v):
        mat[-v-1][-i-1] =st
        st+=1
        for ig in mat:
            print(*ig)
#Заполнение левой вертикальной матрицы
    for i in range(v+1, n-(v+1)):
        mat[-i-1][v]=st
        st+=1
        for ig in mat:
            print(*ig)
    m+=2
#Вывод результата на экран
for i in mat:
    print(*i)