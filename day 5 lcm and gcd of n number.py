def compute_hcf(x, y):
  if x > y:
      smaller = y
  else:
    smaller = x
  for i in range(1, smaller+1):
     if((x % i == 0) and (y % i == 0)):
        hcf = i 
  return hcf
num1 = int(input("Enter the value"))
num2 = int(input("Enter the value"))
print("The H.C.F. is", compute_hcf(num1, num2))
LCM
def compute_lcm(x, y):
 if x > y:
    greater = x
 else:
    greater = y
 while(True):
   if((greater % x == 0) and (greater % y == 0)):
      lcm = greater
      break
   greater += 1
 return lcm
num1 = int(input("Enter the value"))
num2 = int(input("Enter the value"))
print("The L.C.M. is", compute_lcm(num1, num2))
  
