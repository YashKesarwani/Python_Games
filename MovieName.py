import random
movies=["infinity war","endgame","iron man","thor","captain america","doctor strange","antman","spiderman","black panther","captain marvel","the incredible hulk"]

def create_q(movie):
    l=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(l):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn
   
def is_present(letter,movie):
    count=movie.count(letter)
    if count==0:
        return False
    else:
        return True

def unlock(qn,movie,letter):
    ref=list(movie)
    qnlist=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qnlist[i]=='*':
                temp.append('*')
            else:
                temp.append(qnlist[i])
    new_qn=''.join(str(x) for x in temp)
    return new_qn
    
def play():
    player1=input("Enter the name of player1: ")
    player2=input("Enter the name of player2: ")
    pp1=0
    pp2=0
    c=True
    turn=0
    while c:
        if turn%2==0:
            print(player1," your  turn")
            pick_movie=random.choice(movies)
            question=create_q(pick_movie)
            print(question)
            modified_qn=question
            not_said=True
            flag=False
            counter=0
            while counter<7 and not_said:
                letter=input("Input a letter: ")
                if is_present(letter,pick_movie):
                    modified_qn=unlock(modified_qn,pick_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess the movie name or 2 to unlock another letter: "))
                    if  d==1:
                        ans=input("Your answer: ")
                        if ans==pick_movie:
                            pp1=pp1+1
                            print("Correct")
                            not_said=False
                            flag=True
                            print(player1,", your score: ",pp1)
                        else:
                            print("Wrong answer. Try again")
                else:
                    print("Letter not in movie name")
                counter=counter+1
            if counter==7 and flag==False:
                print("You failed to guess. We allow only 7 attempts")
            c=int(input("Press 1 to continue and 0 to exit: "))
            if c==0:
                print(player1,", your score: ",pp1)
                print(player2,", your score: ",pp2)
                print("Thank You for playing.")
                c=False
        else:
            print(player2,"Your turn")
            pick_movie=random.choice(movies)
            question=create_q(pick_movie)
            print(question)
            modified_qn=question
            not_said=True
            flag=False
            counter=0
            while counter<7 and not_said:
                letter=input("Input a letter: ")
                if is_present(letter,pick_movie):
                    modified_qn=unlock(modified_qn,pick_movie,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess the movie name or 2 to unlock another letter: "))
                    if  d==1:
                        ans=input("Your answer: ")
                        if ans==pick_movie:
                            pp2=pp2+1
                            print("Correct")
                            not_said=False
                            flag=True
                            print(player2,", your score: ",pp2)
                        else:
                            print("Wrong answer. Try again")
                else:
                    print("Letter not in movie name")
                counter=counter+1
            if counter==7 and flag==False:
                print("You failed to guess. We allow only 7 attempts")    
            c=int(input("Press 1 to continue and 0 to exit: "))
            if c==0:
                print(player2,", your score: ",pp2)
                print(player1,", your score: ",pp1)
                print("Thank You for playing.")
                c=False
        turn=turn+1
        
        
play()
