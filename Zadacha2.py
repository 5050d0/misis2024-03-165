def read_csv(filename):
    """Описание функции read_csv
    Читает файл csv
    Описание аргументов:
    filename - имя csv файла"""
    
    with open(filename) as file:
        Headers = file.readline().strip().split('$')
        Array = [i.strip().split('$') for i in file.readlines()]
    return Headers,Array


        
def quicksort(a):
    """рекурсивный quicksort

    a - массив"""
    if len(a) <2 or type(a) != list:
        return a
    pivot = a[len(a)//2]
    left= [i for i in a if i<pivot]
    right= [i for i in a if i>pivot]
    centre = [i for i in a if i==pivot]

    return quicksort(left) + quicksort(centre) +quicksort(right)


headers,array = read_csv("Вариант 6/game.txt")
origgames = [i[0] for i in array]
games = list(set(origgames))
games = quicksort(games)
for game in games:
    print(f"{game} - количество багов: {origgames.count(game)}")
    
