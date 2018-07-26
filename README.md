# CreatViewControllerTemplate
## 缘起
之前一直像个咸鱼一样的写 ViewController，就是所有的东西都往 ViewController 里面写。自己也知道这样写很不好，但是已经写了这么多了，很难鼓起勇气去改变。嗯嗯，直到有一天看到了[单向数据流动的函数式 View Controller](https://onevcat.com/2017/07/state-based-viewcontroller/)这篇 blog。也算给了自己一个教程，按照 blog 一步步去改变项目。但是在使用的过程中，发现 Reducer 如果也写在 ViewController 中也会导致 ViewController 变得比较大，但是分层还是很明确的。所以就把 Reducer 从 ViewController 中拿出去了，这样 ViewController 就会变得比较轻量，再加上使用[TinyCoordinator](https://github.com/cuzv/TinyCoordinator)这个简化 UITableView 和 UICollectionView 的写法的库。使得我们写出来的代码更加符合 MVC 设计模式。关于 ViewController 的写法大家可以看上面两篇 blog。到最后应该和我的写法是一样的，如果有什么不一样的想法，也可以和我一起交流，毕竟我资历尚浅，有些东西领悟不到。
## 使用
```
python3 Template.py ClassName ListType // 这里需要切换到 Template.py 的目录执行命令。ClassName 写你想创建类的名称，ListType 传 table 或者 collection，如果 ViewController不包含 UITableView 或者 UICollectionView，ListType可以不传。输出目录默认为桌面。大家可以自己修改脚本。
```
这个目录一个有四个文件，其中三个都是模板，另一个是一个 Python 脚本。我 Python 只看了一点点，因为看了正则和读写文件，所以想到写这样一个脚本。另外 Python 代码写的比较垃圾，大家不要嘲笑。我的想法就是把模板类弄好，然后读取模板类，通过正则替换。比如模板类里面类名我都是用<#ClassName#>，然后使用的时候，用传进来的 ClassName 替换<#ClassName#>。很简单，大家估计都可以看懂，然后根据自己的需求去改。
## 联系方式
使用过程中有任何问题，可以加微信交流，微信号：zdp931525538

