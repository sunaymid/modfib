def fib(n:int, a:int, b:int) -> int:
  ''' 
  Calculates nth fibonacci starting from a,b
  
  Parameters:
  n: int
  index of fibonacci
  a: int
  first term of sequence
  b: int
  second term of sequence

  Return: int 
  nth fibonacci starting from a and b
  '''
  if (n == 1):
    return a
  if (n == 2):
    return b 
  return fib(n-1, b, a+b)
def fibmod(n,m,a,b):
  '''
  Calculates nth fibonacci mod m starting from a,b

  Parameters:
  n: int
  index of fibonacci
  a: int
  first term of sequence
  b: int
  second term of sequence
  m: int
  modulus

  Return: int 
  nth fibonacci starting from a and b mod m
  '''
  return fib(n,a,b) % m
def calculatePeriod(m,a,b):
  '''
  Finds period of fibonacci mod m, starting from a and b

  Parameters:
  m: int
  Modulus
  a: int
  First term of sequence
  b: int
  Second term of sequence

  Returns: int
  Period of fibonacci mod m starting from a and b
  '''
  # reduce values mod m
  if a >= m:
    a = a % m
  if b >= m:
    b = b % m
  # 0,0 has period 1, not 2 or anything else
  if [a,b] == [0,0]:
    return 1
  l = [a,b]
  #add to l until there's a repeat
  l.append(fibmod(3, m, a, b))
  while l[-2] != a or l[-1] != b:
    l.append(fibmod(len(l)+1,m,a,b))
  return len(l) - 2
def findAllPairs(m,p):
  '''
  Given modulus and period, find all starting numbers

  Parameters: 
  m: int
  Modulus
  p: int
  Period

  Returns: list
  List of all starting numbers that have period p mod m
  '''
  l = []
  for a in range(0, m):
    for b in range(0, m):
      if calculatePeriod(m,a,b) != p:
        continue
      l.append(([a,b]))
  return(l)
def findAllPeriods(m):
  '''
  Finds all periods given a modulus m.

  Parameters: 
  m:int
  Modulus

  Returns: dictionary
  Dictionary[period] = number of starting numbers with that period
  '''
  d = {}
  for a in range(0,m):
    for b in range(0,m):
      period = calculatePeriod(m,a,b)
      if period in d:
        d[period] += 1
        continue
      d[period] = 1
  return d
def findModAndStart(period):
  '''
  Finds a modulus and starting numbers that work given period

  Parameters:
  period: int
  the period

  Returns: tuple
  A valid modulus and starting numbers (m,a,b)
  '''
  multiple = (-1)**(period-1)+fib(period-1,1,1)+fib(period+1,1,1)-1
  # m is a factor of multiple, here, just let m=multiple
  m = multiple 
  a = fib(period,1,1)
  b = m+1-fib(period-1,1,1)
  return (m,a,b)

def findFactors(num:int) -> list:
  l = []
  for i in range(1,int(num**(0.5)+1)):
    if num%i == 0:
      l.append(i)
      l.append(int(num/i))
  return l
def checkGWSS(p:int, a:int, b:int) -> boolean: 
  
