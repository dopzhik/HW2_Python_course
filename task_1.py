# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

num_coins = int(input("Введите количество монет => "))
heads_coins = 0
tails_coins = 0
i = 0
while i < num_coins:
    coins = int(input("Введите 0 или 1 => "))
    if coins == 1:
        heads_coins += 1
        i += 1           
    elif coins == 0:
        tails_coins += 1
        i += 1
    else:
        print("Вы ввели неправильное число, введите заново => ")
if heads_coins < tails_coins:
    print(heads_coins)
else:
    print(tails_coins)