import random

# Случайное число от нуля до ста
min, max = 0, 100

number = random.randint(min, max)
left_limit, right_limit = min, max
positiv_answ = ["Y", "y", "Yes", "yes"]
negativ_answ = ["N", "n", "No", "no"]
# Цикл угадываний
while True:
    guess = input("Попробуй угадать! \n")
    # print(type(guess))
    if guess.isdigit():
        guess = int(guess)
        if guess != number:
            if guess > number and guess < right_limit:
                right_limit = guess
            elif guess < number and guess > left_limit:
                left_limit = guess
            print(
                f"Не попал! чиcло должно быть больше чем {left_limit} и меньше чем {right_limit}"
            )
        else:
            while True:
                answ = input("Поздравляю! Ты угадал! \n Продолжим? (Y/N):  ")
                if answ in positiv_answ or answ in negativ_answ:
                    break
            if answ in positiv_answ:
                print("Поехали!")
                number = random.randint(min, max)
                left_limit, right_limit = min, max
            if answ in negativ_answ:
                print("Конец.")
                break
    else:
        print("Нужно число!")