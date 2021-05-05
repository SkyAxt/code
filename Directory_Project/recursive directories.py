from pathlib import *
import shutil
import os
'''NN:  Goal 1: Project that is able to recursively search for endless
                Paths of files and return details of each specific file depending
                on user input. Practice recursion!
        Goal 2: Use Decorators to decorate functions with specific attributes for cleaner code.
                We should only be using libraries from pathlib/shuntil/os. Practice decorators
        Future Goal : create a class that we can set to create as instances instead of relying on userinput

'''
gathered_files = []
gathered_dir = []
bypass = []


def directory_search(func):
    while True:
        try:
            print("Please type in a file name: ")
            path_object = Path(input())
            if path_object.exists():
                return func(path_object)
            else:
                print("error in path name")
        except OSError:
            print("OS Error")
        
@directory_search
'equivalent to directory_search(sec_line)
def input_line(path):
    Local_list = []
    while True:
        try:
            choices_input = input()
            return choices_input
        except OSError:
            print("OS error 2")

def recursive_search(path_object: 'list of Paths') -> list:
    
    objects_in_path = list(path_object.iterdir())
    for element in objects_in_path:
        if element.is_dir():
            gathered_dir.extend(recursive_search(element))
        elif element.is_file():
            gathered_files.append(element)

    return(gathered_files)


def sec_line(path_object: Path):
    global_list = []

    
    while True:
        choices_input = input()
    
        if _valid_sec_input(choices_input):
            if choices_input[0].lower() == "n":
                try:
                    global_list.extend(_n_input(recursive_search(path_object), choices_input))
                    if bypass[-1]:
                        return global_list
                    else:
                        print("ERROR")
                except IndexError:
                    del gathered_files[:]
                    print("ERROR")
                    
            elif choices_input[0].lower() == "e":
                try:
                    global_list.extend(_e_input(recursive_search(path_object), choices_input))
                    if bypass[-1]:
                        return global_list
                    else:
                        print("ERROR")
                except IndexError:
                    del gathered_files[:]
                    print("ERROR")
           
            elif choices_input[0].lower() == "s":
                try:
                    global_list.extend(_s_input(recursive_search(path_object), choices_input))
                    if bypass[-1]:
                        return global_list
                    else:
                        print("ERROR")
                except TypeError:
                    print("ERROR")

            else:
                print("ERROR")
        else:
            print("ERROR")
                

def third_line(interested_files: ['files']):
    while True:
        final_choice_input = input().lower()
        if _valid_third_input(final_choice_input):
            if final_choice_input[0] == "p":
                return _p_input(interested_files)
            elif final_choice_input[0] == 'f':
                return _f_input(interested_files)
            elif final_choice_input[0] == 'd':
                return _d_input(interested_files)
            elif final_choice_input[0] == 't':
                return _t_input(interested_files)
            else:
                print("ERROR")
        else:
            print("ERROR")
            
def _valid_sec_input(choices_input: str) -> bool:
    if len(choices_input[2:]) > 0 and len(choices_input[0]) == 1 and choices_input[1] == " ":
        return True
    else:
        return False
        

           

def _n_input(gathered_files: ['files'], choices_input: 'interesting file'):
    file_name = choices_input[2:]
    lst_of_files = []
    for files in gathered_files:
        str_files = os.path.basename(str(files))
        if str_files == file_name:
            lst_of_files.append(files)
            bypass.append(True)
    return lst_of_files



def _e_input(gathered_files: ['files'], choices_input: 'interesting file'):
    
    
        ext_name = choices_input[2:]
        lst_of_files = []
        
        for files in gathered_files:
            ext_files = files.suffix
            specific_ext = ext_files[1:]
        
            if specific_ext == ext_name or ext_files == ext_name:
                
                lst_of_files.append(files)
                
                bypass.append(True)

        return lst_of_files


def _s_input(gathered_files: ['files'], choices_input: 'interesting file'):
    try:
        size_input = int(choices_input[2:])
        lst_of_files = []
        
        for files in gathered_files:
            size_of_files = files.stat().st_size
            if size_of_files >= size_input:
                lst_of_files.append(files)
                bypass.append(True)
            else:
                if  type(size_input) == int:
                    bypass.append(True)

                
        
        return lst_of_files
    except ValueError:
        pass

def _valid_third_input(final_choice_input):
    if len(final_choice_input) != 1:
        return False
    else:
        return True
        
def _p_input(lst: 'list of dir'):
    for file in lst:
        print(file)

def _f_input(lst: 'list of dir'):
    try:
        for element in lst:
            print(element)
            stuff = open(str(element), "r")
            print(stuff.readline())

    
    finally:
        stuff.close()

def _d_input(lst: 'list of dir'):
    for element in lst:
        shutil.copy(str(element), str(element)+ ".dup")

def _t_input(lst: ['files']):
    for element in lst:
        os.utime(str(element), None)

'List_of_files = recursive_search(
'Files = Char_search(list_of_files(
'''
class Char_Search:
    def __init__(self, gathered_files: ['files'], choices_input: 'interesting file'):
        self.name = name
        self.gathered_files = gathered_files
        self.choices_input = choices_input

    def _e_input(self):
        ext_name = choices_input[2:]
        list_of_files =[]
        for files in gathered_files:
            ext_files = files.suffix
            specific_ext = ext_files[1:]

            if specific_ext == ext_name or ext_files == ext_name:
                list_of_files.append(files)
'''               


def valid_sec_input(choice):
    if len(choice[0]) == 1:
        return choice
    else:
        print("2nd input error")



        
