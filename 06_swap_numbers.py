a =25
b=60
print(" The value of a and b is after swapping ",a,b)
temp=a
a=b
b=temp
# Method 2
a,b=b,a
# Method 3
a = a+b
b = a-b
a = a-b
print(" The value of a and b is before swapping ",a,b)