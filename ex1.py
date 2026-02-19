age = int(input("Enter Age :"))

while True:
    if(age<13):
        print("Child")
    elif(age<=19 and age>=13):
        print("Teenager")
    elif(age<=59 and age>=20):
        print("Adult")
    else:
        print("Senior")
    break