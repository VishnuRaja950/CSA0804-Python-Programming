
import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Create sample department registration files
department_data = {
    "CSE.txt": [
        "192311001;Arun;CSE;arun@gmail.com;Dance"
    ],
    "IT.txt": [
        "192311002;Bala;IT;bala@gmail.com;Music"
    ],
    "ECE.txt": [
        "192311003;Chitra;ECE;chitra@gmail.com;Quiz"
    ],
    "EEE.txt": [
        "192311001;Duplicate;EEE;duplicate@gmail.com;Dance"
    ],
    "MECH.txt": [
        "192311005;Kumar;MECH;invalidemail;Music",
        "192311006;Divya;MECH;divya@gmail.com"
    ]
}

# Write input files
for filename, lines in department_data.items():
    path = os.path.join(INPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")

accepted = []
rejected = []
registered_ids = set()

# Read and validate department files
for filename in department_data:
    path = os.path.join(INPUT_DIR, filename)

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):

                fields = line.strip().split(";")

                if len(fields) != 5:
                    rejected.append(
                        (filename, line_number, "Invalid number of fields")
                    )
                    continue

                reg, name, department, email, event = fields

                if not reg or not name or not department or not email or not event:
                    rejected.append(
                        (filename, line_number, "Missing information")
                    )
                    continue

                if "@" not in email or "." not in email.split("@")[-1]:
                    rejected.append(
                        (filename, line_number, "Invalid email")
                    )
                    continue

                if reg in registered_ids:
                    rejected.append(
                        (filename, line_number, "Duplicate registration")
                    )
                    continue

                registered_ids.add(reg)

                accepted.append([
                    reg, name, department, email, event
                ])

    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as error:
        rejected.append((filename, 0, str(error)))

# Get unique event names
events = sorted({
    event
    for record in accepted
    for event in record[4].split(",")
})

# Create master list
master_path = os.path.join(OUTPUT_DIR, "master_list.csv")

with open(master_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["Register No", "Name", "Department", "Email", "Events"])
    writer.writerows(accepted)

# Create event-wise files
for event in events:
    event_path = os.path.join(
        OUTPUT_DIR, event.lower() + ".txt"
    )

    with open(event_path, "w", encoding="utf-8") as file:
        for record in accepted:
            if event in record[4].split(","):
                file.write(
                    record[0] + ";" + record[1] + "\n"
                )

# Create summary file
summary_path = os.path.join(OUTPUT_DIR, "summary.txt")

with open(summary_path, "w", encoding="utf-8") as file:
    file.write("Accepted registrations: " + str(len(accepted)) + "\n")
    file.write("Rejected registrations: " + str(len(rejected)) + "\n")
    file.write("Events: " + ", ".join(events) + "\n")

# Create error log
error_path = os.path.join(OUTPUT_DIR, "error.log")

with open(error_path, "w", encoding="utf-8") as file:
    for error in rejected:
        file.write(str(error) + "\n")

# Display final output
print("Accepted:", len(accepted))
print()
print("Events:", events)
print()
print("Rejected:", len(rejected))
print("Master list, event-wise files, summary.txt and error.log created")
