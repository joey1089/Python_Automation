# Quick way to find all the files in your current directory, ignores the git related files expect .gitignore
import pandas
import pprintpp
import re
import os
import logging

def list_out_files(logger,directory='.'):
    ''' List out the files in the current directory and the child directory too.'''
    file_list = []
    matches = ""
    
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            #print(f"Current File path : {file_path}") # to be removed
            pattern = r".\/.git/" # regular expression to filter out .git related files
            matches = re.findall(pattern, file_path)
            #print(matches) # to be removed
            if matches :                
                # logger.setLevel()
                logger.info('Igoring Git Files')                
            else :
                file_size = os.path.getsize(file_path)
                file_info = {
                    'File_Name': file_name,
                    'File_Path': file_path,
                    'File_Size': str(file_size)
                }
                file_list.append(file_info)
                logging.info("Files information loaded")
                
    return file_list

def dict_str_loop(str_info, logger):
    ''' Prints out the dictionary using string through the for loop! '''
    for files in file_list:            
        for items in files:
            str_info += items +": " + files[items] +" "
    print("".join(str_info))
    return logger.info("Dictionary String looped and printed")

def pretty_print(list_files, logger):
    ''' Prints out dictionary using pretty print! '''    
    for files in file_list:
        for item,value in files.items():
            list_files += item + ": " + value + " | "
                
    # return pp.pprint(list_files) # with pretty print pprintpp
    print(pprintpp.pformat(list_files))
    return logger.info("Pretty Printed out the List")

# clear the screen and start the execution
os.system('cls' if os.name == 'nt' else 'clear')
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)          
logger = logging.getLogger() 
file_list = list_out_files(logger)
file_info = "" #create a empty string to later store dictionary
print("List of Files found in the current directories!\n")
print(" ********************************************************************************************** ")
user_input = input(str("List out using Dictionary using string enter '1' or Pretty Print '2' or Panda DataFrame '3': "))
if user_input == '1':
    print("List of Files from dictionary to string using for loop:-\n")
    dict_str_loop(file_info, logger)
    
elif user_input == '2':
    print("Do you want to see using pretty print enter-'2' : ")
    print("List of Files from dictionary using pretty print!")
    print(" ********************************************************************************************** ")
    pretty_print(file_info, logger)
        
else:
    print(" ********************************************************************************************** ")
    # cols = [ "File_name", "File_Path", "File_size"]
    print(" List out Files with Panda DataFrame")
    pd = pandas.DataFrame.from_dict(file_list)
    # pd = pandas.DataFrame.from_dict(file_list, orient='index', columns='cols') 
    # https://builtin.com/data-science/dictionary-to-dataframe
    print(pd)
    print("\n =========================================================== \n ")
    print(" List out Files with Panda DataFrame : Set Index as File name ")
    pd.set_index('File_Name', inplace=True)
    print(pd)
    print("\n")

