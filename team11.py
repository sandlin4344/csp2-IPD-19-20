####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'PREDICTABLES' # Only 10 chars displayed.
strategy_name = 'Backtracker'
strategy_description = 'Checks previous rounds to see if they excessively backstabbed'
    
import random
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    betray_count=0
    for move in their_history[-14:]:
      if move =='b':
        betray_count+=1

    if betray_count>=3: # If the other player has betrayed within last 10 rounds, 
        return 'b'               # Betray.'b'
 
    else:
        if random.random()<0.001: # 5% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'         # but 90% of the time collude

