import art
print(art.logo)

# Add
def add(a, b):
  return a+b

def sub(a,b):
  return a-b

def multiply(a, b):
  return a*b

def divide(a,b):
  return a/b

operation = {
  "+": add,
  "-": sub,
  "*": multiply,
  "/": divide
}
def calculator():
  calculation = True
  num1 = float(input("What's the first number: "))
  for operators in operation:
    print(operators)
  while calculation:
    op = input("Which operation would you like to perform: ")

    num2 = float(input("What's the next number: "))
    answer = operation[op](num1, num2)
    print(f"{num1} {op} {num2} = {answer}")
    ask = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new calculation: ")
    if ask == 'n':
      calculation = False
      calculator()
    elif ask == 'y':
      num1 =answer




calculator()