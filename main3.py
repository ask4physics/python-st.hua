import MathsModule3 as MM

isContinue = "y"

while isContinue == "y":

  print("My First Console Calculator\n")

  first = input("Enter First Number: ")
  second = input("Enter Second Number: ")

  print("\nSelect the operation you want to perform:\n\n====\n1. Sum\n2. Subtract\n3. Product\n4. Division\n5. Summation function\n6. Product function\n7. Average\n8. Volume of sphere")
  
  
  option = input("\nEnter Option> ")

  fltRes = -1.0

  BasicMath = MM.basicArithmetic(0)
  InterMath = MM.intermediateMath(0)

  if(int(option) == 1):
    fltRes = BasicMath.add(first, second)
  elif(int(option) == 2):
    fltRes = BasicMath.subtract(first, second)
  elif(int(option) == 3):
    fltRes = BasicMath.simpleproduct(first, second)
  elif(int(option) == 4):
    fltRes= BasicMath.division(first, second)
  elif(int(option) == 5):
    fltRes= InterMath.summationfunction(first, second)
  elif(int(option) == 6):
    fltRes= InterMath.productfunction(first, second)
  elif(int(option) == 7):
    fltRes= BasicMath.average(first, second)
  else:
    fltRes= BasicMath.sphere(first, second)

  #print("\nResult: " + str(fltRes))
  print("\nCalculated result is: %.2f" % fltRes)

  isContinue = input("Do you want to continue?[y/n]")