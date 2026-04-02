num = int(input("set the limit : "))
if num == 0 :
    print("the sum is zero.")
else :
    sum = 0
    for i in range (1, num+1) :
        sum += i
print(sum)