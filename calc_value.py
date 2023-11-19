buy_price = int(input("時価総額:"))
profit = int(input("当期純利益:"))
investing = int(input("投資額:"))
depriciation = int(input("減価償却費:"))
interest = float(input("利子")) / 100

flow = profit + depriciation - investing

value = 0

for i in range(1, 2705):
    value += flow / (1 + interest) ** i
print("-------------------")
print("| {} |".format(int(round(value, 0))))
print("| 時価総額 / 企業価値 = {} |".format(round((buy_price / value), 2)))
if value >= 0:
    if (buy_price / value) < 0.66:
        print("| 割安 |")
    elif (buy_price / value) < 1:
        print("| 少し |")

    else:
        print("| 割高 |")
else:
    print("| マイナス |")
print("-------------------")
