def read_csv(filename):
    """Описание функции read_csv
    Читает файл csv
    Описание аргументов:
    filename - имя csv файла"""
    
    with open(filename) as file:
        Headers = file.readline().strip().split('$')
        Array = [i.strip().split('$') for i in file.readlines()]
    return Headers,Array

headers,array = read_csv("Вариант 6/game.txt")

print('Отчёт:')
for i in array:
    if '55' in i[2]: # Все ошибки с содержанием числа 55
        print(f"У персонажа\t{i[1]}\tв игре\t{i[0]}\tнашлась ошибка с кодом:\t{i[3]}.\tДата фиксации:\t {i[3]}" )
for i in range(len(array)):
    if '55' in array[i][2]:
        array[i][2] = 'Done' # Значение ошибки(буквенное и цифровое) заменяем на Done
        array[i][3] = '0000-00-00'

with open('game_new.csv',mode='w') as file: # Пишем game_new.csv, разделитель - запятая(стандарт для csv)
    file.write(','.join(headers)+'\n')
    for i in array:
        file.write(','.join(i)+'\n')
    
