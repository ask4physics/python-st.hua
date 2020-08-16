isContinue = "y"

while isContinue == "y":

  print("My First Console Calculator\n")

  first = input("Enter First Number: ")
  second = input("Enter Second Number: ")

  print("\nSelect the operation you want to perform:\n\n====\n1. Sum\n2. Subtract\n3. Product\n4. Division\n")

  option = input("Enter Option> ")

  fltRes = -1.0

  if(int(option) == 1):
    fltRes = float(first) + float(second)
  elif(int(option) == 2):
    fltRes = float(first) - float(second)
  elif(int(option) == 3):
    fltRes = float(first) * float(second)
  else:
    fltRes = float(first) / float(second)
  #print("\nResult: " + str(fltRes))
  print("\nCalculated result is: %.2f" % fltRes)

  isContinue = input("Do you want to continue?")
