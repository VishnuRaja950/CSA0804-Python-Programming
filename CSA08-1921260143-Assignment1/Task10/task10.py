from decimal import Decimal
from time import perf_counter
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Task07"))
from milkrate import payout

def run(count, mode):
    start = perf_counter()
    total_float = 0.0
    total_decimal = Decimal("0.00")
    for i in range(count):
        litres, fat, snf = 10, Decimal("4.2"), Decimal("8.7")
        if mode == "float":
            # Deliberately show binary float accumulation for comparison.
            total_float += float(litres) * (30.0 + 7 * 0.40 + 2 * 0.30)
        else:
            total_decimal += payout(Decimal(str(litres)), fat, snf)
    elapsed = perf_counter() - start
    total = total_float if mode == "float" else total_decimal
    return total, elapsed

if __name__ == "__main__":
    for count in (300, 6000, 150000):
        for mode in ("float", "Decimal"):
            total, seconds = run(count, mode)
            print(count, mode, total, f"{seconds:.6f}s")
