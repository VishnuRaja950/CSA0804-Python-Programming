
import re
import sqlite3
import timeit
import random
from collections import Counter

# Positive and negative word lists
POSITIVE = {
    "good", "clean", "fast", "helpful", "improved"
}

NEGATIVE = {
    "bad", "dirty", "slow", "rude", "smoke", "broken"
}

NEGATORS = {"not", "never", "no"}


# Sentiment scoring
def score(text):
    words = re.findall(r"\b\w+\b", text.lower())
    total = 0

    for i, word in enumerate(words):

        value = 1 if word in POSITIVE else (
            -1 if word in NEGATIVE else 0
        )

        if i > 0 and words[i - 1] in NEGATORS:
            value *= -1

        total += value

    return total


def label(text):
    value = score(text)

    if value > 0:
        return "positive"
    elif value < 0:
        return "negative"
    else:
        return "neutral"


# 50 citizen complaints with manual reference labels
base_complaints = [
    ("Roads are clean and the bus was fast.", "positive"),
    ("Smoke from the factory, air is bad.", "negative"),
    ("The staff were not helpful.", "negative"),
    ("Not bad, service improved.", "positive"),
    ("The road is dirty and broken.", "negative"),
    ("The environment is clean and good.", "positive"),
    ("The traffic is slow and bad.", "negative"),
    ("The service is helpful and fast.", "positive"),
    ("Air quality is not good.", "negative"),
    ("The pollution is bad.", "negative")
]

complaints = base_complaints * 5


# B4.1 Sentiment evaluation
print("TASK B4: SENTIMENT ANALYSIS")
print("=" * 55)

correct = 0

for text, expected in complaints:

    predicted = label(text)

    if predicted == expected:
        correct += 1

    print(f"{predicted:8} | {text}")

accuracy = correct / len(complaints) * 100

print("\nTotal complaints:", len(complaints))
print("Correct predictions:", correct)
print("Agreement:", round(accuracy, 2), "%")


# B4.1 Extractive summarisation
STOP = {
    "the", "is", "are", "was", "were", "and",
    "a", "an", "to", "of", "in", "on", "for",
    "from", "with", "it", "this", "that"
}


def summarise(text, k=2):

    sentences = re.split(
        r"(?<=[.!?])\s+", text.strip()
    )

    words = re.findall(r"[a-z]+", text.lower())

    frequency = Counter(
        word for word in words if word not in STOP
    )

    ranked = []

    for i, sentence in enumerate(sentences):

        tokens = re.findall(
            r"[a-z]+", sentence.lower()
        )

        sentence_score = sum(
            frequency[word]
            for word in tokens
        )

        ranked.append((sentence_score, i, sentence))

    selected = sorted(
        sorted(ranked, key=lambda x: (-x[0], x[1]))[:k],
        key=lambda x: x[1]
    )

    return " ".join(item[2] for item in selected)


print("\nEXTRACTIVE TEXT SUMMARISATION")

complaint_text = (
    "Smoke is rising near the school. "
    "The air is dirty. "
    "Residents request a cleaner bus route."
)

print("Original complaint:")
print(complaint_text)

print("\nGenerated summary:")
print(summarise(complaint_text, 2))


# B4.2 Database indexing
print("\nDATABASE INDEXING PERFORMANCE")
print("=" * 55)

con = sqlite3.connect(":memory:")

con.execute("""
CREATE TABLE readings(
station TEXT,
day TEXT,
pm25 REAL
)
""")

random.seed(42)

data = []

for station in range(12):
    for day in range(365):
        for hour in range(24):

            data.append((
                f"ST{station:03d}",
                f"2026-{day+1:03d}",
                round(random.uniform(10, 150), 2)
            ))

con.executemany(
    "INSERT INTO readings VALUES(?,?,?)",
    data
)

con.commit()

query = """
SELECT AVG(pm25)
FROM readings
WHERE station = ?
AND day BETWEEN ? AND ?
"""

parameters = (
    "ST005",
    "2026-050",
    "2026-150"
)


def run_query():
    return con.execute(
        query, parameters
    ).fetchone()


before = timeit.timeit(
    run_query,
    number=200
)

con.execute("""
CREATE INDEX idx_station_day
ON readings(station, day)
""")

con.commit()

after = timeit.timeit(
    run_query,
    number=200
)

print("Total database records:", len(data))
print("Before index:", round(before, 4), "seconds")
print("After index:", round(after, 4), "seconds")

if after > 0:
    print(
        "Speed-up:",
        round(before / after, 2),
        "times"
    )

con.close()


# B4.3 Final engineering decision
print("\nFINAL ENGINEERING DECISION")
print("=" * 55)

print("1. Store readings in SQLite with suitable indexes.")
print("2. Clean and validate CSV data before storage.")
print("3. Use pandas and SQL for data analysis.")
print("4. Use machine learning for advanced sentiment analysis.")
print("5. Generate automated daily and monthly reports.")

print("\nTASK B4 COMPLETED SUCCESSFULLY.")
