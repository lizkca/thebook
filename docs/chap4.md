# 第四章 尝试学习click的源代码 
不要忘记了，click是开源的。而且click的源代码，从我的观点来说，挺适合初学者阅读的。首先，这个库是著名的flask作者的作品。代码的质量，不容置疑。其次，这是个相对比较窄的一个领域。这样的话，容易理解。如何阅读高质量的源代码是需要学习的，特别是大型的源代码库。可以说，网上到处都是宝藏，但你要想从中学习，是不容易的。对于初学者来说，一大堆东西，看了不打瞌睡就算厉害了。但是，对于初学者来说，阅读别人的是一种非常好的学习方法。总的来说，我关于学习阅读源代码的体会是：1.要反复看，多次看。2.要动手。可以编写一些测试，用一用别人的函数、类。
1. 在测试用是用`import click`来导入的。而在click里面，是用`import .utils`之类的来导入的。
第一步，我们把源代码下载下来。
第二步，我们在源代码中加入一个自己的模块。
第三步，我们导入该模块。
你已经下载了click的源代码了。你进入到src/click目录里，那就建立一个mycode.py吧。
```
import utils
print(utils.echo)
```

结果发现报错了。
ImportError: attempted relative import with no know parent package.

上网查了资料，可以这样解决，把mycode.py移到外一层文件夹中，让它与click处于同一层次。
```
import click.utils
print(click.utils.echo)
```
这次，应该可以了。
那好，我们看看utils.py的源代码，utils模块给我们提供了哪些有用的工具？我们试着用一用。

```
import click.utils
print(dir(click.utils))
```
让我们看看，里面有哪些函数，或者类是值得我们把玩一下的。make_default_short_help(help: str, max_length: int = 45) ->str 这个不错，我们研究一下。

