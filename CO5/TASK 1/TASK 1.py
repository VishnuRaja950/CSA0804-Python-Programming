import csv, io, sqlite3
from statistics import median
 
RAW = """station,date,hour,pm25,temperature,temp_unit
Adyar,2026-10-01,08,48,80.6,F
Adyar,2026-10-02,08,NA,82.4,F
Adyar,2026-10-03,08,,84.2,F
Guindy,2026-10-01,09,95,27,C
Guindy,2026-10-02,09,-5,28,C
Guindy,2026-10-03,09,121,29,C
Guindy,2026-10-03,09,121,29,C
T Nagar,2026-10-01,10,1500,30,C
"""
 
def clean_csv(text):
    raw = list(csv.DictReader(io.StringIO(text)))
    print("RAW ROWS:", len(raw))
    for r in raw:
        print(r)
    accepted, rejected, seen = [], [], set()
    for r in raw:
        station = r["station"].strip().upper().replace(" ", "_")
        key = (station, r["date"], r["hour"])
        try:
            value = float(r["pm25"]) if r["pm25"].strip().upper() not in ("", "NA") else None
            if value is not None and not 0 <= value <= 999:
                rejected.append((key, "PM2.5 out of range")); continue
            temp = float(r["temperature"])
            if r["temp_unit"].upper() == "F":
                temp = (temp - 32) * 5 / 9
            if key in seen:
                rejected.append((key, "duplicate")); continue
            seen.add(key)
            accepted.append({"station":station, "date":r["date"],
                "hour":r["hour"], "pm25":value, "temp_c":round(temp,2)})
        except (ValueError, TypeError):
            rejected.append((key, "parse error"))
    # forward-fill by station in date/hour order; median fallback if no prior value
    accepted.sort(key=lambda x:(x["station"],x["date"],x["hour"]))
    history = {}
    valid_values = [x["pm25"] for x in accepted if x["pm25"] is not None]
    fallback = median(valid_values) if valid_values else 0.0
    for x in accepted:
        if x["pm25"] is None:
            x["pm25"] = history.get(x["station"], fallback)
            x["quality"] = "IMPUTED"
        else:
            x["quality"] = "OK"
        history[x["station"]] = x["pm25"]
    return accepted, rejected
 
cleaned, rejected = clean_csv(RAW)
print("\\nCLEANED:")
for row in cleaned: print(row)
print("REJECTED:", rejected)
