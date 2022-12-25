#!/usr/bin/env python3

INPUT = "day25-input.txt"

ORD={'2': 2, '1':1, '0': 0, '-': -1, '=':-2}

def s2d(s):
    """
    >>> s2d('1')
    1
    >>> s2d('2')
    2
    >>> s2d('1=')
    3
    >>> s2d('1-')
    4
    >>> s2d('10')
    5
    >>> s2d('1-0---0')
    12345
    >>> s2d('1121-1110-1=0')
    314159265
    """

    d = 0
    l=len(s)
    for i in range(l):
        d += 5**i * ORD[s[l-i-1]]
    return d

def d2s(d):
    """
    >>> d2s(1)
    '1'
    >>> d2s(2)
    '2'
    >>> d2s(3)
    '1='
    >>> d2s(4)
    '1-'
    >>> d2s(5)
    '10'
    >>> d2s(6)
    '11'
    >>> d2s(7)
    '12'
    >>> d2s(8)
    '2='
    >>> d2s(9)
    '2-'
    >>> d2s(10)
    '20'
    >>> d2s(15)
    '1=0'
    >>> d2s(20)
    '1-0'
    >>> d2s(2022)
    '1=11-2'
    >>> d2s(12345)
    '1-0---0'
    >>> d2s(314159265)
    '1121-1110-1=0'
    >>> d2s(63)
    '1==='
    """

    biggest_power = 0
    i = 0
    while True:
        if 5**i > d:
            biggest_power = i-1
            break
        i += 1
    else:
        raise Exception("too big")
    digits = [] 

    for i in range(biggest_power, -1, -1):
        digit = d // (5**i)
        d -= digit*(5**i)
        digits.append(digit)
    r = []
    carry = 0
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 3:
            digits[i] = '='
            carry = 1
        elif digits[i] == 4:
            digits[i] = '-'
            carry = 1
        elif digits[i] == 5:
            digits[i] = '0'
            carry = 1
        else:
            digits[i] = chr(ord('0') + digits[i])
        if carry:
            if i != 0:
                digits[i-1] += 1
                carry = 0
    if carry:
        digits.insert(0, '1')
    return ''.join(digits)


if __name__ == '__main__':
    sum = 0
    with open(INPUT, 'r') as f:
        for l in f:
            sum += s2d(l.strip())
    print("%s, confirmed 122-12==0-01=00-0=02" % d2s(sum))
