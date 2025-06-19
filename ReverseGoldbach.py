import math
def RevGB(N):
    if (N==2 or N%2!=0):
        raise ValueError("Invalid Value of input")
    prime1=N//2
    prime2=N//2
    flag1=False
    flag2=False
    while(flag1==False and flag2==False):
        for i1 in range(2,int(math.sqrt(prime1))+1):
            if prime1%i1==0:
                flag1=True
                break
        for i2 in range(2,int(math.sqrt(prime2))+1):
            if prime2%i2==0:
                flag2=True
                break
        if (flag1==True and flag2==False) or (flag1==False and flag2==True) or (flag1==True and flag2==True):
            flag1=False
            flag2=False
        elif flag1==False and flag2==False :
            break
        prime1-=1
        prime2+=1
    return prime1,prime2
n=int(input())
print(f"{n} can be broken into {RevGB(n)}")

        