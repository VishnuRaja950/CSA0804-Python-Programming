# Task 1 — Understand the Problem and Identify the Data

## Inputs
- Farmer ID: string (may contain letters/leading zeros).
- Milk quantity in litres: float; must be non-negative.
- Fat percentage: float; allowed range 2.0–7.0 inclusive.
- SNF percentage: float; assumed valid range 6.0–10.0 inclusive for this implementation (confirm with the co-operative if its official limits differ).
- Shift: string, e.g. Morning or Evening.

## Outputs
- Fat steps relative to 3.5% and SNF steps relative to 8.5%.
- Rate per litre in rupees.
- Payment for the entry and ten-day total.
- Clear validation errors for invalid data.

## Constants
BASE_RATE = ₹30.00/L; FAT_STEP_VALUE = ₹0.40/L per 0.1% step; SNF_STEP_VALUE = ₹0.30/L per 0.1% step; STANDARD_FAT = 3.5; STANDARD_SNF = 8.5; FAT_MIN = 2.0; FAT_MAX = 7.0.

## Types and validation
Farmer ID and shift are strings; litres/fat/SNF are decimal numeric inputs; `is_valid` is Boolean. Reject negative litres, fat outside 2.0–7.0, and non-numeric input. Round the final monetary amount to two decimal places. Assumption: each complete 0.1 percentage-point difference changes the rate by one step; fractional steps are rounded to the nearest integer.

## Data structure and complexity
Storing separate lists for litres, fat and SNF uses O(n) space and can accidentally misalign records. A list of records (dictionaries or dataclasses) keeps each farmer's fields together, also O(n) space. Processing n entries takes O(n) time. For 300 farmers, either is practical; records are safer and remain O(n) when scaled to 150,000 farmers.
