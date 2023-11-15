buy_price = int(input("時価総額:"))
profit = int(input("当期純利益:"))
investing = int(input("投資額:"))
depriciation = int(input("減価償却費:"))
interest = float(input("利子")) / 100
capital_cost = 0.09
roic = float(input("ROIC:")) / 100
low_growth_late = round(float(input("成長率:")) / 100, 2)
middle_growth_late = 0.07
high_growth_late = 0.1
extra_high_growth_late = 0.15
holding_period = int(input("保有期間:"))

flow = profit + depriciation - investing

normal_value = 0
low_growth_value = 0
middle_growth_value = 0
high_growth_value = 0
extra_high_growth_value = 0
for i in range(int(holding_period)):
    normal_value += flow / (1 + interest) ** i
    low_growth_value += (flow * (1 + low_growth_late) ** i) / (1 + interest) ** i
    middle_growth_value += (flow * (1 + middle_growth_late) ** i) / (1 + interest) ** i
    high_growth_value += (flow * (1 + high_growth_late) ** i) / (1 + interest) ** i
    extra_high_growth_value += (flow * (1 + extra_high_growth_late) ** i) / (
        1 + interest
    ) ** i

values = {
    "成長なし": int(normal_value),
    "成長あり": int(low_growth_value),
    "7%": int(middle_growth_value),
    "10%": int(high_growth_value),
    "15%": int(extra_high_growth_value),
}

print("{}年後の企業価値は{values}です".format(holding_period, values=values))
