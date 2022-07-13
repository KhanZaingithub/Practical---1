a = int(input(" Enter the coefficient of x^2 \n"))
b = int(input(" Enter the coefficient of x \n"))
c = int(input(" Enter the constant value \n"))
print(" The equation is\n",a,"x^2 +",b,"x +",c)

d = 4*a*c
sqrt_term = b*b-d
print(sqrt_term)

sqrt =(sqrt_term)**0.5

root1 = ((-b)+(sqrt))*0.5/a

root2 = ((-b)-(sqrt))*0.5/a

print(" The roots are \n",root1,"\n",root2)