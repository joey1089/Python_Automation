import re
import sys

def str_sep(str1):
    # from the jumble word get the word like 'one' and convert it to number
    # str1 = 'one'
    
    string = str1
    words = ['zero','one', 'two', 'three','four','five','six','seven','eight','nine']
    word2num = {'zero':0,'one':1, 'two':2, 'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    for word in words:
        for match in re.finditer(r'.*'.join(list(word)), string):
            print(word2num[word])
    return word2num[word]

for line in sys.stdin:
    str_num = line
    line = str_sep(str_num)
    print(line, end="")