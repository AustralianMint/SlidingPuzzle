game_list = [1, 8, 2, 4, 3, 5, 7, 6, 0]

#finding index of empty field
index_of_0 = game_list.index(0)


def print_board():
    print(game_list[:3])
    print(game_list[3:6])
    print(game_list[6:])


def move_piece(game_list, piece_num, index_of_0):
    game_list[piece_num], game_list[index_of_0] = game_list[index_of_0], game_list[piece_num]
    return(list(game_list))



print_board()

piece_num = input("enter number of tile you'd like to move: ")

move_piece(game_list, piece_num, index_of_0)


#game board
#print board
#interactioin(move piece)
#if game is done