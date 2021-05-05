import itertools

class GameState():

    def __init__(self,
                 first_input: int,
                 second_input: int,
                 type_win: "<" or ">",
                 players: (int, int),
                 init_input:(int, int)):

        '''initially define all types of input coming in from module
           user_input_lab.'''
        self._row = first_input
        self._column = second_input
        self._type = type_win
        self._first_player, self._second_player = players
        self._init_input, self._other_input = init_input


    def gameboard(self):
        '''This will set up the initally gameboard based on the init_input'''

        self.logic_board = []
        for element in range(self._column):
            self.logic_board.append(["."] * self._row)
        if self._init_input == 1:
            self.logic_board[int(len(self.logic_board)/2)][int(len(self.logic_board[0])/2)] = self._init_input
            self.logic_board[int(len(self.logic_board)/2)-1][int(len(self.logic_board[0])/2)-1] = self._init_input
            self.logic_board[int(len(self.logic_board)/2)][int(len(self.logic_board[0])/2-1)] = self._other_input
            self.logic_board[int(len(self.logic_board)/2) - 1][int(len(self.logic_board[0])/2)] = self._other_input            
            return(self.logic_board)
        
        elif self._init_input == 2:
            self.logic_board[int(len(self.logic_board)/2)][int(len(self.logic_board[0])/2)] = self._init_input
            self.logic_board[int(len(self.logic_board)/2)-1][int(len(self.logic_board[0])/2)-1] = self._init_input
            self.logic_board[int(len(self.logic_board)/2)][int(len(self.logic_board[0])/2-1)] = self._other_input
            self.logic_board[int(len(self.logic_board)/2) - 1][int(len(self.logic_board[0])/2)] = self._other_input
            return(self.logic_board)
    def _valid_on_board(self, board,row_input, column_input) -> bool:
        '''this will take each player's move every time and check
           if its within the board's length/width and if no other tiles are there'''
        #note that the row_input and column_input takes in inputs from game_move
        #so, all numbers would be numbers that have already been subtracted by 1
        return (board[row_input][column_input] == "." and
                self.on_grid(row_input, column_input))
    
    def on_grid(self, row_input, column_input):

        return (row_input < self._row and row_input >= 0 and
                column_input < self._column and column_input >= 0)

    def dup_gameboard(self,board):
        return board
    def potential_gameboard(self, board):
        return board
    def undo_dup_gameboard(self, board,row_input,column_input):
        board[row_input][column_input] = "."
        return board
    def opposite_turn(self, turn):
        if turn == 1:
            opposite_turn = 2
            return opposite_turn
        elif turn == 2:
            opposite_turn = 1
            return opposite_turn

    def game_move(self, board, player_input, turn):
        user_row_input, user_column_input = player_input
        self._first_player, self._second_player = turn      
        self._row_input = int(user_row_input) - 1
        self._column_input = int(user_column_input) - 1
        if self._valid_on_board(board, self._row_input, self._column_input):
            self.dup_gameboard(board)[self._row_input][self._column_input] = self._first_player
            
            if self._could_flip(self.dup_gameboard(board),self._row_input, self._column_input, turn) == False:
                undo = self.undo_dup_gameboard(board, self._row_input, self._column_input)
                
                return False
            else:
                
                self.new_board = self.flip_board(board)
                self.dup_gameboard(self.new_board)
                
                return True
        else:
            
            return False
    def display_gameboard(self):
        return self.new_board
    def potential_game_moves(self, board, player_input, turn):
        user_row_input, user_column_input = player_input
        first_player,second_player = turn
    
        if self._valid_on_board(board,user_row_input,user_column_input):
            self.potential_gameboard(board)[user_row_input][user_column_input] = first_player
            if self._could_flip(self.potential_gameboard(board),user_row_input,user_column_input, turn) == False:
                self.undo_dup_gameboard(self.potential_gameboard(board), user_row_input, user_column_input)
            else:
                #print("there is a potential move at {}".format((user_row_input+1, user_column_input+1)))
                self.undo_dup_gameboard(self.potential_gameboard(board), user_row_input, user_column_input)
                self._list_of_moves.append((user_row_input+1, user_column_input+1))

        else:
            pass
                #the real board will be given and the dup board will become the new board

    def every_valid_move(self, board, turn):
        column_list = []
        row_list = []
        for element in range(self._row):
            row_list.append(element)
        for element in range(self._column):
            column_list.append(element)
        self._list_of_moves = []
        possible_combinations = list(itertools.product(column_list, row_list))
        for possible_discs in possible_combinations:
            self.potential_game_moves(board, possible_discs, turn)
            
        return self._list_of_moves            
            
            
            
    
    def _could_flip(self,board,row_input, column_input, turn)-> bool:
        '''this method, will give back a boolean, stating if it will flip over
           or not'''
        first_player, second_player = turn
        default_x = row_input
        default_y = column_input

        x = row_input
        y = column_input
 
        self._could_flip_discs = []

        surrounding_discs = [[-1,0],[-1,-1],
                     [0,-1],[1,-1],
                     [1,0],[1,1],
                     [0,1],[-1,1]]
        for x_dir, y_dir in surrounding_discs:
            try:
                x = default_x
                y = default_y
                x += x_dir
                y += y_dir

                if  self.on_grid(x,y):
                    while board[x][y] == second_player:

                        x += x_dir
                        y += y_dir
                        if not self.on_grid(x,y):
                            break
                    if not self.on_grid(x,y):
                        continue
                    if board[x][y] == first_player:
                        while True:
                            
                            x -= x_dir
                            y -= y_dir
                            if x == default_x and y == default_y:
                                break

                            self._could_flip_discs.append([x,y])
            except:
                pass
        
        if len(self._could_flip_discs)==0:
            return False
        else:
            return True

    def flip_board(self, board):
        for element in self._could_flip_discs:
            row_choice, column_choice = element
            board[row_choice][column_choice] = self._first_player
            return board


    
def _count_b(board,score):
    score = 0
    for element in board:
        for item in element:
            if item == 1:
                score += 1
    return score
def winner(scores, winning_type):
    B, W = scores
    if B == W:
        return("WINNER: NONE")
    else:
        if winning_type == ">":
            if B>W:
                return("WINNER: B")
            elif W>B:
                return("WINNER: W")
        elif winning_type == "<":
            if B<W:
                return("WINNER: B")
            elif W<B:
                return("WINNER: W")
def _count_w(board, score):
    score = 0
    for element in board:
        for item in element:
            if item == 2:
                score += 1
    return score
def logic_to_colors(player_logic_color):
    current_turn, next_turn = player_logic_color
    if current_turn == 1:
        return("black")
    else:
        return("white")
        
    
        
def format_colors_for_logic(player_color):
    if player_color == "black":
        return (1,2)
    elif player_color == "white":
        return (2,1)

  
def opposite_turn(player):
    turn, opposite_turn = player
    if turn == 1:
        return (opposite_turn, turn)
    elif turn == 2:
        return (opposite_turn, turn)
    
def player_name(player):
    turn, opposite_turn = player
    if turn == 1:
        print("TURN: B")
    elif opposite_turn == 1:
        print("TURN: W")



                
                

        
