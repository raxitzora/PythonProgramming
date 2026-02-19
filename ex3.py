marks = int(input("Enter marks :"))

if(marks>=90 or marks<=100):
    print("A Grade")
elif(marks>=89 or marks<=80):
    print("B Grade")
elif(marks>=70 and marks<=79):
    print("C Grade")
elif(marks>=60 and marks<=69):
    print("D Grade")
elif(marks<=60):
    print("F Grade")