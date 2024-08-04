maps = [1,2,3,
        4,5,6,
        7,8,9]

# Инициализация победных линий
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

# Вывод карты на экран
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])

    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])

    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])

# Сделать ход в ячейку
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol

# Получить текущий результат игры
def check_winner():
    winner = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            winner = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            winner = "O"

    return winner

# Основная программа
game_over = False
player1 = True

while game_over == False:
    print_maps()
    # 2. Спросим у играющего куда делать ход
    for turn in range(1, 10):
        print(f"Ход: {turn}")
        if player1 == True:
            symbol = "X"
            step = int(input("Игрок 1, ваш ход: "))
        else:
            symbol = "O"
            step = int(input("Игрок 2, ваш ход: "))

        step_maps(step, symbol) # делаем ход в указанную ячейку
        winner = check_winner() # Определим победителя
        if check_winner() == "X":
            game_over = True
            print_maps()
            print("Победа крестиков!")
        if check_winner() == "0":
            game_over = True
            print_maps()
            print("Победа ноликов")
        if check_winner() != "X" and check_winner() != "0" and turn == 9:
            game_over = True
            print_maps()
            print("Победила ничья!")
        print_maps()
        player1 = not(player1)