from decimal import Decimal, InvalidOperation
 
def process_mess_file(filename):
    total = Decimal("0.00")
    report = []
    rejected = []
 
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_no, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    parts = line.strip().split(",")
                    if len(parts) != 3:
                        raise ValueError("expected 3 fields")
                    reg_no, name, amount_text = parts
                    amount = Decimal(amount_text.strip())
                    if amount < 0:
                        raise ValueError("amount cannot be negative")
                    total += amount
                    report.append(f"{name.strip()} {amount:.2f}")
                except (ValueError, InvalidOperation) as error:
                    rejected.append((line_no, line.rstrip(), str(error)))
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as error:
        print(f"File error: {error}")
        return
 
    print("\n".join(report))
    print("Total", f"{total:.2f}")
    print("Rejected:", rejected)
 
if __name__ == "__main__":
    process_mess_file("mess_oct.txt")
