age = int(input("Enter age :"))
day = input("Enter day :")
discount = 2
adult_price = 12
child_price = 8

if(age>=18):
    print(f"{adult_price} for adults")
elif(day=="wednesday"):
    print(f"{adult_price-discount} after discount of wednesday")
if(age<=18):
    print(f"{child_price} $ for child")
elif(day=="wednesday"):
    print(f"{child_price-discount} after discount of wednesday")
        
    
    
    
    
