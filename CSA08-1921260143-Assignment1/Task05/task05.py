def read_number(prompt, *, minimum=None, maximum=None):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Invalid input: enter a number such as 8.5.")
            continue
        if minimum is not None and value < minimum:
            print(f"Value must be at least {minimum}.")
            continue
        if maximum is not None and value > maximum:
            print(f"Value must be at most {maximum}.")
            continue
        return value

def main():
    farmer_id = input("Farmer ID: ").strip()
    litres = read_number("Litres: ", minimum=0)
    fat = read_number("Fat % (2.0–7.0): ", minimum=2.0, maximum=7.0)
    snf = read_number("SNF %: ", minimum=0)
    print(f"Farmer {farmer_id}: {litres:.2f} L, fat {fat:.2f}%, SNF {snf:.2f}%")

if __name__ == "__main__":
    main()
