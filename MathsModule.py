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

def add(firstNum, secondNum):
  res = float(firstNum) + float(secondNum)
  return res

def subtract(firstNum, secondNum):
  res = float(firstNum) - float(secondNum)
  return res

def simpleproduct(firstNum, secondNum):
  res = float(firstNum) * float(secondNum)
  return res

def division(firstNum, secondNum):
  res = float(firstNum) / float(secondNum)
  return res

def summationfunction(firstNum, secondNum):
  res = summation( int(firstNum), int(secondNum) )
  return res

def productfunction(firstNum, secondNum):
  res = product( int(firstNum), int(secondNum) )
  return res

def sphere(firstNum, secondNum):
  res = 4/3 * float(firstNum) * float(secondNum) * float(secondNum) * float(secondNum)
  return res