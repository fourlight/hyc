# hyc库介绍

## 简介

__名称：hyc库__
> _hyc意为Help you calculate（帮助您计算）_

__版本号：4.0.0β2测试版__
> _4.0.0β2测试版功能变化不算大，但内部结构有变化_

__平均版本稳定性：85%以上__
> _该版本稳定性较高，但由于会持续增加功能，稳定性也可能转为α级别_
>
> __各模块版本稳定性__
>
> 模块|稳定性|稳定性描述
> ---|---|---
> `num`模块|98%以上|极高的稳定性，不会存在bug
> `fraction`模块|95%以上|较高的稳定性，基本不会存在bug
> `Percentage`模块|90%以上|较高的稳定性，基本没有bug

__本次更新时间：2021年8月21日__

_[点击我跳转到GitHub界面哦~](https://github.com/fourlight/hyc)_

## 更新记录：

### 4.0.0β2测试版（当前版本）
> * 将`ratio`模块移除，并新建模块`percentage`，将`fraction`模块的`Percentage`类移动至`percentage`模块

### 4.0.0β1测试版

> * 增加了`ratio`模块 __（暂时为空）__
>* 增加了`fraction`模块的`Percentage`类，用于创建百分数对象
>* 将`fraction`模块的`fraction`分数类重命名，改为`Fraction`类，其它无改变

### 3.2.0版本（最新正式版）

> * 修复了少许bug并优化了一些代码
>
> _所有被修复的问题_
> > * 修复了当`1<=Fraction()对象<2`时`__repr__()`函数无返回值的问题
>
> _优化的代码_
> > * 在`num`模块的`factor()`函数中
> >* 在`fraction`模块`Fraction()`类的`__repr__()`方法中

### 3.2.0rc1候选发布版本

> * 修复了介绍中不准确的描述
>* 对3.2.0β1测试版的代码进行了检测，发现并修复了一些bug
>
> _所有被修复的问题_
> > * 修复了`Fraction()`对象作为一个列表被打印时返回`[<fraction.fraction object at ...>]`的问题，将`__str__()`函数替换为`__repr__()`函数
>* 将`__float__()`函数自动保留到小数点后第二位的功能 __取消了__

### 3.2.0β1测试版

> * 增加了分数计算的 __整除__
>* 分数可以和整数 __直接运算__，不需要再用`convert()`函数转换，且分数 __位置随意__，如下
> > 3.1.0版本
> >```python
> ># 表示2分之1加5
> >a = Fraction(2,1)
> >b = convert(5)
> >print(a+b)
> >
> >控制台
> >5又2分之1
> >```
> > 3.2.0β1测试版
> >```python
> ># 表示2分之1加5
> >a = Fraction(2,1)
> >print(a+5)
> >
> >控制台
> >5又2分之1
> >```
>* 增加了比较运算符功能，使分数之间可以进行比较，如下
> >```python
> >from hyc.fraction import *
> >
> >a = Fraction(2,1)
> >b = Fraction(3,1)
> >print(a<b, a<=b, a==b, a>b, a>=b, a!=b)
> >```
> >```
> >控制台
> >False False False True True True
> >```
>* `__str__()`函数修改，改为支持带分数

### 3.1.0版本（最新正式版）

> * 增加了分数计算的 __开方计算__
>* 增加了`fraction`模块的`convert()`函数，可让整数和小数直接化为`Fraction`类型， __直接和分数进行运算__

### 3.0.0版本

> * 3.0.0正式版正式上线Pypi，相比于3.0.0β1测试版修复了一些`fraction`模块的bug以及进行了一些调整
>
> _调整内容_
> > * 规范了介绍的一些问题
> >* 规范了Fraction()类参数的命名
>
> _所有被修复的问题_
> > * 修复了`float()`转换和`int()`转换错误的问题
> >* 由于出现了bug，移除了`__float__()`方法的`rounding` __（四舍五入位数）__ 参数，`__float()__`方法改为自动四舍五入到百分位

### 3.0.0β1测试版（稳定性相当于2.x版本）

> * 对3.0.0α2测试版的README.md进行了一些调整，修复了介绍不准确、遗漏的问题
>* 对3.0.0α2的`num`模块进行了全面测试，修复了一些bug，将3.0.0α2的稳定性提升到β级别
>
> _所有被修复的问题_
> > * pri_fac函数返回的是`参数='质因数1*质因数2*...'`字符串，在2.0.x版本中则是返回`参数='质因数1*质因数2*...*1'`字符串，但是3.0.0α2版本返回的是2.0.x版本的字符串
> >* per_num函数在参数为完全数时返回True，但参数不为完全数时不返回值，于是我们增加了一个`else`分支

### 3.0.0α2测试版（`num`模块存在bug，不推荐使用）

> * 将Fraction()类中加减乘除需要加`[]`的方法进行了优化，变为了直接计算，如下图所示
> > 3.0.0α1测试版
> >```
> >a = Fraction(2, 1)
> >b = Fraction(5, 1)
> >a + [b]
> >```
> > 3.0.0α2测试版
> >```
> >a = Fraction(2, 1)
> >b = Fraction(5, 1)
> >a + b
> >```

### 3.0.0α1测试版（不推荐使用）

> * `fraction`模块代码大重做，移除分数四则运算、约分等内容，添加涵盖四则运算、约分、分数化小数等功能的fraction类
>* 添加参数注释
>* 简介更新

### 2.2.0版本

> * 添加介绍
>* 添加“更新记录”

### 2.1.2.post1版本

> * 优化系统稳定性

### 2.1.2版本

> * 优化系统稳定性

### 2.1.1版本

> * 修复显示bug

### 2.1.0版本

> * 删除报错
>* 删除介绍英文

### 2.1.0版本之前

> * 暂无记录

## 下载方式：

版本稳定性|发布
---|---
α测试版|仅GitHub
β测试版|Pypi（默认下载不会下载）及GitHub
rc预选发布版本|Pypi（默认下载不会下载）及GitHub
正式版|Pypi及GitHub

### 下载正式版（3.2.0版本）：

```
pip install hyc
```

### 下载测试版（当前版本4.0.0β1测试版）：

```
pip install hyc==4.0.0b1
```

## 导入方式：

### 1.

```python
from hyc import *
```

### 2.

```python
from hyc import num
```

### 3.

```python
from hyc.num import *
```

## hyc库内部结构：

```
hyc
├─fraction
│  ├─den_di()
│  ├─covert()
│  ├─Percentage()类
│  │   ├─__radd__()加法
│  │   ├─__rsub__()减法
│  │   ├─__rmul__()乘法
│  │   ├─__rtruediv__()除法
│  │   └─__repr__()方法
│  └─Fraction()类
│      ├─opposide()方法
│      ├─red_fr()方法
│      ├─simp_fr()方法
│      ├─__add__()和__radd__()加法
│      ├─__float__()方法（分数化小数并保留位数）
│      ├─__init__()方法
│      ├─__int__()方法（fraction对象化整数）
│      ├─__mul__()和__rmul__()乘法
│      ├─__repr__()方法（分数读作）
│      ├─__sub__()和__rsub__()减法
│      ├─__turediv__()和__rturediv__()除法
│      ├─__floordiv__()和__rfloordiv__()整除
│      ├─__matmul__()开方
│      └─__le__() __lt__() __eq__() __ne__() __gt__() __ge__()比较运算符
├─ratio
│  └─暂无
└─num
    ├─factor()
    ├─pri_num()
    ├─per_num()
    ├─even_num()
    ├─lcm()
    ├─hcf()
    ├─pri_fac()
    └─comprime()
```

## 使用方式：

_通过调用函数或类完成您想要达成的效果_

### `num`模块

#### 1.`factor()`

该函数是用来寻找一个数的所有因数的，请在括号内填入一个数字，该函数就可以找出括号内数字的所有参数

##### 示例

```python
from hyc.num import *

print(factor(9))
```

```
----
控制台
[1, 3, 9]
```

#### 2.`per_num()`

该函数是用来判断一个数是否为完全数的，请在括号内填入一个数字，该函数返回True或False

##### 示例

```python
from hyc.num import *

print(per_num(9), per_num(27))
```

```
控制台
False True
```

#### 3.`pri_num()`

该函数是用来判断一个数是否为质数的，请在括号内填入一个数字，该函数返回True或False

##### 示例

```python
from hyc.num import *

print(pri_num(9), pri_num(2))
```

```
控制台
False True
```

#### 4.`even_num()`

该函数是用来判断一个数是否为偶数的，请在括号内填入一个数字，该函数返回True或False

##### 示例

```python
from hyc.num import *

print(per_num(9), per_num(28))
```

```
控制台
False True
```

#### 5.`lcm()`

该函数是用来寻找几个数的最小公倍数的，请在括号内填入一个包含两个或以上数字的列表，请勿填入字符串、浮点数

##### 示例

```python
from hyc.num import *

print(lcm([5, 9]))
```

```
控制台
45                    
```

#### 6.`hcf()`

该函数是用来寻找几个数的公因数和最大公因数的，请在括号内填入一个包含两个或以上数字的列表，请勿填入字符串、浮点数；该函数会返回两个值，前一个值为两个数所有的公因数列表，后一个值为两个数的最大公因数

##### 示例

```python
from hyc.num import *

print(hcf([5, 15]))
```

```
控制台
[1, 5], 5
```

#### 7.`pri_fac()`

该函数是用来分解一个数的质因数的，请在括号内填入一个数字，该函数返回‘括号内的数 = 质因数1 * 质因数2 * ...’字符串

##### 示例

```python
from hyc.num import *

print(pri_fac(5))
```

```
控制台
150 = 2*3*5*5              
```

#### 8.`coprime()`

该函数是用来该函数是用来判断几个数是否为互质数的，请在括号内填入一个包含两个及以上数字的列表，该函数返回True或False

##### 示例

```python
from hyc.num import *

print(coprime([9, 12]), coprime([2, 3]))
```

```
控制台
False True
```

### `fraction`模块

_请注意：在hyc库里，分数请先用`name=Fraction(分母,分子)`转换name为fraction类型后再使用_

#### 9.`den_di()`

该函数是用来通分的，请在函数内填入一个分数列表，该函数可以将分数列表中的所有分数化为同分母分数

##### 示例

```python
from hyc.fraction import *

a = Fraction(5, 2)  # 代表五分之二
b = Fraction(9, 1)  # 代表九分之一
print(den_di([a, b]))
```

```
控制台
[45分之18, 45分之5]
```

#### 10.`convert()`

该函数可以直接将整数和小数化为`Fraction`类型

##### 示例

```python
from hyc.fraction import *

a = covert(9.5)
b = covert(8)
print(a, b, a + b)
```

```
控制台
9又2分之1 1分之8 17又2分之1
```

#### 11.`Fraction`类

`Fraction`类是`fraction`模块中最主要的部分，它会创建一个分数对象，如`a=Fraction(5, 2)`就可以创建`五分之二`这个分数；__也支持带分数__，比如`a=Fraction(6, 1, num=5)`
就可以创建`五又六分之一`这个分数，其中的`num`表示带分数的 __整数部分__

其中的`__int__()`函数和`__float__()`基本原理相同，都是将分数化为整数（或小数）

##### 示例

```python
from hyc.fraction import *

a = Fraction(4, 2)
print(int(a))  # 将4分之2化为整数
```

```
控制台
1
```

> 这段代码，就是将4分之2化为整数，因为4分之2等于0.5，0.5四舍五入等于1，因此返回1

`__float__()`函数与`__int__()`函数的不同点在于`__float__()`函数是直接将对象化为小数，而不是保留到个位

#### 示例

```
a = Fraction(8, 1)
print(float(a))
```

```
控制台
0.125
```

> 8分之1等于0.125，因此返回0.125

除了`__int__()`和`__float__()`函数，还有`__repr__()`函数，用于控制对象的名称，比如`Fraction(2, 1)`就是`2分之1`；也支持带分数，如`Fraction(9, 5, num=3)`
为`3又9分之5`，`Fraction(9, 32)`也为`3又9分之5`

剩下的`red_fr()`，`simp_fr()`和`opposide()`函数除了调用方式是

```
a = Fraction(分母,分子)
a.函数()
```

其余用法与[2.2.0版本](https://pypi.org/project/hyc/2.2.0) 相同

剩下的就是加减乘除四则运算了，__可以直接运算__

##### 示例

```python
from hyc.fraction import *

a = Fraction(5, 1)
b = Fraction(4, 1)
c = Fraction(3, 1)

print(a + b + c)
```

```
控制台
60分之47
```

当然，示例中的`+`可以替换成`-`，`*`和`/`，但暂时不支持`//`

不仅如此，还有 __开方运算__

##### 示例

```python
from hyc.fraction import *

a = Fraction(5, 1)

print(a ** 2)
```

但请注意，只支持`a**2`，__不支持__ `2**a`

__混合运算__ 也是可以的

##### 示例

```python
from hyc.fraction import *

a = Fraction(3, 1)
b = Fraction(6, 1)
c = Fraction(3, 2)
print(a + b * c)
```

```
控制台
9分之4
```

也可以做出整数或小数与分数运算的效果

##### 示例

```python
from hyc.fraction import *

a = Fraction(2, 1)
print(a + 5)
```

```
控制台
5又2分之1
```

分数、整数和小数之间还可以进行比较

##### 示例

```python
from hyc.fraction import *

a = Fraction(9, 2)
b = Fraction(9, 1)
print(a < b, a <= b, a == b, a != b, a > b, a >= b, a < 1, a < 1.1)
```

```
控制台
False False False True True True False False
```

但值得注意的是，只能`分数<整数（小数）`，不能`整数（小数）>分数` __（比较运算符前必须是分数）__

### `percentage`模块

#### 12.`Percentage`类

`Percentage`类是一个创建百分数的类，如`Percentage(19)`就可以创建名为`'19%'`的百分数对象

`Percentage`类 __只有运算功能__

`Percentage`类的运算非常特别，如创建`a=Percentage(9)`这个对象后，可以和`int`类型、`float`类型以及上文提到的`Fraction`类进行计算，但只能`其他类型 + a`，不能`a + 其它类型`

如上的规则是因为`Percentage`类一个特殊的运算过程，在`Percentage`类对象前面的数据被称作 __单位“1”(one_unit)__，`Percentage`类的单位“1”直接影响实际运算出的数，如下所示

##### 示例

```python
from hyc.fraction import *

a = Percentage(10)
print(10 + a, 9 + a)
```

```
控制台
11 9.9
```

从如上示例中我们可以得知`Percentage`类的运算方法是这样的
> ```
> 单位“1” + Percentage(a) = 单位“1” + a / 100
>
> 单位“1” - Percentage(a) = 单位”1“ - a / 100
> 
> ... ...
> ```

## `radio`模块

__此模块新添加，暂无功能__

## 分数计算小软件

_如果您觉得hyc库的分数计算太过于麻烦，[请点击这里](http://github.com/fourlight/fra_cal)_

## 希望对您有所帮助
