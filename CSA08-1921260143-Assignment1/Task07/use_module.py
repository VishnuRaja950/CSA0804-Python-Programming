from decimal import Decimal
from milkrate import payout, rate_per_litre

if __name__ == "__main__":
    print("Imported payment:", payout(Decimal("10"), Decimal("3.5"), Decimal("8.5")))
