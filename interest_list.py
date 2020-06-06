# @Time     : 2019/10/29 14:22
# @Auther   : CLannadZSY
# @File     : interest_list.py
# @Software : PyCharm

import pysnooper

"""
all_equal
检查列表中的所有元素是否相等。
使用[1：]和[：-1]比较给定列表中的所有值。
"""


@pysnooper.snoop()
def all_equal(lst):
    return lst[1:] == lst[:-1]


all_equal([1, 2, 3, 4, 5, 6])  # False
all_equal([1, 1, 1, 1])  # True

"""
all_unique
如果列表中的所有值都是唯一的，则返回True，否则返回False。
在给定列表上使用set（）删除重复项，将其长度与列表的长度进行比较。
"""


@pysnooper.snoop()
def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x)  # True
all_unique(y)  # False

"""
bifurcate
将值分为两组。 如果filter中的元素为True，则集合中的对应元素属于第一组； 否则，它属于第二组。

使用list comprehension和enumerate（）将元素添加到基于过滤器的组中。
"""


@pysnooper.snoop()
def bifurcate(lst, filter):
    return [
        [x for i, x in enumerate(lst) if filter[i] == True],
        [x for i, x in enumerate(lst) if filter[i] == False],
    ]


bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])  # [['beep', 'boop', 'bar'], ['foo']]

"""
bifurcate_by
根据函数将值分为两组，该函数指定输入列表中元素所属的组。
如果函数返回True，则该元素属于第一组；否则，该元素属于第一组。 否则，它属于第二组。
使用列表推导根据fn将元素添加到组中。
"""


@pysnooper.snoop()
def bifurcate_by(lst, fn):
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]


bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')

"""
chunk
将列表分成指定大小的较小列表。

使用list（）和range（）创建所需大小的列表。 在列表上使用map（）并使用给定列表的拼接填充它。 最后，返回使用创建的列表。
"""
from math import ceil


@pysnooper.snoop()
def chunk(lst, size):
    return list(
        map(lambda x: lst[x * size:x * size + size],
            list(range(0, ceil(len(lst) / size)))))


chunk([1, 2, 3, 4, 5, 6], 2)  # [[1, 2], [3, 4], [5, 6]]

"""
compact
从列表中删除虚假值。
使用filter（）过滤出虚假的值（False，None，0和“”）。
"""


@pysnooper.snoop()
def compact(lst):
    return list(filter(bool, lst))


compact([0, 1, False, 2, '', 3, 'a', 's', 34])  # [ 1, 2, 3, 'a', 's', 34 ]

"""
count_by
根据给定的功能对列表中的元素进行分组，并返回每个组中元素的计数。

使用map（）通过给定函数映射给定列表的值。 遍历 map，并在每次出现时增加元素计数。
"""


@pysnooper.snoop()
def count_by(arr, fn=lambda x: x):
    key = {}
    for el in map(fn, arr):
        # key[el] = 1 if el not in key else key[el] + 1
        key[el] = key.get(el, 0) + 1
    return key


from math import floor

count_by([6.1, 4.2, 6.3], floor)  # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len)  # {3: 2, 5: 1}

"""
count_occurences
计算列表中某个值的出现次数。

为列表中具有给定值且类型相同的每个项目增加一个计数器。
"""


@pysnooper.snoop()
def count_occurrences(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])


count_occurrences([1, 1, 2, 1, 2, 3], 1)  # 3

"""
deep_flatten
深层拼合列表。

使用递归。 定义一个传播函数，在列表中的每个元素上使用list.extend（）或list.append（）将其展平。 
将list.extend（）与一个空列表和spread函数一起使用以展平一个列表。 递归展平列表中的每个元素。
"""


def spread(arg):
    ret = []
    # for i in arg:
    #     if isinstance(i, list):
    #         ret.extend(i)
    #     else:
    #         ret.append(i)
    # return ret

    _ = [ret.extend(i) if isinstance(i, list) else ret.append(i) for i in arg]
    return ret


@pysnooper.snoop()
def deep_flatten(lst):
    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst)))
    )
    return result


deep_flatten([1, [2], [[3], 4], 5])  # [1,2,3,4,5]

"""
difference_by
在将提供的函数应用于两个列表的每个列表元素之后，返回两个列表之间的差。

通过将fn应用于b中的每个元素来创建集合，然后将列表理解与a上的fn结合使用，以仅保留先前创建的集合_b中未包含的值。

"""


@pysnooper.snoop()
def difference_by(a, b, fn):
    _b = set(map(fn, b))
    return [item for item in a if fn(item) not in _b]


from math import floor

difference_by([2.1, 1.2], [2.3, 3.4], floor)  # [1.2]
difference_by([{'x': 2}, {'x': 1}], [{'x': 1}], lambda v: v['x'])  # [ { x: 2 } ]

"""
every
如果提供的函数对列表中的每个元素返回True，则返回True，否则返回False。

将all（）与map和fn结合使用，以检查fn对于列表中的所有元素是否返回True。
"""


@pysnooper.snoop()
def every(lst, fn=lambda x: x):
    return all(map(fn, lst))


every([4, 2, 3], lambda x: x > 1)  # True
every([1, 2, 3])  # True

"""
every_nth
返回列表中的每个第n个元素。

使用[nth-1 :: nth]创建一个包含给定列表的第n个元素的新列表。
"""


@pysnooper.snoop()
def every_nth(lst, nth):
    return lst[nth - 1::nth]


every_nth([1, 2, 3, 4, 5, 6], 2)  # [ 2, 4, 6 ]

"""
filter_unique
过滤列表中的唯一值。

使用list comprehension和list.count（）创建仅包含非唯一值的列表。
"""


@pysnooper.snoop()
def filter_unique(lst):
    return [x for x in set(item for item in lst if lst.count(item) > 1)]


filter_unique([1, 2, 2, 3, 4, 4, 5])  # [2, 4]

"""
group_by
根据给定的功能对列表的元素进行分组。

使用map（）和fn将列表的值映射到对象的键。 使用列表理解将每个元素映射到适当的键。
"""


@pysnooper.snoop()
def group_by(lst, fn):
    return {key: [el for el in lst if fn(el) == key] for key in map(fn, lst)}


import math

group_by([6.1, 4.2, 6.3], math.floor)  # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len)  # {3: ['one', 'two'], 5: ['three']}

"""
has_duplicates
"""


@pysnooper.snoop()
def has_duplicates(lst):
    return len(lst) != len(set(lst))


x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x)  # True
has_duplicates(y)  # False

"""
initialize_2d_list
初始化给定宽度，高度和值的2D列表。

使用list comprehension和range（）生成h行，其中每行都是一个长度为h的列表，并用val初始化。 如果未提供val，则默认为None。
"""


@pysnooper.snoop()
def initialize_2d_list(w, h, val=None):
    return [[val for x in range(w)] for y in range(h)]


initialize_2d_list(2, 2, 0)  # [[0,0], [0,0]]

"""
longest_item
接受任意数量的可迭代对象或具有length属性的对象，并返回最长的对象。 如果多个对象的长度相同，则将返回第一个。

使用带有len作为键的max（）返回最大长度的项目。
"""


@pysnooper.snoop()
def longest_item(*args):
    return max(args, key=len)


longest_item('this', 'is', 'a', 'testcase')  # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5])  # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar')  # 'foobar'

"""
zip
创建元素列表，并根据原始列表中的位置进行分组。

将max与list comprehension结合使用以获取参数中最长列表的长度。 
循环max_length次分组元素。 如果列表的长度不同，请使用fill_value（默认为无）。
"""


@pysnooper.snoop()
def zip(*args, fill_value=None):
    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
            args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
        ])
    return result


zip(['a', 'b'], [1, 2], [True, False])  # [['a', 1, True], ['b', 2, False]]
zip(['a'], [1, 2], [True, False])  # [['a', 1, True], [None, 2, False]]
zip(['a'], [1, 2], [True, False], fill_value='_')  # [['a', 1, True], ['_', 2, False]]

"""
clamp_number
如果num在该范围内，则返回num。 否则，返回范围内最接近的数字。
"""


@pysnooper.snoop()
def clamp_number(num, a, b):
    return max(min(num, max(a, b)), min(a, b))


clamp_number(2, 3, 5)  # 3
clamp_number(1, -1, -5)  # -1

"""
digitize
"""


@pysnooper.snoop()
def digitize(n):
    return list(map(int, str(n)))


digitize(123)  # [1, 2, 3]


"""
引用自己
"""
def quote_myself():
    a = [1,2]
    a += a
    print(a)
    a.append(a)
    print(a)

quote_myself()


"""
for 实现死循环
"""
for i in iter(int, 1):
    print(i)
    
"""
粘性之禅
"""
def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
        
rtn = product('xyz', '12', repeat=3)
print(list(rtn))        
