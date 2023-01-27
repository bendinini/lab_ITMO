def prost(n):
    d=2
    while n%d!=0:
    
        d=d+1
    return d==n

k=0
for i in range(194441,196500):
    if (prost (i)== True) and (i % 100 == 93):
        k=k+1
        print(k,'',i)
    