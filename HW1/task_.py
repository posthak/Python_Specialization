# name ='Mischa'
# age = None

# a = 42
# print(id(a))
# a = 'Hello world'
# print(id(a))
# a = 3.14/3
# print(id(a))
# print(name,age,a,456,'text',sep=' (=^.^=) ', end = '#')
# print('any text')
# result = input()
# print('result=', result)

# age  = int(input('How old are you?'))
# ADULT = 18
# how_old = ADULT-age
# print(how_old, 'yo left till 18yo')


# pwd = 'text'
# res = input('Inp pass:')
# if res == pwd:
#     print('Access is allowed')
#     my_math = int(input('2 + 2 = '))
#     if 2+2 == my_math:
#         print('Correct!')
#     else:
#         print('Incorrect')
# else:
#     print('Pass is incorrect')
# print('Work is finished')

# # print(*objects, sep=' ',end = ' ',file =s ys.stdout,flush = False)

# color = input('Input color: ')
# if color == 'red':
#     print('Favor bright color')
# elif color == 'green':
#     print('Ohotnik')

# match color:
#     case 'red' | 'orange':
#         print('red')


# высокосный год
# year = int(input('Input year: '))
# if year % 4 != 0:
#     print('Normal year')
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print('Vysoskosnyi')
#     else:
#         print('Normal year')
# else:
#     print('Vysoskosnyi')
# year = int(input('Input year: '))
# if year % 4 != 0 or year % 100 == 0 and year % 400 == 0:
#      print('Vysoskosnyi')

# data = [0,1,1,2,3,5,8,13,21]
# num = int(input('Inp data:' ))
# if num not in data:
#      print('Leo is boring')

#тернарный оператор
# my_match = int(input('2+2 = '))
# print('Correct!' if 2+2 == my_match else 'Are you sure?')

 
# num = float(input('Введите число: '))
# count = 0
# while count < num:
#     print(count)
#     count += 2

# num = float(input('Введите число: '))
# STEP = 2
# limit = num - STEP
# count = -STEP
# while count < limit:
#     count += STEP
#     if count % 12 == 0:
#         continue
#     print(count)

# min_limit = 0
# max_limit = 10
# while True:
#     print('Введи число между', min_limit, 'и', max_limit, '? ')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break
# print('Было введено число ' + str(num))

# min_limit = 0
# max_limit = 10
# count = 3
# while count > 0:
#     print('Попытка ' + str(count))
#     count -= 1
#     num = float(input('Введи число между ' + str(min_limit) + ' и ' + str(max_limit) + ': '))
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else: 
#         break
# else:
#     print('Исчерпаны все попытки. Сожалею.')
#     quit()
# print('Было введено число ' + str(num))

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for item in data:
#     print(item)

# num = int(input('Введите число: '))
# for i in range(0, num, 2):
#     print(i)

# count = 10
# for i in range(count):
#     for j in range(count):
#         for k in range(count):
#             print(i, j, k)

# count = 10
# for i in range(count):
#     print(i)
# for i in range(count):
#     print(i)

# animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
# for animal in animals:
#     print(animal)

# animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
# for i, animal in enumerate(animals, start=1):
#     print(i, animal)

# data = 0
# while data < 100:
#     data += 2
#     if data % 40 == 0:
#         break
# print(data)

# data = 0
# while data < 100:
#     data += 3
#     if data % 40 == 0:
#         print(data)
#         break 
#     else:
#         data += 5
# print(data)

data = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    data += 1
    if data % 40 == 0:
        break 
    else:
        data += 5
print(data)