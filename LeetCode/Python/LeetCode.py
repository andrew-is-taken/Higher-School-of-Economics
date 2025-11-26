import collections
import heapq
import math
import re
import this
from bisect import bisect_left
from collections import defaultdict, Counter
import random
from heapq import heapify, heappop, heappushpop
from typing import List, Optional
from copy import copy
from turtle import *
import itertools
import numpy as np


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_duplicates(a):
    tortoise = a[0]
    hare = a[0]
    while True:
        tortoise = a[tortoise]
        hare = a[a[hare]]
        if tortoise == hare:
            break

    ptr1 = a[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = a[ptr1]
        ptr2 = a[ptr2]

    return ptr1


# print(find_duplicates([4, 3, 1, 1, 8, 3, 1, 8, 8]))

def check(i):
    length = len(i)
    return f'{length == 0 and "no one" or ""}' \
           f'{length == 1 and i[0] or ""}' \
           f'{length == 2 and i[0] + " and " + i[1] or ""}' \
           f'{length == 3 and i[0] + ", " + i[1] + " and " + i[2] or ""}' \
           f'{length > 3 and i[0] + ", " + i[1] + " and " + str(length - 2) + " others" or ""} ' \
           f'like{length < 2 and "s" or ""} this'


# b = filter(check, [1, 'a', 2])
# adults = filter(check, [1, 'a', 2])
# for i in adults:
#     print(list(filter(check(x, int), [1, 'a', 2])))

def tribonacci(signature, n):
    # current = sum(signature[:3])
    for i in range(0, n - 3):
        signature.append(sum(signature[-3::]))
        # current += signature[i+1] - signature[i-2]
    return signature[0:n]


def find_even_index(arr):
    right_sum = sum(arr)
    left_sum = 0
    for i in range(0, len(arr)):
        if left_sum != right_sum - arr[i]:
            left_sum += arr[i]
            right_sum -= arr[i]
        else:
            return i
    return -1


def find_uniq(arr):
    # arr.sort()
    # if arr[0] == arr[1]:
    #     return arr[-1]
    # else:
    #     return arr[0]
    extra = 0
    if arr[0] == arr[1]:
        extra = arr[0]
    else:
        if arr[0] == arr[2]:
            return arr[1]
        elif arr[1] == arr[2]:
            return arr[0]
    for i in range(2, len(arr)):
        if arr[i] != extra:
            return arr[i]


def cakes(recipe, available):
    res = math.inf
    keys = list(recipe.keys())
    for i in range(len(recipe)):
        curr_key = keys[i]
        if curr_key in available:
            div = available[curr_key] // recipe[curr_key]
            res = min(res, div)
            if div <= 0:
                return 0
        else:
            return 0
    return res


# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}


def valid_parentheses(string):
    parentheses = {'(': 0, '[': 0, '{': 0}
    last = ''
    for i in range(0, len(string)):
        if min(parentheses.values()) >= 0:
            if string[i] in '({[':
                parentheses[string[i]] += 1
            elif string[i] == ')':
                if last in '[{':
                    return False
                parentheses['('] -= 1
            elif string[i] == ']':
                if last in '({':
                    return False
                parentheses['['] -= 1
            elif string[i] == '}':
                if last in '([':
                    return False
                parentheses['{'] -= 1
            last = string[i]
        else:
            return False
    res = list(parentheses.values())
    return res[0] == 0 and res[1] == 0 and res[2] == 0


def alphabet_position(text):
    text = text.lower()
    return " ".join([str(ord(i) - 96) for i in text if i.isalpha()])


def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        res = 1
        h *= bounce
        while h > window:
            res += 2
            h *= bounce
        return res
    return -1


def drawHeart():
    speed(100)
    color("red")
    pensize(5)
    left(50)
    forward(133)
    circle(50, 200)
    right(140)
    circle(50, 200)
    forward(133)
    up()
    left(60)
    setposition(0, 100)
    forward(-200)
    color("black")

    left(30)
    forward(-30)
    down()
    forward(30)
    up()
    left(-60)
    forward(-30)
    down()
    forward(30)
    left(30)
    forward(18)
    up()
    left(30)
    forward(-30)
    down()
    forward(30)
    up()
    left(-60)
    forward(-30)
    down()
    forward(30)
    left(30)

    forward(100)
    up()
    forward(82)
    down()
    forward(200)
    up()
    left(30)
    forward(-30)
    down()
    forward(30)
    up()
    left(-60)
    forward(-30)
    down()
    forward(30)
    Screen().exitonclick()


import string


def top_3_words(text):
    text = text.translate(str.maketrans("", "", string.punctuation)).lower() + " "
    last_str = ''
    res = {}
    for i in range(len(text)):
        if text[i] == ' ':
            if last_str in res:
                res[last_str] += 1
            else:
                res[last_str] = 1
            last_str = ''
        else:
            last_str += text[i]
    return sorted(res, key=None, reverse=True)[0:3:]


def alphanumeric(password):
    return password.isalnum()


def determinant(matrix):
    return int(np.rint(np.linalg.det(matrix)))


from itertools import combinations


def comb(f):
    # f = open('FILE_NAME').readline().split()
    for x, y, z in combinations(f.split(), 3):
        print("1: " + x + " 2: " + y + " 3: " + z, end='\n')


def done_or_not(board):
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(board[j][i])
        line = list(dict.fromkeys(board[i]))
        temp = list(dict.fromkeys(temp))
        if len(temp) != 9 or len(line) != 9:
            return 'Try again!'
    for x in range(3):
        for y in range(3):
            temp = []
            for i in range(3):
                for j in range(3):
                    temp.append(board[i + x * 3][j + y * 3])
            temp = list(dict.fromkeys(temp))
            if len(temp) != 9:
                return 'Try again!'
    return 'Finished!'


def parse_int(s):
    a = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
         'nine': 9, 'ten': 10,
         'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
         'seventeen': 17,
         'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
         'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000, 'million': 1000000}
    s = s.replace('-', ' ').lower()
    s = s.split()
    res = ['0', '0', '0', '0', '0', '0', '0']
    for i in range(0, len(s)):
        if s[i] == 'and':
            continue
        elif s[i] == 'hundred':
            res[4] = str(a.get(s[i - 1]))
        elif s[i] == 'thousand':
            for j in range(len(str(a.get(s[i - 1])))):
                res[3 - len(str(a.get(s[i - 1]))) + j + 1] = str(a.get(s[i - 1]))[j]
        elif s[i] == 'million':
            res[0] = 1
        else:
            if i != len(s) - 1:
                if s[i + 1] == 'hundred' or s[i + 1] == 'thousand' or s[i + 1] == 'million':
                    continue
            if len(str(a.get(s[i]))) > 1:
                res[5] = str(a.get(s[i]))[0]
                res[6] = str(a.get(s[i]))[1]
            else:
                res[6] = str(a.get(s[i]))
    for i in range(len(res)):
        if res[i] != '0':
            res = res[i::]
            break
    return int(''.join(str(i) for i in res))


def sort_key(elem):
    return int(elem[1])


def n():
    f = open('del.txt', 'r')
    lines = f.readlines()
    l = [line.strip().split() for line in lines]
    l = sorted(l, key=sort_key, reverse=True)
    # a = l[::2]
    # b = l
    for i in range(0, len(l), 2):
        print(l[i])

    for i in range(1, len(l), 2):
        print(l[i])


def longest_repetition(chars):
    best = 0
    best_char = ''
    cur = 1
    for i in range(1, len(chars)):
        if chars[i - 1] == chars[i]:
            cur += 1
        else:
            if cur > best:
                best = cur
                best_char = chars[i - 1]
            cur = 1
    if cur > best:
        best = cur
        best_char = chars[len(chars) - 1]
    return best_char, best


def zhurnalist():
    file = open('del.txt')
    res = open('res.txt', 'w')
    f = file.readlines()
    f = [line.strip().split() for line in f]
    f = sorted(f, key=len)
    for i in range(len(f)):
        f[i] = sorted(f[i], key=len)
        print(' '.join(f[i]), file=res)


def med():
    f = open('del.txt').readlines()
    res = open('res.txt', 'w')
    f = [line.strip().split() for line in f]
    f = list(zip(*f))
    for i in f:
        print(*i, file=res)


import re


def calls():
    f = open('del.txt', 'r').readlines()
    res = open('res.txt', 'w')
    f = [line.strip().split() for line in f]
    for i in range(len(f) - 1, 0, -1):
        if not f[i]:
            f.pop(i)
    a, b = [], []
    for i in range(len(f)):
        if f[i][2] == 'A':
            a.append(f[i])
        else:
            b.append(f[i])
    a, b = sorted(a, key=lambda x: int(x[1]), reverse=True), sorted(b, key=lambda x: int(x[1]), reverse=True)
    for i in range(len(a)):
        print('\t'.join(a[i]), file=res)
    for i in range(len(b) - 1):
        print('\t'.join(b[i]), file=res)
    print('\t'.join(b[-1]), end='', file=res)
    res.close()


def animals():
    f = open('del.txt').readlines()
    f = [line.strip().split() for line in f]
    animals_list = [line[1] for line in f]
    animals_list = set(animals_list)
    animals_list = sorted(animals_list, key=len)
    print(*animals_list, sep='\n')


def animals1():
    f = open('del.txt').readlines()
    f = [line.strip().split() for line in f]
    f = set((i[1], i[2]) for i in f)
    f = sorted(f, key=lambda x: (len(x[0]), x[0]))
    for i in range(1, len(f)):
        if f[i - 1][0] == f[i][0]:
            print(f[i][0])


def animals2():
    f = open('del.txt').readlines()
    f = [line.strip().split() for line in f]
    f = sorted(f, key=lambda x: (len(x[1]), x[0]))
    res = {}
    for i in range(0, len(f)):
        if f[i][1] in res.keys():
            res[f[i][1]].append(f[i][0])
        else:
            res[f[i][1]] = [f[i][0]]
    k = list(res.keys())
    for i in range(len(k)):
        print(f'{k[i]}: ' + f'{", ".join(res[k[i]])}')


def bin_search(lst) -> int:
    left = 0
    right = len(lst) - 1
    while True:
        mid = (left + right) // 2
        cur = int(lst[mid])
        if cur == 1415:
            return mid
        elif cur > 1415:
            right = mid - 1
        else:
            left = mid + 1


def dresses():
    f = open('input1.csv', encoding="utf-8").readlines()
    f = [line.strip().split()[0].split(",") for line in f]
    sum_1 = sum(int(line[0]) for line in f)
    sum_2 = sum(int(line[1]) for line in f)
    sum_3 = sum(int(line[2]) for line in f)
    s = max(sum_1, sum_2, sum_3)
    if s == sum_1:
        print(1)
    elif s == sum_2:
        print(2)
    elif s == sum_3:
        print(3)


def users():
    f = open('input1.csv').readlines()[1::]
    f = [line.strip().split()[0].split(",") for line in f]
    f = np.asarray(f).astype(float)
    s = [0, 0]
    for i in range(len(f)):
        a = np.std(f[i])
        if abs(a) > 4:
            s[1] += 1
        else:
            s[0] += 1
    print(1 + s.index(max(s)))


def harry_potter():
    f = open('del.txt').readlines()
    f = [line.strip().split()[0].split(",") for line in f]
    res = open('res.txt', 'w')
    for i in range(len(f[0])):
        s = [f[j][i] for j in range(len(f))]
        s = np.asarray(s).astype(int)
        f[0][i] = int(np.average(s) * 1.5)
    for i in range(len(f)):
        print(','.join(map(str, f[i])), file=res)


class GeomRangeIterator:

    def __init__(self, iter_list, iter_x):
        self.list = iter_list
        self.x = iter_x

    def __iter__(self):
        return self

    def __next__(self):
        if self.x + 1 < len(self.list):
            self.x += 1
            return self.list[self.x]
        else:
            raise StopIteration


class GeomRange:

    def __init__(self, *args):

        if len(args) == 1:
            self.a = 1
            self.b = args[0]
            self.c = 2
        elif len(args) == 2:
            self.a = args[0]
            self.b = args[1]
            self.c = 2
        else:
            self.a = args[0]
            self.b = args[1]
            self.c = args[2]

        self.list = []
        self.x = -1
        self.fill_list()

    def fill_list(self):
        curr = self.a
        for i in range(self.a, self.b):
            if curr < self.b:
                self.list.append(curr)
                curr = curr * self.c

    def __getitem__(self, item):
        if item < len(self.list):
            print(self.list[item])
        else:
            raise IndexError("index is out of the progression")

    def __iter__(self):
        return GeomRangeIterator(self.list, self.x)


class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = float(age)

    def __repr__(self):
        return f"Student({self._name}, {self._age})"

    def __str__(self):
        return "Student " + self._name + " of age " + str(self._age)


# import pandas as pd
# df = pd.DataFrame({'name': ["A", "B", "C", "D", "E"], 'phys': [5, 3, 5, 5, 5], 'math': [5, 4, 4, 5, 3]})
#
# query_e = "phys==5"
# a = df.query(query_e)
# print(a['math'].mean())

# import numpy as np
# A = np.arange(126).reshape((9, -1))
# print(A[7:2:-2, 10:5:-1])


def romanToInt(s):
    res = 0
    i = 1
    nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    while i < len(s):
        if s[i - 1:i + 1] in nums:
            res += nums[s[i - 1:i + 1]]
            i += 2
        else:
            res += nums[s[i - 1]]
            i += 1

    if i <= len(s):
        res += nums[s[i - 1]]

    return res


def intToRoman(num):
    res = ""
    i = 12
    ints = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    while num > 0:
        j = num // ints[i]
        res += romans[i] * j
        num -= j * ints[i]
        i -= 1
    return res


def maxStrength(nums):
    if len(nums) == 1:
        return nums[0]

    numsNeg = [i for i in nums if i < 0]
    numsNeg = sorted(numsNeg)
    nums = [i for i in nums if i > 0]

    if len(nums) + len(numsNeg) == 0:
        return 0
    else:
        res = 1

        if len(numsNeg) % 2 == 1:
            numsNeg.pop(-1)

        for i in numsNeg:
            res *= i
        for i in nums:
            res *= i

    return res


class SnapshotArray(object):
    arr = []
    snap_id = -1

    def __init__(self, length):
        self.arr = [[0] for i in range(length)]

    def set(self, index, val):
        self.arr[index][-1] = val

    def snap(self):
        self.snap_id += 1
        for i in range(len(self.arr)):
            self.arr[i].append(self.arr[i][-1])
        return self.snap_id

    def get(self, index, snap_id):
        return self.arr[index][snap_id]


# snapshotArr = SnapshotArray(3)
# snapshotArr.set(0, 5)
# snapshotArr.snap()
# snapshotArr.set(0, 6)
# print(snapshotArr.get(0, 0))

def isSubsequence(s, t):
    left = 0

    for i in range(len(s)):
        found = False
        for j in range(left, len(t)):
            if s[i] == t[j]:
                left = j + 1
                found = True
                break
        if not found:
            return False

    return left >= len(t)


# isSubsequence("ace", "abcde")


def lengthOfLastWord(s):
    return len(s.split()[-1])


# lengthOfLastWord("a")


def isPalindrome(head):
    mas = []
    i = head
    while i:
        mas.append(i)
        i = head.next
    for i in range(0, len(mas) // 2):
        if head[i] == head[-i - 1]:
            continue
        else:
            return False
    return True


# isPalindrome([1,2,2,1])


def mergeAlternately(word1, word2):
    res = ''
    i = 0
    short = min(len(word1), len(word2))
    for i in range(short):
        res += word1[i] + word2[i]

    if short == len(word1):
        return res + word2[i:len(word2):]
    else:
        return res + word1[i:len(word1):]


# print(mergeAlternately("abcd", "yz"))


def distanceTraveled(mainTank, additionalTank):
    res = 0
    while mainTank >= 5 and additionalTank >= 1:
        mainTank -= 4
        additionalTank -= 1
        res += 50
    if mainTank > 5:
        return res + 50
    return res + mainTank * 10


# distanceTraveled(10, 1)


def findNonMinOrMax(self, nums):
    # l = min(nums)
    # r = max(nums)
    # for i in nums:
    #     if i != l and i != r:
    #         return i
    l = nums[0]
    r = l
    for i in nums:
        if i != r:
            r = i
            if i != l:
                return i
    return -1


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def longestAlternatingSubarray(nums, threshold):
    inSs = False
    best = 0
    curr = 0
    for i in range(1, len(nums)):
        if inSs:
            if nums[i - 1] % 2 != nums[i] % 2 and nums[i] <= threshold:
                curr += 1
                if curr >= best:
                    best = curr
            else:
                inSs = False
        else:
            if nums[i - 1] % 2 == 0:
                curr = 1
                if curr >= best:
                    best = curr
                inSs = True


def removeElement(nums, val):
    nums[:] = [i for i in nums if i != val]
    k = len(nums)
    return k


def climbStairs(n):
    if n == 1:
        return 1
    prev = 1
    total = 1
    for i in range(2, n + 1):
        mem = total
        total += prev
        prev = mem
    return total


def twoSum(nums, target):
    sortedNums = sorted(nums)
    l = sortedNums[0]
    r = sortedNums[-1]
    for i in range(l, r + 1):
        for j in range(l, r + 1):
            if sortedNums[i] + sortedNums[j] == target:
                res = [nums.index(sortedNums[i])]
                res.append(nums.index(sortedNums[j], res[0] + 1))
                return res
            elif sortedNums[i] + sortedNums[j] > target:
                break
    maxPossible = len(sortedNums)
    if nums[-1] > target:
        for i in range(maxPossible):
            if nums[i] >= target:
                maxPossible = i + 1
                break
    for i in range(maxPossible):
        for j in range(maxPossible):
            if sortedNums[i] + sortedNums[j] == target:
                res = [nums.index(sortedNums[i])]
                res.append(nums.index(sortedNums[j], res[0] + 1))
                return res
            elif sortedNums[i] + sortedNums[j] > target:
                break


def largestAltitude(gain) -> int:
    res = 0
    curr = 0
    for i in range(len(gain)):
        curr += gain[i]
        if curr > res:
            res = curr
    return res


def moveZeroes(nums) -> None:
    c = nums.count(0)
    nums = [i for i in nums if i != 0]
    nums.extend([0] * c)
    print("AAA")
    # i = 0
    # while i < len(nums):
    #     if nums[i] != 0:
    #         i+=1
    #     else:
    #         nums.append(0)
    #         nums.pop(i)


def addBinary(a, b):
    i = len(a) - 1
    j = len(b) - 1
    temp = 0
    res = ""

    while i >= 0 or j >= 0 or temp != 0:
        if i >= 0:
            temp += int(a[i])
            i -= 1
        if j >= 0:
            temp += int(b[j])
            j -= 1
        res += str(temp % 2)
        temp //= 2

    return res[::-1]


def convert(s: str, numRows: int) -> str:
    res = [[] for i in range(numRows)]
    i = 0
    j = 0
    offset = 0

    if numRows == 1:
        return s

    while i != len(s):
        if offset == 0:
            for x in range(0, numRows):
                if i == len(s):
                    break
                res[x].append(s[i])
                i += 1
            offset = numRows - 2
            j += numRows
        else:
            if j % numRows == offset:
                res[j % numRows].append(s[i])
                i += 1
            else:
                res[j % numRows].append('')
            j += 1
            if j % numRows == numRows - 1:
                res[j % numRows].append('')
                j += 1
                offset -= 1

    ans = "".join(str(item) for res[0] in res for item in res[0])
    return ans


def countAndSay(n: int) -> str:
    ans = "1"
    i = 1
    while i < n:
        cur = ""
        j = 0
        while j < len(ans):
            count = 1
            while j + 1 < len(ans) and ans[j] == ans[j + 1]:
                count += 1
                j += 1
            cur += str(count) + ans[j]
            if j + 1 == len(ans):
                break
            j += 1
        ans = cur
        i += 1
    return ans


def letterCombinations(digits: str) -> List[str]:
    map = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    res = []

    def buildStrings(i, temp):
        if len(temp) == len(digits):
            res.append(temp)
            return
        chars = map[digits[i]]
        for j in chars:
            temp += j
            buildStrings(i + 1, temp)
            temp = temp[:-1:]

    if len(digits) != 0:
        buildStrings(0, "")
    return res


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    newNums = nums1 + nums2
    newNums.sort()

    if len(newNums) % 2 == 0:
        return (newNums[len(newNums) // 2 - 1] + newNums[len(newNums) // 2]) / 2.0

    return newNums[len(newNums) // 2]


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if len(lists) == 0:
        return None
    minI = 0
    minVal = 10000

    i = 0
    while i < len(lists):
        if lists[i] is None:
            del lists[i]
        else:
            if lists[i].val < minVal:
                minVal = lists[i].val
                minI = i
            i += 1

    if len(lists) == 0:
        return None

    head = ListNode(lists[minI].val, None)
    tail = head
    lists[minI] = lists[minI].next
    # if lists[minI] is None:
    #     del lists[minI]

    while any(lists):
        minVal = 10000
        minI = 0
        for i in range(len(lists)):
            if lists[i].val < minVal:
                minVal = lists[i].val
                minI = i
        tail.next = lists[minI]
        tail = tail.next
        lists[minI] = lists[minI].next
        # if lists[minI] is None:
        #     del lists[minI]

    return head


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    elif head.next is None:
        return head

    result = ListNode(head.next.val, None)
    # tail = result.next
    tail = result
    while True:
        tail.next = head.next
        tail.next = head
        tail.next.next = head.next.next
        tail = tail.next.next
    return


def generate(numRows: int) -> List[List[int]]:
    res = [[1], [1, 1]]

    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return res

    for i in range(2, numRows):
        temp = [1]
        for j in range(1, len(res[i - 1])):
            temp.append(res[i - 1][j - 1] + res[i - 1][j])
        temp.append(1)
        res.append(temp)

    return res


def getRow(rowIndex: int) -> List[int]:
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]

    prev = [1, 1]
    for i in range(1, rowIndex):
        temp = [1]
        for j in range(1, len(prev)):
            temp.append(prev[j - 1] + prev[j])
        temp.append(1)
        prev = temp
    return prev


def minimumTotal(triangle: List[List[int]]) -> int:
    if len(triangle) == 1:
        return triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if 0 < j < len(triangle[i]) - 1:
                triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
            elif j == 0:
                triangle[i][j] += triangle[i - 1][0]
            else:
                triangle[i][j] += triangle[i - 1][-1]

    return min(triangle[-1])


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None or q is None:
        return False

    if p is None and q is None:
        return True

    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    return False


# def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:


def restoreIpAddresses(s: str) -> List[str]:
    res = []
    temp = s
    for i in range(len(s), 0, -1):
        a = (temp[i - 1:len(temp)])
        if 0 <= int(temp[i - 1:len(temp)]) <= 255:
            temp = temp[0:i - 1] + '.' + temp[i - 1:len(temp)]
        else:
            break
        for j in range(i - 1, 2, -1):
            a = (temp[j - 1:i - 1])
            if 0 <= int(temp[j - 1:i - 1]) <= 255:
                left = temp[0:j - 1]
                right = temp[i - 2:len(temp)]
                temp = temp[0:j - 1] + '.' + temp[i - 2:len(temp)]
            else:
                break
            for k in range(j - 1, 1, -1):
                a = (temp[k - 1:j - 1])
                if 0 <= int(temp[k - 1:j - 1]) <= 255:
                    left = temp[0:k - 1]
                    right = temp[j - 2:len(temp)]
                    temp = temp[0:k - 1] + '.' + temp[j - 2:len(temp)]
                    res.append(temp)
                else:
                    break
    return []


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    i = left
    a = copy(head)
    temp = ListNode()
    for j in range(left, right):
        while i < right:
            a = a.next
            i += 1
        temp = a.next


def findSubstring(s: str, words: List[str]) -> List[int]:
    def checkSubstring(i):
        amountOfUsedWords = 0
        tempMap = map.copy()
        temp = i

        while temp < i + substringLength:
            substring = s[temp:temp + wordsLen]
            if substring in tempMap:
                tempMap[substring] -= 1
                if tempMap[substring] == 0:
                    amountOfUsedWords += 1
                temp += wordsLen
            else:
                return False

        if amountOfUsedWords == len(tempMap):
            return True
        return False

    wordsLen = len(words[0])
    substringLength = len(words) * wordsLen
    map = {}
    res = []
    i = 0

    for x in words:
        if x in map:
            map[x] += 1
        else:
            map[x] = 1

    while i < len(s) - substringLength + 1:
        if checkSubstring(i):
            res += [i]
        i += 1

    return res


def titleToNumber(columnTitle: str) -> int:
    res = 0
    for i in columnTitle:
        res *= 26
        res += ord(i) - 64
    return res


def convertToTitle(columnNumber: int) -> str:
    res = ""
    while columnNumber > 26:
        columnNumber -= 1
        res += chr((columnNumber % 26) + 65)
        columnNumber //= 26
    res += chr(columnNumber + 64)
    return res[::-1]


def hasCycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False

    map = []

    while head.next is not None:
        if head in map:
            return True
        else:
            map.append(head)
        head = head.next

    return False


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.val]


def singleNumber(nums: List[int]) -> int:
    map = defaultdict(int)
    for i in nums:
        map[i] += 1

    for i in map.items():
        if i[1] == 1:
            return i[0]

    return 0


def candy(ratings: List[int]) -> int:
    n = len(ratings)
    res = [1 for i in range(len(ratings))]

    for i in range(n - 1):
        if ratings[i] < ratings[i + 1]:
            res[i + 1] = max(1 + res[i], res[i + 1])

    for i in range(n - 2, -1, -1):
        if ratings[i + 1] < ratings[i]:
            res[i] = max(1 + res[i + 1], res[i])

    return sum(res)


def countNodes(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    return 1 + countNodes(root.left) + countNodes(root.right)


def isPowerOfTwo(n: int) -> bool:
    res = [2 ** i for i in range(31)]
    return n in res


def summaryRanges(nums: List[int]) -> List[str]:
    i = 1
    res = []
    n = len(nums)
    while i < n:
        j = i
        while nums[j - 1] + 1 == nums[j]:
            j += 1
            if j >= n:
                break

        if i != j:
            res.append(str(nums[i - 1]) + "->" + str(nums[j - 1]))
        else:
            res.append(str(nums[i - 1]))

        i = j
        i += 1

    if i == n:
        res.append(str(nums[i - 1]))

    return res


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return
    root = TreeNode(root.val, root.right, root.left)
    invertTree(root.left)
    invertTree(root.right)

    return root


def addDigits(num: int) -> int:
    n = str(num)
    res = 0

    for i in n:
        res += int(i)

    if len(str(res)) > 1:
        res = addDigits(res)

    return res


def hammingWeight(n: int) -> int:
    s = str(n)
    count = 0
    for i in range(0, len(s)):
        if s[i] == '1':
            count += 1
    return count


def reverseBits(n: int) -> int:
    s = str(bin(n))[2:]
    s = '0' * (32 - len(s)) + s
    s = s[::-1]
    return int(s, 2)


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if head is None:
        return

    res = None
    while res is None:
        if head.val != val:
            res = ListNode(head.val, None)
        head = head.next

    temp = res
    while head is not None:
        if head.val != val:
            temp.next = ListNode(head.val, None)
            temp = temp.next
        head = head.next

    return res


def isHappy(n: int) -> bool:
    def calc(num):
        res = 0
        while num > 0:
            res += (num % 10) ** 2
            num = num // 10
        return res

    for i in range(100):
        if n != 1:
            n = calc(n)
        else:
            return True

    return False


def isIsomorphic(s: str, t: str) -> bool:
    map = {}
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] in map or t[i] in map.values():
            if t[i] != map.get(s[i]):
                return False
        else:
            map[s[i]] = t[i]
    return True


def reverseString(s: List[str]) -> None:
    s.reverse()


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if head is None:
        return ListNode()

    count = 0
    temp = copy(head)

    while temp:
        temp = temp.next
        count += 1

    required = count - n
    if n != count:
        res = copy(head)
        if n == count - 1:
            res.next = res.next.next
            return res
    else:
        return head.next

    count = 2
    temp = res.next

    while temp.next:
        if count == required:
            temp.next = temp.next.next
            return res
        else:
            temp = temp.next
        count += 1


def nextPermutation(nums: List[int]) -> None:
    per = list(itertools.permutations(nums))
    for i in range(len(per)):
        if list(per[i]) == nums:
            if i == len(per) - 1:
                nums = list(per[0])
            else:
                nums = list(per[i + 1])
            break


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    map = {}
    for i in strs:
        combination = ''.join(sorted(i))
        if combination in map:
            map[combination].append(i)
        else:
            map[combination] = [i]
    return [map[i] for i in map.keys()]


# def exist(board: List[List[str]], word: str) -> bool:
#     for i in range(0, len(board[0])):
#         for j in range(0 , len(board)):
#             if board[j][i] == word[0]:
#                 char_index = 0
#                 while char_index != len(word):
#
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    left = inorderTraversal(root.left)
    right = inorderTraversal(root.right)
    return left + [root.val] + right


def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None
    res = TreeNode(nums[len(nums) // 2])
    res.left = sortedArrayToBST(nums[0:len(nums) // 2])
    res.right = sortedArrayToBST(nums[len(nums) // 2 + 1:])
    return res


def sortedListToBST(head: Optional[ListNode]) -> Optional[TreeNode]:
    nums = []
    while head is not None:
        nums.append(head.val)
        head = head.next

    def createBinaryTree(l):
        if len(l) == 0:
            return None
        res = TreeNode(l[len(l) // 2])
        res.left = createBinaryTree(l[0:len(l) // 2])
        res.right = createBinaryTree(l[len(l) // 2 + 1:])
        return res

    return createBinaryTree(nums)


def hIndex(citations: List[int]) -> int:
    citations.sort()
    citations.reverse()
    h = 0
    while h < len(citations) and citations[h] > h:
        h += 1
    return h


def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    return str1[:math.gcd(len(str1), len(str2))]


def reverseWords(s: str) -> str:
    i = len(s) - 1
    res = ""
    temp = ""
    while i >= 0:
        if s[i] != " ":
            temp += s[i]
        else:
            if temp != "":
                res = res + " " + temp[::-1]
                temp = ""
        i -= 1
    if temp != "":
        res = res + " " + temp[::-1]
    res = res[1:len(res)]
    return res


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix_product = 1
    postfix_product = 1
    result = [0] * n
    for i in range(n):
        result[i] = prefix_product
        prefix_product *= nums[i]
    for i in range(n - 1, -1, -1):
        result[i] *= postfix_product
        postfix_product *= nums[i]
    return result


def increasingTriplet(nums: List[int]) -> bool:
    min_num = max(nums)
    mid_num = min_num
    for i in nums:
        if i <= min_num:
            min_num = i
        elif i <= mid_num:
            mid_num = i
        else:
            return True
    return False


def compress(chars: List[str]) -> int:
    i = 0
    seq_len = 0
    while i < len(chars) - 1:
        seq_len += 1
        if chars[i] != chars[i + 1]:
            if seq_len > 1:
                for j in range(1, len(str(seq_len)) + 1):
                    chars[i - seq_len + j + 1] = str(seq_len)[j - 1]
                chars = chars[:i - seq_len + 1] + chars[
                    i - seq_len + 1:i - seq_len + 1 + len(str(seq_len)) + 1] + chars[
                            i + 1:]
            seq_len = 0
        i += 1
    if seq_len > 0:
        seq_len += 1
        if seq_len > 1:
            for j in range(1, len(str(seq_len)) + 1):
                chars[i - seq_len + j + 1] = str(seq_len)[j - 1]
            chars = chars[:i - seq_len + 1] + chars[i - seq_len + 1:i - seq_len + 1 + len(str(seq_len)) + 1] + chars[
                i + 1:]
    return len(chars)


def reverseVowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    temp = ""
    s = list(s)
    for i in range(len(s)):
        if s[i] in vowels:
            temp += s[i]
    temp = temp[::-1]
    j = 0
    for i in range(len(s)):
        if s[i] in vowels:
            s[i] = temp[j]
            j += 1
    return ''.join(s)


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    res = []
    maxCandies = max(candies)
    for i in range(len(candies)):
        res.append(candies[i] + extraCandies >= maxCandies)
    return res


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    maxArea = 0
    while left < right:
        currentArea = min(height[left], height[right]) * (right - left)
        maxArea = max(maxArea, currentArea)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxArea


def maxOperations(nums: List[int], k: int) -> int:
    searching_for = {}
    i = 0
    res = 0
    while i < len(nums):
        if nums[i] in searching_for:
            if len(searching_for[nums[i]]) == 1:
                searching_for.pop(nums[i])
            else:
                searching_for[nums[i]].pop(0)
            res += 1
        else:
            if k - nums[i] in searching_for:
                searching_for[k - nums[i]].append(i)
            else:
                searching_for[k - nums[i]] = [i]
        i += 1
    return res


def findMaxAverage(nums: List[int], k: int) -> float:
    curr = 0
    for i in range(k):
        curr += nums[i]
    res = curr / k
    for i in range(1, len(nums) - k + 1):
        curr -= nums[i - 1]
        curr += nums[i + k - 1]
        if curr / k > res:
            res = curr / k
    return res


def longestSubarray(nums: List[int]) -> int:
    n = len(nums)
    prev = 0
    curr = 0
    i = 0
    max_l = 0

    while nums[i] == 0:
        i += 1

    while i < n - 1:
        if nums[i] != 0:
            curr += 1
        else:
            if curr + prev > max_l:
                max_l = curr + prev
            prev = curr
            curr = 0
        i += 1

    if nums[n - 1] == 1:
        curr += 1

    if curr == n:
        return n - 1

    if curr + prev > max_l:
        max_l = curr + prev

    return max_l


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def calc(array, temp, candidates, target, start):
        if temp == target:
            res.append(array)
        for i in range(start, len(candidates)):
            curr = candidates[i]
            if temp + i > target:
                return
            new_array = list(array)
            new_array.append(curr)
            new_temp = temp + curr
            calc(new_array, new_temp, candidates, target, i)

    res = []
    candidates.sort()
    calc([], 0, candidates, target, 0)

    return res


def minFlips(a: int, b: int, c: int) -> int:
    a = str(bin(a))[2:]
    b = str(bin(b))[2:]
    c = str(bin(c))[2:]

    max_l = max(len(a), len(b), len(c))
    if len(a) < max_l:
        a = "0" * (max_l - len(a)) + a
    if len(b) < max_l:
        b = "0" * (max_l - len(b)) + b
    if len(c) < max_l:
        c = "0" * (max_l - len(c)) + c

    res = 0
    for i in range(len(c)):
        if c[i] == "0":
            res += 1 if a[i] != "0" else 0
            res += 1 if b[i] != "0" else 0
        else:
            res += 1 if (a[i] != "1" and b[i] != "1") else 0

    return res


def pivotIndex(nums: List[int]) -> int:
    s = sum(nums)
    s -= nums[0]
    temp_s = 0
    if temp_s == s:
        return 0

    for i in range(1, len(nums)):
        temp_s += nums[i - 1]
        s -= nums[i]
        if temp_s == s:
            return i

    return -1


def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    com = itertools.combinations(range(1, 10), k)
    res = []
    for i in com:
        if sum(i) == n:
            res.append(i)
    return res


def maxVowels(s: str, k: int) -> int:
    vowels = 'aeiou'
    substr = s[0:k]
    res = 0
    temp = 0
    for i in substr:
        if i in vowels:
            temp += 1
    if temp > res:
        res = temp
    for i in range(k, len(s)):
        if s[i] in vowels:
            temp += 1
        if substr[0] in vowels:
            temp -= 1
        substr = substr[1:k]
        substr += s[i]
        if temp > res:
            res = temp
        if res == k:
            break
    return res


def longestOnes(self, nums: List[int], k: int) -> int:
    l = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            k -= 1
        if k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
    return i - l + 1


def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def getLeaf(root) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        return getLeaf(root.left) + getLeaf(root.right)

    return getLeaf(root1) == getLeaf(root2)


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    amountOfRooms = len(rooms)
    leftKeys = rooms[0]
    visitedRooms = [0]
    while len(leftKeys) > 0:
        newKeys = []
        for i in range(len(leftKeys)):
            if leftKeys[i] not in visitedRooms:
                visitedRooms.append(leftKeys[i])
                newKeys += rooms[leftKeys[i]]
        leftKeys = newKeys
    return len(visitedRooms) == amountOfRooms


def predictPartyVictory(senate: str) -> str:
    i = 0
    r_count = senate.count('R')
    d_count = senate.count('D')
    curr_r = 0
    curr_d = 0
    while i < len(senate) and d_count > 0 and r_count > 0:
        if senate[i] == 'R':
            if curr_r <= r_count:
                curr_r += 1
                d_count -= 1
            else:
                return 'Dire'
        else:
            if curr_d <= d_count:
                curr_d += 1
                r_count -= 1
            else:
                return 'Radiant'
        i += 1
    return 'Radiant' if r_count > d_count else 'Dire'


class Trie:

    def __init__(self):
        self.l = []

    def insert(self, word: str) -> None:
        self.l.append(word)

    def search(self, word: str) -> bool:
        return word in self.l

    def startsWith(self, prefix: str) -> bool:
        for i in self.l:
            if i.startswith(prefix):
                return True
        return False


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root is not None and root.val != val:
        if root.val > val:
            root = root.left
        else:
            root = root.right
    return root


def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return root

    if root.val > key:
        root.left = deleteNode(root.left, key)
    elif root.val < key:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        if root.left and root.right:
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = deleteNode(root.right, root.val)

    return root


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    res = 0
    min_i = -5 * 10 ** 4
    intervals = sorted(intervals, key=lambda x: x[1])
    for i in intervals:
        if (i[0] >= min_i):
            min_i = i[1]
        else:
            res += 1
    return res


def findMinArrowShots(points: List[List[int]]) -> int:
    res = 1
    min_i = -math.inf
    max_i = math.inf
    points = sorted(points)
    for i in points:
        if i[0] >= min_i and i[0] <= max_i:
            max_i = min(i[1], max_i)
        else:
            max_i = i[1]
            res += 1
        min_i = i[0]
    return res


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > stack[-1][0]:
            temp_i = stack.pop()[1]
            res[temp_i] = i - temp_i
        stack.append([temperatures[i], i])
    return res


class StockSpanner:

    def __init__(self):
        self.l = []

    def next(self, price: int) -> int:
        res = 1
        while self.l and self.l[-1][0] <= price:
            prev = self.l.pop()[1]
            res += prev
        self.l.append((price, res))
        return res


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()
    max_potion = potions[-1]
    n = len(potions)
    stack = []
    for i in range(len(spells)):
        required = math.ceil(success / spells[i])
        if required > max_potion:
            stack.append(0)
        else:
            index_potion = bisect_left(potions, required)
            stack.append(n - index_potion)
    return stack


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    if root.right is not None:
        return [root.val] + rightSideView(root.right)
    else:
        return [root.val] + rightSideView(root.left)


def maxLevelSum(root: Optional[TreeNode]) -> int:
    def calcLevel(root, level):
        if map.get(level) is None:
            map[level] = root.val
        else:
            map[level] += root.val
        if root.right is not None:
            calcLevel(root.right, level + 1)
        if root.left is not None:
            calcLevel(root.left, level + 1)

    map = {}
    calcLevel(root, 1)
    res = 0
    maxSum = -100000
    for i in range(len(map.values())):
        if map[i + 1] > maxSum:
            maxSum = map[i + 1]
            res = i + 1
    return res


def uniqueOccurrences(arr: List[int]) -> bool:
    arr.sort()
    res = []
    i = 0
    while i < len(arr):
        temp = arr.count(arr[i])
        res.append(temp)
        i += temp
    return len(res) == len(set(res))


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = {}
        self.ratings = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisines[cuisine].add((-rating, food))
            self.ratings[food].append((cuisine, rating))
        self.cuisines = sorted(self.cuisines)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.ratings[food][0]
        self.cuisines[cuisine].remove((-rating, food))
        self.cuisines[cuisine].add((-newRating, food))
        self.ratings[food][0] = (cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines[cuisine][0][1]


def closeStrings(word1: str, word2: str) -> bool:
    map1 = Counter(word1)
    map2 = Counter(word2)
    return sorted(map1.keys()) == sorted(map2.keys())


def equalPairs(grid: List[List[int]]) -> int:
    counter = collections.Counter()
    for row in grid:
        counter[tuple(row)] += 1

    res = 0
    n = len(grid)
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(grid[j][i])
        res += counter[tuple(temp)]

    return res


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    odd, even_start = head, head.next
    even_end = even_start

    while even_end and even_end.next:
        odd.next, even_end.next = odd.next.next, even_end.next.next
        odd, even_end = odd.next, even_end.next

    odd.next = even_start

    return head


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    temp = head
    count = 0

    while temp:
        count += 1
        temp = temp.next

    temp = head
    mid = count // 2
    if mid == 0:
        return None

    i = 0
    while temp:
        i += 1
        if i == mid:
            temp.next = temp.next.next
            break
        temp = temp.next

    return head


def maxProductDifference(nums: List[int]) -> int:
    highest = max(nums)
    nums.remove(highest)
    preHighest = max(nums)

    lowest = min(nums)
    nums.remove(lowest)
    preLowest = min(nums)

    return (highest * preHighest) - (lowest * preLowest)


def imageSmoother(img: List[List[int]]) -> List[List[int]]:
    res = []
    for i in range(len(img)):
        res.append(copy(img[i]))
        for j in range(len(img[i])):
            avg = img[i][j]
            counted = 1

            if i + 1 < len(img):
                avg += img[i + 1][j]
                counted += 1
            if i - 1 >= 0:
                avg += img[i - 1][j]
                counted += 1

            if j + 1 < len(img[i]):
                avg += img[i][j + 1]
                counted += 1
                if i + 1 < len(img):
                    avg += img[i + 1][j + 1]
                    counted += 1
                if i - 1 >= 0:
                    avg += img[i - 1][j + 1]
                    counted += 1

            if j - 1 >= 0:
                avg += img[i][j - 1]
                counted += 1
                if i + 1 < len(img):
                    avg += img[i + 1][j - 1]
                    counted += 1
                if i - 1 >= 0:
                    avg += img[i - 1][j - 1]
                    counted += 1

            res[i][j] = avg // counted

    return res


def pairSum(head: Optional[ListNode]) -> int:
    if not head.next.next:
        return head.val + head.next.val

    temp = copy(head)
    count = 0
    while temp:
        count += 2
        temp = temp.next.next

    count //= 2
    left = []
    right = []
    i = 1
    temp = copy(head)
    while i <= count:
        left.append(temp.val)
        temp = temp.next
        i += 1

    i = 1
    while i <= count:
        right.append(temp.val)
        temp = temp.next
        i += 1

    s = 0
    n = len(left)
    for i in range(n):
        if left[i] + right[n - 1 - i] > s:
            s = left[i] + right[n - 1 - i]

    return s


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    temp = head
    while temp:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    return prev


def removeStars(s: str) -> str:
    stack = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '*':
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
    return "".join(stack)


def rob(nums: List[int]) -> int:
    if len(nums) < 3:
        return max(nums)
    M = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        M = M[1], max(nums[i] + M[0], M[1])
    return M[1]


def buyChoco(prices: List[int], money: int) -> int:
    m1 = min(prices)
    prices.remove(m1)
    m2 = min(prices)
    if m1 + m2 > money:
        return money
    return money - m1 - m2


def asteroidCollision(asteroids: List[int]) -> List[int]:
    goingRight = []
    goingLeft = []
    for i in asteroids:
        if i > 0:
            goingRight.append(i)
        else:
            goingLeft.append(i)

    while len(goingRight) > 0 and len(goingLeft) > 0:
        a = abs(goingRight[-1])
        b = abs(goingLeft[0])
        if a > b:
            goingLeft.pop(0)
        elif b > a:
            goingRight.pop(-1)
        else:
            goingLeft.pop(0)
            goingRight.pop(-1)

    if len(goingRight) > 0:
        return goingRight
    return goingLeft


def decodeString(s: str) -> str:
    n = 0
    res = ''
    stack = []

    for i in s:
        if i.isnumeric():
            n = n * 10 + int(i)
        elif i == '[':
            stack.append(res)
            stack.append(n)
            res = ''
            n = 0
        elif i == ']':
            count = stack.pop()
            prev = stack.pop()
            res = prev + count * res
        else:
            res += i

    return res


def findCircleNum(isConnected: List[List[int]]) -> int:
    l = [i + 1 for i in range(len(isConnected[0]))]

    def union(x, y):
        tempX = l[x]
        tempY = l[y]
        if tempX != tempY:
            for i in range(0, len(l)):
                if l[i] == tempY:
                    l[i] = tempX

    for i in range(0, len(isConnected)):
        for j in range(i + 1, len(isConnected[0])):
            if isConnected[i][j] == 1:
                union(i, j)

    return len(set(l))


def minCostClimbingStairs(cost: List[int]) -> int:
    cost.append(0)
    for i in range(len(cost)):
        cost[i] += min(cost[i - 1], cost[i - 2])
    return cost[-1]


def maxScore(s: str) -> int:
    left = 1 if s[0] == '0' else 0
    right = 0
    for i in range(1, len(s)):
        right += int(s[i])
    m = left + right
    for i in range(1, len(s) - 1):
        if s[i] == '0':
            left += 1
        else:
            right -= 1
        if left + right > m:
            m = left + right
    return m


def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    adjacencyList = collections.defaultdict(list)
    for i, eq in enumerate(equations):
        a, b = eq
        adjacencyList[a].append([b, values[i]])
        adjacencyList[b].append([a, 1 / values[i]])

    def bfs(src, trg):
        if src not in adjacencyList or trg not in adjacencyList:
            return -1
        q = collections.deque()
        visited = set()
        q.append([src, 1])
        visited.add(src)
        while q:
            n, w = q.popleft()
            if n == trg:
                return w
            for neighbor, weight in adjacencyList[n]:
                if neighbor not in visited:
                    q.append([neighbor, w * weight])
                    visited.add(n)
        return -1

    return [bfs(query[0], query[1]) for query in queries]


def uniquePaths(m: int, n: int) -> int:
    curr_row = [1] * n
    prev_row = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            curr_row[j] = curr_row[j - 1] + prev_row[j]
        curr_row, prev_row = prev_row, curr_row

    return prev_row[-1]


def minDistance(word1: str, word2: str) -> int:
    len1 = len(word1) + 1
    len2 = len(word2) + 1
    dp = [[-1 for j in range(len2)] for j in range(len1)]

    for i in range(len1):
        for j in range(len2):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i - 1][j - 1], dp[i][j - 1]))

    return dp[len1 - 1][len2 - 1]


def longestCommonSubsequence(s1: str, s2: str) -> int:
    prev = [0 for _ in range(len(s1) + 1)]
    cur = [0 for _ in range(len(s1) + 1)]

    for ch2 in s2:
        i = len(s1) - 1
        for ch1 in s1:
            if ch1 == ch2:
                cur[i] = prev[i + 1] + 1
            else:
                cur[i] = max(cur[i + 1], prev[i])
            i -= 1
        cur, prev = prev, cur

    return prev[0]


def maxProfit(prices: List[int], fee: int) -> int:
    if len(prices) <= 1:
        return 0

    buy = -prices[0]
    sell = 0
    for i in range(1, len(prices)):
        buy = max(buy, sell - prices[i])
        sell = max(sell, prices[i] - fee + buy)

    return sell


def minOperations(s: str) -> int:
    curr1 = 0
    s1 = s[0]
    curr2 = 0
    s2 = '0' if s[0] == '1' else '1'
    for i in range(1, len(s)):
        if s1[i - 1] == '0':
            if s[i] == '1':
                curr1 += 1
        else:
            if s[i] == '1':
                curr1 += 1
        if s2[i - 1] == '0':
            if s[i] == '0':
                curr2 += 1


class Sol:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(root, max_val):
            if root is None:
                return

            if root.val >= max_val:
                self.good += 1
                max_val = root.val

            dfs(root.left, max_val)
            dfs(root.right, max_val)

        dfs(root, float('-inf'))
        return self.good

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0

        def search(root, possibleSums):
            if root is None:
                return
            possibleSums.append(root.val)
            if possibleSums[-1] == targetSum:
                self.count += 1
            for i in range(len(possibleSums) - 1):
                possibleSums[i] += root.val
                if possibleSums[i] == targetSum:
                    self.count += 1
            search(root.left, possibleSums)
            search(root.right, possibleSums)
            last = possibleSums.pop(-1)
            for i in range(len(possibleSums)):
                possibleSums[i] -= last

        search(root, [])
        return self.count

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root, 0, None)]
        while stack:
            temp = stack.pop()
            if temp[0]:
                res = max(res, temp[1])
                stack.append((temp[0].left, 1 if temp[2] else temp[1] + 1, 1))
                stack.append((temp[0].right, temp[1] + 1 if temp[2] else 1, 0))

        return res

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return TreeNode()

        if root == p or root == q:
            return root

        leftNode = self.lowestCommonAncestor(root.left, p, q)
        rightNode = self.lowestCommonAncestor(root.right, p, q)

        if leftNode and rightNode:
            return root

        if leftNode is None:
            return rightNode
        else:
            return leftNode


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    j = 0
    map = {}
    while j < len(nums):
        if nums[j] in map.keys():
            if map[nums[j]] < 2:
                map[nums[j]] += 1
                nums[i] = nums[j]
                i += 1
        else:
            map[nums[j]] = 1
            nums[i] = nums[j]
            i += 1
        j += 1
    return i


def rotate(nums: List[int], k: int) -> None:
    c = copy(nums)
    n = len(nums)
    for i in range(n):
        nums[i] = c[(i - k) % n]


def maxProfit(prices: List[int]) -> int:
    res = 0
    temp = 0
    for i in range(0, len(prices)):
        if temp > prices[i]:
            temp = prices[i]
        else:
            res += prices[i] - temp
    return res


class RandomizedSet:

    def __init__(self):
        self.l = set()

    def insert(self, val: int) -> bool:
        if not val in self.l:
            self.l.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.l:
            self.l.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.l))


def trap(height: List[int]) -> int:
    maxI = 0
    n = len(height)
    res = 0

    for i in range(1, n):
        if height[i] > height[maxI]:
            maxI = i

    tempMax = height[0]
    for i in range(1, maxI):
        if height[i] > tempMax:
            tempMax = height[i]
        else:
            res += tempMax - height[i]

    tempMax = height[n - 1]
    for i in range(n - 1, maxI, -1):
        if height[i] > tempMax:
            tempMax = height[i]
        else:
            res += tempMax - height[i]

    return res


def minimumLength(s: str) -> int:
    map = {}

    for i in range(len(s)):
        temp = s[i]
        if temp in map.keys():
            map[temp] += 1
        else:
            map[temp] = 1

    res = 0
    for v in map.values():
        if v % 2 == 0:
            res += 2
        else:
            res += v % 2

    return res


def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    n = len(A)
    res = [0] * n
    count = [0] * (n + 1)
    temp = 0

    for i in range(n):
        count[A[i]] += 1
        if count[A[i]] == 2:
            temp += 1

        count[B[i]] += 1
        if count[B[i]] == 2:
            temp += 1

        res[i] = temp

    return res


def minimizeXor(num1, num2):
    onesInNum1 = bin(num1).count('1')
    onesInNum2 = bin(num2).count('1')

    if onesInNum1 == onesInNum2:
        return num1

    if onesInNum1 < onesInNum2:
        diff = onesInNum2 - onesInNum1
        pos = 0

        while diff > 0:
            while (num1 >> pos) & 1 == 1:
                pos += 1
            num1 = num1 | (1 << pos)
            diff -= 1

        return num1

    diff = onesInNum1 - onesInNum2

    while diff > 0:
        num1 = num1 & (num1 - 1)
        diff -= 1

    return num1


def xorAllNums(nums1: List[int], nums2: List[int]) -> int:
    xor1, xor2 = 0, 0

    for i in nums1:
        xor1 ^= i

    for j in nums2:
        xor2 ^= j

    res = 0
    if len(nums2) % 2 == 1:
        res ^= xor1
    if len(nums1) % 2 == 1:
        res ^= xor2

    return res


def doesValidArrayExist(derived: List[int]) -> bool:
    res = 0

    for i in derived:
        res = res ^ i

    return res == 0


def minCost(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dist = [[10000] * n for _ in range(m)]
    dq = collections.deque([(0, 0)])
    dist[0][0] = 0
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    while dq:
        x, y = dq.popleft()
        curDir = grid[x][y] - 1

        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < m and 0 <= ny < n:
                cost = dist[x][y] + (0 if dir == curDir else 1)
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    if dir == curDir:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))

    return dist[m - 1][n - 1]


def trapRainWater(heightMap: List[List[int]]) -> int:
    if heightMap is None or heightMap[0] is None:
        return 0

    m, n = len(heightMap), len(heightMap[0])
    visited = [[False] * n for _ in range(m)]
    heap = []

    for j in range(n):
        heapq.heappush(heap, (heightMap[0][j], 0, j))
        heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
        visited[0][j] = visited[m - 1][j] = True

    for i in range(1, m - 1):
        heapq.heappush(heap, (heightMap[i][0], i, 0))
        heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
        visited[i][0] = visited[i][n - 1] = True

    res = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while heap:
        height, row, col = heapq.heappop(heap)
        for k in range(4):
            new_row, new_col = row + dx[k], col + dy[k]
            if (new_row < 0 or new_row >= m or new_col < 0 or new_col >= n or
                    visited[new_row][new_col]):
                continue
            if heightMap[new_row][new_col] < height:
                res += height - heightMap[new_row][new_col]
                heapq.heappush(heap, (height, new_row, new_col))
            else:
                heapq.heappush(heap, (heightMap[new_row][new_col], new_row, new_col))
            visited[new_row][new_col] = True

    return res


def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])

    to_i = [-1] * (m * n + 1)
    to_j = [-1] * (m * n + 1)

    for i, row in enumerate(mat):
        for j, x in enumerate(row):
            to_i[x] = i
            to_j[x] = j

    R = [0] * m
    C = [0] * n

    for i, x in enumerate(arr):
        R[to_i[x]] += 1
        C[to_j[x]] += 1
        if R[to_i[x]] == n or C[to_j[x]] == m:
            return i

    return -1


def gridGame(grid: List[List[int]]) -> int:
    done, temp = sum(grid[0]) - grid[0][0], 0
    res = done

    for i in range(1, len(grid[0])):
        done -= grid[0][i]
        temp += grid[1][i - 1]
        res = min(res, max(done, temp))

    return res


def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    m, n = len(isWater), len(isWater[0])
    res = [[-1] * n for _ in range(m)]

    queue = collections.deque()

    for i in range(m):
        for j in range(n):
            if isWater[i][j] == 1:
                queue.append((i, j, 0))
                res[i][j] = 0

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, h = queue.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < m and 0 <= nc < n and res[nr][nc] == -1:
                res[nr][nc] = h + 1
                queue.append((nr, nc, h + 1))

    return res


def countServers(grid: List[List[int]]) -> int:
    # m, n = len(grid), len(grid[0])
    # res = 0
    #
    # for i in range(m):
    #     row_pcs = sum(grid[i])
    #     for j in range(n):
    #         if grid[i][j] == 1:
    #             if row_pcs > 1:
    #                 res += 1
    #             else:
    #                 col_pcs = sum([r[j] for r in grid])
    #                 if col_pcs > 1:
    #                     res += 1
    #
    # return res
    res, n = 0, len(grid)

    for r in range(n):
        s = sum(grid[r])
        if s > 1:
            res += s
        elif s == 1:
            col = grid[r].index(1)
            if sum(grid[r][col] for r in range(n)) > 1:
                res += 1

    return res


def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    checked = [0] * len(graph)

    def check_loop(node):
        if checked[node] == -1:
            return True
        if checked[node] == 1:
            return False

        checked[node] = -1
        for i in graph[node]:
            if check_loop(i):
                return True
        checked[node] = 1

        return False

    return [node for node in range(len(graph)) if not check_loop(node)]


def lexicographicallySmallestArray(nums: List[int], limit: int) -> List[int]:
    n, group = len(nums), 0
    sorted_nums = sorted(nums)
    sets = [0]
    map = {sorted_nums[0]: 0}

    for i in range(1, n):
        if sorted_nums[i] - sorted_nums[i - 1] > limit:
            sets.append(i)
            group += 1
        map[sorted_nums[i]] = group

    for i in range(n):
        temp = map[nums[i]]
        nums[i] = sorted_nums[sets[temp]]
        sets[temp] += 1

    return nums


def maximumInvitations(favorite: List[int]) -> int:
    # def dfs(person, temp, fav, left, right):
    #     if fav[person][0] != person:
    #         if not fav[person][1]:
    #             temp += 1
    #             fav[person][1] = True
    #             if person == right or fav[person][0] == left or fav[person][0] == right:
    #                 return max(dfs(fav[person][0], temp, fav, person, right), temp)
    #             else:
    #                 return max(dfs(fav[person][0], temp, fav, person, right), temp-1)
    #         else:
    #             if person == right or fav[person][0] == left or fav[person][0] == right:
    #                 return temp
    #             else:
    #                 return temp - 1
    #     else:
    #         return 2
    #
    # n = len(favorite)
    # res = 0
    # for i in range(n):
    #     favorite_cpy = [[favorite[i], False] for i in range(n)]
    #     res = max(dfs(i, 0, favorite_cpy, 0, i), res)
    #
    # return res

    adj = defaultdict(list)
    transpose = defaultdict(list)
    for i in range(len(favorite)):
        adj[i].append(favorite[i])
        transpose[favorite[i]].append(i)

    stack = []
    visited = [False] * len(favorite)

    def dfs(node):
        visited[node] = True
        for n in adj[node]:
            if not visited[n]:
                dfs(n)
        stack.append(node)

    for i in range(len(favorite)):
        if not visited[i]:
            dfs(i)

    sccs = []
    scc = set()
    visited = [False] * len(favorite)

    def traverseForScc(node):
        visited[node] = True
        scc.add(node)
        for n in transpose[node]:
            if not visited[n]:
                traverseForScc(n)

    while stack:
        top = stack.pop()
        if not visited[top]:
            scc = set()
            traverseForScc(top)
            sccs.append(scc)

    res = max([len(scc) if len(scc) != 2 else -1 for scc in sccs])

    def findLongestArm(a, b):
        l = 0
        for node in transpose[a]:
            if node != b:
                l = max(l, 1 + findLongestArm(node, b))
        return l

    twoNodeSccs = 0
    for n1, n2 in [scc for scc in sccs if len(scc) == 2]:
        twoNodeSccs += 2 + findLongestArm(n1, n2) + findLongestArm(n2, n1)

    return max(res, twoNodeSccs)


def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    matrix = [[False] * numCourses for _ in range(numCourses)]

    for pre, course in prerequisites:
        matrix[pre][course] = True

    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                if matrix[i][k] and matrix[k][j]:
                    matrix[i][j] = True

    return [matrix[u][v] for u, v in queries]


def findMaxFish(grid: List[List[int]]) -> int:
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == 0:
            return 0
        temp = grid[i][j]
        visited[i][j] = True
        temp += dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        return temp

    m, n, res = len(grid), len(grid[0]), 0
    visited = [[False] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0 and not visited[i][j]:
                res = max(dfs(i, j), res)

    return res


def magnificentSets(n: int, edges: List[List[int]]) -> int:
    graph = [[] for _ in range(n)]

    for temp, b in edges:
        graph[temp - 1].append(b - 1)
        graph[b - 1].append(temp - 1)

    map = defaultdict(int)
    for i in range(n):
        queue = collections.deque([i])
        dist = [0] * n
        dist[i] = mx = 1
        root = i
        while queue:
            temp = queue.popleft()
            root = min(root, temp)
            for b in graph[temp]:
                if dist[b] == 0:
                    dist[b] = dist[temp] + 1
                    mx = max(mx, dist[b])
                    queue.append(b)
                elif abs(dist[b] - dist[temp]) != 1:
                    return -1
        map[root] = max(map[root], mx)

    return sum(map.values())


def largestIsland(grid: List[List[int]]) -> int:
    def dfs(start):
        queue = collections.deque()
        queue.append(start)
        water = set()
        temp = 1
        while queue:
            i, j = queue.pop()
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
                        temp += 1
                    elif grid[ni][nj] == 0:
                        water.add((ni, nj))
        for cell in water:
            map[cell] += temp

    m, n = len(grid), len(grid[0])

    map = defaultdict(int)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 2
                dfs((i, j))

    if map:
        return 1 + max(map.values())
    elif grid[0][0] == 0:
        return 1

    return m * n


def isArraySpecial(nums: List[int]) -> bool:
    n = len(nums)

    if n == 1:
        return True

    for i in range(1, n):
        if nums[i] % 2 == nums[i - 1] % 2:
            return False

    return True


def longestMonotonicSubarray(nums: List[int]) -> int:
    n = len(nums)
    res, temp_inc, temp_dec = 1, 1, 1

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            temp_dec += 1
            temp_inc = 1
        elif nums[i] < nums[i + 1]:
            temp_inc += 1
            temp_dec = 1
        else:
            temp_inc = temp_dec = 1
        res = max(temp_inc, temp_dec, res)

    return res


def maxAscendingSum(nums: List[int]) -> int:
    n = len(nums)
    res, temp = nums[0], nums[0]

    for i in range(n - 1):
        if nums[i] < nums[i + 1]:
            temp += nums[i + 1]
        else:
            temp = nums[i + 1]

        if temp > res:
            res = temp

    return res


def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    n, diff, swaps = len(s1), [], 0
    for i in range(n):
        if s1[i] != s2[i]:
            diff.append((s1[i], s2[i]))
            if len(diff) > 2:
                return False

    i, j = diff[0]
    if (j, i) in diff:
        return True
    else:
        return False


def tupleSameProduct(nums: List[int]) -> int:
    n, res = len(nums), 0
    count = {}

    for i in range(n):
        for j in range(i + 1, n):
            temp = nums[i] * nums[j]
            if temp in count:
                res += 8 * count[temp]
                count[temp] += 1
            else:
                count[temp] = 1

    return res


def queryResults(limit: int, queries: list[list[int]]) -> list[int]:
    node, col = {}, {}
    res = []

    for x, y in queries:
        if x in node:
            prev_color = node[x]
            if prev_color == y:
                res.append(len(col))
                continue
            if col[prev_color] == 1:
                del col[prev_color]
            else:
                col[prev_color] -= 1
        node[x] = y
        col[y] = col.get(y, 0) + 1
        res.append(len(col))

    return res


def countBadPairs(nums: List[int]) -> int:
    n, res = len(nums), 0
    map = {}

    for i in range(n):
        key = nums[i] - i
        val = map.get(key, 0)
        res += map.get(key, 0)
        map[key] = val + 1

    return (n * (n - 1)) // 2 - res


def clearDigits(s: str) -> str:
    i = 0

    while i < len(s):
        if s[i].isnumeric():
            s = s[:i - 1:] + s[i + 1::]
            i -= 2
        i += 1

    return s


def removeOccurrences(s: str, part: str) -> str:
    i, n = 0, len(part)
    while i < len(s):
        if s[i:i + n:] == part:
            s = s[:i:] + s[i + n::]
            i -= n
        i += 1
    return s


def maximumSum(nums: List[int]) -> int:
    n, s = len(nums), -1
    nums = sorted(nums)

    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if nums[i] + nums[j] > s:
                sum_i = sum(int(_) for _ in list(str(nums[i])))
                sum_j = sum(int(_) for _ in list(str(nums[j])))
                if sum_i == sum_j:
                    s = nums[i] + nums[j]
            else:
                break

    return s


import bisect


def minOperations(nums: List[int], k: int) -> int:
    # nums, res = sorted(nums), 0
    # smallest = nums[0]
    #
    # while smallest < k and len(nums) > 1:
    #     x, y = nums.pop(0), nums.pop(0)
    #     bisect.insort(nums, x * 2 + y)
    #     smallest = nums[0]
    #     res += 1
    #
    # return res

    heapify(nums)
    res = 0
    num = heappop(nums)

    while num < k:
        new = 2 * num + heappop(nums)
        num = heappushpop(nums, new)
        res += 1

    return res


def punishmentNumber(n: int) -> int:
    def suitableNumber(temp, target):
        if temp == target:
            return True
        if temp == 0:
            return target == 0

        for m in (10, 100, 1000):
            if suitableNumber(temp // m, target - temp % m):
                return True

        return False

    res = 1
    for i in range(2, n + 1):
        temp = i * i
        if suitableNumber(temp, i):
            res += temp

    return res


def numTilePossibilities(tiles: str) -> int:
    res = set()

    for i in range(1, len(tiles) + 1):
        for p in itertools.permutations(tiles, i):
            res.add(p)

    return len(res)


def smallestNumber(pattern: str) -> str:
    res = []
    stack = []

    for i in range(len(pattern) + 1):
        stack.append(str(i + 1))

        if i == len(pattern) or pattern[i] == 'I':
            while stack:
                res.append(stack.pop())

    return "".join(res)


def getHappyString(n: int, k: int) -> str:
    res = ['_' for _ in range(n + 1)]
    chars = "abc"

    min_k, max_k = 0, 0
    for i in range(1, n + 1):
        for ch in chars:
            if ch != res[i - 1]:
                min_k = max_k + 1
                max_k += 2 ** (n - i)

                if min_k <= k <= max_k:
                    max_k = min_k - 1
                    res[i] = ch
                    break

        if res[i] == '_':
            return ''

    return ''.join(res[1:])


def findDifferentBinaryString(nums: List[str]) -> str:
    n, res = len(nums), ''

    for i in range(n):
        if nums[i][i] == '0':
            res += '1'
        else:
            res += '0'

    return res


def lenLongestFibSubseq(arr: List[int]) -> int:
    nums = set(arr)
    res = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            a, b = arr[i], arr[j]
            temp = 2

            while a + b in nums:
                a, b = b, a + b
                temp += 1

            if temp > 2 and temp > res:
                res = temp

    return res


def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    res = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i][0] == nums2[j][0]:
            res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
            i += 1
            j += 1
        elif nums1[i][0] < nums2[j][0]:
            res.append(nums1[i])
            i += 1
        elif nums1[i][0] > nums2[j][0]:
            res.append(nums2[j])
            j += 1

    while i < len(nums1):
        res.append(nums1[i])
        i += 1

    while j < len(nums2):
        res.append(nums2[j])
        j += 1

    return res


def checkPowersOfThree(n: int) -> bool:
    for i in range(14, -1, -1):
        temp = 3 ** i
        if n >= temp:
            n -= temp

    return n == 0


def coloredCells(n: int) -> int:
    if n == 1:
        return 1

    return n * n + (n - 1) * (n - 1)


def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    n = len(grid)
    map = [0] * (n * n + 1)
    res = [-1, -1]

    for i in grid:
        for j in i:
            map[j] += 1

    for j in range(1, n * n + 1):
        if map[j] == 2:
            res[0] = j
        if map[j] == 0:
            res[1] = j

    return res


def minimumRecolors(blocks: str, k: int) -> int:
    res = blocks.count('W')

    for i in range(0, len(blocks) - k + 1):
        temp = blocks[i:i + k:].count('W')
        if temp < res:
            res = temp

    return res


def findAllRecipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    available = set(supplies)
    needs = {r: set(i) for r, i in zip(recipes, ingredients)}
    changed = True

    while changed:
        changed = False
        for r in recipes:
            if r in available:
                continue

            if needs[r].issubset(available):
                available.add(r)
                changed = True

    return [r for r in recipes if r in available]


def countSymmetricIntegers(low: int, high: int) -> int:
    res = 0

    for i in range(low, high + 1):
        temp = str(i)
        n = len(temp)
        if n % 2 != 0:
            continue
        left, right = temp[:n // 2:], temp[n // 2::]
        s_left = sum([int(i) for i in left])
        s_right = sum([int(i) for i in right])

        if s_left == s_right:
            res += 1

    return res


def isMatch(s: str, p: str) -> bool:
    s_i, p_i, temp, l = 0, 0, 0, -1
    while s_i < len(s):
        if p_i < len(p) and (p[p_i] == '?' or p[p_i] == s[s_i]):
            s_i += 1
            p_i += 1
        elif p_i < len(p) and p[p_i] == '*':
            l = p_i
            temp = s_i
            p_i += 1
        elif l != -1:
            p_i = l + 1
            temp += 1
            s_i = temp
        else:
            return False

    while p_i < len(p) and p[p_i] == '*':
        p_i += 1

    return p_i == len(p)


def countLargestGroup(n: int) -> int:
    map = defaultdict(int)
    for i in range(1, n + 1):
        s = sum([int(j) for j in str(i)])
        map[s] += 1

    res = 1
    vals = sorted(map.values())
    i = len(vals) - 2
    while i > 0:
        if vals[i] < vals[i + 1]:
            break
        res += 1
        i -= 1

    return res


def countSubarrays(nums: List[int], k: int) -> int:
    if len(nums) == 1:
        return 0

    tempMax = max(nums)
    res, left, tempCount = 0, 0, 0

    for right in range(len(nums)):
        if nums[right] == tempMax:
            tempCount += 1
        while tempCount == k:
            res += len(nums) - right
            if nums[left] == tempMax:
                tempCount -= 1
            left += 1

    return res


def findNumbers(nums: List[int]) -> int:
    return len([i for i in nums if len(str(i)) % 2 == 0])


# res_l1 = set()
# res_t1 = set()
# res_l2 = set()
# res_s1 = set()
# res_s2 = set()
# res_d1 = set()
# res_d2 = set()
#
# for a in range(0, 10):
#     for b in range(0, 10):
#         for c in range(0, 10):
#             l1 = [a, b, c]
#             res_l1.add(str(l1))
#
#             t1 = (a, b, c)
#             res_t1.add(t1)
#
#             l2 = [a, b, a, c]
#             res_l2.add(str(l1))
#
#             s1 = {a, b, c}
#             res_s1.add(frozenset(s1))
#
#             s2 = {a, b, a, c}
#             res_s2.add(frozenset(s2))
#
#             d1 = {'X': a, 'Y': b, 'Z': c}
#             res_d1.add(tuple(d1.items()))
#
#             d2 = {}
#             d2[a] = 'X'
#             d2[b] = 'Y'
#             d2[c] = 'Z'
#             res_d2.add(tuple(d2.items()))
#
# print(len(res_l1))
# print(len(res_t1))
# print(len(res_l2))
# print(len(res_s1))
# print(len(res_s2))
# print(len(res_d1))
# print(len(res_d2))


def numTilings(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 5

    a, b, c = 1, 2, 5
    for i in range(3, n):
        a, b, c = b, c, 2 * c + a

    return c % (10 ** 9 + 7)


def generateParenthesis(n: int) -> List[str]:
    res = []

    def dp(opening, closing, arr):
        if opening == n and closing == n:
            res.append(arr)
            return

        if opening < n:
            dp(opening + 1, closing, arr + "(")

        if closing < opening:
            dp(opening, closing + 1, arr + ")")

    dp(0, 0, "")
    return res


def kthSmallestProduct(nums1: List[int], nums2: List[int], k: int) -> int:
    smallest1, smallest2, largest1, largest2, temp = 0, 0, len(nums1) - 1, len(nums2) - 1, 1
    while temp != k:
        curr = []
        if smallest1 < 0:
            curr.append(nums1[smallest1] * nums2[largest2])
        temp += 1


def longestSubsequence(s: str, k: int) -> int:
    n = len(s)
    numZeros = s.count('0')
    numOnes = 0
    value, power = 0, 1

    for i in range(n - 1, -1, -1):
        if s[i] == '1':
            if value + power > k:
                continue
            value += power
            numOnes += 1
        power <<= 1
        if power > k:
            break

    return numZeros + numOnes


def swimInWater(grid: List[List[int]]) -> int:
    def checkNeighbors(a: tuple):
        a = list(a)
        if a[0] > 0 and not map[a[1]][a[0] - 1]:
            if grid[a[1]][a[0] - 1] <= t:
                reached.add((a[0] - 1, a[1], 0))
                map[a[1]][a[0] - 1] = True
                a[2] += 1

                newVal = checkNeighbors((a[0] - 1, a[1], 0))
                if newVal[2] == 4:
                    toRemove.append(tuple(a))
        else:
            a[2] += 1
        if a[0] < n - 1 and not map[a[1]][a[0] + 1]:
            if grid[a[1]][a[0] + 1] <= t:
                reached.add((a[0] + 1, a[1], 0))
                map[a[1]][a[0] + 1] = True
                a[2] += 1

                newVal = checkNeighbors((a[0] + 1, a[1], 0))
                if newVal[2] == 4:
                    toRemove.append(tuple(a))
        else:
            a[2] += 1
        if a[1] > 0 and not map[a[1] - 1][a[0]]:
            if grid[a[1] - 1][a[0]] <= t:
                reached.add((a[0], a[1] - 1, 0))
                map[a[1] - 1][a[0]] = True
                a[2] += 1

                newVal = checkNeighbors((a[0], a[1] - 1, 0))
                if newVal[2] == 4:
                    toRemove.append(tuple(a))
        else:
            a[2] += 1
        if a[1] < n - 1 and not map[a[1] + 1][a[0]]:
            if grid[a[1] + 1][a[0]] <= t:
                reached.add((a[0], a[1] + 1, 0))
                map[a[1] + 1][a[0]] = True
                a[2] += 1

                newVal = checkNeighbors((a[0], a[1] + 1, 0))
                if newVal[2] == 4:
                    toRemove.append(tuple(a))
        else:
            a[2] += 1
        return tuple(a)

    n, t = len(grid), 2
    map = [[False] * n for _ in range(n)]
    map[0][0] = True
    reached = {(0, 0, 0)}

    while not map[n - 1][n - 1]:
        toRemove = []
        for i in reached.copy():
            if i[2] < 4:
                newVal = checkNeighbors(i)
                if newVal[2] == 4:
                    toRemove.append(i)
        for i in toRemove:
            reached.remove(i)
        t += 1
    return t - 1


import string


def maxPartitionsAfterOperations(s: str, k: int) -> int:
    empty_alphabet_map = dict.fromkeys(string.ascii_lowercase, 0)

    def findPrefixEnd():
        map = copy(empty_alphabet_map)
        to_change = -1
        for i in range(0, k):
            map[s[i]] += 1
            if map[s[i]] == 2:
                map[s[i]] -= 1
                if to_change == -1:
                    to_change = i
                else:
                    if sum(map.values()) == 26:
                        return i - 1
                    else:
                        return i
        return k

    res = 0
    while s != "":
        i = findPrefixEnd()
        s = s[:i]
        res += 1

    return res


def findLexSmallestString(s: str, a: int, b: int) -> str:
    def add(s):
        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = str((int(s[i]) + a) % 10)
        return ''.join(s)

    def rot(s):
        return s[n - b:n] + s[:n - b]

    n = len(s)
    stack = set()
    stack.add(s)
    checked = set()
    res = s
    while stack:
        temp = stack.pop()
        if temp in checked:
            continue

        checked.add(temp)
        if temp < res:
            res = temp
        stack.add(rot(temp))
        stack.add(add(temp))

    return res


def maxFrequency(nums: List[int], k: int, numOperations: int) -> int:
    def checkValue(target):
        res, left, right = 1, i - 1, i + 1
        tempOper = numOperations

        while left > 0 and nums[left] == target:
            left -= 1
            res += 1

        while right < n and nums[right] == target:
            right += 1
            res += 1

        while tempOper > 0 and left > 0:
            if nums[left] + k >= target:
                left -= 1
                res += 1
            else:
                break
            tempOper -= 1

        while tempOper > 0 and right < n:
            if nums[right] - k <= target:
                right += 1
                res += 1
            else:
                break
            tempOper -= 1

        return res

    nums = sorted(nums)
    i, n, resFreq = 0, len(nums), 1
    while i < n:
        tempFreq = checkValue(nums[i])
        if tempFreq > resFreq:
            resFreq = tempFreq
        i += 1

    return resFreq


def hasSameDigits(s: str) -> bool:
    while len(s) > 2:
        res = []
        for i in range(1, len(s)):
            res.append(str((int(s[i]) + int(s[i - 1])) % 10))
        s = "".join(res)

    return s[0] == s[1]


def nextBeautifulNumber(n: int) -> int:
    def solve(x: int) -> bool:
        s = str(x)
        vec = [0] * 10
        for ch in s:
            vec[ord(ch) - 48] += 1
        for ch in s:
            c = ord(ch) - 48
            if c == 0 or vec[c] != c:
                return False
        return True

    i = n + 1
    while True:
        if solve(i):
            return i
        i += 1


def countValidSelections(nums: List[int]) -> int:
    def loop(i: int, startRight):
        temp, r = i, startRight
        l, s = copy(nums), sum(nums)
        while n > temp >= 0 != s:
            if l[temp] != 0:
                l[temp] -= 1
                s -= 1
                r = not r
            if r:
                temp += 1
            else:
                temp -= 1

        if sum(l) == 0:
            return True

        return False

    n, res = len(nums), 0
    for start in range(0, n):
        if nums[start] == 0:
            if loop(start, True):
                res += 1
            if loop(start, False):
                res += 1

    return res


def minNumberOperations(target: List[int]) -> int:
    res, initial = 1, [1 for _ in range(len(target))]

    while initial != target:
        i = 0
        while i < len(target):
            j = i
            changed = False
            while j < len(target) and target[j] > initial[j]:
                initial[j] += 1
                j += 1
                changed = True
            i = j
            if changed:
                res += 1
            else:
                i += 1

    return res


def getSneakyNumbers(nums: List[int]) -> List[int]:
    nums.sort()
    res, n = [], len(nums)

    for i in range(0, n):
        if nums[i] == nums[i + 1]:
            res.append(nums[i])

    return res


def findXSum(nums: List[int], k: int, x: int) -> List[int]:
    def processArray(arr):
        arr.sort()
        top, ans, a = [], set(), 1

        for i in range(len(arr) - 1, 0, -1):
            if i != 0 or arr[i] == arr[i - 1]:
                a += 1
            else:
                if len(top) < x:
                    top.append(a)
                else:
                    m = min(top)
                    if m < a:
                        top.remove(m)
                        top.append(a)
                a = 1

        return sum(top)

    n = len(nums)
    res = []

    for i in range(0, n - k):
        temp = nums[i:i + k]
        res.append(processArray(temp))

    return res


def minCost(colors: str, neededTime: List[int]) -> int:
    n = len(colors)
    l = 0
    removes = 0

    for r in range(n):
        if colors[r] != colors[l]:
            sameColors = neededTime[l:r]
            removes += sum(sameColors) - max(sameColors)
            l = r

    removes += sum(neededTime[l:]) - max(neededTime[l:])
    return removes


def minOperations(nums: List[int]) -> int:
    s = sum(nums)
    i, j = 0, 0
    last_min = -1
    res = 0

    while s != 0:
        while i < len(nums):
            temp_min = nums[i]
            j = i
            while j < len(nums) and nums[j] >= nums[i]:
                if temp_min > nums[j]:
                    temp_min = nums[j]
                j += 1
            for k in range(i, j):
                if nums[k] == temp_min:
                    s -= temp_min
                    nums[k] = 0
            i += 1
        res += 1

    return res


def minOperations(nums: List[int]) -> int:
    if math.gcd(*nums) > 1:
        return -1

    res, n = math.inf, len(nums)
    for i in range(1, n):
        if math.gcd(nums[i], nums[i-1]) == 1:
            return n

    for i in range(1, n - 1):
        temp = 0
        while sum(nums) != n:
            gcd = math.gcd(nums[i], nums[i-1])
            nums[i] = gcd
            temp += 1
            if math.gcd(nums[i], nums[i-1]) == 1 or math.gcd(nums[i], nums[i+1]) == 1:
                temp += n


def smallestRepunitDivByK(k: int) -> int:
    if k % 2 == 0 or k % 5 == 0:
        return -1

    rem = 1
    for i in range(1, k):
        rem = (rem * 10 + 1) % k
        if rem == 0:
            return i + 1

    return -1


print(smallestRepunitDivByK(3))
