#calculator task

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /):")

match operator:
    case "+":
        print(f"the resut is: {num1+num2}")
    case "-":
        print(f"the result is: {num1-num2}")
    case "*":
        print(f"the result is: {num1*num2}")
    case "/":
        print(f"the result is: {num1/num2}")