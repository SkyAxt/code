import tkinter
import point_final as point
import reversi_logic
import Reversi_Model
import Reversi_Setup


GAME_FONT = ('Helvectica', 10)


class Reversi_Gui:
    def __init__(self):
        '''establish a an empty, where it shall append a dimensional of squares'''
        self.board = []

    def start(self):
        '''load all the data that has been gridded onto a seperate grid of its own'''
        self._start_data()
        self.reversi_gameboard().grid(
            row =0, column = 0, padx = 10, pady = 10,
            sticky= tkinter.W+ tkinter.S + tkinter.N + tkinter.E)
        self.score_turn_winner().grid(
            row = 1,column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)
        
        
        self._root_window.mainloop()

    def _start_data(self):
        '''obtain the data from Reversi_Setup.'''
        
        self._setup = Reversi_Setup.Setup()
        self._setup.start()
        
        self._rows = self._setup.rows
        self._columns = self._setup.columns
        self._win_type = self._setup.win_type
        
        self._player_colors_ = self._setup.player_colors
        self._initial_color_ = self._setup.initial_color
        #self._player_colors and self._initial_color are tuples, must create a method to unpack
        self._player_colors = (reversi_logic.format_colors_for_logic(self._player_colors_))
        self._initial_color = (reversi_logic.format_colors_for_logic(self._initial_color_))
        self._gamestate = reversi_logic.GameState(self._rows,
                                                  self._columns,
                                                  self._win_type,
                                                  self._player_colors,
                                                  self._initial_color)
        if self._win_type == "win by most tiles":
            self._win_type = ">"
        elif self._win_type == "win by least tiles":
            self._win_type = "<"
        
        
        
        
        
        
    def draw_gameboard(self):
        '''obtain the coordinates from Reversi_model using point to make it
           porpotional to the canvas'''
        self._canvas.delete(tkinter.ALL)
        self._w_score.set(reversi_logic._count_w(self.gameboard[-1],0))
        self._b_score.set(reversi_logic._count_b(self.gameboard[-1],0))
        for y_values in range(self._gamestate._row):
            for x_values in range(self._gamestate._column):
 
                minimum_x = x_values/self._gamestate._column
                minimum_y = y_values/self._gamestate._row
                maximum_x = (x_values + 1)/ self._gamestate._column
                maximum_y = (y_values + 1)/ self._gamestate._row


                top_left_point = point.from_frac(minimum_x, minimum_y)
                bot_right_point = point.from_frac(maximum_x,maximum_y)
                
                canvas_width = self._canvas.winfo_width()
                canvas_height = self._canvas.winfo_height()

        
                canvas_top_left_x,canvas_top_left_y = top_left_point.pixel(
                    canvas_width, canvas_height)
                canvas_bottom_right_x,canvas_bottom_right_y = bot_right_point.pixel(
                    canvas_width, canvas_height)
                
                


                color = "silver"

                if self.gameboard[-1][y_values][x_values] == 1:
                    color = "black"
                elif self.gameboard[-1][y_values][x_values] == 2:
                    color = "white"
                

                self.board.append(Reversi_Model.Model(top_left_point,
                                                     bot_right_point,
                                                     canvas_width,
                                                     canvas_height,
                                                     x_values,
                                                     y_values))
                self._canvas.create_rectangle(canvas_top_left_x, canvas_top_left_y,
                                              canvas_bottom_right_x, canvas_bottom_right_y,
                                              fill = "gray")
                self._canvas.create_oval(canvas_top_left_x, canvas_top_left_y,
                                         canvas_bottom_right_x, canvas_bottom_right_y,
                                         fill = color)
        
                                 
    def _clicked_button(self, event):
        '''when button is clicked, obtain the x and y info, and use those values
           for the logic board, which will be used later to configure'''
        x = (event.x)
        y = (event.y)
        
        for element in self.board:
            if element.position(x,y):
                
                every_valid_move = self._gamestate.every_valid_move(
                    self.gameboard[-1],self._player_colors)
                every_other_valid_move = self._gamestate.every_valid_move(
                    self.gameboard[-1],(reversi_logic.opposite_turn(self._player_colors)))
                
                    #this happens when no more valid move from other player
                    #instantly switch players turn. if other player can't go,
                    #break and raise a winner immediately.
                game_move = self._gamestate.game_move(self.gameboard[-1],
                                                          (element._y,element._x),
                                                          self._player_colors)
                
                    
                if game_move == False:

                    pass
                else:
                    total_move = self._gamestate.display_gameboard()
                    
                    self._player_colors = reversi_logic.opposite_turn(self._player_colors)
                    self._colors_for_turn = reversi_logic.logic_to_colors(self._player_colors)
                    self._current_color.set(self._colors_for_turn)
                    self.gameboard.append(total_move)

                    self.draw_gameboard()
                    
        if len(every_valid_move) ==0 and len(every_other_valid_move) == 0:
            '''in the case where both players run out of turn, a winner is raised'''
            
            top = tkinter.Toplevel()
            top.title("Reversi Gameover")
            msg = tkinter.Message(top,
                                  text = "GAME OVER\nwinner: {}".format(
                                      reversi_logic.winner(
                                          (reversi_logic._count_w(self.gameboard[-1],0),reversi_logic._count_b(self.gameboard[-1],0)),
                                          self._win_type)))
            msg.pack()
            button = tkinter.Button(top, text = "Dismiss", command = top.destroy)
            button.pack()
        
            


                
                    
                
            
        
        
    def _on_resize(self, event):
        self.draw_gameboard()                
                
    def reversi_gameboard(self):
        '''layout the information so we can constantly obtain the score later'''
        self._root_window = tkinter.Tk()
        self._root_window.title("REVERSI GUI")
        self._b_score = tkinter.IntVar()
        self._w_score = tkinter.IntVar()
        self._winner = tkinter.StringVar()
        self._current_color = tkinter.StringVar()
        self.gameboard = [self._gamestate.gameboard()]
        
        self._current_color.set(reversi_logic.logic_to_colors(self._player_colors))

        self._canvas = tkinter.Canvas(master = self._root_window,
                                      width = 250, height = 250)
        self._root_window.rowconfigure(0, weight= 1)
        self._root_window.columnconfigure(0, weight =1)
        
    
        self._canvas.bind('<Configure>',self._on_resize)
        self._canvas.bind('<Button-1>',self._clicked_button)
        
        return self._canvas
    def score_turn_winner(self):
        '''this method just takes in values from the game while being looped
           so we can find the information needed to grid into info for user'''

        self.root_frame = tkinter.Frame(master = self._root_window)
        self.white_label = tkinter.Label(
            master = self.root_frame, text = "white:",
            font = GAME_FONT)
        self.white_label.grid(row = 0, column = 0)
        self.w_score_label = tkinter.Label(
            master = self.root_frame, textvariable = self._w_score,
            font = GAME_FONT)
        self.w_score_label.grid(row = 0, column = 1)
        
        self.black_label = tkinter.Label(
            master = self.root_frame, text = "black: ",
            font = GAME_FONT)
        self.black_label.grid(row = 0, column = 2)
        
        self.b_score_label = tkinter.Label(
            master = self.root_frame, textvariable = self._b_score,
            font = GAME_FONT)
        self.b_score_label.grid(row = 0, column = 3)
        self.turn_option_label = tkinter.Label(
            master = self.root_frame,
            text = "current turn:",
            font = GAME_FONT)
        self.turn_option_label.grid(row = 1,column = 0)
        self.turn_label = tkinter.Label(
            master = self.root_frame,
            textvariable =self._current_color,
            font = GAME_FONT)
        self.turn_label.grid(row = 1, column = 1)

        
        return self.root_frame
        
        

                                                 
                                                 
        
    

    
if __name__ == "__main__":
    x = Reversi_Gui()
    x.start()
