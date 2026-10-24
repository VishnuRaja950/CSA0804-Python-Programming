"""Seasonal milk payment calculator for Task 12."""
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
FAT_MIN = Decimal("2.0")
FAT_MAX = Decimal("7.0")

RATE_CARDS = {
    "standard": {"base": Decimal("30.00"), "fat": Decimal("0.40"), "snf": Decimal("0.30")},
    "seasonal": {"base": Decimal("32.00"), "fat": Decimal("0.45"), "snf": Decimal("0.30")},
}

def rounded_steps(value, standard):
    return int(((value - standard) * 10).quantize(Decimal("1"), rounding=ROUND_HALF_UP))

def rate_per_litre(fat, snf, season="standard"):
    """Calculate rate using the selected rate card."""
    if season not in RATE_CARDS:
        raise ValueError("season must be 'standard' or 'seasonal'")
    card = RATE_CARDS[season]
    rate = card["base"] + rounded_steps(fat, STANDARD_FAT) * card["fat"] + rounded_steps(snf, STANDARD_SNF) * card["snf"]
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def payout(litres, fat, snf, season="standard", bonus_eligible=False):
    """Calculate payment, including the seasonal bonus when eligible."""
    if litres < 0:
        raise ValueError("litres cannot be negative")
    if not FAT_MIN <= fat <= FAT_MAX:
        raise ValueError("fat must be between 2.0 and 7.0")
    if snf < 0:
        raise ValueError("SNF cannot be negative")
    amount = litres * rate_per_litre(fat, snf, season)
    if season == "seasonal" and bonus_eligible and litres > 500:
        amount += litres * Decimal("0.50")
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    tests = [
        (Decimal("10"), Decimal("3.50"), Decimal("8.50"), "standard", False),
        (Decimal("10"), Decimal("3.50"), Decimal("8.50"), "seasonal", False),
        (Decimal("501"), Decimal("3.50"), Decimal("8.50"), "seasonal", True),
        (Decimal("500"), Decimal("3.50"), Decimal("8.50"), "seasonal", False),
        (Decimal("8.5"), Decimal("4.2"), Decimal("8.7"), "seasonal", False),
    ]
    for row in tests:
        litres, fat, snf, season, eligible = row
        print(row, "rate=", rate_per_litre(fat, snf, season),
              "payment=", payout(litres, fat, snf, season, eligible))
