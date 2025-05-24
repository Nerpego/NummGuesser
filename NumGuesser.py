import random

# Случайное число от нуля до ста
min, max = 0, 100
number = random.randint(min, max)
left_limit, right_limit = min, max
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
                if (
                    answ == "Y"
                    or answ == "Yes"
                    or answ == "y"
                    or answ == "yes"
                    or answ == "N"
                    or answ == "No"
                    or answ == "n"
                    or answ == "no"
                ):
                    break
            if answ == "Y" or answ == "Yes" or answ == "y" or answ == "yes":
                print("Поехали!")
                number = random.randint(min, max)
                left_limit, right_limit = min, max
            if answ == "N" or answ == "No" or answ == "n" or answ == "no":
                print("Конец.")
                break
    else:
        print("Нужно число!")