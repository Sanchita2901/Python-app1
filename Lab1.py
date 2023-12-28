#python program to convert the temparature in degree Centigrade to Fahrenheit.

def a():
    c=float(input("Enter the temperature in degree:"))
    f=(c*1.8)+32
    print(" Temperature in fahrenhite:",f)

a()

#Accept two numbers and print that which one is the largest using ternary operator.
def b():
    x=int(input("Enter 1st number:"))
    y=int(input("Enter 2nd number:"))
    z=x if x>y else y
    print(" The largest number is ",z)

b()
