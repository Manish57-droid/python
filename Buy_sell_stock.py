def maxProfit(price, start, end):

	# If the stocks can't be bought
	if (end <= start):
		return 0

	profit = 0
h the stock
	for i in range(start, end, 1):
		for j in range(i+1, end+1):
			if (price[j] > price[i]):

				# Update the current profit
				curr_profit = price[j] - price[i] +\
					maxProfit(price, start, i - 1) + \
					maxProfit(price, j + 1, end)

				# Update the maximum profit so far
				profit = max(profit, curr_profit)

	return profit

if __name__ == '__main__':
	price = [100, 180, 260, 310, 40, 535, 695]
	n = len(price)

	print(maxProfit(price, 0, n - 1))

