import re
import os


def list_out_files(directory='.'):
    file_list = []
    matches = ""
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            print(f"Current File path : {file_path}")
            pattern = r".\/.git/" # regular expression to filter out .git related files
            matches = re.findall(pattern, file_path)
            print(matches)
            if matches :
                print("Igoring Git Files")
            else :
                file_size = os.path.getsize(file_path)
                file_info = {
                    'file_name': file_name,
                    'file_path': file_path,
                    'file_size': file_size
                }
                file_list.append(file_info)
                
    return file_list

file_list = list_out_files()
os.system('cls' if os.name == 'nt' else 'clear')
print("List of Files found in the current directories!")
for file_info in file_list:
    print(file_info)