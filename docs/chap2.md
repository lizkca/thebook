# 第二章 Click初步入门 

&emsp;&emsp;click是一个命令行库。可以先试想一下，一个命令行库需要实现些什么功能呢？先来个简单的click程序。
```
import click

@click.command()
def main():
    print("hello world!"）

```
&emsp;&emsp;非常简单，直接。你导入click，在你的函数前加上一个@click.command()，就行了。再看一个官方教程（[tutorial](https://click.palletsprojects.com/en/8.0.x/)）的例子。

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
&emsp;&emsp;按照《自学是门手艺》上说的，学一样东西，可以先大概知道怎么用，具体原理后面在慢慢理解。通过看这个例子，其实也很容易大概知道该怎么用click了。现在需要做的是，可以尝试让该程序运行起来，并自己做一些改动，（例如可以照着例子，你自己也增加一个@click.option()，诸如此类）然后再运行。可以多这样操作几次。接下来，就该看一下官方的文档了。可以先粗略的看一遍。（以后需要详细的多看几遍。遇到问题，就针对具体问题再仔仔细细的看。）
