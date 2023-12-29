from EasyObj.BetterList import BetterList
from test import Expect

e = Expect("length")
e.run(BetterList([1, 2, 5]).length)
e.toBe(3)

e = Expect("at")
e.run(BetterList([1, 2, 5]).at(1))
e.toBe(2)

e = Expect("map")
e.run(BetterList([1, 2, 5]).map(lambda x: x * 2))
e.toBe([2, 4, 10])

e = Expect("filter")
e.run(BetterList([1, 2, 5]).filter(lambda x: x > 2))
e.toBe([5])

e = Expect("forEach 1")
temp = []
BetterList([6, 2, 9]).forEach(lambda val, index: temp.append((val, index)))
e.run(temp)
e.toBe([(6, 0), (2, 1), (9, 2)])

e = Expect("forEach 2")
temp = []
BetterList([6, 2, 9]).forEach(
    lambda val: temp.append(val), noIndex=True)
e.run(temp)
e.toBe([6, 2, 9])

e = Expect("concat")
e.run(BetterList([1, 2, 5]).concat([3, 4]))
e.toBe([1, 2, 5, 3, 4])

e = Expect("reduce 1")
e.run(BetterList([1, 2, 5]).reduce(lambda x, y: x + y))
e.toBe(8)

e = Expect("reduce 2")
e.run(BetterList([1, 2, 5]).reduce(lambda x, y: x + y, 10))
e.toBe(18)

e = Expect("reduceRight 1")
e.run(BetterList([1, 2, 5]).reduceRight(lambda x, y: x + y))
e.toBe(8)

e = Expect("reduceRight 2")
e.run(BetterList([1, 2, 5]).reduceRight(lambda x, y: x + y, 10))
e.toBe(18)

e = Expect("find 1")
e.run(BetterList([1, 2, 5]).find(lambda x: x > 2))
e.toBe(5)

e = Expect("find 2")
e.run(BetterList([1, 2, 5]).find(lambda x: x > 10))
e.toBe(None)

e = Expect("findIndex 1")
e.run(BetterList([1, 2, 5]).findIndex(lambda x: x > 2))
e.toBe(2)

e = Expect("findIndex 2")
e.run(BetterList([1, 2, 5]).findIndex(lambda x: x > 10))
e.toBe(-1)

e = Expect("every 1")
e.run(BetterList([1, 2, 5]).every(lambda x: x > 2))
e.toBe(False)

e = Expect("every 2")
e.run(BetterList([1, 2, 5]).every(lambda x: x > 0))
e.toBe(True)

e = Expect("flat", showTimes=True)
e._(BetterList([1, 2, 5, [3, 4]]).flat(), [1, 2, 5, 3, 4])
e._(BetterList([1, 2, 5, [3, [4]]]).flat(), [1, 2, 5, 3, [4]])
e._(BetterList([1, 2, 5, [3, [4]]]).flat(2), [1, 2, 5, 3, 4])
e._(BetterList([1, 2, [5, [3, [4]]]]).flat(2), [1, 2, 5, 3, [4]])
e._(BetterList([1, 2, [5, [3, [4]]]]).flat(4), [1, 2, 5, 3, 4])

e = Expect("fill 1")
temp = BetterList([1, 2, 5])
temp.fill(3)
e.run(temp)
e.toBe([3, 3, 3])

e = Expect("fill 2")
temp = BetterList([1, 2, 5])
temp.fill(3, 1)
e.run(temp)
e.toBe([1, 3, 3])

e = Expect("fill 3")
temp = BetterList([1, 2, 5])
temp.fill(3, 1, 2)
e.run(temp)
e.toBe([1, 3, 5])

e = Expect("copyWithin", showTimes=True)
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(0, 3), [4, 5, 3, 4, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(1, 3), [1, 4, 5, 4, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(1, 2), [1, 3, 4, 5, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(2, 2), [1, 2, 3, 4, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(0, 3, 4), [4, 2, 3, 4, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(1, 3, 4), [1, 4, 3, 4, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(1, 2, 4), [1, 3, 4, 4, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(0, -2), [4, 5, 3, 4, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(0, -2, -1), [4, 2, 3, 4, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(-4, -3, -2), [1, 3, 3, 4, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(-4, -3, -1), [1, 3, 4, 4, 5])
e._(BetterList([1, 2, 3, 4, 5]).copyWithin(-4, -3), [1, 3, 4, 5, 5])

e = Expect("entries", showTimes=True)
e._(BetterList(['a', 'b', 'c']).entries(), [(0, 'a'), (1, 'b'), (2, 'c')])
e._(BetterList([1, 2, 3]).entries(), [(0, 1), (1, 2), (2, 3)])

e = Expect("flatMap", showTimes=True)
e._(BetterList([1, 2, 3, 4]).flatMap(
    lambda x: [x, x * 2]), [1, 2, 2, 4, 3, 6, 4, 8])
e._(BetterList([1, 2, 3, 4]).flatMap(lambda x: [[x, x * 2]]),
    [[1, 2], [2, 4], [3, 6], [4, 8]])
e._(BetterList([1, 2, 3, 4]).flatMap(lambda x: [x, [x * 2]]),
    [1, [2], 2, [4], 3, [6], 4, [8]])

e = Expect("from", showTimes=True)
e._(BetterList._from([1, 2, 3, 4]), [1, 2, 3, 4])
e._(BetterList._from([]), [])

e = Expect("includes", showTimes=True)
e._(BetterList([1, 2, 3, -0, object]).includes(1), True)
e._(BetterList([1, 2, 3, -0, object]).includes(-0), True)
e._(BetterList([1, 2, 3, -0, object]).includes(0), True)
e._(BetterList([1, 2, 3, -0, object]).includes(object), True)
e._(BetterList([1, 2, 3, -0, object]).includes(4), False)
e._(BetterList([1, 2, 3, -0, object]).includes(-0.5), False)
e._(BetterList([1, 2, 3, -0, object]).includes({}), False)
e._(BetterList([1, 2, 3, -0, object]).includes(None), False)
e._(BetterList([None]).includes(None), True)

e = Expect("indexOf", showTimes=True)
e._(BetterList([1, 1, 1]).indexOf(1), 0)
e._(BetterList([1, 2, 3]).indexOf(1, 1), -1)
e._(BetterList([1, 2, 3]).indexOf(2, 1), 1)
e._(BetterList([1, 2, 3]).indexOf(2, -1), -1)
e._(BetterList([1, 2, 3]).indexOf(2, -2), 1)
e._(BetterList([None]).indexOf(None), 0)

e = Expect("isArray", showTimes=True)
e._(BetterList.isArray([]), True)
e._(BetterList.isArray([1, 2, 3]), True)
e._(BetterList.isArray({}), False)
e._(BetterList.isArray(None), False)
e._(BetterList.isArray(1), False)
e._(BetterList.isArray("1"), False)

e = Expect("join", showTimes=True)
e._(BetterList(['a', 'b', 'c']).join(), "a,b,c")
e._(BetterList([1, 2, 3]).join(), "1,2,3")
e._(BetterList([1, 2, 3]).join(""), "123")
e._(BetterList([1, 2, 3]).join(" "), "1 2 3")
e._(BetterList([1, 2, 3]).join("a"), "1a2a3")
e._(BetterList([1, 2, 3]).join(None), "1None2None3")

e = Expect("keys", showTimes=True)
e._(BetterList(['a', 'b', 'c']).keys(), [0, 1, 2])
e._(BetterList([1, 2, 3]).keys(), [0, 1, 2])

e = Expect("lastIndexOf", showTimes=True)
e._(BetterList([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]).lastIndexOf(1), 9)
e._(BetterList([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]).lastIndexOf(1, 8), 0)
e._(BetterList([1, 2, 3, 4, 5, 6, 7, 8, 1, 9]).lastIndexOf(1, 7), 0)
e._(BetterList([1, 2, 3, 4, 5, 6, 7, 8, 1, 9]).lastIndexOf(10), -1)
e._(BetterList([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]).lastIndexOf(1, 9), 9)

e = Expect("of", showTimes=True)
e._(BetterList.of(1, 2, 3, 4), [1, 2, 3, 4])

e = Expect("pop", showTimes=True)
temp = BetterList([1, 2, 3, 4])
e._(temp.pop(), 4)
e._(temp, [1, 2, 3])

e = Expect("push", showTimes=True)
temp = BetterList([1, 2, 3, 4])
e._(temp.push(5), 5)
e._(temp, [1, 2, 3, 4, 5])

e = Expect("shift", showTimes=True)
temp = BetterList([1, 2, 3, 4])
e._(temp.shift(), 1)
e._(temp, [2, 3, 4])

e = Expect("slice", showTimes=True)
e._(BetterList([1, 2, 3, 4]).slice(), [1, 2, 3, 4])
e._(BetterList([1, 2, 3, 4]).slice(1), [2, 3, 4])
e._(BetterList([1, 2, 3, 4]).slice(1, 2), [2])
e._(BetterList([1, 2, 3, 4]).slice(1, 3), [2, 3])
e._(BetterList([1, 2, 3, 4]).slice(1, 4), [2, 3, 4])
e._(BetterList([1, 2, 3, 4]).slice(1, 5), [2, 3, 4])
e._(BetterList([1, 2, 3, 4]).slice(1, 0), [])
e._(BetterList([1, 2, 3, 4]).slice(1, -1), [2, 3])
e._(BetterList([1, 2, 3, 4]).slice(1, -2), [2])

e = Expect("some", showTimes=True)
e._(BetterList([1, 2, 3, 4]).some(lambda x: x > 2), True)
e._(BetterList([1, 2, 3, 4]).some(lambda x: x > 4), False)

e = Expect("sort", showTimes=True)
temp = BetterList([1, 3, 2, 4])
e._(temp.sort(), [1, 2, 3, 4])
e._(temp, [1, 2, 3, 4])
temp = BetterList([1, 2, 3, 4])
e._(temp.sort(lambda x, y: y - x), [4, 3, 2, 1])

e = Expect("splice", showTimes=True)
temp = BetterList([1, 2, 3, 4])
e._(temp.splice(), [])
e._(temp, [1, 2, 3, 4])
temp = BetterList([1, 2, 3, 4])
e._(temp.splice(1), [2, 3, 4])
e._(temp, [1])
temp = BetterList([1, 2, 3, 4])
e._(temp.splice(1, 2), [2, 3])
e._(temp, [1, 4])
temp = BetterList([1, 2, 3, 4])
e._(temp.splice(1, 2, 5), [2, 3])
e._(temp, [1, 5, 4])
temp = BetterList([1, 2, 3, 4])
e._(temp.splice(1, 2, 5, 6), [2, 3])
e._(temp, [1, 5, 6, 4])
temp = BetterList([1, 2, 3, 4])
e._(temp.splice(1, 2, 5, 6, 7), [2, 3])
e._(temp, [1, 5, 6, 7, 4])
temp = BetterList([1, 2, 3, 4])
e._(temp.splice(1, 2, 5, 6, 7, 8), [2, 3])
e._(temp, [1, 5, 6, 7, 8, 4])

e = Expect("toSorted", showTimes=True)
values = BetterList([1, 10, 21, 2])
sortedValues = values.toSorted(lambda a, b: a - b)
e._(sortedValues, [1, 2, 10, 21])
e._(values, [1, 10, 21, 2])

e = Expect("toSpliced", showTimes=True)
arr = BetterList([1, 3, 4, 6])
e._(arr.toSpliced(1, 2), [1, 6])

e = Expect("toString", showTimes=True)
e._(BetterList(['a', 'b', 'c']).toString(), "a,b,c")
e._(BetterList([1, 2, 3]).toString(), "1,2,3")

e = Expect("unshift", showTimes=True)
temp = BetterList([1, 2, 3, 4])
e._(temp.unshift(5, 6), 6)
e._(temp, [5, 6, 1, 2, 3, 4])

e = Expect("values", showTimes=True)

e = Expect("with", showTimes=True)
arr = BetterList([1, 2, 3, 4, 5])
e._(arr._with(2, 5), [1, 2, 5, 4, 5])
e._(arr, [1, 2, 3, 4, 5])
