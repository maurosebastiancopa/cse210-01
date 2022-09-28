"""
Tic tac toe game
Author: Mauro Sebastian Copa
"""
def main():
    decisions_list = []
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = "x"
    board = f"{board_list[0]}|{board_list[1]}|{board_list[2]}\n-+-+-\n{board_list[3]}|{board_list[4]}|{board_list[5]}\n-+-+-\n{board_list[6]}|{board_list[7]}|{board_list[8]}"
    print(board)

    while win_condition:
        win_condition(board_list, player)
        user_decision = int(input(f"{player}'s turn to choose a square (1-9): "))
        while user_decision >= 1 and user_decision <= 9 and user_decision not in decisions_list:
            player, board, decisions_list = decision_display(user_decision, player, board, decisions_list, board_list)
            user_decision = 0


def decision_display(user_decision, player, board, decisions_list, board_list):
    #line 15 is used to storage the decision of the user (e.g: 1) so, the number one cannot be used again.
    decisions_list.append(user_decision)
    #line 17 allows us to find the string "1" in the "board" variable. If "1" was an int, the program wouldn't find in the variable.
    user_decision = str(user_decision)
    #if "1" were found in board, so it will be replaced by "x" or "o", depending the turn of the player.
    if user_decision in board:
        board = board.replace(user_decision, player)
        user_decision = int(user_decision)
        board_list[user_decision - 1] = player
    #lines 22 to 25 allows to change the player.
    if player != "o":
        player = "o"
    elif player == "o":
        player = "x"
    print(board)
    return player, board, decisions_list

def win_condition(board_list, player):

    if board_list[0] == player and board_list[1] == player and board_list[2] == player:
        print(f"{player} Won!")
        quit()
    elif board_list[3] == player and board_list[4] == player and board_list[5] == player:
        print(f"{player} Won!")
        quit()
    elif board_list[6] == player and board_list[7] == player and board_list[8] == player:
        print(f"{player} Won!")
        quit()
    elif board_list[0] == player and board_list[3] == player and board_list[6] == player:
        print(f"{player} Won!")
        quit()
    elif board_list[1] == player and board_list[4] == player and board_list[7] == player:
        print(f"{player} Won!")
        quit()
    elif board_list[2] == player and board_list[5] == player and board_list[8] == player:
        print(f"{player} Won!")
        quit()
    elif board_list[0] == player and board_list[4] == player and board_list[8] == player:
        print(f"{player} Won!")
        quit()
    elif board_list[2] == player and board_list[4] == player and board_list[6] == player:
        print(f"{player} Won!")
        quit()
    elif 1 not in board_list and 2 not in board_list and 3 not in board_list and 4 not in board_list and 5 not in board_list and 6 not in board_list and 7 not in board_list and 8 not in board_list and 9 not in board_list:
        print("you draw.")
        quit()


if __name__ == "__main__":
    main()