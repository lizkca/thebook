# 第三章 更多更多的例子

本章主要是通过演示如何从零开始编写一个又一个的例子，让你对click有更多的了解。
##3.1 pdftool.py
###3.1.1程序简介
让我们用click写一个简单的PDF工具程序。让人吃惊的是，这个小小的程序竟然给我本人带来实际的用处,我会经常使用到它，它也确实能带给我很大的便利。（也就是说，这不仅仅是一个用来示范的玩具程序，而且是真的在被人用。**并且实实在在给人来了益处!!!**当然你可以简单修改一下，让它更符合你的实际）
###3.1.2过程
1. 设想一下，该程序应该有些什么功能。用mit那本经典的魔法书（sicp)教的方法，假设我们已经拥有了这个程序，它会是怎么样的？我想把PDF的全部页面旋转90度:`cli rotate input.pdf -a 90`
，我想把PDF的第三页旋转-90度:`cli rotate input.pdf -a "-90" -p 3`，想把某个文件夹里的pdf合并成一个新的文件并放到默认的文件夹里: `cli meger folder`，或者放到一个指定的文件夹里:`cli meger folder -o newfolder -n result.pdf`
2. 这里要用到子命令，在click里也很简单，用@click.group()包裹一下就可以了。不理解也没关系，继续看下去就好了。
```
import click

@click.group()
def cli():
    "group cli."


@click.command()
@click.option("-f", "--path", "filepath", default="e:/a.pdf")
@click.option("-p", "--page", "page", default=0)
def rotate(filepath, page):
    "rotate command"
    click.echo("have rotated the {filepath}")


@cli.command(filepath)
@click.option("-f", "--path", "filepath", default="e:/merge")
def merge(filepath):
    "merge command"
    click.echo("have merged the {filepath} pdf files.")


@cli.command(filepath, page)
@click.option("-f", "--path", "filepath", default="e:/a.pdf")
@click.option("-p", "--page", "page", default=0)
def delete(page):
    "delete command"
    click.echo("have deleted the {page} page of the {filepath}")


if __name__ == '__main__':
    cli()
```
##3.2 git.py
###3.2.1程序简介
让我们尝试用click来写个迷你的Git程序吧。（希望你曾经用过Git。如果你确实没用过，可以先上网搜一下，并且安装、使用一下这个程序。）
###3.2.2过程
1.想一下，我们平时使用Git的一些经典情形。
```
git init
git config --global user.name "[firstname lastname]"
git config --global user.email "[valid-email]"
git clone [url]
git add [file]
git reset
git diff
git diff --staged
git commit -m "[descriptive message]"
git branch
git branch [branch-name]
git checkout
git merge [branch]
git log
git log branchB...branchA
git log --follow[file]
git diff branchB...branchA
git show [SHA]
git remote add [alias] [url]
git fetch [alias]
git merge [alias]/[branch]
git pull
git rm [file]
git mv [existing-path] [new-path]
git log --stat -M
git rebase [branch]
git reset --hard [commit]
git status
git status list
git stash pop
git stash drop
```
这是[git小抄](https://education.github.com/git-cheat-sheet-education.pdf)上的关于git的命令，我们将实现一部分，剩下的作为练习，由读者你去实现。

```
""" a command line tool for git."""


import os
import click


class Repo(object):
    def __init__(self, home=None, debug=False):
        self.home = os.path.abspath(home or '.')
        self.debug = debug


@click.group()
def cli():
    "group cli."


@cli.command()
@click.option("-f", "--path", "filepath", default="e:/a.pdf")
def init(filepath):
    "init"
    click.echo("have init in the {filepath}")


@cli.command()
@click.option("-f", "--path", "filepath", default="e:/merge")
@click.option("--global", "global_", type=(str, str)) 
def config(filepath,global_):
    "config"
    click.echo("have merge the {filepath} pdffiles.")
    click.echo("have set{global_[0]) to {global_[1]")


@cli.command()
@click.option("-f", "--path", "filepath", default="e:/a.pdf")
@click.option("-p", "--page", "page", default=0)
def clone():
    "clone"
    click.echo("have clone}")


@cli.command()
@click.option("-p", "--page", "page", default=0)
@click.option("-f", "--path", "filepath", default="e:/a.pdf")
def add():
    "add"
    click.echo("have add}")


def reset():
    pass


def diff():
    pass

 
@cli.command()
@click.option("-m", "--message", multiple=True)
def commit(message):
    "commit"
    click.echo("you have commit with the message {message}")


def branch():
    pass


def checkout():
    pass


def merge():
    pass

def log():
    pass

def show():
    pass

def remote():
    pass


def fetch():
    pass

def merge():
    pass


def pull():
    pass


def rm():
    pass


def mv():
    pass


def rebase():


def reset():
    

def status():
    pass

if __name__ == '__main__':
    cli()
```
2.
##3.3 simmarket.py
###3.3.1程序简介
让我们尝试用click写个游戏程序吧。（当然这是个命令行游戏，对于这一点你不会感到奇怪吧。）尽管click的官方文档从来没说过它可以用来写游戏。
###3.3.2过程
该怎么实现这个东西。现在好像没什么头绪。让我们先写个，最简单的，你觉得这个程序是啥样的。（这里有一个要点很重要，哪怕你一点头绪都没，但写个简单的，写一点点东西出来，比你啥都都不写，差距很大。你写出来一点点东西，然后你看着你写出来的，会帮助到你写更多的东西。这点很重要。）
```

"""a cli game,use keyboard a lot."""

import click
import random

commodity = {"water": 100,"book": 30, "car": 1000, "dog": 50}

def need_cmd():
    for k, v in commodity.items():
        click.echo(k,v)
        click.echo("what's your choice?")
        print(commodity)
 

@click.command()
@click.option(
    "--cmd", prompt="please keep typing the f j key.", help="keep what use typing"
)
def cli(cmd):
    click.echo(f"you have typed {cmd} key.")


if __name__ == "__main__":
    cli()
    need_cmd()

```
##3.4 everyday.py
###3.4.1程序简介
让我们写个每天自我评分的程序，记录下每天为实现目标的波形。
```
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

```
##3.5 learn.py
让我们尝试用click来写个帮助学习和练习click的程序吧。
##3.6 tar.py
尝试编写一个压缩，解压缩的程序
##3.7 navi.py
###3.7.1程序简介

##3.8 bookmark.py
###3.8.1程序简介
我看到好一点的网站就喜欢把它的网址保存下来，这导致我的书签变得越来越多。我决定用click写个命令行程序，帮我定期把我的书签发布出来。
###3.8.2
##3.9 metoo.py
最后作为一个作者，我非常渴望能得到读者的反馈。你的一点点微不足道的反馈，都将是我极大的动力。让我们来写个程序metoo.py程序吧。如果你觉得本书对你有一点点帮助，请运行一下这个程序，让我知道。
##3.10 总结
通过写了这么多个click的程序。你该能感受到click的优点了吧。很多时候，写一个命令行程序，我感到更多需要思考的是如何写这个程序的逻辑本身。也就是说，如何让它变得更cli的程序你不太用思考。你用click可以很自然的让它实现，具有命令行的程序。有一个帮助，解析命令参数，并且可以嵌套，支持子命令。这正说明click的优秀。想一下，如果你要自己实现这些那该多麻烦。但是有了click，叮一声，你就有这些功能了。




