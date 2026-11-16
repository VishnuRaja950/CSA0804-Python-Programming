import re, time
 
sources = [
 {"name":"Dr. Ravi", "phones":["+91 98400 12345"], "emails":["ravi@x.in"]},
 {"name":"ravi kumar", "phones":["9840012345"], "emails":["ravi.k@x.in"]},
 {"name":"Meena", "phones":["+91-90000-11111"], "emails":[]},
 {"name":"Meena", "phones":[], "emails":["meena@x.in"]},
 {"name":"Arun", "phones":["90000 22222"], "emails":["arun@x.in"]},
]
 
def normalize_phone(value):
    digits = re.sub(r"\\D", "", value)
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits if len(digits) == 10 else None
 
def merge_contacts(records):
    merged, without_number = {}, []
    for record in records:
        numbers = {n for raw in record.get("phones", [])
                   if (n := normalize_phone(raw))}
        if not numbers:
            without_number.append(record.copy())
            continue
        for number in numbers:
            item = merged.setdefault(number,
                {"names": set(), "phones": set(), "emails": set()})
            if record.get("name"):
                item["names"].add(record["name"].strip())
            item["phones"].add(number)
            item["emails"].update(e.lower() for e in record.get("emails", []))
    return merged, without_number
 
merged, no_number = merge_contacts(sources)
for number, data in sorted(merged.items()):
    print(number, sorted(data["names"]), sorted(data["emails"]))
print("without usable number:", len(no_number))
