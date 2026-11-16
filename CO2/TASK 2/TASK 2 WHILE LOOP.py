correct_otp = "482916"
attempts = 0
limit = 3
verified = False

while attempts < limit:
    entered = input("Enter OTP: ").strip()
    if entered == "":
        print("Blank entry ignored")
        continue
    attempts += 1
    if entered == correct_otp:
        verified = True
        print("OTP verified")
        break
    else:
        print("Wrong OTP")
else:
    print("Account locked for 30 minutes")

if not verified:
    print("Verification failed")
