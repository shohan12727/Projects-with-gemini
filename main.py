print('shohan')

name = 'king shohan'

print(name)

age = 21 
print(age)

# name = input('What is your name?')

# print(f"hello, {name}")


cg = 3.32
if cg <= 4.00 and cg >= 3.5:
    print('Good')
elif cg < 3.5 and cg >= 3.3:
    print('avarage')    
else:
    print('bad cg')



def add(a,b):
    return a+b 
print(add(6,10))   



def calc(n1, n2, op):
    if(op == '+'):
        return n1 + n2
    elif(op == '-'):
        return n1 - n2
    else:
        return 'you are done'
    
# print(calc(40, 30,'+'))    

# list in python

list = [1,2,3,'shohan']
print(list)

# dictionary in python

info = {"name": "shohan", "dept": "csc"}
