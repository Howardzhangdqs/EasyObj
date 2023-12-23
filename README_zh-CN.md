<div align="center"><h1>EasyDict</h1></div>

<div align="center">

[English](https://github.com/Howardzhangdqs/EasyObj/blob/master/README.md) | [中文简体](https://github.com/Howardzhangdqs/EasyObj/blob/master/README_zh-CN.md)

</div>

`EasyObj` 让你操作对象就像在 `JavaScript` 里一样方便。

## 安装

```bash
pip install easyobj
```

## 用法

### Better List

```python
from EasyObj import BetterList

betterlist = BetterList([1, 2, 3, 4, 5])
# betterlist: BetterList([1, 2, 3, 4, 5])

print(betterlist.length)
# 5

betterlist.append(6)
# betterlist: BetterList([1, 2, 3, 4, 5, 6])

print(betterlist.join(" "))
# '1 2 3 4 5 6'

print(betterlist.filter(lambda x: x >= 4))
# BetterList([4, 5, 6])

print(betterlist.concat(["a", "b", "c"]))
# BetterList([1, 2, 3, 4, 5, 6, 'a', 'b', 'c'])

print(betterlist.map(lambda x: x * 2))
# BetterList([2, 4, 6, 8, 10, 12])
```

就像这样以此类推...

大多数 Method 与 JavaScript 中 [Array](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array) 对象的方法完全相同。

但是由于 Python 不支持使用保留字作为方法名称，我们将一些方法名的名字进行了转换：

| JavaScript | Python |
| :---: | :---: |
| `Array.prototype.with()` | `EasyObj.BetterList._with()` |
| `Array.from()` | `EasyObj.BetterList._from()` |


### Better Dict

因为 Python 中很难实现 JavaScript 的 Object 中的很多功能，所以我们就只实现了一部分。

每个 `BetterDict` 对象都会进行一次类似 [`EasyDict`](https://github.com/tisfeng/Easydict) 的操作，将普通字典转换为嵌套的 `BetterDict` 对象。

```python
from EasyObj import BetterDict

betterdict = BetterDict({"非常": "好"})
# {'非常': '好'}

betterdict.非常
# '好'
```

由于 Python 语法限制，我们无法像 JavaScript 那样在 `BetterDict` 类上加入新方法，因此需要引入另外一个 `DictUtils` 类来实现 JavaScript 中的部分功能

```python
from EasyObj import DictUtils

DictUtils.keys(betterdict)
# ['非常']
```

`EasyObj` 还实现了 `Object.seal` 和 `Object.freeze` 方法，用于将 `BetterDict` 对象转换为 `SealedBetterDict` 和 `FrozenBetterDict` 对象。

```python
sealedDict = DictUtils.seal(betterdict)
# {'非常': '好'}

sealedDict.非常 = "不好"
# {'非常': '不好'}

sealedDict.a = 1
# AttributeError: SealedDict object does not support assigning new attributes

frozenDict = DictUtils.freeze(betterdict)
# {'非常': '好'}

sealedDict.非常 = "不好"
# AttributeError: SealedDict object does not support assigning new attributes

sealedDict.a = 1
# AttributeError: SealedDict object does not support assigning new attributes
```


由于 Python 语法限制，我们将一些方法名的名字进行了转换：

| JavaScript | Python |
| :---: | :---: |
| `Object` | `EasyObj.DictUtils` |
| `Object.prototype.isPrototypeOf()` | `EasyObj.DictUtils.isPrototypeOf()` |


由于 Python 语法限制，以下方法暂无法实现：

| 方法名 |
| :--: |
| `Object.defineProperty()` | 
| `Object.getOwnPropertyDescriptor()` |
| `Object.getOwnPropertyDescriptors()` |
| `Object.getPrototypeOf()` |
| `Object.isExtensible()` |
| `Object.preventExtensions()` |
| `Object.setPrototypeOf()` |
| `Object.prototype.hasOwnProperty()` |
| `Object.prototype.propertyIsEnumerable()` |
| `Object.prototype.toLocaleString()` |
| `Object.prototype.toString()` |
| `Object.prototype.valueOf()` |

## License

GPLv3

## TODO

+ 实现 BetterStr 更好的字符串
+ 实现更多 JavaScript 方法