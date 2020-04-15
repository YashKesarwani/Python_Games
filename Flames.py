import string

name1=input("Enter first name: ")
name2=input("Enter second name: ")
name1=name1.lower()
name2=name2.lower()

n1=list(name1)
n2=list(name2)
for i in range(len(n1)):
	if n1[i] in n2:
				ind=n2.index(n1[i])
				n1[i]='#'
				n2[ind]='#'

count=0
for i in range(len(n1)):
	if n1[i]!='#':
		count=count+1
for i in range(len(n2)):
	if n2[i]!='#':
		count=count+1

fl=['Friends','Love','Affection','Marriage','Enemy','Sibling']

while(len(fl)!=1):
    i=count%len(fl)-1
    if i>=0:
        r=fl[i+1:]
        l=fl[:i]
        fl=r+l
    else:
        fl=fl[:len(fl)-1]


print(str(fl[0]))
