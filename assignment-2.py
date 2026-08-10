'''


#Q1. Take input in two integer variables and perform all bitwise operators
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("Bitwise AND (&) =", a & b)
print("Bitwise OR (|) =", a | b)
print("Bitwise XOR (^) =", a ^ b)
print("Bitwise NOT (~) of first number =", ~a)
print("Left Shift (<<) =", a << 1)
print("Right Shift (>>) =", a >> 1)


# Q2. Grade a student based on marks
marks = int(input("Enter marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("Grade =", grade)


#Q3. Use nested loops to print the given pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#Q4. Display day using match-case
day = int(input("Enter a number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input")    
'''
#Q5. Perform operations on a string
text = input("Enter a string: ")

print("Number of characters =", len(text))
print("Uppercase =", text.upper())
print("Lowercase =", text.lower())
print("First character =", text[0])
print("Last character =", text[-1])
print("Without whitespaces =", text.replace(" ", ""))