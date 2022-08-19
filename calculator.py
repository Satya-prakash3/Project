a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=input('Operator')

if c== '+':
    print(a+b)
elif c== '-':
    print(a-b)
elif c== '*':
    print(a*b)
elif c== '/':
    print(a/b)
else:
    print('invalid operator')