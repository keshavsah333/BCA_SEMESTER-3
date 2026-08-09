if 2%2==0:
    print("The number is even.")
else:
    print("the number is odd.")
    

# github copilot even and odd statement
'''
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
'''

#know i have to check if the number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# git hub progress of the code is done and uploaded to the git hub repository

