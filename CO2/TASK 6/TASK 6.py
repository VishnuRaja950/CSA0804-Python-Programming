from functools import lru_cache
import sys

calls = 0
def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

memo_calls = 0
@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

calls = 0
print("naive:", ways_naive(25), "calls =", calls)
memo_calls = 0
ways_memo.cache_clear()
print("memo :", ways_memo(25), "calls =", memo_calls)
print("recursion limit:", sys.getrecursionlimit())
try:
    print("n=1000:", ways_memo(1000))
except RecursionError:
    print("RecursionError at n=1000")
