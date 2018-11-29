# -*- coding: utf-8 -*-

# 递归
# 如果使用循环，程序的性能可能更高；如果使用递归，程序可能更容易理解，如何选择要看什么对你来说更重要。

def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)

print('100! = ', fact(100))


