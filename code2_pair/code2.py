# from collections import Counter
raw='raw'
ag='ag'
aj='aj'
l = [1,1,2,3,2,4,3,4,4,4,3,raw,raw,raw,ag,aj,ag,aj,7,6]

#n = int(input("Enter the number of elements: "))

# for i in range(n):
#     lin = input("Enter element: ")
#     l.append(lin)


# dt = Counter(l)
x = dict((x,l.count(x)) for x in set(l))
# print(x)

x = dict((x,l.count(x)) for x in set(l))
x1 = list(x.items())
x2=[]
s3=[]
for i in range(len(x1)):
    if x1[i][1] % 2==0 or x1[i][1] > 2:
        nu = 'even'
        x2.append((x1[i][0],x1[i][0])* (x1[i][1]//2))

        
        
    
    if x1[i][1] % 2!=0:
        s3.append(x1[i][0])
print(tuple(x2) , len(x2))
print(tuple(s3), len(s3))