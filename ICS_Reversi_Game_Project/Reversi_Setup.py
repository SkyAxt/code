import tkinter


DISPLAY_FONT = ('Helvetica', 18)
GAME_FONT = ('Helvectica', 10)
class Setup:
    def __init__(self):
        self._root_window = tkinter.Tk()
        self._data = tkinter.Frame(master = self._root_window)
##        self._player_one = tkinter.StringVar()
##        self._init_color = tkinter.StringVar()
##        self._win_type = tkinter.StringVar()
        
    def widgets(self):
        '''gather the setup so we can make it expand to size'''
        self._root_window.title("REVERSI SETUP")
        self._setup().grid(row = 0 , column = 0, sticky =  tkinter.W + tkinter.W + tkinter.S + tkinter.N)
        self._root_window.rowconfigure(0,weight = 1)
        self._root_window.columnconfigure(0, weight=1)
        
    def _setup(self):
        '''get all widgets and pack this into setup'''
        self._init_text = tkinter.Label(master = self._data,text = "Complete the following data",
                                      font = DISPLAY_FONT)
        
        self._init_text.grid(row = 0, column = 0)
        self._rows_columns_setup().grid(row = 1, column = 0, sticky = tkinter.W)
        

        self._players_setup().grid(row = 2, column = 0,sticky = tkinter.W)

        self._win_less_more().grid(row = 3, column = 0, sticky = tkinter.W)
        self._data.rowconfigure(0,weight=2)
        self._data.rowconfigure(1,weight=2)
        self._data.rowconfigure(2,weight=2)
        self._data.columnconfigure(0,weight=2)
        self._data.columnconfigure(1,weight=2)

        self._input_button = tkinter.Button(master = self._data,
                                            text = "finished inputs",
                                            font = DISPLAY_FONT,
                                            command = self.submit)
        self._input_button.grid(row = 4, column = 0)
        
        return self._data

    def _players_setup(self):
        '''user will input information for reversi'''
        self._player_frame = tkinter.Frame(master = self._data)
        self._first_player = tkinter.Label(master = self._player_frame,
                                           text = "Colors:",
                                           font = DISPLAY_FONT)
        self._first_player.grid(row = 1, column = 0, sticky = tkinter.W)
        self._color_entry = tkinter.Spinbox(master = self._player_frame,
                                            values = ("BLACK","WHITE"),
                                          width = 10, font = DISPLAY_FONT)
                                            
        self._color_entry.grid(row = 1, column = 1)

        self._init_setup_label = tkinter.Label(master = self._player_frame,
                                               text = "Starting Setup",
                                               font = DISPLAY_FONT)
        self._init_setup_label.grid(row = 1, column = 2)
        self._init_setup_entry = tkinter.Spinbox(master = self._player_frame,
                                                 values = ("BLACK","WHITE"),
                                               width = 10,font = DISPLAY_FONT)
        self._init_setup_entry.grid(row = 1, column =3)
    
        return self._player_frame
    def _rows_columns_setup(self):
        '''create a frame that gathers rows and columns'''
        self._reversi_grid = tkinter.Frame(master = self._data)

        self._row_label = tkinter.Label(master = self._reversi_grid,
                                        text = "Rows:  ",
                                        font = DISPLAY_FONT)
        self._row_label.grid(row = 0, column = 0)
        self._row_entry = tkinter.Spinbox(master = self._reversi_grid,
                                        increment = 2,
                                          from_ = 4,
                                          to = 16, width = 10)
        self._row_entry.grid(row = 0, column = 1, sticky = tkinter.W)

        self._column_label = tkinter.Label(master = self._reversi_grid,
                                           text = "Columns:        ",
                                           font = DISPLAY_FONT)
        self._column_label.grid(row = 0, column = 2, sticky = tkinter.W)
        self._column_entry = tkinter.Spinbox(master = self._reversi_grid,
                                        increment = 2,
                                          from_ = 4,
                                          to = 16, width = 10)
        self._column_entry.grid(row = 0, column = 3, sticky = tkinter.W)
        

        return self._reversi_grid

    def _win_less_more(self):
        '''create a frame that gathers the user's win choice'''
        self._win_type_frame = tkinter.Frame(master = self._data)
        self._win_type_label = tkinter.Label(master = self._win_type_frame,
                                             text = "Win Type:",
                                             font = DISPLAY_FONT)
        self._win_type_label.grid(row = 0, column = 0, sticky= tkinter.W)
        self._win_type_entry = tkinter.Spinbox(master = self._win_type_frame,
                                               values= ("Win by MOST tiles",
                                                        "Win by LEAST tiles"),
                                             width = 16, font = DISPLAY_FONT)
        self._win_type_entry.grid(row = 0, column = 1, sticky= tkinter.W)
        return self._win_type_frame

    def submit(self):
        '''if valid, gather all the data and send it to the Othello gui module'''
        self.rows = int(self._row_entry.get())
        self.columns = int(self._column_entry.get())
        self.player_colors = self._color_entry.get().lower()
        self.initial_color = self._init_setup_entry.get().lower()
        self.win_type = self._win_type_entry.get().lower()
        if self._valid_inputs():
            self._root_window.destroy()
        else:
            top = tkinter.Toplevel()
            top.title("Reversi Error")
            msg = tkinter.Message(top, text = "ERROR: wrong inputs!")
            msg.pack()
            button = tkinter.Button(top, text = "Dismiss", command = top.destroy)
            button.pack()
            
        
    def _valid_inputs(self):
        
        correct_rows = 4<= self.rows<=16 and self.rows%2 ==0
        correct_columns = 4<= self.columns<=16 and self.columns%2 == 0
        correct_player = (not(self.player_colors == ' ')and (self.player_colors == ("black") or self.player_colors == ("white")))
        correct_init_color = (not(self.initial_color == ' ')and (self.initial_color == ("black") or self.initial_color == ("white")))
        correct_win_type = (self.win_type == ("win by most tiles") or self.win_type == "win by least tiles")
        return correct_rows and correct_columns and correct_player and correct_init_color and correct_win_type
    
        
        
        

    def start(self):
        self.widgets()
        self._root_window.mainloop()
