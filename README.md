# 文件结构

- exam：pdf格式的试题
- hw-desciption：hw的描述文档，也就是hw的题目
- hw01-10：家庭作业
- lab00-12：实验
- proj：项目代码
- project -> tests: 测试案例在这里，也许可以找到测试答案也说不定

[课程网站地址](https://www.learncs.site/docs/curriculum-resource/cs61a/syllabus)
> 文件夹格式代表已完成，zip格式代表未开始，已完成的可借鉴
> 目前仍留有proj scheme 未解决，其余均解决完毕
> 2024/11/4 update 总结了dp题目解题方法【cats -> Problem 7】
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
        - [cats -> Problem 7 （minimum_mewtations函数）](#cats---problem-7-minimum_mewtations%E5%87%BD%E6%95%B0)
            - [解题步骤，首先你要明白这几点](#%E8%A7%A3%E9%A2%98%E6%AD%A5%E9%AA%A4%E9%A6%96%E5%85%88%E4%BD%A0%E8%A6%81%E6%98%8E%E7%99%BD%E8%BF%99%E5%87%A0%E7%82%B9)
        - [Ants](#ants)
        - [Hw4 -> Q3: Balanced](#hw4---q3-balanced)
        - [Hw7 -> Q1: Pow](#hw7---q1-pow)
        - [Lab10 -> Q2,Q3,Q4](#lab10---q2q3q4)
        - [lab12 and hw10](#lab12-and-hw10)
    - [四、我认为值得注意的地方](#%E5%9B%9B%E6%88%91%E8%AE%A4%E4%B8%BA%E5%80%BC%E5%BE%97%E6%B3%A8%E6%84%8F%E7%9A%84%E5%9C%B0%E6%96%B9)
    - [总结](#%E6%80%BB%E7%BB%93)

<!-- /TOC -->

---

## 前言

这里是我学习**CS61A 2024**的一些记录和心得

---

## 一、CS61A是什么？

CS61A是加州大学伯克利分校（UC Berkeley）的计算机科学导论课程。这门课程旨在教授计算机科学的基本概念和编程技能，主要使用编程语言Python。它是许多学生的第一门计算机科学课程，涵盖了从程序设计基础到数据结构和算法的内容。

CS61A通常被认为是一门非常有挑战性但也非常有价值的课程，为学生提供了扎实的编程基础和计算机科学思维方式。

主要是用Python来掌握函数式编程、面向对象以及SQL等等

## 二、OK自动评分器的使用

`py环境的配置我就不多提了，网上很多，我使用的是VS Code`

### 使用

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

### 此外

1. [okpy命令生成器](https://ok-help.cs61a.org/)

2. 有一种情况是py版本太高，ok不适用了，降降版本就行了

3. 如果输入代码后报错，也可能是文件解压格式后的地址不正确

- "...\CS61A\hw\hw01\hw01.py"
- "...\CS61A\lab\lab01\lab01.py"
- "...\CS61A\proj\cats\cats.py"
- "...\CS61A\hw\hw05\hw05\hw05.py"  （错误地址）
有的时候解压完毕可能出现，两个hw05，这时就报错了
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/2567783e57824ab79b08b043eeb1f4ac.png)

## 三、期间遇到的一些难点

我不会每个都有解析的，只是记录一下我学习时遇到的，每个人遇到的可能都不太一样，但还是希望帮助一下和我问题相似的同学
当然，也可以看看我的例子，分享分享你的解法
最后，希望各位同学勤于思考，不要太懒惰哦！

### 写题时的方法

这些题嘛倒不是很难，重要的是对题意的理解，以及上下文的分析

 1. 因为是英文，所有你可能需要一款沉浸式翻译的插件
[沉浸式翻译插件网址](https://immersivetranslate.com/download/?utm_source=extension&utm_medium=extension&utm_campaign=options_nav)
 2. 首先，要明白函数的大致作用
 3. 其次，联系上下文，明白函数接收的参数是什么，返回的是什么
 4. 接着，你要根据例子，逐步理解函数内部是如何对数据进行操作的
 5. 最后，你可以开始根据你的经验和知识构筑函数啦

### hogs -> Problem 8（make_averaged函数）

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
    def average(*args):
        count = 0
        for i in range(samples_count):
            count += original_function(*args)
        return count / samples_count
    return average
    # END PROBLEM 8
```

---

### cats -> Problem 7 （minimum_mewtations函数）

1. 这个题使用了动态规划算法（DP），和贪心有点像，但每一步操作都和上一个状态有关
2. typed: 起始字符串，需要通过编辑操作变换成 source。
 source: 目标字符串，我们希望 typed 变换成它。
 limit: 编辑操作的上限。写的时间长，我也忘了为什么没用它就过了
3. dp我使用了二维数组，一个维度代表移除，一个添加，两个加起来就是替换了，是不是很妙
4. 我好像疏忽了点什么，limit应该是提前结束的一个标志，一旦操作数超过limit就自动结束，但是这在二维表里很难操作，不加反而过了

#### 解题步骤，首先你要明白这几点

1. dp 数组（dp table）以及下标的含义
    `dp[i][j]` 的含义：`dp[i][j]` 表示将 typed 的前 i 个字符转换为 source 的前 j 个字符所需的最少编辑次数。
2. 确定递推公式
   - 递推公式：
   - 如果 `dna1[i-1] == dna2[j-1]，则 dp[i][j] = dp[i-1][j-1]`，即不需要任何编辑操作。
   - 如果 `dna1[i-1] != dna2[j-1]，则 dp[i][j]` 可以通过以下三种操作之一得到：
       - 替换：`dp[i-1][j-1] + 1`
       - 删除：`dp[i-1][j] + 1`
       - 插入：`dp[i][j-1] + 1`
   - 所以，`dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1`
3. dp 数组如何初始化
   - 初始化：
       - `dp[0][j]` 表示将空字符串转换为 typed 的前 j 个字符，需要 j 次插入操作。
       - `dp[i][0]` 表示将 source 的前 i 个字符转换为空字符串，需要 i 次删除操作。
4. 确定遍历顺序
   - 遍历顺序：从左到右，从上到下。
5. 举例推导 dp 数组
6. 结束条件
   - 对于 `dp[i][j] <= limit`，即如果操作数超过 limit，则停止计算。
    【注】：可能很难操作

</details>

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

---

### Ants

Hello，别想着在这里找太多教程了！这个项目目的就是为了让你搞懂它的结构。你可能会遇到一些“小麻烦”，但别慌，解决方案都藏在源码里。其实，它没什么复杂的算法，更多的是需要你细心发掘。预祝各位在这趟项目之旅中一路顺风！如果实在需要帮助，不妨翻翻本仓库的Ants项目，阅读源码也是一种乐趣。Good Luck！

- self.place.bees： 一个实例所存在的地点，该地点所存在的bees，返回一个bees列表。
- 有些问题或许在父类中直接解决会更好。
- 当你在遍历一个列表的同时对其进行修改时，可能会导致某些元素被跳过，这是因为遍历时列表的长度和索引会发生变化。

---

### Hw4 -> Q3: Balanced

1. 移动式结构（Mobile）的定义：一个移动式结构由多个臂组成，每个臂可能悬挂一个行星（Planet）或另一个移动式结构（Mobile）。
2. 平衡的定义：一个移动式结构被认为是平衡的，需要满足以下条件：
    - 左右两边的扭矩相等。
    - 每个悬挂在臂端的移动式结构或行星本身也是平衡的。
3. 这个函数本身不难实现，难在对 arm 结构的理解 与 total_mass(), end()函数的应用,
4. 实现不是很难，理解以上三个定义即可顺利写出，我就不多说了

```python
def arm(length, mobile_or_planet):
    """Construct an arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]
    
def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> p = mobile(arm(3, t), arm(2, u))
    >>> balanced(p)
    False
    >>> balanced(mobile(arm(1, v), arm(1, p)))
    False
    >>> balanced(mobile(arm(1, p), arm(1, v)))
    False
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'balanced', ['Index'])
    True
    """
    if is_planet(m): # termination condition
        return True
    else: #左右判断，加递归判断
        left_mass =  total_mass(end(left(m))) * length(left(m))
        right_mass = total_mass(end(right(m))) * length(right(m))
        return left_mass == right_mass and balanced(end(left(m))) and balanced(end(right(m)))
```

---

### Hw7 -> Q1: Pow

1. 这道题的描述很难评，它大概是想要以下这种效果

    ```scheme
    scm> (pow-expr 2 0)     ;case 1
    1
    scm> (pow-expr 2 1)     ;case 2
    (* 2 1)
    scm> (pow-expr 2 5)     ;case 4 odd？ 奇数
    (* 2 (square (square (* 2 1))))

    scm> (pow-expr 2 15)    ;case 4
    (* 2 (square (* 2 (square (* 2 (square (* 2 1)))))))

    scm> (pow-expr 2 16)    ;case 3 even？ 偶数
    (square (square (square (square (* 2 1)))))
    ```

    > 以上描述来自 lab11 -> Q3: Exponential Powers

2. 这就是个求幂的函数，你只需要逐步实现case1-4，简简单单？
3. 写完这道题可以去看看 lab11 -> Q3: Exponential Powers，差不多是一样的
4. 哦，对了当情况为偶数时，(- exp 2)是不可取的，原因是太慢了会超时，望周知

```scheme
(define (square n) (* n n))

(define (pow base exp) 
  (cond 
    ((= exp 0) 1)
    ((= exp 1) base)
    ((even? exp) (square (pow base (/ exp 2)))) ;减少时间复杂度，避免超时
    (else (* base (pow base (- exp 1)))))
)
```

---

### Lab10 -> Q2,Q3,Q4

1. 这题说难也不难，你需要多揣摩，毕竟只是填代码，有时候直觉也可以得出答案
2. 先说有几种情况：
    a. exp是Pair类型
    b. exp在OPERATORS（字典）里，转化为所需函数名
    c. int/bool类型 直接输出
    d. exp在bindings（字典）里，替换成数值输出
3. case a 细分
    - operator is and 逻辑操作符
    - operator is define 关键字
    - 余下的情况就是需要有一个统一的处理，涉及calc_apply(op, args), 被包含在了OPERATORS字典里
    > OPERATORS = { "//": floor_div, "+": addition, "-": subtraction, "*": multiplication, "/": division }
4. operands.map(calc_eval)很重要，快去搜一下map的作用，再揣摩一下代码吧
5. 逻辑已经有了，我还需要一步步实现嘛？！加油！！

```python
def calc_eval(exp):
    """
    >>> calc_eval(Pair("define", Pair("a", Pair(1, nil))))
    'a'
    >>> calc_eval("a")
    1
    >>> calc_eval(Pair("+", Pair(1, Pair(2, nil))))
    3
    """
    if isinstance(exp, Pair):
        operator = exp.first # exp的第一个操作数
        operands = exp.rest # exp余下的数据
        if operator == 'and': 
            return eval_and(operands)
        elif operator == 'define':
            return eval_define(operands)
        else:  
            return calc_apply(calc_eval(operator), operands.map(calc_eval)) # UPDATE THIS FOR Q2
    elif exp in OPERATORS:   # Looking up procedures
        return OPERATORS[exp]
    elif isinstance(exp, int) or isinstance(exp, bool):   # Numbers and booleans
        return exp
    elif exp in bindings: # CHANGE THIS CONDITION FOR Q4
        return bindings[exp] # UPDATE THIS FOR Q4

def calc_apply(op, args):
    return op(args)
```

---

### lab12 and hw10

1. 如果你和我一样先完成了 HW 10，可能会感到有些困惑。不过，回过头来看 Lab 12，你会恍然大悟，因为基础语法和项目的完成方法在 Lab 12 中都有详细说明。
2. 这一部分的目的是让大家初步了解 SQL 数据库语言的使用，从逻辑上来说并不复杂，主要是对基础语法的运用。因此，理解它们将对你的学习大有裨益。
3. 建议先进行 lab12

>以下是一份可能会用到的语法的说明，希望对你有所帮助：

- **`SELECT`**: 指定要查询的列。
- **`FROM`**: 指定查询的数据表。
- **`INNER JOIN ... ON`**: 连接两个表，并指定连接条件。
- **`WHERE`**: 筛选满足特定条件的记录。
- **`GROUP BY`**: 将结果按指定列分组，以便进行聚合计算。
- **`HAVING`**: 对分组后的结果应用条件，通常用于聚合函数。
- **`ORDER BY`**: 指定结果集的排序方式。
  - **ASC**: 表示按升序排序。
  - **DESC**: 表示按降序排序。
- **`AS`**: 用于给列或表起别名。
- **`MAX()`**, **`MIN()`**, **`AVG()`**: 聚合函数，用于计算最大值、最小值和平均值，这样的函数还有很多。

>如果仍有语法疑问，这个网站可能会帮到你 [SQL](https://www.runoob.com/sql/sql-tutorial.html)

接下来，我将给出一个实例，来展示SQL中基础语法的使用

```SQL
-- 创建 departments 表
CREATE TABLE departments (
    id INT PRIMARY KEY,              -- 部门 ID
    department_name VARCHAR(50)      -- 部门名称
);

-- 插入示例数据到 departments 表
INSERT INTO departments (id, department_name) VALUES
(1, '人力资源'),
(2, '技术支持'),
(3, '市场营销'),
(4, '财务部');

-- 创建 employees 表
CREATE TABLE employees (
    id INT PRIMARY KEY,               -- 员工 ID
    name VARCHAR(50),                 -- 员工姓名
    salary DECIMAL(10, 2),            -- 员工薪资
    department_id INT,                -- 部门 ID
    status VARCHAR(20)                -- 员工状态
);

-- 插入示例数据到 employees 表
INSERT INTO employees (id, name, salary, department_id, status) VALUES
(1, '张三', 60000, 1, 'active'),
(2, '李四', 55000, 1, 'active'),
(3, '王五', 70000, 2, 'active'),
(4, '赵六', 40000, 2, 'inactive'),
(5, '钱七', 80000, 3, 'active'),
(6, '孙八', 30000, 3, 'active'),
(7, '周九', 90000, 4, 'active'),
(8, '吴十', 50000, 4, 'inactive');

SELECT 
    d.department_name AS department_name,  -- 选择部门名称，并重命名为 department_name
    MAX(e.salary) AS max_salary,           -- 获取该部门的最高薪资，重命名为 max_salary
    MIN(e.salary) AS min_salary,           -- 获取该部门的最低薪资，重命名为 min_salary
    AVG(e.salary) AS avg_salary             -- 获取该部门的平均薪资，重命名为 avg_salary
FROM 
    employees e                             -- 从 employees 表中选择数据，并将其简写为 e
INNER JOIN 
    departments d ON e.department_id = d.id  -- 内连接 departments 表，通过部门 ID 进行连接
WHERE 
    e.status = 'active'                     -- 仅选择状态为 'active' 的员工
GROUP BY 
    d.department_name                        -- 按部门名称分组
HAVING 
    AVG(e.salary) > 50000                   -- 仅保留平均薪资大于 50000 的部门
ORDER BY 
    avg_salary DESC;                        -- 按照平均薪资降序排列结果
```

## 四、我认为值得注意的地方

 1. C++与py中逻辑运算符的差别
 2. 条件运算符的使用（"x is greater" if x > y else "y is greater"）
 3. 这里gcd的实现（同时赋值（tuple unpacking））
    ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/752c688c6af64128be130d7e86dfaa66.png)
 4. 如何快速准确构建递归抽象
 5. 先转化为柯里化函数，再使用，有什么好处
 6. 你对于scheme中的 括号的使用 有什么想法， 用不好会这样报错
     ![image](https://github.com/user-attachments/assets/fc4fe5aa-76f0-4369-b1c8-75d93aee7818)
 7. scheme中，引号与准引号的用法，与py中f{value}相似
 8. 概念是相似的，语言是不同的，但相同的概念在不同的语言中都有展现
 9. 先模仿，再创造，最终超越，如果是初学者，碰到难以理解的也是正常的

## 总结

本人较菜，有疏漏的地方请及时反馈，多多包涵呦！
