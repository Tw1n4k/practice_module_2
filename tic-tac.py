# Создаем игровое поле
maps = [1,2,3,
        4,5,6,
        7,8,9]

# Инициализация победных комбинаций
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

# Выводим поля на экран
def print_maps():
    print(maps[0], end = ' ')
    print(maps[1], end = ' ')
    print(maps[2])

    print(maps[3], end = ' ')
    print(maps[4], end = ' ')
    print(maps[5])

    print(maps[6], end = ' ')
    print(maps[7], end = ' ')
    print(maps[8])

# Ход в ячейку
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol

# Получение текущего результата игры
def check_winner():
    winner = ''

    for i in victories:
        if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
            winner = 'X'
        if maps[i[0]] == 'O' and maps[i[1]] == 'O' and maps[i[2]] == 'O':
            winner = 'O'

    return winner

# Основа игрового процесса
game_over = False
player1 = True

while game_over == False:
    # Выводим игровое поле
    print_maps()
    # Спрашиваем у играющего куда делать ход
    for turn in range(1, 10):
        print(f'Ход: {turn}') # Ограничиваем количество ходов
        if player1 == True:
            symbol = 'X'
            step = int(input('Игрок 1, ваш ход: '))
        else:
            symbol = 'O'
            step = int(input('Игрок 2, ваш ход: '))

        step_maps(step, symbol) # Делаем ход в указанную ячейку
        winner = check_winner() # Определяем победителя
        if check_winner() == 'X':
            game_over = True
            print_maps()
            print('Победа крестиков!')
        if check_winner() == '0':
            game_over = True
            print_maps()
            print('Победа ноликов')
        if check_winner() != 'X' and check_winner() != '0' and turn == 9:
            game_over = True
            print_maps()
            print('Победила ничья!')
        print_maps()
        player1 = not(player1)
