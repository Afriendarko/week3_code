def swapc(x):
    swapcount = 0
    for j in range(len(x)):
        for i in range(1, len(x)-j):
            if x[i-1] > x[i]:
                swapcount += 1
                x[i-1], x[i] = x[i], x[i-1]
    return swapcount

def sortlist(x):
    swapcount = 0
    for j in range(len(x)):
        for i in range(1, len(x)-j):
            if x[i-1] > x[i]:
                swapcount += 1
                x[i-1], x[i] = x[i], x[i-1]
    return x


a = [5,6,7,4,8,'beta','alpha']
l=[]
p=[]

for x in range(len(a)):
    if type(a[x]) == int:
        l.append(a[x])
    else:
        p.append(a[x])


swl = swapc(l)
swp = swapc(p) 
sw = swl + swp

l = sortlist(l)
p = sortlist(p)

print(p + l)
print("Swapcount: ", sw+2)