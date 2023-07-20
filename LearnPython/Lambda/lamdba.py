# Learning Lambda - it reduces the code and makes it more readable - like instead of writing a 
# function - def add(x,y): return x+y - we can write it as - lambda x,y: x+y

add = lambda x,y: x+y
print(add(2,3))
print(add(2,3)*2)


# Another example -
names = ['alex', 'ben', 'justin' ,'chris', 'dave']
sort_names = sorted(names, key=lambda x: len(x)) # sorts the names based on the length of the name
print(sort_names)