"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

while (income := input('Enter income ')) and not income.isnumeric():
    print('Wrong number, try again')

while (outcome := input('Enter outcome ')) and not outcome.isnumeric():
    print('Wrong number, try again')

income = int(income)
outcome = int(outcome)
profit = income - outcome

if profit > 0:
    print('Your firm performed well')
    profitability = profit / income * 100
    print(f'Your firm has profitability: {profitability:.2f}')
    while (employees_count := input('Enter employees count ')) and not employees_count.isnumeric():
        print('Wrong number, try again')
    employees_count = int(employees_count)
    print(f'Profit per employee: {profit / employees_count:.2f}')
elif profit < 0:
    print('Your firm performed bad. Fire your director!')
else:
    print('Your firm is odd')
