# Quick way to find all the files in your current directory, ignores the git related files expect .gitignore
import pandas
import re
import os


def list_out_files(directory='.'):
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
               msg = "Igoring Git Files"
            else :
                file_size = os.path.getsize(file_path)
                file_info = {
                    'File_Name': file_name,
                    'File_Path': file_path,
                    'File_Size': str(file_size)
                }
                file_list.append(file_info)
                
    return file_list

# clear the screen and start the execution
os.system('cls' if os.name == 'nt' else 'clear')
file_list = list_out_files()
print("List of Files found in the current directories!\n")
print("List of Files from dictionary to string using for loop:-\n")

for files in file_list:
    file_info = "" #create a empty string to later store dictionary
    for item,value in files.items():
        file_info += item + ": " + value + " | "
    print(file_info)
print("\n =========================================================== \n")
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
