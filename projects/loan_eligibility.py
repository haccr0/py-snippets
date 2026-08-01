high_income = True
good_credit = False

# high income and also good credit

if high_income and good_credit:
    print("eligible for loan")

    # high income true and good credit flase

elif high_income and not good_credit:
    print("not eligible for loan")

    # either one of them is true

elif high_income or good_credit:
    print("maybe!")

else:
    print("sorry")
