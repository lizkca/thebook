# Chapter a quick look at click

click is about command line.you can think it by yourself, what a command line lib shoud do?ok, let's a simple program using click.
```
import click

@click.command()
def main():
    print("hello world!"）

```
very simple and direcly.just import click ,and add this line before your function,@click.command(),that's it.one more example from it's docs ([tutorial](https://click.palletsprojects.com/en/8.0.x/)) 

```
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
```
As a book said,you can use it before you know it.So yo shoud try to use click, follow the example,practice it (ie. you can add some @click.option(), on the example ,etc.)and make the program run.next ,you should read the tutorial.i may read it very quick this time,any more carfully next time.(you should read it much time.)

This chapter is short ,cause click just so easy to use.
