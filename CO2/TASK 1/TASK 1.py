def separate_if(units, ration_card, senior_member):
    results = []
    if units <= 100:
        results.append("Full subsidy")
    if units <= 200 and ration_card:
        results.append("Partial subsidy")
    if units > 200 and senior_member:
        results.append("Senior subsidy")
    if not results:
        results.append("No subsidy")
    return results

def chained_decision(units, ration_card, senior_member):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200 and ration_card:
        return "Partial subsidy"
    elif units > 200 and senior_member:
        return "Senior subsidy"
    else:
        return "No subsidy"

tests = [(100, True, False), (101, True, False),
         (200, False, False), (201, False, True),
         (201, True, False), (80, False, False),
         (150, False, True), (100, True, True)]
for case in tests:
    print(case, "=>", separate_if(*case), "|", chained_decision(*case))
