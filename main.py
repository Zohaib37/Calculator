def add(n1, n2):
  return n1 + n2

def subtract (n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2    

def divide(n1, n2):
  return n1 / n2

from replit import clear
from art import logo

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num_1 = float(input("Enter first number: "))

  for key in operations:
    print(key)

  to_continue = True
  run_again = ""

  while to_continue:
    operation_symbol = input("Enter operation: ") 
    num_2 = float(input("Enter next number: "))
    function = operations[operation_symbol]
    result = function(num_1, num_2)
    print(f"{num_1} {operation_symbol} {num_2} = {result}")

    run_again = input(f"Type 'y' to continue calculating with {result}, or type 'n' for new calculation: ")
    if run_again == "n":
      clear()
      calculator()
    else:
      num_1 = result

calculator()
