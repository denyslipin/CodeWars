"""
An isogram is a word that has no repeating letters, consecutive or 
non-consecutive. Implement a function that determines whether a string 
that contains only letters is an isogram. Assume the empty string is an 
isogram. Ignore letter case.

https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
"""


def is_isogram(string):
    word = string.lower()
    lst = list(word)
    new_lst = []
    for ch in lst:
        if ch in new_lst:
            return False
        else:
            new_lst.append(ch)
    if len(new_lst) >= 0:
        return True
