has_high_income = True
has_good_credit = True
# below is the code written to be eligible for loan if the client does not have a criminal record and has a good credit
if has_high_income and has_good_credit:
    print("Eligible for loan.")
else:
    if not has_high_income:
        print("Not Eligible for loan, your income is below the limit.")
    else:
        print("Not Eligible for loan, you have a bad credit score.")


