# Problem:5 - reverses of each other
# for example, "ABC" and "CBA" are reverses of each other. Assume that the two strings are not empty and have the same length.
# compare the first char of string_1 to the third char of string_2, then second char of string_1 to second char of string_2 and the third char of string_1 to the first char of string_2.

def are_reverses(string_1,string_2):
  if string_1 == string_2:
    return False
  for str_1 in range(len(string_1)):
    str_2 = len(string_2) - str_1 -1
    if string_1[str_1] != string_2[str_2]:
      return False
  return True

def reverses_2(string_1,string_2):
  if string_1 == string_2:
    return "Given strings are equal",False
  for str_1 in range(len(string_1)):
    str_2 = len(string_2) - str_1 -1
    if string_1[str_1] != string_2[str_2]:
      return "Given strings are not equal",False
  return "Given strings are equal",True
  

str_1 = "ABC"
str_2 = "CBA"
print('Are "ABC" and "CBA" reverses of each other? (should be True.)')
print(f"Are they reverses of each other? : {are_reverses(str_1,str_2)}")
print("Are 'CBA' and 'BAC' reverses of each other? (should be False.)",are_reverses("CBA","BAC"))