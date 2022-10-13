def add(a,b):
 print(int(a)+int(b))

#add(2,3)

def sub(a,b):
 print(int(a)-int(b))

#sub(102,4)

def div(a,b):
 print(int(a)/int(b))

#div(150,3)

def multi(a,b):
 print(int(a)*int(b))

#multi(2,3)


a=input("Enter a value:")
b=input("Enter another value:")
c=input("Option + or - or / or * or X FOR EXIT:")
#while (c!= 0):
if (c=='+'):add(a,b)
elif(c=='-') :sub(a,b)

elif (c=='/'):div(a,b) 
elif (c=='*'):multi(a,b)
elif(c=='x'):exit()
