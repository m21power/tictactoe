#tic tac toe game
def display_board(board):
    print('\n'*100)
    print("**GOOD LUCK!**")
    '''print('----------')'''
    print(' '+' | '+" "+' | ')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('----------')
    
    print(board[4]+' | '+board[5]+' | '+board[6])
    print(' '+' | '+" "+' | ')
    print('----------')
    
    print(board[7]+' | '+board[8]+' | '+board[9])
    print(' '+' | '+" "+' | ')
    '''print('----------')'''
   
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('enter X OR O: ').upper()
    player1=marker
    
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2)
def place_marker(board,marker,position):
    board[position]=marker
def win_check(board,mark):
    return(
        (board[1]==board[2]==board[3]==mark) or
        (board[4]==board[5]==board[6]==mark) or
        (board[7]==board[8]==board[9]==mark) or
        (board[1]==board[4]==board[7]==mark) or
        (board[2]==board[5]==board[8]==mark) or
        (board[3]==board[6]==board[9]==mark) or
        (board[1]==board[5]==board[9]==mark) or
        (board[7]==board[3]==board[5]==mark))
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'player 1'
    else:
        return 'player 2'
def space_check(board,postion):
    return board[postion]==' '
def full_boardcheck(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input("choose a position: (1-9)"))
    return position
def replay():
    choice=input("play again? Yes or No ").lower() 
    return choice=='yes'

print("WELCOME TO THE GAME: ") 
while True:
    test=[' ']*17
    

    
    #what the two players represent wether or not represent X or O
    player1_marker,player2_marker=player_input()
    #who will go first
    turn=choose_first()
    print(turn +' will go first')
    play_game=input('ready to play? y or n: ').lower()
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        
        if turn=='player 1':
            #1-look at the board
            display_board(test)
            #2-choosing the position
            position=player_choice(test)
            #3-taking that position to mark on it
            place_marker(test,player1_marker,position)
            if win_check(test,player1_marker):
                display_board(test)
                print(f'player \"{player1_marker}\" won ')
                game_on= False
            else:
                if full_boardcheck(test):
                    display_board(test)
                    print("it is a tie! ")
                    game_on= False
                else:
                    turn='player 2'
        else:
            display_board(test)
            position=player_choice(test)
            place_marker(test,player2_marker,position)
            if win_check(test,player2_marker):
                display_board(test)
                print(f'player \"{player2_marker}\" won ')
                game_on= False
            else:
                if full_boardcheck(test):
                    display_board(test)
                    print("it is a tie! ")
                    game_on= False
                else:
                    turn='player 1'
    
                

    if not replay():
        break