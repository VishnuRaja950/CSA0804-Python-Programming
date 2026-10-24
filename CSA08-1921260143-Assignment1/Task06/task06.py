from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
CENT = Decimal("0.01")

def rate_per_litre(fat, snf):
    """Calculate and return the rounded rate per litre."""
    fat_steps = int(((fat - STANDARD_FAT) * 10).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    snf_steps = int(((snf - STANDARD_SNF) * 10).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def payout(litres, fat, snf):
    """Return the rounded payment for one milk delivery."""
    amount = litres * rate_per_litre(fat, snf)
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)

def ten_day_total(payments):
    """Return the sum of payment amounts for a ten-day period."""
    return sum(payments, Decimal("0.00")).quantize(CENT, rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    for litres, fat, snf in [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]:
        l, f, s = Decimal(str(litres)), Decimal(str(fat)), Decimal(str(snf))
        rate = rate_per_litre(f, s)
        pay = payout(l, f, s)
        print(f"{l:5} L  fat {f}  snf {s}  rate {rate:.2f}  pay {pay:.2f}")
