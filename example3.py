####
# Each team's file must define four tokens:
#     team_name: a string 
#     strategy_name: Opposite Player
#     strategy_description: starts with betrayal and collude betray
#     move: A function that returns 'c' or 'b'
####

team_name = 'E3'
strategy_name = 'Betray but change based on previous round'
strategy_description = '''\
Betray first round, then do the opposite'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; betray.
        return 'b'
    elif their_history[-1]=='b': #Colludes after they betray
        return 'c' 
    elif their_history[-1]=='c': #Betrays after they collude
        return 'b'