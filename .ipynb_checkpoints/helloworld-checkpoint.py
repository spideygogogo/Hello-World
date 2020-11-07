#import numpy as np
#game_board = np.zeros((3,3))
print(game_board)

def getP1_step():
    while True:
        print('Please select your step Player 1')
        P1_x_value = input("Please input the place for horizontal'(0-2)'")
        P1_y_value = input("Please input the place for vertical '(0-2)'")      
        # check if it is a number 
        if P1_x_value.isdigit() and P1_y_value.isdigit():
            P1_x_value_int = int(P1_x_value)
            P1_y_value_int = int(P1_y_value)
        # check the range of P1_x_value
            if (P1_x_value_int <= 2) and (P1_x_value_int >= 0) and (P1_y_value_int <= 2) and (P1_y_value_int >= 0):
                    # if within range:
                  return P1_x_value_int , P1_y_value_int
                        # ask again continue???

                        def getP2_step():
    while True:
        print('Please select your step Player 2')
        P2_x_value = input("Please input the place for horizontal'(0-2)'")
        P2_y_value = input("Please input the place for vertical '(0-2)'")      
        # check if it is a number 
        if P2_x_value.isdigit() and P2_y_value.isdigit():
            P2_x_value_int = int(P2_x_value)
            P2_y_value_int = int(P2_y_value)
        # check the range of P2_x_value
            if (P2_x_value_int <= 2) and (P2_x_value_int >= 0) and (P2_y_value_int <= 2) and (P2_y_value_int >= 0):
                    # if within range:
                  return P2_x_value_int , P2_y_value_int
                        # ask again continue???

                        def P1_isWin(gameBoard):
    #check for row matches
    for row in range(0, 3):
        if gameBoard[row][0] == "1" and gameBoard[row][1] == "1" and gameBoard[row][2] == "1":
            return True
        if gameBoard[0][row] == "1" and gameBoard[1][row] == "1" and gameBoard[2][row] == "1":
            return True

            def P2_isWin(gameBoard):
    #check for row matches
    for row in range(0, 3):
        if gameBoard[row][0] == "2" and gameBoard[row][1] == "2" and gameBoard[row][2] == "2":
            return True
        if gameBoard[0][row] == "2" and gameBoard[1][row] == "2" and gameBoard[2][row] == "2":
            return True

            # MAIN
## setup game
#Import game board 3x3
import numpy as np
game_board = np.zeros((3,3))

BOARD_SIZE = 3
game_board = np.zeros((3,3))


p1_retry = True
p2_retry = True

game_boardFull = (game_board[0,0] > 0) and (game_board[0,1] > 0) and (game_board[0,2] > 0) and (game_board[1,0] > 0) and (game_board[1,1] > 0) and (game_board[1,2] > 0) and (game_board[2,0] > 0) and (game_board[2,1] > 0) and (game_board[2,2] > 0)
while game_boardFull == False:
    print(game_board)
    while p1_retry == True:
        getP1_step()
        if game_board[(getP1_step())] == 0:
            game_board[(getP1_step())] = 1
            p1_retry == False
            if P1_isWin(gameBoard) == True:
                Print ("Player 1 is WIN!!")
            else:
                print ("Now Player 2's turn")
        elif print('place already reserve, please select the other step'):
            p1_retry == True
    while p2_retry == True:
        getP2_step()
        if game_board[(getP2_step())] == 0:
            game_board[(getP2_step())] = 1
            p2_retry == False
            if P2_isWin(gameBoard) == True:
                Print ("Player 1 is WIN!!")
            else:
                print ("Now Player 1's turn")       
        elif print('place already reserve, please select the other step'):
            p2_retry == True
else:
    break
    print ("all place are full, Draw game")


def HelloWorld():
    print ("Hello World")

