
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create attendance records
sample_data = {
    "day1.csv": [
        "192311002,Day1,A",
        "192311001,Day1,P"
    ],
    "day2.csv": [
        "192311002,Day2,A"
    ],
    "day3.csv": [
        "192311002,Day3,A"
    ]
}

records = []
errors = []

# Read CSV files
for filename, rows in sample_data.items():
    path = os.path.join(BASE_DIR, filename)

    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(rows) + "\n")

    try:
        with open(path, "r", encoding="utf-8") as file:
            for number, line in enumerate(file, 1):
                fields = line.strip().split(",")

                if len(fields) != 3 or fields[2] not in ("P", "A"):
                    errors.append((filename, number, "invalid record"))
                else:
                    records.append(tuple(fields))

    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        errors.append((filename, 0, str(e)))

# Find three-day absentees
by_student = {}

for reg, date, status in records:
    by_student.setdefault(reg, []).append(status)

absentees = [
    reg for reg, statuses in by_student.items()
    if len(statuses) >= 3
    and any(statuses[i:i+3] == ["A", "A", "A"]
            for i in range(len(statuses)-2))
]

print("Records:", len(records))
print("Three-day absentees:", absentees)
print("Errors:", errors)
print("Attendance package executed")
