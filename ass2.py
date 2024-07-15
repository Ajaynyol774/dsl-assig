def union(x,y):
    r=x.copy()
    for i in y:
        if(i not in r):
            r.append(i)

    return r 

def intersection(x,y):
    r=[]

    for i in x:
        if(i in y):
            r.append(i)

    return r  
def subtract(x,y):
    r=[]

    for i in x:
        if(i not in y):
            r.append(i)

    return r 
n=int(input("Enter total no. of student: "))
a=[]
b=[]
c=[]
n_a=int(input("Enter number student who play cricket: "))
print("enter roll no.s of student who play cricket: ")
for i in range(n_a):
    x=int(input())
    a.append(x)
    
n_b=int(input("Enter number student who play badminton: "))
print("enter roll no.s of students who play badminton: ")
for i in range(n_b):
    y=int(input())
    b.append(y)
n_c=int(input("Enter number student who play football: "))
print("enter roll no.s of students who play football: ")
for i in range(n_c):
    z=int(input())
    c.append(z)

print("the required list are:")
print("cricket:",a)
print("badminton:",b)
print("football:",c)

print("student who play both cricket and badminton:",intersection(a,b))
print("student who play either cricket or badminton but not both:",subtract(union(a,b),intersection(a,b)))

print("number of student who play neither cricket nor badminton:",n-len(union(a,b)))

print("number of student who play cricket and football but not  badminton",len(union(a,b))-len(c))
print("student who do not play any game",n-len(union(c,union(a,b))))
print("student who play atleast one game",union(c,union(a,b)))
print("student who play all the game:",intersection(c,intersection(a,b)))
