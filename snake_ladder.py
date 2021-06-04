import sys
import string
import random

snakes = {
    8: 4,
    18: 1,
    26: 10,
    54: 36,
    60: 23,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}

# ladder takes you up from 'key' to 'value'
ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}

def get_players_name():
    name=input()
    return name
    
def get_dice_value(min_dice, max_dice):
    dicevalue=random.randint(min_dice,max_dice)
    print("its " +str(dicevalue)+"\n")
    return dicevalue
    
def check_snake_ladder(c_position):
    if c_position in snakes:
        c_pos=snakes[c_position]
        print("player got snake he went down to: "+str(c_pos))
    elif c_position in ladders:
        c_pos=ladders[c_position]
        print("player got ladder he moved up to: "+str(c_pos))
    else:
        c_pos=c_position
    return c_pos

def check_win(c_posi):
    if c_posi==100:
        return True
    return False

def check_invalid(current_pos, old_pos):
    if current_pos>100:
        curr_pos=old_pos
        return old_pos
    return current_pos
    
    
    
    

no_ppl=int(input("how many players? "))
no_dice=int(input("how many dices:1/2? "))
pplname={}
if no_dice==1:
    max_dice_value=6
    min_dice_value=1
else:
    max_dice_value=12
    min_dice_value=2
players=[]*no_ppl
for i in range(no_ppl):
    print("Enter Player "+str(i+1)+" name:")
    players.append(get_players_name())
print( "Each player will start with 0. Exact 100 needs to be done for the home. Lets start:")
current_position=[0]*no_ppl
for k in range(no_ppl):
    dictt={k:players[k]}
    pplname.update(dictt)
i=0
old_pos=[0]*no_ppl
while(True):
    input("Hit Enter to roll dice. "+players[i]+" is playing:")
    dice_value=get_dice_value(min_dice_value, max_dice_value)
    old_pos[i]=current_position[i]
    current_position[i]+=dice_value
    current_position[i]=check_invalid(current_position[i], old_pos[i])
    win_check=check_win(current_position[i])
    if win_check==True:
        print(players[i]+ " has reached max value and won the match")
        sys.exit()
    current_position[i]=check_snake_ladder(current_position[i])
    print(players[i]+" moved to:"+str(current_position[i]))
    if i==no_ppl-1:
        i=0
    else:
        i+=1
