"""
everyday.py
keep record everyday's point.
"""

import click
import random 
import pickle
from datetime import date

@click.command()
@click.argument("point")
def everyday(point):
    for i in range(90):
        click.echo("*"*int(point))



def test_everyday():
    pass


if __name__ == '__main__':
    everyday()
