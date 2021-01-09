"""
This time no story, no theory. The examples below show you how to write function accum:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
"""

def accum(s):
    a = ""
    n = 0
    for i in s:
        a = a + i.upper() + i.lower() * n + "-"
        n += 1
    return a[:-1]
