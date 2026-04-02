num = int(input("Insert the factorial limit :"))
if num == 0 :
    print("The factorial result is : 1")
else :
    fact = 1
    for i in range (1, num + 1 ) :
        fact = fact * i
print(f"The factorial result is : {fact}")
