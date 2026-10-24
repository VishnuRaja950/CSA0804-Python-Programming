"""Task 1: Analyse inputs and demonstrate validation for the milk payment problem."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_MIN = 2.0
FAT_MAX = 7.0

def identify_data():
    """Print the inputs, outputs, constants, types and validation examples."""
    print("TASK 1 - MILK PAYMENT PROBLEM ANALYSIS")
    print("\nInputs: farmer_id (str), litres (float >= 0), fat (float 2.0-7.0),")
    print("        SNF (float >= 0; confirm official range), shift (str).")
    print("Outputs: fat_steps, snf_steps, rate_per_litre, payment, ten_day_total.")
    print("\nNamed constants:")
    print(f"BASE_RATE = Rs {BASE_RATE:.2f}")
    print(f"FAT_STEP_VALUE = Rs {FAT_STEP_VALUE:.2f}")
    print(f"SNF_STEP_VALUE = Rs {SNF_STEP_VALUE:.2f}")
    print(f"STANDARD_FAT = {STANDARD_FAT}%")
    print(f"STANDARD_SNF = {STANDARD_SNF}%")
    print(f"FAT_MIN = {FAT_MIN}%, FAT_MAX = {FAT_MAX}%")
    print("\nValidation examples:")
    examples = [
        ("F001", 10.0, 3.5, 8.5, "Morning"),
        ("F002", -2.0, 3.5, 8.5, "Evening"),
        ("F003", 5.0, 7.5, 8.5, "Morning"),
    ]
    for farmer_id, litres, fat, snf, shift in examples:
        valid = litres >= 0 and FAT_MIN <= fat <= FAT_MAX and snf >= 0
        print(f"{farmer_id}: litres={litres}, fat={fat}, SNF={snf}, shift={shift} -> "
              f"{'VALID' if valid else 'INVALID'}")

if __name__ == "__main__":
    identify_data()
