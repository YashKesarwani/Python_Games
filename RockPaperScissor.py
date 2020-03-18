import random
def rock_paper_scissor(num1,num2,bit1,bit2):
	p1=int(num1[bit1])%3
	p2=int(num2[bit2])%3
	if player_one[p1]==player_two[p2]:
		print("Draw")
	elif player_one[p1]=='Rock' and player_two[p2]=='Scissor':
		print("Player1 wins")
	elif player_one[p1]=='Rock' and player_two[p2]=='Paper':
		print("Player2 wins")
	elif player_one[p1]=='Paper' and player_two[p2]=='Scissor':
		print("Player2 wins")
	elif player_one[p1]=='Paper' and player_two[p2]=='Rock':
		print("Player1 wins")
	elif player_one[p1]=='Scissor' and player_two[p2]=='Rock':
		print("Player2 wins")
	elif player_one[p1]=='Scissor' and player_two[p2]=='Paper':
		print("Player1 wins")

#player_one={0:'Rock',1:'Paper',2:'Scissor'}
player_one={}
print("Player1 Enter values for different items")
for i in range(0,3):
    n=random.randint(0,2)
    while n in player_one:
            n=random.randint(0,2)
    str=input(f"Enter value for {n}")
    player_one[n]=str
#player_two={0:'Paper',1:'Rock',2:'Scissor'}
player_two={}
print("Player2 Enter values for different items")
for i in range(0,3):
    n=random.randint(0,2)
    while n in player_two:
            n=random.randint(0,2)
    str=input(f"Enter value for {n}")
    player_two[n]=str
while 1:
	num1=input('Player1, Enter your choice: ')
	num2=input('Player2, Enter your choice: ')
	bit1=int(input("Player1, Enter your bit position: "))   #Bit should be in range 0-(len(n)-1)
	bit2=int(input("Player2, Enter your bit position: "))
	rock_paper_scissor(num1,num2,bit1,bit2)
	ch=input("Do you want to continue?")
	if ch=='n':
		break
