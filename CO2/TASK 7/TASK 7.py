def ways_original(n):
    if n <= 1:
        return 1
    return ways_original(n - 1) + ways_original(n - 2)

def ways_redesigned(n):
    if n <= 1:
        return 1
    previous, current = 1, 1
    for step in range(2, n + 1):
        previous, current = current, previous + current
    return current

for n in (10, 20, 25, 30):
    print(n, ways_redesigned(n))
print("n=1000 digits:", len(str(ways_redesigned(1000))))
