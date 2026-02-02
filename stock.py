def maxProfit(prices):
    b = prices[0]
    Pf = 0
    for i in range(1, len(prices)):
        if prices[i] > b:
            Pf = max(Pf, prices[i] - b)
        else:
            b = prices[i]
    return Pf
