import getopt, sys

def fizzbuzz (val):
   for i in range(0, int(val)):
      if i % 2 ==0 and i % 3 ==0:
       print  'fizzbuzz'
      elif i % 2 ==0 :
       print  'fizz'
      elif i  % 3 == 0:
       print   "buzz"
      else:
       print i
val=sys.argv[1]
fizzbuzz(val)

print  val
#a, b = 0, 1
#while b < 10:
# print b
# a, b = b, a+b

