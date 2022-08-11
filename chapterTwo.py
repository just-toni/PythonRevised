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

#2.8
print("number \t square \t cube")
numbers = [0, 1, 2, 3, 4, 5]


def square_of_numbers(number1):
    square = number1 * number1
    return square


def cube_of_numbers(number1):
    cube = number1 ** 3
    return cube


for number in numbers:
    print(number, "\t\t", square_of_numbers(number), "   \t\t", cube_of_numbers(number))

# 2.9
choice = str(input("Enter anything of your choice: "))
print(ord(choice))

# 2.10
answer1 = int(input("Enter the first number: "))
answer2 = int(input("Enter the second number: "))
answer3 = int(input("Enter the third number: "))


def calculate_sum(param1, param2, param3):
    addition = param1 + param2 + param3
    return addition


def calculate_average(param1, param2, param3):
    average = calculate_sum(param1, param2, param3) / 3
    return average


def calculate_product(param1, param2, param3):
    product = param1 * param2 * param3
    return product


def calculate_smallest(param1, param2, param3):
    smallest = param1
    if smallest < param2:
        smallest = param2
    if smallest < param3:
        smallest = param3
    return smallest

def calculate_largest(param1, param2, param3):
    largest = param1
    if largest > param2:
        largest = param2
    if largest > param3:
        largest = param3
    return largest


print("Addition:", calculate_sum(answer1, answer2, answer3))
print("Product:", calculate_product(answer1, answer2, answer3))
print("Average:", calculate_average(answer1, answer2, answer3))
print("Smallest:", calculate_smallest(answer1, answer2, answer3))
print("Largest:", calculate_largest(answer1, answer2, answer3))

#2.11
user_answer = int(input("Enter a five digit number: "))
first_digit = user_answer % 10
user_answer = user_answer // 10
second_digit = user_answer % 10
user_answer = user_answer // 10
third_digit = user_answer % 10
user_answer = user_answer // 10
fourth_digit = user_answer % 10
user_answer = user_answer // 10
fifth_digit = user_answer % 10
print(fifth_digit, "   ", fourth_digit, "   ", third_digit, "   ", second_digit, "   ", first_digit)
