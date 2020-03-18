import random
import matplotlib.pyplot as plt

account=0
x=[]
y=[]
for i in range(365):
    x.append(i+1)
    bet=random.randint(1,10)
    #bet=int(input("Your bet from 1 to 10"))
    lucky_draw=random.randint(1,10)
    #print("Bet=",bet)
    #print("Lucky draw= ",lucky_draw)
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100
    y.append(account)
    #print("Amount in account= ",account)
print("Amount in account= ",account)
plt.plot(x,y)
plt.show()
#infinity can be assogned to a variable in to python using float("inf")
#There is a poem in python which can be read by just writing import this
#we can print string stored in a variable x, n times using print(x*n)
#You can check memory usage of variable x using sys.getsizeof(x)
