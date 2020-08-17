class basicArithmetic:
  isDebug = 0
  def __init__(self, debugging):
    self.isDebug = debugging

  def add(self, firstNum, secondNum):
    res = float(firstNum) + float(secondNum)
    return res

  def subtract(self, firstNum, secondNum):
    res = float(firstNum) - float(secondNum)
    return res

  def simpleproduct(self, firstNum, secondNum):
    res = float(firstNum) * float(secondNum)
    return res

  def division(self, firstNum, secondNum):
    res = float(firstNum) / float(secondNum)
    return res

  def sphere(self, firstNum, secondNum):
    res = 4/3 * float(firstNum) * float(secondNum) * float(secondNum) * float(secondNum)
    return res

  def average(self, firstNum, secondNum):
    res = (float(firstNum) + float(secondNum))/2
    return res

class intermediateMath:
  isDebug = 0
  def __init__(self, debugging):
    self.isDebug = debugging

  def summation(self, x, y):
    res = 0.0
    for i in range(x, y + 1):
      res = res + i
    return float(res)

  def product(self, x, y):
    res = 1.0
    for i in range(x, y + 1):
      res = res * i
    return float(res)


  def summationfunction(self, firstNum, secondNum):
    res = self.summation( int(firstNum), int(secondNum) )
    return res

  def productfunction(self, firstNum, secondNum):
    res = self.product( int(firstNum), int(secondNum) )
    return res

