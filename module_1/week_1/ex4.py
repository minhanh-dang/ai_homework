import math

def check_n(n):
  if isinstance(n, int) == 0 and n > 0:
    return True

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

def approx_cos (x , n) :
  sum = 0
  for n in range(0, n):
    sum = sum + pow((-1),n) * pow(x, 2 * n) / factorial(2 * n)
  return sum

def approx_sin (x , n) :
  sum = 0
  for n in range(0, n):
    sum += pow((-1),n) * pow(x, 2 * n + 1) / factorial(2 * n + 1)
  return sum

def approx_sinh (x , n) :
  sum = 0
  for n in range(0, n):
    sum += pow(x, 2 * n + 1) / math.factorial(2 * n + 1)
  return sum

def approx_cosh (x , n) :
  sum = 0
  for n in range(0, n):
    sum += pow(x, 2 * n) / math.factorial(2 * n)
  return sum