

def merge(a,b,c):
    i=0
    j=0

    for x in range(len(c)):
        if j==len(b):
            c[x::]=(a[i::])
            return c
            exit()
        elif i==len(a):
            c[x::]=(b[j::])
            return c
            exit()
        elif a[i]<=b[j]:
            c[x]=a[i]
            i+=1
        elif a[i]>=b[j]:
            c[x]=b[j]
            j+=1
            
            
            


    print(c)

a=[1,5,5,6,7,8,9,12,16,23]
b=[1,5,6,8,90]
c=a+b

print(merge(a,b,c))
