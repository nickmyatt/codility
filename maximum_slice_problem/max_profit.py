# https://codility.com/demo/take-sample-test/max_profit/

def solution(prices):
    max_profit = 0
    if prices:
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
    return max_profit
