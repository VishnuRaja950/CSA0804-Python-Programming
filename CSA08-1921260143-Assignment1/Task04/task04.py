from math import floor

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5

def steps(value, standard):
    # Round the difference in tenths to the nearest whole step.
    return round((value - standard) * 10)

def rate_per_litre(fat, snf):
    return round(BASE_RATE + steps(fat, STANDARD_FAT) * FAT_STEP_VALUE
                 + steps(snf, STANDARD_SNF) * SNF_STEP_VALUE, 2)

if __name__ == "__main__":
    for fat in (4.2, 3.1):
        print(fat, "steps:", steps(fat, STANDARD_FAT))
    print("rate:", rate_per_litre(4.2, 8.7))
    print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
    print("round example:", round((4.2 - 3.5) / 0.1))
    print("round/int/floor for 3.1 fat steps:",
          round((3.1 - 3.5) / 0.1), int((3.1 - 3.5) / 0.1),
          floor((3.1 - 3.5) / 0.1))
