# Task 5 — Input and Conversion

`input()` always returns a string. Convert numeric strings with `int()` or `float()` inside a `try` block and catch `ValueError` for text such as `8,5` or `eight`. String validation can reject commas/letters before conversion, but it duplicates numeric parsing rules; conversion plus `try/except` is usually simpler and reliable. Each entry takes O(1) time and O(1) extra space.
