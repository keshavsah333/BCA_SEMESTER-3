'''
#Q1. Store "Hello" and "World" in two variables and print in one line

a = "Hello"
b = "World"

print(a, b)


# Q2. Perform arithmetic operations on two or more numbers through user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)


#Q3. Concatenate two strings using + operator
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + str2

print("Concatenated string:", result)


#Q4. Print the largest of 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)


#Q5. Print all prime numbers up to n number

n = int(input("Enter a number: "))

print("Prime numbers up to", n, "are:")

for num in range(2, n + 1):
    prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")
        
'''
#Q6. Convert temperature from Fahrenheit to Celsius
f = float(input("Enter temperature in Fahrenheit: "))

c = (f - 32) * 5 / 9

print("Temperature in Celsius:", round(c, 2))


# git hub progress of the code is done and uploaded to the git hub repository