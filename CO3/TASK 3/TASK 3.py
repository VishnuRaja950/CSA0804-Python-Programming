from collections import Counter
import re
 
calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}
 
def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in re.findall(r"\\b[a-z]+\\b", text.lower()):
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts
 
def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]
 
district_calls = [
    ("Madurai", "seeds delayed", "Paddy"),
    ("Salem", "fertiliser price high", "Sugarcane"),
    ("Madurai", "irrigation issue", "Paddy"),
]
by_district, by_crop = {}, {}
for district, complaint, crop in district_calls:
    by_district[district] = by_district.get(district, 0) + 1
    by_crop.setdefault(crop, []).append(complaint)
 
counts = frequencies(calls, STOP)
print(top(counts, 3))
print("district counts:", by_district)
print("crop groups:", by_crop)
print("Counter:", Counter(w for t in calls for w in
      re.findall(r"\\b[a-z]+\\b", t.lower()) if w not in STOP))
