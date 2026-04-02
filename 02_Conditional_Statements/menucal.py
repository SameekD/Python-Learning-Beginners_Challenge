operation = int(input(
"1 -> Perform Addition (+)\n" 
"2 -> Perform Substraction (-)\n" 
"3 -> Perform Multiplication (*)\n" 
"4 -> Perform Division (/)\n" 
"5 -> Exit program\n"
" Please select an operation to perform : "
    )
)
if operation == 5:
    exit(0);

num1,num2 = map(int, input("Enter two number to perform the operation: " ).split())
match operation:
    case 1 :
        print(f"The result is : {num1 + num2}")
    case 2 :
        if num1 > num2 :
            print(f"The result is : {num1 - num2}")
        else :
            print(f"The result is : {num2 - num1}")
    case 3 :
        print(f"The result is : {num1 * num2}")
    case 4 :
        if num2 == 0 :
            print("undefine")
        else :
            print(f"The result is : {num1 / num2}")
    case _ :
        print("The input operation selected is invalid.")