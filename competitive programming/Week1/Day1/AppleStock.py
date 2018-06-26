def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Insufficient stocks.')

    lowprice = stock_prices[0]
    max_profit = stock_prices[1] - lowprice

    for i in range(1, len(stock_prices)):
        profit = stock_prices[i] - lowprice
        max_profit = max(max_profit, profit)
        lowprice  = min(lowprice, stock_prices[i])
    return max_profit

if __name__ == '__main__':
    stock_list = eval(input())
    try:
        print(str(get_max_profit(stock_list)))
    except ValueError:
        print('Insufficient stocks.')