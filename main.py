import MathsModule as MM

isContinue = "y"

while isContinue == "y":

  print("My First Console Calculator\n")

  first = input("Enter First Number: ")
  second = input("Enter Second Number: ")

  print("\nSelect the operation you want to perform:\n\n====\n1. Sum\n2. Subtract\n3. Product\n4. Division\n5. Summation function\n6. Product function\n7. Volume of sphere\n")
  
  
  option = input("Enter Option> ")

  fltRes = -1.0

  if(int(option) == 1):
    fltRes = MM.add(first, second)
  elif(int(option) == 2):
    fltRes = MM.subtract(first, second)
  elif(int(option) == 3):
    fltRes = MM.simpleproduct(first, second)
  elif(int(option) == 4):
    fltRes= MM.division(first, second)
  elif(int(option) == 5):
    fltRes= MM.summationfunction(first, second)
  elif(int(option) == 6):
    fltRes= MM.productfunction(first, second)
  else:
    fltRes= MM.sphere(first, second)

  #print("\nResult: " + str(fltRes))
  print("\nCalculated result is: %.2f" % fltRes)

  isContinue = input("Do you want to continue?[y/n]")