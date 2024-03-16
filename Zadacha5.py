def read_csv(filename):
    """Описание функции read_csv
    Читает файл csv
    Описание аргументов:
    filename - имя csv файла"""
    
    with open(filename) as file:
        Headers = file.readline().strip().split('$')
        Array = [i.strip().split('$') for i in file.readlines()]
    return Headers,Array

#Преобразование букв в числа
alf = dict()
j=1
for i in sorted('qwertyuiopasdfghjklzxcvbnm'):
    alf[i] = j
    j+=1
for i in sorted('qwertyuiopasdfghjklzxcvbnm'.upper()):
    alf[i] = j
    j+=1
for i in "1234567890:-' .":
    alf[i] = j
    j+=1
# В примере 0 -> 63, но это невозможно т.к. цифр всего 10, а значит 0->62
# также встречаются пробелы, точки и запятые


def hash(x):
    """ Функция расчёта хеша (hash(s) из условия)
    x - s, строка для которой считается хеш"""
    p = 65
    m = 10**9 + 9
    h = 0
    j = 0
    for i in str(x):

        h += alf.get((i)) * p**j

        j+=1
    return h




headers,array = read_csv("Вариант 6/game.txt")
headers.insert(0,'hash')

for i in range(len(array)):
    array[i].insert(0,hash(array[i][0]+array[i][1]))
array.sort(key = lambda x: x[0]) 
for i in range(len(array)):
    array[i][0] = str(array[i][0])
with open('game_with_hash.csv',mode='w') as file: # Пишем game_with_hash.csv, разделитель - запятая(стандарт для csv)
    file.write(','.join(headers)+'\n')
    for i in array:
        file.write(','.join(i)+'\n')
    

