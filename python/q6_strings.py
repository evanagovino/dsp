# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count >= 10:
        count = 'many'
    print('Number of donuts:', count)
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    #raise NotImplementedError


def both_ends(s):
    if len(s) > 2:
        print(s[:2] + s[-2:])
    else:
        print("")
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    #raise NotImplementedError


def fix_start(s):
    x = s[0]
    y = s[1:]
    y = y.replace(x, "*")
    print(x + y)
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    #raise NotImplementedError


def mix_up(a, b):
    a0 = a[0:2]
    b0 = b[0:2]
    a1 = a[2:]
    b1 = b[2:]
    a = b0 + a1
    b = a0 + b1
    print(a, b)
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    #raise NotImplementedError


def verbing(s):
    if len(s) >= 3:
        if s[-3:] == 'ing':
            y = s[-3:]
            y = y.replace('ing', 'ly')
            s = s[:-3] + y
        else:
            s = s + 'ing'
    print(s)
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    #raise NotImplementedError


def not_bad(s):
    import re
    p = re.compile('not(.*)bad')
    s = p.sub('good', s, count=1)
    print(s)
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    #Having issues limiting this to one replacement, this will not work if I add a second not bad to a string
    #raise NotImplementedError


def front_back(a, b):
    def split_string(x):
        strlength = len(x) / 2
        if strlength % 1 != 0:
            strlength = int(strlength + 0.5)
        else:
            strlength = int(strlength)
        return(x[:strlength], x[strlength:])
    a1, a2 = split_string(a)
    b1, b2 = split_string(b)
    print(a1 + b1 + a2 + b2)
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    #raise NotImplementedError