def max_profit(prices):
    profit = 0
    for index, price in enumerate(prices):
        future_prices = prices[index:]
        highest_future_price = max(future_prices)
        p = highest_future_price - price
        profit = max(p, profit)
    return profit


if __name__ == '__main__':
    print(max_profit(prices=[10, 8, 7, 5, 2]))
