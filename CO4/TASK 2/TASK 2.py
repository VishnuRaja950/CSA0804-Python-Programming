
import os
import csv
from collections import defaultdict

base_folder = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(base_folder, "input")
output_folder = os.path.join(base_folder, "output")

os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Create sample input files automatically
sample_data = {
    "day1.csv": [
        ["101", "Arun", "P"],
        ["102", "Bala", "P"],
        ["103", "Chitra", "A"]
    ],
    "day2.csv": [
        ["101", "Arun", "P"],
        ["102", "Bala", "A"],
        ["103", "Chitra", "P"],
        ["104", "Divya", "P", "Extra"]
    ]
}

for filename, rows in sample_data.items():
    path = os.path.join(input_folder, filename)

    if not os.path.exists(path):
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)


def process_attendance(folder):

    attendance = defaultdict(lambda: [0, 0])
    damaged = []

    files = sorted(
        f for f in os.listdir(folder)
        if f.lower().endswith(".csv")
    )

    for filename in files:

        path = os.path.join(folder, filename)

        with open(path, "r", newline="") as file:
            reader = csv.reader(file)

            for line_no, row in enumerate(reader, start=1):

                if len(row) != 3:
                    damaged.append(
                        (filename, line_no, "Invalid number of fields")
                    )
                    continue

                reg, name, status = [x.strip() for x in row]
                status = status.upper()

                if not reg or not name or status not in ("P", "A"):
                    damaged.append(
                        (filename, line_no, "Invalid record")
                    )
                    continue

                attendance[reg][1] += 1

                if status == "P":
                    attendance[reg][0] += 1

    # Monthly report
    with open(os.path.join(output_folder, "monthly_attendance.csv"),
              "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(["Register No", "Present", "Total", "Percentage"])

        for reg, values in sorted(attendance.items()):
            present, total = values
            percentage = present / total * 100
            writer.writerow([reg, present, total, f"{percentage:.2f}"])

    # Below 75% report
    with open(os.path.join(output_folder, "below_75.csv"),
              "w", newline="") as file:

        writer = csv.writer(file)
        writer.writerow(["Register No", "Present", "Total", "Percentage"])

        for reg, values in sorted(attendance.items()):
            present, total = values
            percentage = present / total * 100

            if percentage < 75:
                writer.writerow([reg, present, total, f"{percentage:.2f}"])

    print("Processed files:", len(files))
    print("Students:", len(attendance))
    print("Damaged lines:", len(damaged))
    print("Monthly report:", os.path.join(output_folder, "monthly_attendance.csv"))
    print("Below 75% report:", os.path.join(output_folder, "below_75.csv"))
    print("Rejected records:", damaged)


process_attendance(input_folder)
