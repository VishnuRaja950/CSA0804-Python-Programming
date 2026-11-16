import os
import tempfile
 
class InvalidRecord(Exception):
    """Raised when an attendance line is not valid."""
 
def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}")
    reg_no, date, status = parts
    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")
    return reg_no, date, status
 
def summarise(path):
    present, absent, errors = 0, 0, []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_no, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    _, _, status = parse_line(line)
                    if status == "P":
                        present += 1
                    else:
                        absent += 1
                except InvalidRecord as error:
                    errors.append((line_no, str(error)))
    except FileNotFoundError as error:
        raise RuntimeError("attendance file not found") from error
    except (PermissionError, UnicodeDecodeError) as error:
        raise RuntimeError("cannot read attendance file") from error
    else:
        print("File processed successfully")
    finally:
        print("File processing attempt completed")
    return present, absent, errors
 
data = ("192311001,2026-10-08,P\\n"
        "192311002,2026-10-08,A\\n"
        "192311003,2026-10-08\\n"
        "192311004,2026-10-08,L\\n")
with tempfile.NamedTemporaryFile("w", suffix=".csv",
        delete=False, encoding="utf-8") as tmp:
    tmp.write(data)
print(summarise(tmp.name))
os.remove(tmp.name)
