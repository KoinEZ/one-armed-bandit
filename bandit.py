import random

# Символы и их вероятности выпадения
symbols = ['♥', '♦', '♣', '♠']  # можно добавить другие символы
probabilities = [0.3, 0.3, 0.2, 0.2]

# Функция для случайного выбора символа в соответствии с вероятностью
def spin():
    rand = random.random()
    cumulative_prob = 0
    for symbol, prob in zip(symbols, probabilities):
        cumulative_prob += prob
        if rand <= cumulative_prob:
            return symbol

# Функция для отображения результатов спина
def display_spin(result):
    print("Результат спина: " + ' | '.join(result))

# Главная функция игры
def play_slot_machine():
    print("Добро пожаловать в однорукого бандита!")
    while True:
        input("Нажмите Enter, чтобы сделать спин...")
        result = [spin() for _ in range(3)]
        display_spin(result)
        if all(symbol == result[0] for symbol in result):
            print("Победа!")
        else:
            print("Попробуйте еще раз!")

        choice = input("Желаете ли вы продолжить игру? (y/n): ")
        if choice.lower() != "y":
            break

# Запуск игры
play_slot_machine()
