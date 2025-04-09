import random

board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

numbered_board = [
    ['0','1','2'],
    ['3','4','5'],
    ['6','7','8']
]

def take_space(space,player):
    if board[space // 3][space - ((space // 3) * 3)] != '-':
        return False
    else:
        board[space // 3][space - ((space // 3) * 3)] = player
        return True
    
def main():  

    print("-~-~-~-~-~-~-~-~Tic/Tac/Toe-~-~-~-~-~-~-~-~")

    turn = -1
    game_state = 0
    # Game State Key
    # 0 = No Winner
    # 1 = Player Won
    # 2 = CPU Won

    while game_state == 0:

        if turn == -1:
            print('If you ever need to be reminded of the space number. Type "-1" to get the numbered board')
            for row in numbered_board:
                print(row)

            input('If you understand, enter anything. ')
            turn = 0

        if turn % 2 == 0:
            player_move = int(input("What space would you like to take: "))

            if player_move == -1:
                for row in numbered_board:
                    print(row)
                continue

            if take_space(player_move,'X') == False:
                print("Oops! Seems like that space is taken! Please try again.")
                continue
            else: 
                for row in board:
                    if row == ['X','X','X']:
                        game_state = 1
                
                for column in range(0,2):
                    if board[0][column] == board[1][column] and board[1][column] == board[2][column] and board[0][column] == 'X':
                        game_state = 1

                if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == 'X':
                    game_state = 1
                elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == 'X':
                    game_state = 1
                        
                turn += 1
        else:           
            if take_space(random.randint(0,8),'O') == False:
                continue
            else:
                print("CPU making move...") 

                for row in board:
                    if row == ['O','O','O']:
                        game_state = 2

                for column in range(0,2):
                    if board[0][column] == board[1][column] and board[1][column] == board[2][column] and board[0][column] == 'O':
                        game_state = 2

                if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == 'O':
                    game_state = 2
                elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == 'O':
                    game_state = 2

                turn += 1

        for row in board:
            print(row)

    if game_state == 1:
        print("You Won!")
    else:
        print("CPU Won!")