import time

def build_plus(parts):
    text = ""
    for part in parts:
        text += part + ";"
    return text

def build_join(parts):
    return ";".join(parts) + ";"

def build_fstring(parts):
    return "".join(f"{part};" for part in parts)

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]
a = build_plus(items)
b = build_join(items)
print("same text:", a == b, "| length:", len(b))

for size in (1_000, 10_000, 200_000):
    sample = items[:size]
    plus_times, join_times = [], []
    for _ in range(3):
        start = time.perf_counter()
        build_plus(sample)
        plus_times.append(time.perf_counter() - start)
        start = time.perf_counter()
        build_join(sample)
        join_times.append(time.perf_counter() - start)
    print(size, "plus avg:", sum(plus_times)/3,
          "join avg:", sum(join_times)/3)
