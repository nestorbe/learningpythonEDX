balance = 999999
annualInterestRate = .18
monthly_interest_rate = annualInterestRate / 12.0
mp_low_start = balance / 12
mp_high_start = (balance * ((1 + monthly_interest_rate) ** 12)) / 12
minimum_payment = (mp_low_start + mp_high_start) / 2
epsilon = 0.01
count = 0


def year_check(minimum_payment, balance, annualInterestRate):
    month = 1
    while month <= 12:
        monthly_interest_rate = annualInterestRate / 12.0

        def monthly_unpaid_balance(balance, minimum_payment):
            return balance - minimum_payment

        monthly_unpaid_balance = monthly_unpaid_balance(balance, minimum_payment)
        updated_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        balance = updated_balance
        month += 1

        if month == 12:
            return balance

while balance - year_check(minimum_payment, balance, annualInterestRate) >= epsilon:

    if minimum_payment - year_check(minimum_payment, balance, annualInterestRate) < epsilon and minimum_payment - year_check(minimum_payment, balance, annualInterestRate) > -epsilon:
        print("Lowest payment: " + str(round(minimum_payment, 2)))
        print(count)
        break

    if minimum_payment < year_check(minimum_payment, balance, annualInterestRate):
        mp_low_start = minimum_payment

    else:
        mp_high_start = minimum_payment

    minimum_payment = (mp_low_start + mp_high_start) / 2
    count += 1











