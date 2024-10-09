# %%NBQA-CELL-SEPfaab7c
"Module on solving tasks from the book Python easy."


# %%NBQA-CELL-SEPfaab7c
# Tatyana

yearly_income = 200000
purchase_price = 1000000
sale_price = 250000
invetment_rate = 0.08

percantage_of_yearly_income_after_amortization = yearly_income / (
    purchase_price - sale_price
)
min_period = (purchase_price - sale_price) / 200000

yearly_income = purchase_price * (1 + invetment_rate)
min_period, (
    12 / 100
) * 75, percantage_of_yearly_income_after_amortization, yearly_income


# %%NBQA-CELL-SEPfaab7c
# Tanya. Решение с учетом капитализации процентов
# Уходит в бесконечный цикл, тк вариант с авто никогда не догоняет по выгоде инвестиционный вариант
years_count = 0
yearly_income = 200000
purchase_price = 1000000
year = 0
new = purchase_price
income = 0

real_price_for_a_car = 250000 - 1000000

price_car = real_price_for_a_car

while price_car < new * 1.08:
    price_car += 200000
    income = new * 0.08
    new += income
    year += 1

year
