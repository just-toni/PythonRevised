# exercise 2.5
radius = 2
diameter = 2 * radius
circumference = 2 * radius * 3.14159
area = 3.14159 * (radius ** 2)

print("Diameter of radius 2 is: ", diameter)
print("Area of radius 2 is: ", area)
print("Circumference of radius 2 is: ", circumference)

# 2.6
choice = int(input("Enter a number: "))
if choice % 2 == 0:
    print("Even number")
if choice % 2 == 1:
    print("Odd number")

# 2.7
if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
else:
    print("1024 is not a multiple of 4")

if 2 % 10 == 0:
    print("2 is a multiple of 10")
else:
    print("2 is not a multiple of 10")

# 2.8
print("number \t square \t cube")
numbers = [0, 1, 2, 3, 4, 5]


def square_of_numbers(number1):
    square = number1 * number1
    return square


def cube_of_numbers(number1):
    cube = number1 ** 3
    return cube


for number in numbers:
    print(number + "\t" + square_of_numbers(number) + "\t" + cube_of_numbers(number))
    # print()
    # print(cube_of_numbers(number))
