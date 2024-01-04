################1
# a = int(input("таблицу умножения от 1 до 10 введите число: "))
# for i in range(1, 11):
#      print(f"{a} * {i} = {a * i}")
################2
#while True:
#   conver= input('Если хотите выйти введите любой символ \n В какую волюту хотите в  доллары в евро в фунты:')
#   a = float(input('введите свою сумму в рублях:'))
#   if conver =="доллары":
#      print(f'Резултат вычесления: {(a * 90)}')
#   elif conver =="евро":
#      print(f'Резултат вычесления: {(a * 100)}')
#   elif conver == "фунты":
#      print(f'Резултат вычесления: {(a * 120)}')
#      print("приложение конвертер завершил работу!")
#      break
###################3
# print("Пользователь вводит с клавиатуры две границы диапазона и число.")
# a = int(input("Введите 1 границу диапазона: "))
# b = int(input("Введите 2 границу диапазона: "))
# c = int(input("Введите число: "))
#
# for i in range(a, b):
#     if i == c:
#         print(f"!{i}!", end=" ")
#         continue
#
#     print(f"{i}", end=" ")
####################4

import random
import time
computer_number = random.randint(1, 500)
attempts = 0
stime = time.time()
while True:
    a = int(input(" Угодайте число от 1 до 500. Если надоело угадывать нажмите 0 для выхода: "))
    if a == 0:
        print("Пока.")
        break
    attempts += 1
    if a < computer_number:
        print("Загаданное число больше")
    elif a > computer_number:
        print("Загаданное число меньше")
    else:
        endtime = time.time()
        time = endtime - stime
        print(f"Вы угадали {computer_number}!")
        print(f"Сколько попыток: {attempts}")
        print(f"Сколько времяни занело: {time:.2f} секунд")
        break





