def read_csv(filename):
    """Описание функции read_csv
    Читает файл csv
    Описание аргументов:
    filename - имя csv файла"""
    
    with open(filename) as file:
        Headers = file.readline().strip().split('$')
        Array = [i.strip().split('$') for i in file.readlines()]
    return Headers,Array
def count_occurences(game,data):
    """функция count_occurences считает количество вхождений элемнта game в массив data
    game - элемент
    data - массив"""
    counter = 0
    for i in data:
        if i==game:
            counter+=1
    return counter


headers,array = read_csv("Вариант 6/game.txt")
origgames = [i[0] for i in array]
headers.append('counter')

for i in range(len(array)):
    array[i].append(str(count_occurences(array[i][0],origgames)))

array.sort(key = lambda x: x[4]) 
                    
with open('game_counter.csv',mode='w') as file: # Пишем game_new.csv, разделитель - запятая(стандарт для csv)
    file.write(','.join(headers)+'\n')
    for i in array:
        file.write(','.join(i)+'\n')
    

