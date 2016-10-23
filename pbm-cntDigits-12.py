#Python

def count_digits(n) :
  x = 0
  while n > 0 :
    n = n//10
    x += 1
  return x

print(count_digits(12340))
