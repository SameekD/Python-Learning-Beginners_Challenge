num1 = int(input ( 'Enter a number :'))
num2 = int(input ( 'Enter another number :'))
opt = input ( 'Chose the operation ( + , - , * , /) :')
if opt == "+" :
    result = num1 + num2 
elif opt == "-" :
    result = num1 - num2
elif opt == "*" :
    result = num1 * num2
elif opt == "/" :
    result = num1 + num2
else :
    result = "You did not select correct opperation"
print ( f"{result}" )