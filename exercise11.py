cash = int(input("Enter cash you have: "))
price = int(input("Enter price: "))

def changeFunction(cash, price):
    bills = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    money = []
    change = cash - price
    x = 0
    while True:
        if x >= 10:
            break
        if change >= bills[x]:
            money.append(bills[x])
            change -= bills[x]
        elif change < bills[x]:
            x += 1
    return money


print(changeFunction(cash, price))