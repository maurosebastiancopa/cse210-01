def main():
    decisions_list = []
    board = "1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"
    player = "x"
    print(board)
    while player == "x" or player == "o":
        user_decision = int(input(f"{player}'s turn to choose a square (1-9): "))
        while user_decision >= 1 and user_decision <= 9 and user_decision not in decisions_list:
            player, board, decisions_list = decision_display(user_decision, player, board, decisions_list)
            user_decision = 0


def decision_display(user_decision, player, board, decisions_list):
    #line 15 is used to storage the decision of the user (e.g: 1) so, the number one cannot be used again.
    decisions_list.append(user_decision)
    #line 17 allows us to find the string "1" in the "board" variable. If "1" was an int, the program wouldn't find in the variable.
    user_decision = str(user_decision)
    #if "1" were found in board, so it will be replaced by "x" or "o", depending the turn of the player.
    if user_decision in board:
        board = board.replace(user_decision, player)
    #lines 22 to 25 allows to change the player.
    if player != "o":
        player = "o"
    elif player == "o":
        player = "x"
    print(board)
    return player, board, decisions_list

if __name__ == "__main__":
    main()