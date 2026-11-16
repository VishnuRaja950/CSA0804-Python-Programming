
import os

# Get program folder
base = os.path.dirname(os.path.abspath(__file__))

# Create input and output folders
input_folder = os.path.join(base, "input")
output_folder = os.path.join(base, "output")

os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Automatically create three daily files
daily_data = {
    "day1.txt": ["Book-A", "Book-B"],
    "day2.txt": ["Book-C"],
    "day3.txt": ["Book-D", "Book-E"]
}

for filename, books in daily_data.items():
    path = os.path.join(input_folder, filename)

    with open(path, "w") as file:
        for book in books:
            file.write(book + "\n")


# Output files
returns_file = os.path.join(output_folder, "returns.txt")
error_file = os.path.join(output_folder, "error_log.txt")


# Function to save book returns
def save_returns(filename):
    try:
        with open(filename, "r") as file:
            books = file.readlines()

        with open(returns_file, "a") as file:
            for book in books:
                file.write(book.strip() + "\n")

        print("Processed:", os.path.basename(filename))

    except FileNotFoundError as e:
        with open(error_file, "a") as log:
            log.write(str(e) + "\n")


# Clear old output before running
open(returns_file, "w").close()
open(error_file, "w").close()


# Process all daily files
for filename in daily_data:
    path = os.path.join(input_folder, filename)
    save_returns(path)


# Display returns
print("\nReturns log:")

with open(returns_file, "r") as file:
    print(file.read(), end="")


# Demonstrate missing file error
print("\nChecking missing file:")

missing_file = os.path.join(input_folder, "missing_day.txt")
save_returns(missing_file)


# Display error log
print("\nError log:")

with open(error_file, "r") as file:
    print(file.read(), end="")
