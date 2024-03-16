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
characterlist = [i[1] for i in array]
print(characterlist)
while (inpt:=input())!='game':
    if inpt in characterlist:
        print(f"Персонаж {inpt} встречается в играх:")
        print('\n'.join(set([i[0] for i in array if i[1]==inpt])))
    else:
        print("Этого персонажа не существует")
        
