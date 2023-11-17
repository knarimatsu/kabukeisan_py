buy_price = int(input("時価総額:"))
profit = int(input("当期純利益:"))
investing = int(input("投資額:"))
depriciation = int(input("減価償却費:"))
interest = float(input("利子")) / 100

flow = profit + depriciation - investing

value = 0

for i in range(1, 2705):
    value += flow / (1 + interest) ** i
print('-------------------')
print('| {} |'.format(int(round(value, 0))))
print('| {} |'.format(round((buy_price / value), 2) ))
print('| {} |'.format(round((value / buy_price ), 2) ))
print('-------------------')
