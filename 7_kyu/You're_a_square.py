"""
Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer 
that is the square of an integer; in other words, it is the product of some integer with itself.
The tests will always use some integral number, so don't worry about that in dynamic typed languages.

https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python
"""


def is_square(n):    
    return (True if n >= 0 and n == int(n ** 0.5) ** 2 else False)
