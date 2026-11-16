import random, time
 
def naive_average(values, width=7):
    return [sum(values[i:i+width]) / width
            for i in range(len(values)-width+1)]
 
def running_average(values, width=7):
    if len(values) < width:
        return []
    total = sum(values[:width])
    result = [total / width]
    for i in range(width, len(values)):
        total += values[i] - values[i-width]
        result.append(total / width)
    return result
 
random.seed(12)
readings = [round(random.uniform(0, 30), 1) for _ in range(365)]
weekly = [sum(readings[i:i+7]) for i in range(0, 365, 7)]
averages = running_average(readings)
wettest = max(range(len(weekly)), key=weekly.__getitem__)
driest = min(range(len(weekly)), key=weekly.__getitem__)
dry_days = [i+1 for i, value in enumerate(readings) if value == 0]
print("Readings:", len(readings))
print("Weekly totals:", len(weekly), "(last week may be partial)")
print("Wettest week:", wettest+1, "total =", round(weekly[wettest], 1))
print("Driest week:", driest+1, "total =", round(weekly[driest], 1))
print("Moving averages:", len(averages))
print("Dry days:", dry_days)
print("Short input:", running_average([1, 2, 3]))
print("Empty input:", running_average([]))
