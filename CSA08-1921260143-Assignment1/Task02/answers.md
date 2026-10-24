# Task 2 — Values and Types

- `10` is `int`; `10.0` is `float`; `"10"` is `str`; `True` is `bool`; `[10, 8.5]` is `list`.
- `7 / 2` → `3.5`; `7 // 2` → `3`; `7 % 2` → `1`; `-7 // 2` → `-4` because floor division rounds down.
- `0.1 + 0.2 == 0.3` is `False` because binary floating-point cannot represent many decimal fractions exactly.
- `Decimal("0.1") + Decimal("0.2") == Decimal("0.3")` is `True`.
- Use `Decimal` constructed from strings for money. `Decimal(float("0.1"))` preserves the float's binary approximation and therefore contains extra digits; prefer `Decimal("0.1")`.
- `Decimal` and integer paise are appropriate exact-money strategies. Floats with rounding after every addition can accumulate rounding error. All three are O(n) time; a running total uses O(1) additional space.
