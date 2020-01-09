#challenge 2 - sums of digit

n = 12345
def red(n):
  sums = 0
  if n < 10:
    return n
  while n >= 10:
    n = sum(int(num) for num in str(n))
  return n

#challenge 3 - Is n divisible by x and y

def is_divisible(n,x,y):
    return  n%y == 0  and n%x == 0