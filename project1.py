
from pathlib import Path
from pathlib import PurePosixPath
import os
import shutil


def search_files(path_to_directory:str) -> list:
    '''Search through directories and pull out all files'''
    list_of_directories = []
    file_list = []
    path = Path(path_to_directory)

    if path.is_dir()==True:
        for directory in path.iterdir():
            if directory.is_file()==False:
                list_of_directories.extend(search_files(directory))
            else:
                list_of_directories.append(directory)
                continue
    else:
        list_of_directories.append(path)
    return(list_of_directories)

def final_files_by_name(file_list:list, search_characteristics:str) -> list:
    '''Search through all files and pull out file(s) that match input name'''
    files = []
    for file in file_list:
        x = Path(file)
        if str(PurePosixPath(x).name) == search_characteristics[2:] + PurePosixPath(x).suffix:
            files.append(x)
        else:
            continue
    return files

def final_files_by_extension(file_list:list, search_characteristics:str) ->list:
    '''Search through all files and pull out file(s) that match input extension'''
    files = []
    search_characteristic = search_characteristics[2:]
    search_extension = ''
    if search_characteristic[0] != '.':
        search_extension = "." + str(search_characteristic)
    else:
        search_extension = str(search_characteristic)
    
    for file in file_list:
        x=Path(file)
        if str(PurePosixPath(x).suffix) == search_extension:
            files.append(file)
        else:
            continue
    return files

def final_files_by_size(file_list: list, search_sizes: int) -> list:
    '''Search through all files and pull out file(s) that are bigger than iinput size'''
    files = []
    search_size = int(search_sizes[2:])
    for file in file_list:
        size=os.path.getsize(str(file))
        if size > search_size and search_size >= 0:
            files.append(file)
        else:
            continue
    return files


def file_search_main() -> None:
    '''Searches for files and directories within the given path that match the characteristics and executes the given action'''
    path_to_directory = None
    file_list = []
    files = []
    
    while True:
        path_to_directory = input()
        if os.path.exists(str(path_to_directory)) == False:
            print("Error")
            continue
        else:
            break

    

    running = True
    while running:
        search_characteristics = input()
        search_characteristic = search_characteristics[0].upper()
        
        if search_characteristic == 'N':      
            file_list = search_files(path_to_directory)
            files = final_files_by_name(file_list, search_characteristics)
            running = False
            
        elif search_characteristic == 'E':
            file_list = search_files(path_to_directory)
            files = final_files_by_extension(file_list, search_characteristics)
            running = False
            
        elif search_characteristic == 'S':
            file_list = search_files(path_to_directory)
            files = final_files_by_size(file_list, search_characteristics)
            running = False
        
        else:
            print('ERORR')

    action = True
    while action:
        action_characteristics = input()
        action_characteristic = action_characteristics[0].upper()
        
        if action_characteristic == 'P':      
            for file in files:
                print(file)
                action = False

        elif action_characteristic == 'F':
            for file in files:
                x = Path(file)
                print_file = open(str(x), 'r')  
                print(print_file.readline())
                print_file.close()
                action = False
                
        elif action_characteristic == 'D':
            for file in files:
                shutil.copyfile(str(file), str(file)+'.dup')
                action = False

        elif action_characteristic == 'T':
            for file in files:
                x = Path(file)
                x.touch(exist_ok=True)
                action = False
                
        else:
            print('ERORR')


if __name__ == '__main__':
    file_search_main()

