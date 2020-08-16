def summation(x, y):
  res = 0.0
  for i in range(x, y + 1):
    res = res + i
  return float(res)

def product(x, y):
  res = 1.0
  for i in range(x, y + 1):
    res = res * i
  return float(res)

isContinue = "y"

while isContinue == "y":

  print("My First Console Calculator\n")

  first = input("Enter First Number: ")
  second = input("Enter Second Number: ")

  print("\nSelect the operation you want to perform:\n\n====\n1. Sum\n2. Subtract\n3. Product\n4. Division\n5. Summation function\n6. Product function\n7. Volume of sphere\n")
  
  
  option = input("Enter Option> ")

  fltRes = -1.0

  if(int(option) == 1):
    fltRes = float(first) + float(second)
  elif(int(option) == 2):
    fltRes = float(first) - float(second)
  elif(int(option) == 3):
    fltRes = float(first) * float(second)
  elif(int(option) == 4):
    fltRes= float(first) / float(second)
  elif(int(option) == 5):
    fltRes= summation( int(first), int(second) )
  elif(int(option) == 6):
    fltRes= product( int(first), int(second) )
  else:
    fltRes= 4/3 * float(first) * float(second) * float(second) * float(second)

  #print("\nResult: " + str(fltRes))
  print("\nCalculated result is: %.2f" % fltRes)

  isContinue = input("Do you want to continue?[y/n]")