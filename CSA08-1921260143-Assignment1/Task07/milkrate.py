"""Rate card and payment functions for the village milk co-operative."""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
CENT = Decimal("0.01")

def rate_per_litre(fat, snf):
    """Return the price per litre rounded to two decimal places."""
    fat_steps = int(((fat - STANDARD_FAT) * 10).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    snf_steps = int(((snf - STANDARD_SNF) * 10).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    return (BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE).quantize(CENT)

def payout(litres, fat, snf):
    """Return the rounded payment for a delivery."""
    return (litres * rate_per_litre(fat, snf)).quantize(CENT, rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    for litres, fat, snf in [(10, Decimal("3.5"), Decimal("8.5")),
                             (Decimal("8.5"), Decimal("4.2"), Decimal("8.7")),
                             (12, Decimal("3.1"), Decimal("8.3"))]:
        litres = Decimal(str(litres))
        rate = rate_per_litre(fat, snf)
        print(f"{litres:5} L  fat {fat}  snf {snf}  rate {rate:.2f}  pay {payout(litres, fat, snf):.2f}")
