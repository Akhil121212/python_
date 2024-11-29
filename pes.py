
a = 2
b = 3
print(a+b,a-b,a*b,a//b,a**b,a/b,a%b)

a=5
b=6
c=8
if(a>b & a>c):
    print("a is larger")
elif(b>a & b>c):
    print("b is greater")
else:
    print("c is greater")





discount=0
amt=1200
if amt>10000:
    discount=amt*10/100
    print("amt =",amt-discount)
    amt=2500
    print('amt=',amt)
    if amt>10000:
        discount=amt*20/100
    else:
        if amt>5000:
            discount=amt*10/100
            
else:
        if amt>1000:
                discount = amt*5/100
        else:
            discount=0
            print("payabme amount=",amt-discount)
    

