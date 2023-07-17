# Перевірити чи всі значення першої строки знаходяться в другій строці

# string_1 = input("Enter your text: ")
# string_2 = input("Enter your text to compare: ")

# for char in string_1:
#     if char not in string_2:
#         print(False)
#         break
# else:
#     print(True)

# У математиці послідовність Фібоначчі - це послідовність, у якій кожне число є сумою двох попередніх.
# За визначенням, перші два числа в послідовності Фібоначчі є або 1 і 1, або 0 і 1, залежно від обраного початку,
# а кожне наступне число є сумою двох попередніх.

# a, b = 0, 1
# for _ in range(10):
#     a, b = b, a + b
#     print(a)

# Перевірка чи число є простим (Додатков знайти всі числа в діапазоні який веде користувач)

# user_input = int(input("Enter your number"))
# for num in range(user_input):
#     try:
#         if user_input < 0:
#             break
#         for i in range(2, int(num**0.5 + 1)):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
#     except ValueError:
#         print("Please use natural numbers")

# Скласти програму перевірки, чи є задане тризначне число паліндромом

# num = int(input("Please enter 3-digit number: "))

# hundreds = num // 100
# digits = num % 10

# if hundreds == digits:
#     print(f"{num} is palindrome")
# else:
#     print(f"{num} is not palindrome")

# Дано координати 2-х точок. Розрахувати чи є відстань між ними меншою за 5.

# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))

# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))

# distance = round((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5), 2)

# if distance > 5:
#     print(f"Distance between dots is more than 5. Distance is {distance}")
# elif distance < 5:
#     print(f"Distance between dots is less than 5. Distance is {distance}")
# else:
#     print("Distance is 5")

# Скласти програму, яка вводить цілі k, l. Якщо вони не рівні, то менше з них замінює більшим, інакше обидва замінює на 0.

# k = float(input("Enter k: "))
# l = float(input("Enter l: "))

# if k > l:
#     l = k 
# elif l > k:
#     k = l    
# else:
#     k, l = 0, 0
# print(k, l)

# Скласти програму, яка запитує дату (число, місяць, рік) і перевіряє коректність введених даних

# year = int(input("Enter your year of birth: "))
# month = int(input("Enter your month of birth: "))
# day = int(input("Enter your day of birth: "))

# is_leap_year = False

# if year > 2023:
#     print("Please enter existing date")2
#     if month > 7:
#         print("Please enter existing date")
#     elif day > 17:
#         print("Please enter existing date")

# if year > 2023 and month > 7 and day > 17:
#     print("Please enter existing date")  
#     if day and month and year:
#         if month <= 0 or month > 12:
#             print("Please enter existing date")
#         if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#             if day <= 0 or day > 31:
#                 print("Please enter existing date")
#         else:
#             if day <= 0 or day > 30:
#                 print("Please enter existing date")

#         if month == 2:
#             if year % 400 == 0:
#                 is_leap_year = True
#             elif year % 100 == 0:
#                 is_leap_year = False
#             elif year % 4 == 0:
#                 is_leap_year = True
#             else:
#                 is_leap_year = False
            
#             if is_leap_year:
#                 if day <= 0 or day > 29:  
#                     print("Please enter existing date")
#             else:
#                 if day <= 0 or day > 28:  
#                     print("Please enter existing date")

#         print(f"Your date of birth is {day}, {month}, {year}")
#     else:
#         print("Please enter existing date")


# Усі трикутники можуть бути віднесені до того чи іншого класу (рівнобедрені, рівнобічні та різнобічні) на підставі довжин їхніх сторін.
# Рівносторонній трикутник характеризується однаковою довжиною всіх трьох сторін, рівнобедрений - двох сторін з трьох,
# а у різностороннього трикутника всі сторони різної довжини. Напишіть програму, яка запитуватиме 
# у користувача довжини всіх трьох сторін трикутника і видаватиме повідомлення про те, до якого типу слід його відносити.

# triangle = None
# side_1 = float(input("Enter side 1 of triangle: "))
# side_2 = float(input("Enter side 2 of triangle: "))
# side_3 = float(input("Enter side 3 of triangle: "))


# if (side_1 + side_2) > side_3 and (side_1 + side_3) > side_2 and (side_3 + side_2) > side_1:
    
#     if side_1 == side_2 and side_2 == side_3 and side_3 == side_1:
#         triangle = "Triangle is equilateral."
#     elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
#         triangle = "Triangle is isosceles."
#     else:
#         triangle = "Triangle is scalene."
    
#     print(triangle)
    
# else:
#     print("It is not a triangle")
# # a + b > c
# b + c > a
# c + a > b

# У банк поклали 100 доларів під 5 % річних. Скласти програму обчислення кількості грошей на рахунку через 10 років. (складні щомісячні відсотки)

# PERCENT = 0.05
# money = 100

# deposit = money * (1 + PERCENT/ 12) ** (12 * 10)
# print(round(deposit))

# PERCENT = 0.05
# money = 100
# waiting_year = 10

# for year in range(1, waiting_year + 1):
#     new_deposit = money * (1 + PERCENT/ 12) ** 12
#     money = new_deposit
# print(f"Your deposit will be {round(money, 2)}")

# Користувач вводить строку, перевірити чи дана строка є паліндромом

# line = input("Enter your text: ")
# line = line.lower()

# if line == line[::-1]:
#     print("Is palindrome")
# else:
#     print("Not a palindrome")
