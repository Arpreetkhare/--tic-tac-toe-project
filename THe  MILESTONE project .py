

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    
test_board = ['#','X','O','X','O','X','O','X','O','X']
print(display_board(test_board)) 

def player_input():
    choice='word'
    while choice not in ['X','O']:
        if choice not in ['X','O']:
            choice=input('pick a sign between (X,O):')
    

    player1=choice
    if player1=='X':
        player2='O'
    else:
         player2='X'

    return(player1,player2)
        
print(player_input()) 

def place_marker(board, marker, position):
    board[position]=marker
test_board=['#','X','O','X','O','X','O','X','O','X']

print(place_marker(test_board,'@',8) ) 
display_board(test_board) 


def win_check(board, mark):
    return (board[1]==board[2]==board[3]==mark) or ( board[4]==board[5]==board[6]==mark) or(board[7]==board[8]==board[9]==mark) or(board[1]==board[4]==board[7]==mark)or( board[2]==board[5]==board[8]==mark)or(board[3]==board[6]==board[9]==mark)or( board[1]==board[5]==board[9]==mark)or(board[3]==board[5]==board[7]==mark)

    
    
print(win_check(test_board,'X')) 
display_board(test_board)  


import random

def chosose_first():
    flip= random.randint(0,1)
    if flip == 0:
        return'player1'
    else:
        return 'player2'
   
def space_check(board,position):
    return board[position]==''

def board_full(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    position=0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('choce a position betweenw 1 to 9:'))
        return(position)
    return board
print(player_choice([1,2,3,4,5,6,7,8,9])
)


def replay():

    return input('do you wanna play again, Enter (YES or NO)').lower().startswith('y')

print(replay())   

def gameon():
    print('welcome to tic,toc,toe')

    while  True:
      theboard=[]*10
      

      player1_marker , player2_marker= player_input()

      turn=chosose_first()

      print(turn+'will go first')

      player_game= input('wanna play Y,N')
      if player_game=='Y':
        gameon=True
      else:
        gameon=False 

      while gameon: 
        if turn=='player1':
            display_board(theboard)  
            position=player_choice(theboard)  
            place_marker(theboard,player1_marker,position)  
            if win_check(theboard,player1_marker):
                display_board(theboard)
                print('player1 has won')
                gameon=False
            else:
                if board_full(theboard):
                    display_board(theboard)
                    print('tie!')
                    gameon=False
                else:
                    turn='player2'
        else:
            turn=='player2'
            display_board(theboard)  
            position=player_choice(theboard)  
            place_marker(theboard,player2_marker,position)  
            if win_check(theboard,player2_marker):
                display_board(theboard)
                print('player2 has won')
                gameon=False
            else:
                if board_full(theboard):
                    display_board(theboard)
                    print('tie!')
                    gameon=False
                else:
                    turn='player1'
      if not replay():
        return False  
print(gameon('theboard'))      
                          





