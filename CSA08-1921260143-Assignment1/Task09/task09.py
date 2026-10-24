from decimal import Decimal
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Task07"))
from milkrate import payout

def validate_and_pay(litres, fat, snf):
    litres, fat, snf = Decimal(str(litres)), Decimal(str(fat)), Decimal(str(snf))
    if litres < 0:
        raise ValueError("litres cannot be negative")
    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("fat must be between 2.0 and 7.0")
    if snf < 0:
        raise ValueError("SNF cannot be negative")
    return payout(litres, fat, snf)

def run_tests():
    cases = [
        ("standard", 10, 3.5, 8.5, "300.00"),
        ("high fat/SNF", 8.5, 4.2, 8.7, "283.90"),
        ("low fat/SNF", 12, 3.1, 8.3, "333.60"),
        ("zero litres", 0, 3.5, 8.5, "0.00"),
        ("minimum fat", 1, 2.0, 8.5, "24.00"),
        ("maximum fat", 1, 7.0, 8.5, "44.00"),
    ]
    for name, litres, fat, snf, expected in cases:
        actual = str(validate_and_pay(litres, fat, snf))
        assert actual == expected, f"{name}: expected {expected}, got {actual}"
        print("PASS", name, actual)
    invalid = [(-1, 3.5, 8.5), (1, 1.9, 8.5), (1, 7.1, 8.5), (1, 3.5, -1)]
    for case in invalid:
        try:
            validate_and_pay(*case)
        except ValueError:
            print("PASS invalid", case)
        else:
            raise AssertionError(f"Expected ValueError for {case}")

if __name__ == "__main__":
    run_tests()
