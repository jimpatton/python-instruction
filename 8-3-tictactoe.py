boardBoarder = "+---+---+---+"
board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
def display_board():
    boardString = boardBoarder + "\n"
    for r in range(len(board)):
        boardString += "|"
        for c in range(len(board[r])):
            boardString += f" {board[r][c]} |"
        boardString += "\n" + boardBoarder + "\n"
    print(boardString)    
# display_board()

def is_board_full():
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == " ":
                return False
    return True

def is_winner():
    winner = False
    for r in range(len(board)):
        if (board[r][0] != " " and board[r][0] == board[r][1] and board[r][1] == board[r][2]):
            print(f"Winner is {board[r][0]}")
            return True    
    for c in range(len(board[0])):
        if (board [0][c] != " " and board [0][c] == board[1][c] and board[1][c] == board [2][c]):
            print(f"Winner is {board[0][c]}")
            return True    
    if (board[0][0] != " " and board [0][0] == board[1][1] and board [1][1] == board[2][2]):
        print(f"Winner is {board[0][0]}")
        return True    
    if (board[0][2] != " " and board[0][2] == board[1][1] and board [1][1] == board [2][0]):
        print(f"Winner is {board[0][2]}")
        return True
    return False
    
def main():
    print("Tic Tac Toe")
    choice = "y"
    while (choice.lower()=="y"):
        global board
        board = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]
        winner = False
        while (not winner and not is_board_full()):
            display_board()
            print("X's turn")
            validMove = False
            while (not validMove):
                row = int(input("Enter row (1,2,3)"))-1
                col = int(input("Enter row (1,2,3)"))-1
                if (board[row][col] == " "):
                    board[row][col] = "X"
                    validMove = True
                    display_board()
                else:
                    print("Spot already taken, choose again")
                winner = is_winner()
                if winner:
                    break
            if winner or is_board_full():
                break

            print("O's turn")
            validMove = False
            while (not validMove):
                row = int(input("Enter row (1,2,3): "))-1
                col = int(input("Enter row (1,2,3): "))-1
                if (board[row][col] == " "):
                    board[row][col] = "O"
                    validMove = True
                    display_board()
                else:
                    print("Spot already taken, choose again")
                winner = is_winner()
                if winner:
                    break
            if winner or is_board_full():
                break

        if (not winner and is_board_full()):
            print("It's a tie")
            
        choice = input("Another game? (y/n): ")
if __name__ == "__main__":
    main()