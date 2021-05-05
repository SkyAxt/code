from pathlib import *
import shutil
import os
'''NN:  Goal 1: Project that is able to recursively search for endless
                Paths of files and return exact details of each specific file depending
                on user input.
        Goal 2: Use Decorators to decorate functions with specific attributes for cleaner code.
                We should only be using libraries from pathlib/shuntil/os
        Goal 3: create a class that we can set to create instances

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
def sec_line(path):
    Local_list = []
    while True:
        try:
            choices_input = input()
            return choices_input
        except OSError:
            print("OS error 2")

'List_of_files = recursive_search(
'Files = Char_search(list_of_files(

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
                


def valid_sec_input(choice):
    if len(choice[0]) == 1:
        return choice
    else:
        print("2nd input error")


class conditional_decorator(object):
    def _init_(self, dec, condition):
        self.decorator = dec
        self.condition = condition

    def _call_(self, func):
        
