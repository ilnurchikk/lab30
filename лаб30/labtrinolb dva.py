################1
# [a, b] = [int (c) for c in input ("Введите два числа через пробел чтобы посчитать\n"
#                                   "сумму в указоном диапозоне и среднее арифметическое: ").split ()]
# mn = min(a, b)
# mx = max(a, b)
# rn = range(mn, mx + 1)
# sm = sum(rn)
# print(f"Сумма от {mn} до {mx}: = {sm}")
# print(f"Среднее арифметическое от {mn} до {mx}: = {sm / len (rn)}")
#
# [a, b] = [int(c) for c in input("Введите два числа через пробел: ").split()]
# mn = min(a, b)
# mx = max(a, b)
# rn = range(mn, mx + 1)
# sm = 0
# for d in rn: sm += d
#
# print(f"Сумма от {mn} до {mx}: = {sm}")
# print(f"Среднее арифметическое от {mn} до {mx}: = {sm / len(rn)}")

################2
#print("Формула для расчета факториала: n!")
#a = int(input('ВВедите  число:'))
#b = 1
#for i in range(2, a + 1):
#    b *= i
#print(f"факториал числа {a}! = {b} ")
#########################3
# a = int(input("введите длинну линии в горизонтальном положении "))
# for i in range(a):
#     for j in range(a):
#         if (i == 0):
#             print("*", end=" ")
###########################4
a = int(input("Введи число для линии: "))
b = input("Введите символ для линии: ")
for i in range(a):
    print(b)



