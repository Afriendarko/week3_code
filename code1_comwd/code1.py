st1 = input("Eneter first string: ")
lst1 = st1.split(" ")
lc = []
lci = []

st2 = input("Enter second string: ")
lst2 = st2.split(" ")

for i in range(len(lst1)):
    if lst1[i] in lst2:
        lc.append(lst1[i])
    
print(lc)

for i in range(min(len(lst1),len(lst2))):
    if lst1[i] == lst2[i]:
        lci.append(lst1[i])
        
print(lci)