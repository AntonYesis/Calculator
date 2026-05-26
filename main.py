print("-----------------------------------------")
num1 = int(input("Введите первое значение: "))
print("-----------------------------------------")
num2 = int(input("Введите второе значение: "))
print("-----------------------------------------")
operation = input("Введите операцию(+, -, /, *): ")
print("-----------------------------------------")
if operation == "+":
   result = num1 + num2
elif operation == "-":
   result = num1 - num2
elif operation == "/":
   result = num1 / num2
elif operation == "*":
   result = num1 * num2
else:
   result = "Неизвестная операция"
print(f'Your answer: {result}')
print("-----------------------------------------")