#two lists for comparison
game_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 0]
finished_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

def print_board():
    print(game_list[:4])
    print(game_list[4:8])
    print(game_list[8:12])
    print(game_list[12:])


def move_piece(game_list, piece_num, index_of_0):
    #Checks left/ right square for 0
    if piece_num + 1 == index_of_0 or piece_num - 1 == index_of_0:
        game_list[piece_num], game_list[index_of_0] = game_list[index_of_0], game_list[piece_num]    
        return(list(game_list))
    #Checks top/ bottom square for 0
    elif piece_num + 4 == index_of_0 or piece_num - 4 == index_of_0:
        game_list[piece_num], game_list[index_of_0] = game_list[index_of_0], game_list[piece_num]    
        return(list(game_list))
    else:
        print("This is not a valid move... ")


#combining functions in a while loop
while game_list != finished_list:
    print_board()
    index_of_0 = game_list.index(0)
    piece_num = int(input("enter number of tile you'd like to move: ")) - 1 
    move_piece(game_list, piece_num, index_of_0)
else:
    print("You have won!")



#game board
#print board
#interactioin(move piece)
#if game is done