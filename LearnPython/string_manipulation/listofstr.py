# learning list, set and tuple
import gc

thislist = ["apple", "banana", "orange", "apple", "orange"]
print("\n")
print(thislist)
convert2tuple = ("This is a tuple","contains","fruits") # tuple can be used to hold a single record
convert2set = set(thislist) # set can be used to hold multiple records but no duplicates allowed
set2freeze = frozenset(thislist) # set can be used to hold multiple records but no duplicates allowed
set2order = sorted(thislist) # set can be used to hold multiple records but no duplicates allowed

print(convert2set)
print(convert2tuple)
print(set2freeze)
print(set2order.append("banana")) # returns None after appending 'banana'

print("\n")
for word in convert2tuple:
    print(word, end=" ")   
print("\n")
for word in convert2set:
    print(word.capitalize(), end=" ")  
print("\n") 
for word in set2order:
    print(word.capitalize(), end=" ")

print("\n")
# print(thislist[0:3]) 
# del thislist[0:3] # delete the list
del convert2tuple # delete the tuple
del convert2set   # delete the set
del set2freeze    # delete the frozenset
gc.collect()  #  gc.collect() are the available methods to clear the memory  
