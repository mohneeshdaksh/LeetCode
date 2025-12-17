# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# prices = [7,2,8,1,5,3,6,4]
prices = [7,6,5,4,3,2,1]

max_profit = 0


for buy_day in range(len(prices)):
    for sell_day in range((buy_day+1), len(prices)):
        profit = prices[sell_day] - prices[buy_day]
        if profit > max_profit:
            max_profit = profit
            # day_to_buy = buy_day + 1
            # day_to_sell = sell_day + 1

print(f'Maximum Profit = {max_profit}')
# print(f'Day to buy a stock = {day_to_buy}')
# print(f'Day to sell that stock = {day_to_sell}')