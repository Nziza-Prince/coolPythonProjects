import re

board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
    
]

def declareWinner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' '  or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    
    return False 
def board_is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def printBoard(board):
    print('---+---+---')
    for row in board:
        print(f' {row[0]} | {row[1]} | {row[2]} ')
        print('---+---+---')

def main():
    currentPlayer = 'X'
    printBoard(board)
    while True:
        print(f'player {currentPlayer} turn')
        try:
            rowToInsert = int(input("Enter row to insert: "))
            columnToInsert = int(input('Enter column to insert: '))
            
            if(board[rowToInsert][columnToInsert] == ' '):
                    board[rowToInsert][columnToInsert] = currentPlayer
            else:
                print("spot already taken")

            printBoard(board)
            if declareWinner(board):
                print(f"Player {currentPlayer} wins!")
                break

            if board_is_full(board):
                print('Board is full')
                break
            
            if currentPlayer == 'O':
                currentPlayer = 'X'

            else:
                currentPlayer = 'O'
        except Exception as e:
            print(e)
            
if __name__ == '__main__':
    main()