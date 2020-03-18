import random
doors=[0]*3
goatdoor=[0]*2
swap=0
dont_swap=0
j=0
while j<10:
    x=random.randint(0,2)
    doors[x]='Bmw'
    for i in range(0,3):
    if i==x:
        continue
    else:
        doors[x]='Goat'
        goatdoor.append(i)
    choice=int(input("Enter your choice: "))
    door_open=random.choice(goatdoor)
    while door_open==choice:
    door_open=random.choice(goatdoor)
    ch=input("Do you want to swap? ")
    if ch=='y':
    if doors[choice]=='Goat':
        print("Player Wins!")
        swap=swap+1
    else:
        print("Player loses!")
    else:
    if doors[choice]=='Goat':
        print("Player loses!")
    else:
        print("Player Wins")
        dont_swap=dont_swap+1
    j=j+1

print(swap," ",dont_swap)      
