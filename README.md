# 文件结构

- exam：pdf格式的试题
- hw-desciption：hw的描述文档，也就是hw的题目
- hw01-10：家庭作业
- lab00-12：实验
- proj：项目代码

[课程网站地址](https://www.learncs.site/docs/curriculum-resource/cs61a/syllabus)
> 文件夹格式代表已完成，zip格式代表未开始，已完成的可借鉴
> 目前我还没有学习完毕，仍在更新中

---

<!-- TOC depthfrom:1 depthto:4 -->

- [文件结构](#%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84)
- [前言](#%E5%89%8D%E8%A8%80)
- [一、CS61A是什么？](#%E4%B8%80cs61a%E6%98%AF%E4%BB%80%E4%B9%88)
- [二、OK自动评分器的使用](#%E4%BA%8Cok%E8%87%AA%E5%8A%A8%E8%AF%84%E5%88%86%E5%99%A8%E7%9A%84%E4%BD%BF%E7%94%A8)
    - [使用](#%E4%BD%BF%E7%94%A8)
    - [此外](#%E6%AD%A4%E5%A4%96)
- [三、期间遇到的一些难点](#%E4%B8%89%E6%9C%9F%E9%97%B4%E9%81%87%E5%88%B0%E7%9A%84%E4%B8%80%E4%BA%9B%E9%9A%BE%E7%82%B9)
    - [写题时的方法](#%E5%86%99%E9%A2%98%E6%97%B6%E7%9A%84%E6%96%B9%E6%B3%95)
    - [hogs -> Problem 8（make_averaged函数）](#hogs---problem-8make_averaged%E5%87%BD%E6%95%B0)
    - [cats -> Problem 7](#cats---problem-7)
- [四、我认为值得注意的地方](#%E5%9B%9B%E6%88%91%E8%AE%A4%E4%B8%BA%E5%80%BC%E5%BE%97%E6%B3%A8%E6%84%8F%E7%9A%84%E5%9C%B0%E6%96%B9)
- [总结](#%E6%80%BB%E7%BB%93)

<!-- /TOC -->

---

# 前言

这里是我学习**CS61A 2024**的一些记录和心得

---

# 一、CS61A是什么？

CS61A是加州大学伯克利分校（UC Berkeley）的计算机科学导论课程。这门课程旨在教授计算机科学的基本概念和编程技能，主要使用编程语言Python。它是许多学生的第一门计算机科学课程，涵盖了从程序设计基础到数据结构和算法的内容。

CS61A通常被认为是一门非常有挑战性但也非常有价值的课程，为学生提供了扎实的编程基础和计算机科学思维方式。

主要是用Python来掌握函数式编程、面向对象以及SQL等等

# 二、OK自动评分器的使用

`py环境的配置我就不多提了，网上很多，我使用的是VS Code`

## 使用

写完函数，测试时要呼出终端，但方式不止一种，这是vs的一种方式
![请添加图片描述](https://i-blog.csdnimg.cn/direct/b68cd15d588b41ba8c5cab14e512a38f.png)
![image](https://github.com/user-attachments/assets/291feb49-e1a3-4d67-86fa-3d971da8e998)

也可以在文件夹中打开测评

![image](https://github.com/user-attachments/assets/f2acf04c-fb11-4902-a891-520201a7eb86)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/1717e7496cf14f2a8a490d048ff03262.png)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8471a855e24d4491a62dedd3ce2cd0cc.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/276dcaf00ef34ad292817e7ffa3edff7.png)

测试代码一般在文档之中都有写：

![请添加图片描述](https://i-blog.csdnimg.cn/direct/396987eba612463e9268eb2f1a3192f7.png)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/6d5752dc3f864403bcdcb29ca8094591.png)

后边加上 **--local**  表明在本地测试即可：

```python
python3 ok -q falling --local
python3 ok -q digit_distance --local
```

## 此外

1. [okpy命令生成器](https://ok-help.cs61a.org/)

3. 有一种情况是py版本太高，ok不适用了，降降版本就行了

4. 如果输入代码后报错，也可能是文件解压格式后的地址不正确

- "...\CS61A\hw\hw01\hw01.py"
- "...\CS61A\lab\lab01\lab01.py"
- "...\CS61A\proj\cats\cats.py"
- "...\CS61A\hw\hw05\hw05\hw05.py"  （错误地址）
有的时候解压完毕可能出现，两个hw05，这时就报错了
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/2567783e57824ab79b08b043eeb1f4ac.png)

# 三、期间遇到的一些难点

我不会每个都有解析的，只是记录一下我学习时遇到的，每个人遇到的可能都不太一样，但还是希望帮助一下和我问题相似的同学
当然，也可以看看我的例子，分享分享你的解法
最后，希望各位同学勤于思考，不要太懒惰哦！

## 写题时的方法

这些题嘛倒不是很难，重要的是对题意的理解，以及上下文的分析

 1. 因为是英文，所有你可能需要一款沉浸式翻译的插件
[沉浸式翻译插件网址](https://immersivetranslate.com/download/?utm_source=extension&utm_medium=extension&utm_campaign=options_nav)
 2. 首先，要明白函数的大致作用
 3. 其次，联系上下文，明白函数接收的参数是什么，返回的是什么
 4. 接着，你要根据例子，逐步理解函数内部是如何对数据进行操作的
 5. 最后，你可以开始根据你的经验和知识构筑函数啦

## hogs -> Problem 8（make_averaged函数）

我只是稍作分析哈！

 1. 函数的作用：输入参数，调用original_function函数samples_count次，将其值累加汇总起来，求平均。需要注意的是original_function函数的运作，不然的话有些例子很难理解。
 2. 该函数接收：一个original_function函数，samples_count=1000（调用original_function的次数）
 3. 返回：一个函数，这个局部函数接收与original_function函数，具有相同数量的参数

```python
def make_averaged(original_function, samples_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called SAMPLES_COUNT times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0    嗨嗨嗨：注意这里，例子过不去，就要再会过头去理解理解roll_dice函数了。
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def average(*args):
        count = 0
        for i in range(samples_count):
            count += original_function(*args)
        return count / samples_count
    return average
    # END PROBLEM 8
```

## cats -> Problem 7

1. 这个题使用了动态规划算法（DP），和贪心有点像，但每一步操作都和上一个状态有关
2. typed: 起始字符串，需要通过编辑操作变换成 source。
 source: 目标字符串，我们希望 typed 变换成它。
 limit: 编辑操作的上限。写的时间长，我也忘了为什么没用它就过了
3. dp我使用了二维数组，一个维度代表移除，一个添加，两个加起来就是替换了，是不是很妙
4. 我好像疏忽了点什么，limit应该是提前结束的一个标志，一旦操作数超过limit就自动结束，但是这在二维表里很难操作，不加反而过了

```python
def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    a = len(typed)
    b = len(source)

    #初始化
    dp = [[0] * (b+1) for _ in range(a+1)]
    for i in range(1, b+1):
        dp[0][i] = i
    for i in range(1, a+1):
        dp[i][0] = i
    
    #执行判断
    for i in range(0, a):
        for j in range(0, b):
            if typed[i] == source[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i][j] + 1,
                                   dp[i][j+1] + 1,
                                   dp[i+1][j] + 1)          
    return dp[a][b]
```

# 四、我认为值得注意的地方

其实这个课程让我学到蛮多的，这里有些太过繁琐也不便一一列举了，留心处处皆学问。

 1. C++与py中逻辑运算符的差别
 2. 条件运算符的使用（"x is greater" if x > y else "y is greater"）
 3. 这里gcd的实现（同时赋值（tuple unpacking））![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/752c688c6af64128be130d7e86dfaa66.png)
 4. 如何快速准确构建递归抽象
 5. 概念是相似的，语言是不同的，但相同的概念在不同的语言中都有展现
 6. 先模仿，再创造，最终超越，如果是初学者，碰到难以理解的也是正常的

# 总结

本人较菜，有疏漏的地方请及时反馈，多多包涵呦！
