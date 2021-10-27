"""
everyday.py
keep record everyday's point.
"""

import click
import random 

def everyday():
    for i in range(90):
        print("*"*random.randint(0,10))


def test_everyday():
    pass


if __name__ == '__main__':
    everyday()
