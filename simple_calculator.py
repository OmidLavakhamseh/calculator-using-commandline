import sys
a=float(sys.argv[1])
c=sys.argv[2]
b=float(sys.argv[3])
#c=input("Operator:")
if c=='+': 
    out=a+b
if c=='-': 
    out=a-b
if c=='/':
    out=a/b
if c=='*':
    out=a*b
print(out)