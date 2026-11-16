timetable = {
 "12631": {"name":"Nellai Express",
   "stops":[("Chennai Egmore","19:50","20:00"),
            ("Villupuram","22:05","22:07"),("Tirunelveli","06:45","06:50")],
   "days":{"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}},
 "12632": {"name":"Nellai Return",
   "stops":[("Tirunelveli","20:00","20:05"),
            ("Madurai","23:00","23:05"),("Chennai Egmore","07:00","07:10")],
   "days":{"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}},
 "16127": {"name":"Guruvayur Express",
   "stops":[("Chennai Egmore","09:00","09:10"),
            ("Tambaram","09:35","09:37"),("Villupuram","11:30","11:32")],
   "days":{"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}},
 "20605": {"name":"Chennai Express",
   "stops":[("Chennai Egmore","10:00","10:05"),
            ("Madurai","16:00","16:05")],
   "days":{"Mon","Wed","Fri"}},
 "12605": {"name":"Pallavan Express",
   "stops":[("Chennai Egmore","15:00","15:05"),
            ("Villupuram","17:00","17:02")],
   "days":{"Mon","Tue","Wed","Thu","Fri","Sat"}}
}
station_index = {}
for number, details in timetable.items():
    for station, arrival, departure in details["stops"]:
        station_index.setdefault(station, []).append(number)
 
def trains_at(station, day):
    numbers = [n for n in station_index.get(station, [])
               if day in timetable[n]["days"]]
    return sorted(numbers, key=lambda n: next(
        dep for s, arr, dep in timetable[n]["stops"] if s == station))
 
matches = trains_at("Villupuram", "Mon")
print("Villupuram on Mon:", matches)
for n in matches:
    print(n, timetable[n]["name"])
print("Unknown station:", trains_at("Unknown", "Mon"))
print("Third stop departure:", timetable["12631"]["stops"][2][2])
