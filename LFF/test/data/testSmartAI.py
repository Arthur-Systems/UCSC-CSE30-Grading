from board import Board
from player import Player, AI, SmartAI

if __name__ == '__main__':
    
    for i in range(3): 
        board = Board()
        player1 = SmartAI("Bob", "X", board)
        player2 = SmartAI("Alice", "O", board)       
        turn = True
        while True:
            board.show()
            if turn:
                player1.choose(board)
                turn = False
            else:
                player2.choose(board)
                turn = True
            if board.isdone():
                break
        board.show()
        if board.get_winner() == player1.get_sign():
            print(f"{player1.get_name()} is a winner!")
        elif board.get_winner() == player2.get_sign():
            print(f"{player2.get_name()} is a winner!")
        else:
            print("It is a tie!")

