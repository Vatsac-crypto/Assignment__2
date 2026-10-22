a = float(input('enter your 1st number'))
b = float(input('enter your 2nd number'))
c = float(input('enter your 3rd number'))
if a>=b and a>=c:
    i = a
elif b>=a and b>=c:
    i = b
elif c>=b and c>=a:
    i = c 

print('The Largest number =', i)