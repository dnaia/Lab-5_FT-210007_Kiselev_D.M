counter1 = 0  # Вспомогательный счетчик
while counter1 != 1:  # Проверка, чтобы ввели число.
    # | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        matrix_size = int(input('Введите числом размерность квадратичной матрицы: '))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        counter1 += 1
        counter1 = counter1
        print('Размерность вашей матрицы:', matrix_size, 'на', matrix_size)

matrix = [[0] * matrix_size for _ in range(matrix_size)]
# print(matrix)

header_matrix = []
counterheader = 1
for counter in range(matrix_size):  # Заполнение шапки таблицы горизонтально(основных критериев)
    print(counterheader, 'условие')
    row = input().split()
    for counter in range(len(row)):
        row[counter] = (row[counter])
        counterheader += 1
    header_matrix.append(row)
# print('    ', header_matrix, sep=' ')

# for counter in range(matrix_size):  # Заполнение шапки таблицы вертикально(основных критериев)
# print(header_matrix[counter], sep='\n')

help1 = 0
help = 0
ss = []
k = 0
print('Таблица отношений: ')
print(
    '1 -равная важность\n3 -умеренное превосходство одного над другим\n5 -существенное превосходство одного над другим\n7 -значительное превосходство одного над другим\n9 -очень сильное превосходство одного над другим\n2, 4, 6, 8 -соответствующие промежуточные значения\n')
while k < 1:  # Проверка, чтобы ввели число.
    # | Диалоговый режим с пользователем и обработкой ошибок ввода
    try:
        for counter2 in range(matrix_size):  # Заполняем матрицу
            if help1 != matrix_size:
                if help1 == 0:
                    help1 += 1
                    one = 1
                    ss.append(one)
                else:
                    print('Введите ваше отношение в числовом эквиваленте', header_matrix[0], 'на', header_matrix[help1])
                    answer = int(input())
                    ss.append(answer)
                    help1 += 1
    except ValueError:
        print('Вы ввели не число!\nПопробуйте снова\n')
    else:
        k += 1

matrix[0] = []
matrix[0].append(ss)
dd = []
helpzero = 0
helpone = 1

counteritem = 1  # Вспомогательный счетчик
for item in ss:  # Заполняет весь первый столбик
    if counteritem == len(ss):
        break
    s2 = 1 / ss[helpone]
    sanswer = int(s2 * 100) / 100  # Два знака после запятой
    matrix[counteritem][0] = (sanswer)
    helpzero += 1
    helpone += 1
    counteritem += 1

dd = []
counteritem1 = 1  # Вспомогательный счетчик
for item1 in range(matrix_size):  # Заполняет единицы по диагонали
    if item1 != 0:
        matrix[item1][counteritem1] = 1
        counteritem1 += 1

# print('Матрица', *matrix, sep='\n')

leftobj = 0
helpobj = 1
subtractfirst = 2
helpcounter = matrix_size
helpmatrixsize = matrix_size
while helpcounter != 0:
    helpcounter = helpmatrixsize - subtractfirst  # Кол-во оставшихся элементов в строке, которые нужно ввести
    subtractfirst += 1  # Шаг вычитания
    leftobj += helpcounter  # Кол-во объектов, которые нужно ввести

print('Осталось ввести - ', leftobj, 'элементов')

u = 0
help1 = 0
helpobj = 1
helpone = 1

gorizont = 1
vertical = 2
spind = []
header_matrix = header_matrix

for i in range(matrix_size - 1):  # Узнаем индексы единичек, а после вводим дальше необходимые данные
    index = matrix[helpobj].index(helpone)
    spind.append(index)
    helpobj += 1

n = 0
element = 1
element2 = 2  # Сейчас заполняем правую диагональ матрицы
chetchik = 0
while chetchik != 1:  # Проверка, чтобы ввели число.
    # | Диалоговый режим с пользователем и обработкой ошибок ввода

    try:
        for j in range(1, matrix_size - 1):  # Работаем от (1:размера матрицы-1) строки
            for k in range(spind[n], matrix_size - 1):  # Работаем от (Индекса 1:размера матрицы-1) элементы в строке
                print('Введите ваше отношение в числовом эквиваленте', header_matrix[element], 'на',
                      header_matrix[element2])
                cntrlv = int(input())
                matrix[element][element2] = cntrlv
                element2 += 1
                if element2 + 1 > matrix_size:
                    element += 1
                    n += 1
                    element2 = 2 + n

                if n > len(spind):
                    break
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        chetchik += 1
# Заполнен 1 столбик, единицы, правая диагональ


counteritem_1 = 1  # Вспомогательный счетчик
step = matrix_size
helptwo = 2
numind = 0

for l in range(matrix_size - 2):  # Заполняем левую диагональ столбцами, кроме первого
    spisok = []
    # print('L', l)
    helpzero = 0
    hcounter = 2 + l
    num = 1 + l
    nhelp = 2 + l
    numstroki = 1 + l
    zero = 0
    stopflag = int(matrix_size) - 2
    if numstroki == matrix_size:
        break
    for i in matrix[numstroki]:  # Составили список элементов после 1
        if zero == stopflag:
            break
        if nhelp >= matrix_size:
            break
        a = matrix[numstroki][nhelp]
        spisok.append(a)
        nhelp += 1
        zero += 1
        # print('spisok', spisok)

    for h in spisok:
        if num == matrix_size:
            break
        a2 = 1 / spisok[helpzero]
        aanswer = int(a2 * 100) / 100
        matrix[hcounter][num] = aanswer
        helpzero += 1
        hcounter += 1

print('    ', header_matrix)

for counter in range(matrix_size):  # Заполнение шапки таблицы вертикально(основных критериев)
    print(header_matrix[counter], ' | ', matrix[counter], sep=' ')  # Не получается у меня вывести человеческую таблицу

sss = []
spissr = []
for o in range(matrix_size):
    if o == 0:
        mhelp = ss
    else:
        mhelp = matrix[o]

    sumOfElements = sum(mhelp)
    srznach = sumOfElements / len(matrix[o])
    sranswer = int(srznach * 100) / 100  # Два знака после запятой
    spissr.append(sranswer)
sss.append(spissr)
# print(sss)
'''
y = 0

# for counter in range(matrix_size):  # Заполнение шапки таблицы вертикально(основных критериев)
while y !=matrix_size:
    print(header_matrix[y], ' | ', sss[y], sep=' ')
    y += 1

# print(*matrix, sep='\n')
'''