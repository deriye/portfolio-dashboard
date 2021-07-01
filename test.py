import pandas_datareader as web



# name
# date
# amount invested
# commision fee (default 1%)

# example:
# name: Bitcoin
# buy price: 3843.520020 (2019-01-01)
# amount invested: 1 000
# commision fee: 10

# price today: 33468.308594 (2021-07-01)

# price difference in precentage: (buy price - price today)/buy price * 100


def percentage_change(buy_price, sell_price):
    return (sell_price - buy_price) / buy_price

#print(percentage_change(10000, 5000))

while True:
    assets = []

    option = input("Options (Add, Delete, List, Quit): ")

    if (option == "Quit"):
        break

    asset_name = input("Asset name: ") #input("Asset name: ")
    closing_prices = web.DataReader(asset_name, data_source="yahoo", start="2019-01-01", end="2021-07-01")["Close"]#["2021-06-26"]
    year = input("Year: ")
    month = input("Month: ")
    day = input("Day: ")
    buy_date = year + "-" + month + "-" + day
    amount_invested = int(input("Amount invested: "))
    buy_price = closing_prices[buy_date]
    today_date = "2021-07-01"
    sell_price = closing_prices[today_date]
    print("buy price:", buy_price)
    print("sell price:", sell_price)
    change = percentage_change(buy_price, sell_price)
    portfolio_value = amount_invested * (1 + change)
    print("amount invested:", amount_invested)
    print("portfolio value:", portfolio_value)
    print("profit:", portfolio_value - amount_invested, "("+ str(round(change * 100, 2)) +"%)")
    print("")