strok = 3
eliments = 3
A = []  # матрица
s = 0  # счетчик строк
c = 0  # счетчик элементов в строке
while s < strok:  # создает строки
    a = []
    c = 0
    p = 0
    if s > 0:
        print("Cледующая строка ")
    while c < eliments:  # элементы в строках
        p = float(input("Введите число в строке "))
        a.insert(c, p)
        c += 1
    s += 1
    A.insert(s, a)
one = [[0 for o in range(3)] for p in range(3)]
for i in range(3):
    for j in range(3):
        if i == j:
            one[i][j] = 1
        else:
            one[i][j] = 0
# если расписать определитель матрицы через треугольники
a = -1  # всегда потому А - ЛЯБДА[Е]
b = (A[0][0] + A[1][1] + A[2][2])
c = (A[0][2] * A[2][0] + A[0][1] * A[0][2] + A[1][2] * A[2][1] - A[1][1] * A[0][0] - A[0][0] * A[2][2] - A[1][1] * A[2][2])
c = A[0][2] * A[2][0] + A[0][1] * A[1][0] + A[1][2] * A[2][1] - A[1][1] * A[0][0]-A[0][0] * A[2][2] - A[1][1] * A[2][2]
d = A[0][1] * A[1][2] * A[2][0] + A[0][2] * A[1][0] * A[2][1] + A[1][1] * A[0][0] * A[2][2] - A[0][1] * A[1][0] * A[2][2] - A[1][1] * A[0][2] * A[2][0] - A[0][0] * A[1][2] * A[2][1]
if b >= 0:
    b = '+' + str(b)
if c >= 0:
    c = '+' + str(c)
if d >= 0:
    d = '+' + str(d)
print(a, 'xxx', b, 'xx', c, 'x', d, sep='')

