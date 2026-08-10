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

'''
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