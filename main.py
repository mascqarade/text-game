import random

def print_slow(str):
    import time
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

def explore_house():
    print_slow("Вы находитесь у входа в заброшенный дом. Вы не знаете, что вас ждет внутри.")
    print_slow("Вам нужно найти ключ, чтобы открыть сейф с сокровищами.")
    
    while True:
        print("\n1 - Войти в дом")
        print("2 - Уйти от дома")
        choice = input("Что вы выберете? (Введите 1 или 2): ")

        if choice == "1":
            explore_room()
            break
        elif choice == "2":
            print_slow("Вы ушли от дома. Пока что вы не смогли найти сокровище.")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 1 или 2.")

def explore_room():
    print_slow("Вы входите в первую комнату дома.")
    print_slow("Комната полна пыли и паутины. На стене висит забытая картина.")
    print_slow("На полу вы замечаете таинственный ключ.")

    while True:
        print("\n1 - Взять ключ")
        print("2 - Осмотреть картины")
        print("3 - Выйти из комнаты")
        choice = input("Что вы выберете? (Введите 1, 2 или 3): ")

        if choice == "1":
            print_slow("Вы взяли ключ.")
            play_game()
            break
        elif choice == "2":
            print_slow("Вы рассматриваете картины, но ничего интересного не находите.")
        elif choice == "3":
            print_slow("Вы выходите из комнаты.")
            explore_house()
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 1, 2 или 3.")

def play_game():
    print_slow("Теперь у вас есть ключ. Вы идете дальше по коридору.")
    print_slow("На пути у вас возникают две двери.")
    print_slow("За одной из них, возможно, находятся сокровища, а за другой - опасность.")

    treasure_door = random.randint(1, 2)

    while True:
        print("\n1 - Открыть левую дверь")
        print("2 - Открыть правую дверь")
        choice = input("Какую дверь вы выберете? (Введите 1 или 2): ")

        if choice == "1":
            if treasure_door == 1:
                print_slow("Вы открываете левую дверь и находите сокровища! Поздравляю, вы победили!")
            else:
                print_slow("Вы открываете левую дверь и попадаете в ловушку. Игра окончена.")
            break
        elif choice == "2":
            if treasure_door == 2:
                print_slow("Вы открываете правую дверь и находите сокровища! Поздравляю, вы победили!")
            else:
                print_slow("Вы открываете правую дверь и попадаете в ловушку. Игра окончена.")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 1 или 2.")

if __name__ == "__main__":
    print_slow("Добро пожаловать в текстовую игру!")
    explore_house()
