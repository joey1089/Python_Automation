# Learn Data convertion with Panda framework
import os
import pandas as pd

people = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'Chicago'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]
os.system('cls' if os.name == 'nt'else 'clear')
print("\n ============================================ \n")
display_table = pd.DataFrame(people)
print(display_table)
print("\n ============================================ \n")
display_table.set_index('name', inplace=True)
print(display_table)
print("\n ============================================ \n")
