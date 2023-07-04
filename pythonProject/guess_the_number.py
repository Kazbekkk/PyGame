# Это игра по угадыванию чисел.
import random

guessesTake = 0

print('Привет! Как тебя зовут?')
myName = input()

number = random.randint(1, 20)
print('Что ж, ' + myName + 'я загадываю число от 1 до 20.')

for guessesTake in range (6):
    print('Попробуй угадать.')
    guess = int(input())

    if guess < number:
        print('Твое число слишком маленькое.')

    if guess > number:
        print('Твое число слишком большое.')

    if guess == number:
        break

if guess == number:
    guessesTake = str(guessesTake + 1)
    print('Отлично' + myName + '! Ты справился за ' + guessesTake + ' попытки!')

if guess != number:
    number = str(number)
    print('Увы. Я загадал число ' + number + '.')