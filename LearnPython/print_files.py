# Quick way to find all the files in your current directory, ignores the git related files expect .gitignore

import re
import os


def list_out_files(directory='.'):
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
                    'File_name': file_name,
                    'Path': file_path,
                    'File_size': str(file_size)
                }
                file_list.append(file_info)
                
    return file_list

file_list = list_out_files()
os.system('cls' if os.name == 'nt' else 'clear')
print("List of Files found in the current directories!")
for files in file_list:
    # Create an empty string
    str = ""    
    # Convert the dictionary keys into a string
    # using for loop only
    for item in files:
        str += item + ": " + files[item] + " | "
        # print(type(str))
    print(str)
# print("\n===========================================================")
# for files in file_list:
#     print(files)

   
