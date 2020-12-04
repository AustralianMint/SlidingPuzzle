#two lists for comparison
game_list = [1, 2, 3, 4, 5, 6, 8, 7, 0]
finished_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]

def print_board():
    print(game_list[:3])
    print(game_list[3:6])
    print(game_list[6:])

#Attempt at counting game moves
#declared vars inside move_counter() since i get 'referenced before assignment' if I don't
#Counter stops at 1 since my if statements don't cover the cases where 'round1' is e.g 1
#Checking if roundX == 0 to see which variable i need to fill with numbers. Maybe the var is already filled.
def move_counter():
    round1 = int()
    round2 = int()
    round3 = int()

    if round1 == 0:
        round1 = round1 + 1
        return round1
    elif round2 == 0:
        round1 = round2 + 1
        return round2
    else:
        round3 = round3 + 1



def move_piece(game_list, piece_num, index_of_0):
    #Checks left/ right square for 0
    if piece_num + 1 == index_of_0 or piece_num - 1 == index_of_0:
        game_list[piece_num], game_list[index_of_0] = game_list[index_of_0], game_list[piece_num]
        move_counter()    
        return(list(game_list))
    #Checks top/ bottom square for 0 
    elif piece_num + 3 == index_of_0 or piece_num - 3 == index_of_0:
        game_list[piece_num], game_list[index_of_0] = game_list[index_of_0], game_list[piece_num]
        move_counter()
        return(list(game_list))
    else:
        print("This is not a valid move... ")
    


#combining functions in a while loop
while game_list != finished_list:
    print_board()
    index_of_0 = game_list.index(0)
    piece_num = int(input("enter number of tile you'd like to move: ")) - 1 
    move_piece(game_list, piece_num, index_of_0)
    print(move_counter())
else:
    print("You have won!")

