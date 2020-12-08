annual_salary = 150000
semi_annual_raise = 0.07

total_cost = 1000000
down_payment = total_cost * 0.25

low, high = 0, 10000
portion_saved = (high + low) // 2
epsilon = 100

current_savings = 0
months_require = 36
steps_used = 0


def savings(annual_salary, portion_saved):
    current_savings = 0
    for months_passed in range(36):
        if months_passed % 6 == 0 and months_passed != 0:
            annual_salary *= 1 + semi_annual_raise

        current_savings += (
            portion_saved / 10000 * annual_salary / 12 + current_savings * 0.04 / 12
        )
    return current_savings


current_savings = savings(annual_salary, high)
if current_savings < down_payment:
    print("It is not possible to pay the down payment in three years.")

else:
    current_savings = savings(annual_salary, portion_saved)
    steps_used += 1
    while abs(down_payment - current_savings) >= epsilon:
        if down_payment > current_savings:
            low = portion_saved
        else:
            high = portion_saved
        portion_saved = (high + low) // 2
        current_savings = savings(annual_salary, portion_saved)
        steps_used += 1

    print("Best savings rate:", portion_saved / 10000)
    print("Steps in bisection search:", steps_used - 1)