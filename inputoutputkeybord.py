### Print 2 input from keybord in one single line

a,b=[int(x) for x in input('Enter 2 Nuber:').split()]

print('The 2 value in +', a+b)
print('The 2 value in *', a*b)

## Print 4 int value with  ',' split

a,b,c,d=[int(x) for x in input('Enter 4 number:').split(',')]

print('The 2 value in +', a+b+c+d)
print('The 2 value in *', a*b*c*d)

## Print 3 flote value with ':' split

a,b,c,=[float(x) for x in input('Enter 3 number:').split(':')]

print('The 2 value in +', a+b+c)
print('The 2 value in *', a*b*c)

