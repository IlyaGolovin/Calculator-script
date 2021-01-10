def add(x,y):
    return x+y
    
def sub(x,y):
    return x-y
      
def dev(x,y):
    return x/y
      
def mult(x,y):
    return x*yls
    
print("Hello! This is a simle calulator")
print("welcome aboard")
print("+-------------+")       
num1 = float(input("Enter first digit "))
num2 = float(input("Enter second digit "))
print("1 for addition")
print('2 for subtraction')
print("3 for devision")
print("4 for multiplication")
choice = int(input("Choose 1/2/3/4 ")) 

if choice == 1:
    
    a = add(num1,num2)
    print(a)
    
elif choice == 2:
     b=sub(num1,num2)
     print(b)
    
elif choice==3:
     c=dev(num1,num2)
     print(c)
    
elif choice==4:
     d=mult(num1,num2)
     print(d)
else:
     print("Hello")