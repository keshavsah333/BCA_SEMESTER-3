age = 20
citizen = True
k=int(input("Enter a number: "))
c=str(input("citizenship status (True/False): "))

if c == "True":
    citizen = True
else:
    citizen = False
if age >= 18:
    if citizen:
        print("Eligible")
    else:
        print("Citizenship required")
else:
    print("Underage")
    
