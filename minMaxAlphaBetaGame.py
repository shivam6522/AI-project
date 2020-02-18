import sys
import random

class Format:
    end = '\033[0m'
    underline = '\033[4m'

MAX=9999
MIN=-9999
        
def evaluate(sticks_left, alpha,beta,level):
    if sticks_left==1:
        if level%2==0:return 0
        else:return 1
    if level%2==0:#for max node
        sticks=0
        flag=0
        for i in range(1,4):
            if sticks_left-i>0:
                alpha = max(alpha,evaluate(sticks_left-i,alpha,beta,level+1))
                if level==0 and alpha==1 and flag==0:
                    sticks=i
                    flag=1
                if alpha>=beta:
                    #print('sticked picked by A = %d'%(i))
                    return beta
        #print('sticked picked by A = 3')
        #if level==0 and sticks==0:print('pick any random no of sticks')
        #else:
        #     if level==0:print('no of sticks to pick = ',sticks)
        if level==0:return alpha,sticks
        else:return alpha
    else:#for min node
        for i in range(1,4):
            if sticks_left-i>0:
                beta = min(beta,evaluate(sticks_left-i,alpha,beta,level+1))
                if alpha>=beta:
                    #print('sticked picked by B = %d'%(i))
                    return alpha

        #print('sticked picked by B = 3')
        return beta


print('----------WELCOME TO THE GAME OF STICKS----------\n')
print(Format.underline + 'Rules of the game are' + Format.end)
print('\n♦ It is a 2-player game.\n♦ There is a heap of sticks on a board, say n. (where n is given externally)\n♦ Each player picks up sticks alternatively.\n♦ On their turn, each player has to pick at least 1 stick and he can pick at most 3 sticks.\n♦ The one who has to pick the final stick will be the loser.\n♦ First turn will be randomly decided with toss.')

while 1:
    player=1
    choice = int(input('\nENTER YOUR CHOICE OF GAME MODE-:\n1. AI vs AI\n2. AI vs human\n3. to exit\n'))
    if choice<1 or choice>3:
        print('invalid choice')
    elif choice==1:
        n=int(input('enter the number of sticks for the game >1 or <32 or 53-: '))
        print('-------Its time for the toss------\n')
        if random.randrange(1,3)==1:
            print('player 1 won the toss\n')
        else:
            player=2
            print('player 2 won the toss\n')
        if n!=53 and (n<1 or n>32):print('not in the choice of sticks')
        elif n==53:
            required=49
            while n:
                if n==1:
                    if player==1:
                        print('player 2 is the winner')
                        break
                    if player==2:
                        print('player 1 is the winner')
                        break
                if player==1:
                    print('player 1\'s move\n')
                    rnd=random.randrange(1,4)
                    print('player 1 picked %d sticks'%(rnd))
                    n=n-rnd
                    print('no of sticks left = %d\n'%(n))
                    print('player 2\'s move\n')
                    st=n-required
                    print('player 2 picked %d sticks'%(st))
                    required-=4
                    n=n-st
                    print('no of sticks left = %d\n'%(n))
                if player==2:
                    print('player 2\'s move\n')
                    rnd=random.randrange(1,4)
                    print('player 2 picked %d sticks'%(rnd))
                    n=n-rnd
                    print('no of sticks left = %d\n'%(n))
                    print('player 1\'s move\n')
                    st=n-required
                    print('player 1 picked %d sticks'%(st))
                    required-=4
                    n=n-st
                    print('no of sticks left = %d\n'%(n))
                    
        else:
            while(n):
                if n==1:
                    if player==1:
                        print('player 2 is the winner')
                        break
                    if player==2:
                        print('player 1 is the winner')
                        break
                if player==1:
                    print('player 1\'s move\n')
                    (a,s)=evaluate(n,MIN,MAX,0)
                    if s>0:
                        print('player 1 picked %d sticks'%(s))
                        n=n-s
                        print('no of sticks left = ',n)
                        print('')
                    else:
                        rnd=random.randrange(1,4)
                        print('player 1 picked %d sticks'%(rnd))
                        n=n-rnd
                        print('no of sticks left = ',n)
                        print('')

                    player=2
                else:
                    print('player 2\'s move\n')
                    (a,s)=evaluate(n,MIN,MAX,0)
                    if s>0:
                        print('player 2 picked %d sticks'%(s))
                        n=n-s
                        print('no of sticks left = ',n)
                        print('') 
                    else:
                        rnd=random.randrange(1,4)
                        print('player 2 picked %d sticks'%(rnd))
                        n=n-rnd
                        print('no of sticks left = ',n)
                        print('')
                    player=1
                    

    elif choice==2:
        bot=1
        n=int(input('enter the number of sticks for the game >1 or <32 or 53-: '))
        print('-------Its time for the toss------\n')
        if random.randrange(1,3)==1:
            print('bot won the toss\n')
        else:
            bot=0
            print('Woooo you won the toss\n')
        
        if n!=53 and (n<1 or n>32):print('not in the choice of sticks')
        elif n==53:
            required=49
            while(n):
                if n==1:
                    if bot==1:
                        print('Hurrrrraah!!! you won the game')
                        break
                    if bot==0:
                        print('ooops! you lost the game..........try once more')
                        break
                if bot==1:
                    print('bot\'s move\n')
                    rnd=random.randrange(1,4)
                    print('bot  picked %d sticks'%(rnd))
                    n=n-rnd
                    print('no of sticks left = ',n)
                    print('')
                    
                    print('your move\n')
                    while 1:
                        stk=int(input('enter the number of sticks you want to pick '))
                        if stk>3 or stk<1:
                            print('oops invalid choice of sticks......see the rules')
                        else:break
                    n=n-stk
                    print('no of sticks left = ',n)
                    print('')
                else:
                    print('your move\n')
                    while 1:
                        stk=int(input('enter the number of sticks you want to pick '))
                        if stk>3 or stk<1:
                            print('oops invalid choice of sticks......see the rules')
                        else:break
                    n=n-stk
                    print('no of sticks left = ',n)
                    print('')
                    print('bots move\n')
                    st=n-required
                    print('bot picked %d sticks'%(st))
                    required-=4
                    n=n-st
                    print('no of sticks left = %d\n'%n)
        else:
            while(n):
                if n==1:
                    if bot==1:
                        print('Hurrrrraah!!! you won the game')
                        break
                    if bot==0:
                        print('ooops! you lost the game..........try once more')
                        break
                if bot==1:
                    print('bot\'s move\n')
                    (a,s)=evaluate(n,MIN,MAX,0)
                    if s>0:
                        print('bot  picked %d sticks'%(s))
                        n=n-s
                        print('no of sticks left = ',n)
                        print('')
                    else:
                        rnd=random.randrange(1,4)
                        print('bot  picked %d sticks'%(rnd))
                        n=n-rnd
                        print('no of sticks left = ',n)
                        print('')

                    bot=0
                else:
                    print('your move\n')
                    while 1:
                        stk=int(input('enter the number of sticks you want to pick '))
                        if stk>3 or stk<1:
                            print('oops invalid choice of sticks......see the rules')
                        else:break
                    n=n-stk
                    print('no of sticks left = ',n)
                    print('')
                    bot=1

    else:
        print('exiting........')
        sys.exit()