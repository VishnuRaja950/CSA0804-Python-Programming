# Task 12 — Day-4 Design Challenge

## A. Impact analysis
The analyser now gives fat/SNF to two decimal places; seasonal base rate rises to ₹32.00 from April through June; each fat step is ₹0.45 in that season; and a bonus of ₹0.50 per litre applies only when a farmer delivers more than 500 L during a ten-day period. These changes affect constants, rate selection, step calculation, input precision, and ten-day bonus eligibility. Two-decimal readings require a documented rule for converting fractional 0.1% steps; this implementation rounds to the nearest whole step using Decimal and ROUND_HALF_UP.

## B. Evaluate original design
A single fixed base rate and fat step cannot satisfy seasonal pricing. The modular functions remain useful, but rate calculation needs a season/rate-card parameter and bonus logic needs a ten-day aggregate. Decimal is appropriate for precise input and money. The original design is retained structurally but modified to support new rules.

## C. Adaptation
`task12.py` selects a standard or seasonal rate card. The bonus is added only for seasonal entries marked eligible with a ten-day total greater than 500 L. In a real system, bonus eligibility must be calculated across all deliveries for that farmer during the ten-day period; the sample function receives that eligibility flag from the caller. The production implementation should aggregate litres by farmer and period before calculating the bonus.

## D. Evidence-based defence
Run `python task12.py`. Test standard pricing, seasonal pricing, 500 L exactly (no bonus), and 501 L (bonus applies). Seasonal base rate at standard fat/SNF is ₹32.00/L; for 501 L, the bonus adds ₹250.50, making ₹16,282.50 total. A rate-card dictionary centralises changes and is easier to maintain than duplicated expressions. The algorithm remains O(n) time; rate-card storage is O(1) for the two cards.
