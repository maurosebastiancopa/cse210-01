def main():
    decisions_list = []
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player = "x"
    board = f"{board_list[0]}|{board_list[1]}|{board_list[2]}\n-+-+-\n{board_list[3]}|{board_list[4]}|{board_list[5]}\n-+-+-\n{board_list[6]}|{board_list[7]}|{board_list[8]}"
    player_one = "x"
    player_two = "o"
    print(board)
    while player == "x" or player == "o":
        user_decision = int(input(f"{player}'s turn to choose a square (1-9): "))
        while user_decision >= 1 and user_decision <= 9 and user_decision not in decisions_list:
            player, board, decisions_list = decision_display(user_decision, player, player_one, player_two, board, decisions_list, board_list)
            win_condition(board_list, player_one, player_two)
            user_decision = 0


def decision_display(user_decision, player, player_one, player_two, board, decisions_list, board_list):
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
        player = player_two
    elif player == "o":
        player = player_one
    print(board)
    return player, board, decisions_list

def win_condition(board, player_one, player_two):

    if board[0] == player_one and board[1] == player_one:
        quit()

    if board[0] == player_one and board[1] == player_one and board[2] == player_one:
        quit()
    elif (board[3] == player_one and board[4] == player_one and board[5] == player_one):
        pass
    elif (board[6] == "x" and board[7] == "x" and board[8] == "x"):
        pass
    elif (board[0] == "x" and board[3] == "x" and board[6] == "x"):
        pass
    elif (board[1] == "x" and board[4] == "x" and board[7] == "x"):
        pass
    elif (board[1] == "x" and board[5] == "x" and board[8] == "x"):
        pass
    elif (board[0] == "x" and board[4] == "x" and board[8] == "x"):
        pass
    elif (board[2] == "x" and board[4] == "x" and board[6] == "x"):
        pass

    """
    if (board[1], board[2]) == player_one:
        print("you win")
        quit()
    """
if __name__ == "__main__":
    main()