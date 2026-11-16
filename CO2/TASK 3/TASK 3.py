def normalise(text):
    return text.replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    middle_length = len(reg) - 8
    return (reg[0:2].isalpha()
            and reg[2:4].isdigit()
            and reg[4:4 + middle_length].isalpha()
            and reg[4 + middle_length:].isdigit())

def format_receipt(reg):
    if not is_valid(reg):
        return "INVALID"
    middle_length = len(reg) - 8
    return (reg[:2] + " " + reg[2:4] + " "
            + reg[4:4 + middle_length] + " " + reg[-4:])

for raw in ["tn 09 ab 1234", "KA-01-M-0007",
            "TN9AB1234", "TN 22 1234 AB"]:
    reg = normalise(raw)
    print(f"{raw:15} -> {reg:11} "
          f"{'valid' if is_valid(reg) else 'INVALID'}")
print(format_receipt(normalise("tn 09 ab 1234")))
