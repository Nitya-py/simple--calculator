print("My first 'CALCULATOR'")
print("-------------")           
num1 = float(input("Enter First number:"))
operator = input("Enter operator: + , - , * , / , = :")
num2 = float(input("Enter Second number:"))

if operator == "+" :
  result = num1 + num2
elif operator == "-" :
  result = num1 - num2
elif operator == "*" :
  result = num1 * num2
elif operator == "/" :
     if num2 != 0 :
      result = num1 / num2
     else : 
       result = "Can not divide by 0. "
else : 
     result = "Invalid calculation!!"
print("Result" , result)
