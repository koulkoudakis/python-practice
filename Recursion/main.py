# POWER OF TWO RECURSIVEL


def powerOfTwo(n):
  if n == 0:
    return 1
  else:
    power = powerOfTwo(n - 1)
    return power * 2


# print(powerOfTwo(8))

# POWER OF TWO ITERATIVELY


def powerOfTwoIt(n):
  i = 0
  power = 1
  while i < n:
    power = power * 2
    i += 1
  return power


# print(powerOfTwoIt(8))


# FACTORIALS
def factorial(n):
  assert n >= 0 and int(n) == n, 'The number must be positive integer'
  if n < 2:
    return 1
  else:
    result = n * factorial(n - 1)
    return result


# print(factorial(10))


# FIBONACCI
def fib(n):
  assert n >= 0 and int(n) == n, 'n must be positive int'
  if n in [0, 1]:
    return n
  else:
    return fib(n - 1) + fib(n - 2)


# print(fib(11))


# SUM OF DIGITS IN INT
def sumdig(num):
  assert num >= 0 and int(num) == num, 'num must be positive int'
  if num == 0:
    return num
  else:
    return num % 10 + sumdig(num // 10)


# print(sumdig(123))

# POWER OF NUM


def powerOfNum(base, n):
  assert int(n) == n, 'n must be int'
  if n == 0:
    return 1
  elif n < 0:
    return 1 / base * powerOfNum(base, n + 1)
  else:
    return base * powerOfNum(base, n - 1)


# print(powerOfNum(2,-10))

# Greatest common divisor


def gcd(a, b):
  assert int(a) == a and int(b) == b, 'a and b must be int'
  if a < 0:
    a *= -1
  if b < 0:
    b *= -1

  if b == 0:
    return a
  else:
    return gcd(b, a % b)


# print(gcd(12, 32))

# Decimal to binary

def decToBin(num):
  assert int(num) == num, 'num must be int'
  if num == 0:
    return 0
  if num // 2 == 0:
    return 1
  else:
    return num % 2 + 10 * decToBin(num//2)

# print(decToBin(2))

# FIND MAX RECURSIVELY

sampleArray = [11, 4, 12, 7, 17, 8, 2, 6, 18, 24, 20, 1, 5]

def findMaxNumRec(sampleArray, n):
  if n==1:
    return sampleArray[0]
  return max(sampleArray[n-1], findMaxNumRec(sampleArray, n-1))

print(findMaxNumRec(sampleArray, len(sampleArray)))