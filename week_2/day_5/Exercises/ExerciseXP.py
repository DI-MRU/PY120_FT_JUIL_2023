def display_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("*---*")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("*---*")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def player_input(player):
    while True:
        position= input(f"Player {player}: Enter a position from 1 - 9: ")
        if position.isdigit() and 1 <= int(position) <=9:
            return int(position) - 1
        print("Invalid")

def check_win(board):
    win_combination=[
        (0,1,2),(3,4,5),(6,7,8)
        ,(0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for combo in win_combination:
        if board[combo[0]] == board[combo[1]]==board[combo[2]] != " ":
            return True
    return False

def display_scoreboard(score_board):
    print("\nScoreboard")

    for player,score in score_board.items():
        print(f"Player : {player} : {score}")

def play():
    players = ["X","O"]

    score_board = {players[0]:0,players[1]:0}

    while True:
        board=[" " for _ in range(9)]
        current_player = 0

        display_board(board)

        for _ in range(9):
            position=player_input(players[current_player])

            while board[position] != " ":

                print(f"Position Taken")
                position= player_input(players[current_player])

            board[position] = players[current_player]
            display_board(board)

            if check_win(board):
                print(f"You won {players[current_player]}")
                score_board[players[current_player]] += 1
                break
            current_player = (current_player + 1) % 2
        
        else:
            print("Tie")
        
        display_scoreboard(score_board)

        while True:
            choice = input("Do you want to play again? (yes or no): ")
            if choice.lower() in ['yes','no']:
                break
            print("Invalid choice")
        if choice.lower()== 'no':
            print("Thank for playing")
            break

if __name__ == "__main__":
    play()