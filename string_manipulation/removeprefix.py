
links = {
    "www.youtube.com/watch?v=b1ZqKzpzZ5o",
    "www.google.com",
    "www.amazon.com",
    "www.reddit.com",
    "www.twitter.com"
}
for link in links:
    print(link)
    print(link.split(".")[1]) # split the string and print the second element

print("========== Remove Prefix  www. ===========")    

for link in links:    
    print(link.removeprefix("www.")) # remove prefix www.

print("========== Remove Suffix .com  ===========")
for link in links:
    print(link.removesuffix(".com")) # remove last 4 character # doesn't work for rest of youtube link
    