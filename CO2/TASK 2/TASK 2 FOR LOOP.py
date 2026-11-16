correct_otp = "482916"
verified = False

for attempt in range(3):
    entered = input("Enter OTP: ").strip()
    if not entered:
        print("Blank entry ignored")
        continue
    if entered == correct_otp:
        verified = True
        print("OTP verified")
        break
    print("Wrong OTP")
else:
    print("Account locked for 30 minutes")

# pass is used when a branch is intentionally left empty.
security_question_pending = False
if security_question_pending:
    pass
