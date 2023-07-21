import re
import sys

# Check the first letter of list of words with the string if it's not matching then go for next word in the list, 
# Check if the first letter is found in the string if found go for second letter if not back out and go for the 
# next word in the list then repeat the process.
# If all is found, then add it to the found list. Print it out with dictionary list to get the value of the word. 
# And repeat for no of words in the list.

# write a code for solving a string of jumbled letters that contains words of numbers like 'one' and convert it to number like 1
for line in sys.stdin:
    string = line
    words = ['zero','one', 'two', 'three','four','five','six','seven','eight','nine']
    word2num = {'zero':0,'one':1, 'two':2, 'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    word = ''
    letter = ''
    temp = ''
    addtostr = ''
    # Check the first letter of list of words with the string if it's not matching then go for next word in the list
    # string to check reuonnoinfe
    listofString = list(string.rstrip())
    print(listofString)
    i = 0
    for word in words:
        if word[i] in listofString:
            while i < len(word) and len(word) < len(listofString):
                print(word[i])     
                addtostr +=  word[i]
                try:
                    listofString.remove(word[i])
                except ValueError:
                    print('Value not found')
                    break
                finally:    
                    print(listofString)
                    i += 1
            if addtostr != "":
                print(addtostr)
                print(word2num[addtostr])
                temp += str(word2num[addtostr])
                print(temp)
                i = 0
                addtostr = ''
            else:
                i = 0
                addtostr = ''
                continue