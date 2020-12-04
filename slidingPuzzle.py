#two lists for comparison
game_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]
finished_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def print_board():
    print(game_list[:3])
    print(game_list[3:6])
    print(game_list[6:])


def move_piece(game_list, piece_num, index_of_0):
    game_list[piece_num], game_list[index_of_0] = game_list[index_of_0], game_list[piece_num]
    return(list(game_list))

#combining functions in a while loop
while game_list != finished_list:
    print_board()
    index_of_0 = game_list.index(0)
    piece_num = int(input("enter number of tile you'd like to move: ")) - 1 
    move_piece(game_list, piece_num, index_of_0)
    print(game_list)
else:
    print("You have won!")





#game board
#print board
#interactioin(move piece)
#if game is done