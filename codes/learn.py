"""
learn.py
"""

import click

@click.command()
@click.option("--list", is_flag=True)
def learn(list):
    for list_ in (dir(click)):
        print(list_)

if __name__ == '__main__':
    learn()
