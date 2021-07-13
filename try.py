x=int(input("Type the number: "))

def check_d(n, digit):
    return(digit!=0 and n%digit==0)

def alldigitsd(n):
    temp=n
    while temp>0:
        digit=temp%10
        if((check_d(n, digit))==False):
            return False
        temp= temp//10
    return True

if (alldigitsd(x)):
    print("Yes")
else:
    print("No")