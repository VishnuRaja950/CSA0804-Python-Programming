BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_MIN = 2.0
FAT_MAX = 7.0

RATE_CARD = {"base": BASE_RATE, "fat": FAT_STEP_VALUE, "snf": SNF_STEP_VALUE}

if __name__ == "__main__":
    litres = 10
    fat = 4.2
    snf = 8.7
    print("Rate card:", RATE_CARD)
    print("Before swap:", litres, fat)
    litres, fat = fat, litres
    print("After swap:", litres, fat)
    value = 10
    value = "ten"  # Python variables can be rebound to another type.
    print(type(value).__name__, value)
