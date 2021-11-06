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
下一步，我想让它竖向表示。
##3.5 learn.py
###3.5.1程序简介
我发现学习编程，仅仅看文档（哪怕你看了许多遍，并且知道该怎么做了），是不够的，必须多动手练习。在初学阶段，有时候又不知怎么动手练习，那让我们尝试用click来写个程序帮我们完成这个任务吧。
###3.5.2
```
"""
learn.py
"""

import click

def learn():
    print(help(click))

if __name__ == '__main__':
    learn()
```
没太多头绪，先尽量写出简单的第一版吧，再逐步添加功能吧。
看了click的文档，我觉得需要动手练习的首先是option这一章。让我们设计点关于option的需动手的练习吧。
先把要掌握的知识点列一下。
1. Basic Value Options
2. Multi Value Options
3. Tuples as Multi Value Options
4. Multiple Options
5. Counting
6. Boolean Flags 
7. Feature Switches
8. Choice Options
9. Prompting
10. Password Prompts
11. Dynamic Defaults for Prompts
12. Callbacks and Eager Options
13. Yes Parameters
14. Values from Environment Variables
15. Multiple Values from Environment Values
16. Oter prefix Characters
17. Range Options
18. Callbacks for validation
19. Optional value 

```
import click
import random

doc = """
1. Basic Value Options
2. Multi Value Options
3. Tuples as Multi Value Options
4. Multiple Options
5. Counting
6. Boolean Flags 
7. Feature Switches
8. Choice Options
9. Prompting
10. Password Prompts
11. Dynamic Defaults for Prompts
12. Callbacks and Eager Options
13. Yes Parameters
14. Values from Environment Variables
15. Multiple Values from Environment Values
16. Oter prefix Characters
17. Range Options
18. Callbacks for validation
19. Optional value 
"""
def learn():
    choice = random.range(19)
    click.echo(choice)

if __name__ == '__main__':
    learn()


```

##3.6 zip.py
###3.6.1程序简介
尝试编写一个压缩，解压缩的程序，有时还挺实用的。
###3.6.2过程
看看外观是咋样的？
```
"""
zip.py

先看一下zip的常见用法
```
zip [-AcdDfFghjJKlLmoqrSTuvVwXyz$][-b <工作目录>][-ll][-n <字尾字符串>][-t <日期时间>][-<压缩效率>][压缩文件][文件...][-i <范本样式>][-x <范本样式>]
zip [-AcdDfFghjJKlLmoqrSTuvVwXyz$][-b <工作目录>][-ll][-n <字尾字符串>][-t <日期时间>][-<压缩效率>][压缩文件][文件...][-i <范本样式>][-x <范本样式>]
参数：

-A 调整可执行的自动解压缩文件。
-b<工作目录> 指定暂时存放文件的目录。
-c 替每个被压缩的文件加上注释。
-d 从压缩文件内删除指定的文件。
-D 压缩文件内不建立目录名称。
-f 更新现有的文件。
-F 尝试修复已损坏的压缩文件。
-g 将文件压缩后附加在既有的压缩文件之后，而非另行建立新的压缩文件。
-h 在线帮助。
-i<范本样式> 只压缩符合条件的文件。
-j 只保存文件名称及其内容，而不存放任何目录名称。
-J 删除压缩文件前面不必要的数据。
-k 使用MS-DOS兼容格式的文件名称。
-l 压缩文件时，把LF字符置换成LF+CR字符。
-ll 压缩文件时，把LF+CR字符置换成LF字符。
-L 显示版权信息。
-m 将文件压缩并加入压缩文件后，删除原始文件，即把文件移到压缩文件中。
-n<字尾字符串> 不压缩具有特定字尾字符串的文件。
-o 以压缩文件内拥有最新更改时间的文件为准，将压缩文件的更改时间设成和该文件相同。
-q 不显示指令执行过程。
-r 递归处理，将指定目录下的所有文件和子目录一并处理。
-S 包含系统和隐藏文件。
-t<日期时间> 把压缩文件的日期设成指定的日期。
-T 检查备份文件内的每个文件是否正确无误。
-u 与 -f 参数类似，但是除了更新现有的文件外，也会将压缩文件中的其他文件解压缩到目录中。
-v 显示指令执行过程或显示版本信息。
-V 保存VMS操作系统的文件属性。
-w 在文件名称里假如版本编号，本参数仅在VMS操作系统下有效。
-x<范本样式> 压缩时排除符合条件的文件。
-X 不保存额外的文件属性。
-y 直接保存符号连接，而非该连接所指向的文件，本参数仅在UNIX之类的系统下有效。
-z 替压缩文件加上注释。
-$ 保存第一个被压缩文件所在磁盘的卷册名称。
-<压缩效率> 压缩效率是一个介于1-9的数值。
```
"""

import click
import zipfile

@click.group
def cli():
    pass


@cli.command()
@click.option("-c", "--create", create, help="Create zipfile from sources.")
@click.option("-e", "--extract", extract, help="Extract zipfile into target dir.")
@click.option("-l", "--list", list_, help="Show listing of a zipfile.)
@click.option("-t", "--test", test, help="Test if a zipfile is valid.")
@click.argument()
def zip(create,extract,list_,test):
    if create in not None:
        zip_name = 

```
看了一下文档，我不知道该如何实现tar xf hhh.tar hhh 这样的用法。也就是，用tar xf 而不是tar -x -f。但在click里，怎么实现不用短横线的两个参数呢?也不知道究竟是click不支持这样的用法，还是我不会用。所以，看一下别人是怎么用click的，就很重要。带着这个问题，去看别人怎么用。
事实上zipfile.py这个标准模块里，有提供这个功能，但不是用click实现的，而是用argparse实现的。（顺便一句，zipfile.py这个标准模块，很适合初学者学习，可以多看看。）
因此我们可以
```
python -m zipfile -c monty.zip spam.txt eggs.txt
python -m zipfile -c monty.zip life-of-brian_1979/
python -m zipfile -e monty.zip target-dir/
python -m zipfile -l monty.zip
```
我们现在尝试用click来实现
```
import click
import zipfile

@click.command()
@click.argument('src', type=click.Path(exists=True))
@click.option('-c','--create',create,is_flag=True)
def zip(src,create):
    
```

##3.7 navi.py
###3.7.1程序简介
###3.7.2过程
##3.8 bookmark.py
###3.8.1程序简介
我看到好一点的网站就喜欢把它的网址保存下来，这导致我的书签变得越来越多。我决定用click写个命令行程序，帮我定期把我的书签发布出来。
###3.8.2过程
##3.9 words.py
###3.9.1
帮助学习单词。可以增加，打星，上网搜查，列出
words --add implement
words --learn implement
words --list
##3.10 metoo.py
最后作为一个作者，我非常渴望能得到读者的反馈。你的一点点微不足道的反馈，都将是我极大的动力。让我们来写个程序metoo.py程序吧。如果你觉得本书对你有一点点帮助，可以运行一下这个程序，让我知道。
##3.11 总结
通过写了这么多个click的程序。你该能感受到click的优点了吧。很多时候，写一个命令行程序，我感到更多需要思考的是如何写这个程序的逻辑本身。也就是说，如何让它变得更cli的程序你不太用思考。你用click可以很自然的让它实现，具有命令行的程序。有一个帮助，解析命令参数，并且可以嵌套，支持子命令。这正说明click的优秀。想一下，如果你要自己实现这些那该多麻烦。但是有了click，叮一声，你就有这些功能了。




