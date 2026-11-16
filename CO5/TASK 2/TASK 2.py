import csv, io
 
REQUIRED = {"station", "date", "hour", "pm25"}
 
def validate_csv(text):
    if not text.strip():
        return "ERROR: empty file"
    reader = csv.DictReader(io.StringIO(text))
    fields = set(reader.fieldnames or [])
    if not REQUIRED.issubset(fields):
        return f"ERROR: missing columns {sorted(REQUIRED - fields)}"
    return f"OK: {sum(1 for _ in reader)} data rows"
 
print(validate_csv("station,date,hour\\nAdyar,2026-10-01,08"))
print(validate_csv("station;date;hour;pm25\\nAdyar;2026-10-01;08;48"))
print(validate_csv(""))
try:
    "station,date,hour,pm25".encode("utf-16").decode("utf-8")
except UnicodeDecodeError:
    print("ERROR: invalid UTF-8; verify source encoding")
