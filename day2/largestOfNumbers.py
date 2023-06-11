#Largest of 2 numbers
a,b=10,20
print("a is largest") if a>b else print("b is largest")

#Largest of 3 numbers
a,b,c=10,20,30
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")