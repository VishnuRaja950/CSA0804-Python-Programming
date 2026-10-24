# Task 8 — Algorithm Before Coding

## Stages
1. Understand inputs, outputs, rules, and edge cases.
2. Plan formula and validation.
3. Implement small functions.
4. Test normal, boundary, and invalid cases; fix and retest.

## Pseudocode
```
READ farmer_id, litres, fat, snf, shift
IF litres is not numeric OR litres < 0: report error and stop
IF fat is not numeric OR fat < 2.0 OR fat > 7.0: report error and stop
IF snf is not numeric OR snf < 0: report error and stop
fat_steps = round((fat - 3.5) / 0.1)
snf_steps = round((snf - 8.5) / 0.1)
rate = 30.00 + fat_steps*0.40 + snf_steps*0.30
payment = round(litres * rate, 2)
DISPLAY rate and payment
ADD payment to ten-day running total
```

## Flowchart (text)
Start → Read values → Are all values valid? — No → Show error → End; Yes → Calculate steps → Calculate rate → Calculate payment → Update total → Display result → End.

## Hand trace
- 10 L, fat 3.5, SNF 8.5 → 0 fat steps, 0 SNF steps → ₹30.00/L → ₹300.00.
- 8.5 L, fat 4.2, SNF 8.7 → +7 fat steps, +2 SNF steps → ₹33.40/L → ₹283.90.
- 12 L, fat 3.1, SNF 8.3 → −4 fat steps, −2 SNF steps → ₹27.80/L → ₹333.60.

Storing all entries and calculating later takes O(n) time and O(n) space. A running total takes O(n) time and O(1) extra space; retain individual records only when audit/history or recalculation is needed.
