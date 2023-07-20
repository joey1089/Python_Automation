import re
import sys

# def str_sep(str1):
#     # from the jumble word get the word like 'one' and convert it to number
#     # str1 = 'one'
    
#     string = str1
#     words = ['zero','one', 'two', 'three','four','five','six','seven','eight','nine']
#     word2num = {'zero':0,'one':1, 'two':2, 'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
#     for word in words:
#         for match in re.finditer(r'.*'.join(list(word)), string):
#             print(word2num[word])
#     return word2num[word]

# for line in sys.stdin:
#     string = line
#     words = ['zero','one', 'two', 'three','four','five','six','seven','eight','nine']
#     word2num = {'zero':0,'one':1, 'two':2, 'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
#     for word in words:
#         for match in re.finditer(r'.*'.join(list(word)), string):
#             print(word2num[word])
#     print(word2num[word])

# for line in sys.stdin:
#     string = line
#     words = ['zero','one', 'two', 'three','four','five','six','seven','eight','nine']
#     word2num = {'zero':0,'one':1, 'two':2, 'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
#     word = ''
#     for i in string:
        
#         for i in words:
#             if re.search(r'.*'.join(list(word)), string):
#                 print(word2num[word])
#             break
#     for words in string:
#         for i in words:
#                 if i in string:
#                     word = i
#                     break
#                 print(word2num[word])
#         if re.search(r'.*'.join(list(word)), string):

#             print(word2num[word])
#     # print(word2num[word])

# write a code for solving a string of jumbled letters that contains words of numbers like 'one' and convert it to number like 1
for line in sys.stdin:
    string = line
    words = ['zero','one', 'two', 'three','four','five','six','seven','eight','nine']
    word2num = {'zero':0,'one':1, 'two':2, 'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    word = ''
    letter = ''
    i = 0
    for letter in string: # loop through the given string
        if letter in words[i]: # if the letter is in the word then go 
            for letter in string: # loop through the given string
                word += letter
                print(word)
                if word in words[i]:
                    print(word2num[words[i]])
                    break
            print(words[i])      
            print(word2num[words[i]])
            i += 1
            # for letter in words[i]: # loop through the first word of the list of words
            #     i += 1
            #     # print(letter)
            #     word += letter
            #     print(word)                            
            
   
    
