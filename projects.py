import random

plays=['Rock','Paper','Scissors']

system=random.choice(plays)
player=False

while player==False:
    player=input('rock,paper,scissors:')
    
    if player==system:
        print('Tie')
    elif player=='rock':
        if system=='paper':
            print('You lose!' + system  + ' covers ' + player)
        else:
                print('You win!' + player + ' smashes ' + system)

    elif player=='paper': 
        if system=='scissors':
            print('You lose' + system + ' cuts ' +  player) 

        else :
            print(' You lose ' + player + ' covers ' + system)

    elif player=='scissors':
        if system=='rock':
            print('you lose' + system + ' smashes ' + player)
    
        else:
            print('You win'  +  player  + ' cuts ' + system)

else: 
    print('try again')
player=False
system=random.choice(plays)        
                       