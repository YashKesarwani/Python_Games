import string
import random
symbols=[]
symbols=list(string.ascii_letters)  #it will print all the alphhabets in both lowercase and upper case
card1=[0]*5
card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
samesym=random.choice(symbols)
symbols.remove(samesym)
if pos1==pos2:
    card2[pos1]=samesym
    card1[pos1]=samesym
else:
    card1[pos1]=samesym
    card2[pos2]=samesym
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while i<5:
    if i!=pos1 and i!=pos2:
        alphabet1=random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2=random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i]=alphabet1
        card2[i]=alphabet2
    i=i+1
print(card1)
print(card2)
ch=input("Enter same symbol: ")
if ch==samesym:
    print("Right")
else:
    print("Wrong")
    