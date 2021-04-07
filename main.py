field = [['-'] * 3 for _ in range(3)]
positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
# Функция отрисовки игрового поля
def game_filed(f):
    num ='  0 1 2'
    print(num)
    for row, i in zip(f, num.split()):
        print(f"{i} {' '.join(str(j) for j in row)}") # вывод игрового поля в консоль

# ход игрока
def users_move(f, user):
    while True:
        place = input(f"Ходит {user} .Введите координаты, сначала x, затем y:").split()

        if not (place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        if len(place) != 2:
            print('Введите две координаты')
            continue
        x, y = map(int, place)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Вышли за пределы поля')
            continue
        if f[x][y] != '-':
            print('Клетка занята игроком')
            continue
        break
    return x, y

# определение победителя
def win_line(f, user):
    f_list = []
    for l in f:
        f_list += l
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False

# опрелеляем, чей ход, четное х, нечетное у
def start(field):
    count = 0
    while True:
        game_filed(field)
        if count % 2 == 0:
            user = 'x'
        else:
            user = '0'
        if count < 9:
            x, y = users_move(field, user)
            field[x][y] = user
# проверяем заполненность клеток
        elif count == 9:
            print('Ничья')
            break
        if count > 3:
            if win_line(field, user):
                game_filed(field)
            print(f"Победил {user}!")
            break
        count += 1


start(field)