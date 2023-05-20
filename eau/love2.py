def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    return fibo(x-1) + fibo(x-2)


"""
créer 3 vars
a,b,c

a=0
b=1
c=a+b

a=b
b=c
c=a+b


"""

def fibo2(x):
    a=0
    b=1
    c=a+b
    for i in range(x-2):
        # print("dans la boucle")
        a=b
        b=c
        c=a+b

    # print(f"A vaut : {a}")
    # print(f"B vaut : {b}")
    # print(f"C vaut : {c}")
    return c


x= 100

print(fibo2(x))
#print(fibo(x))