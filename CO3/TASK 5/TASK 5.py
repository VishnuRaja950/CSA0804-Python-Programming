readings = [4.0, 9.5, 55.0, -60.0, 6.0, 1.0, 8.5]
valid_loop = []
for c in readings:
    if -50 <= c <= 50:
        valid_loop.append(c)
fahrenheit_loop = [c * 9/5 + 32 for c in valid_loop]
 
valid_comp = [c for c in readings if -50 <= c <= 50]
fahrenheit_comp = [c * 9/5 + 32 for c in readings
                   if -50 <= c <= 50]
valid_map = list(filter(lambda c: -50 <= c <= 50, readings))
fahrenheit_map = list(map(lambda c: c * 9/5 + 32, valid_map))
alarm_minutes = [i for i, c in enumerate(readings, start=1)
                 if -50 <= c <= 50 and not 2 <= c <= 8]
 
print("Valid C:", valid_comp)
print("Valid F:", [round(x, 1) for x in fahrenheit_comp])
print("map/filter matches:", valid_loop == valid_map)
print("comprehension matches:", valid_loop == valid_comp)
print("Alarm minutes:", alarm_minutes)
print("All invalid:", [c for c in [80, -90] if -50 <= c <= 50])
