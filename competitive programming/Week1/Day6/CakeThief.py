def max_duffel_bag_value(cake_tuples, weight_capacity):
    for tup in cake_tuples:
        if (tup[0] == 0 and tup[1] != 0):
            return float('inf')
    n = len(cake_tuples)
    return unboundedKnapsack(cake_tuples, weight_capacity, n)
    return -1


def unboundedKnapsack(cake_tuples, W, n):
    dp = [0 for i in range(W + 1)]

    for i in range(W + 1):
        for j in range(n):
            if (cake_tuples[j][0] <= i):
                dp[i] = max(dp[i], dp[i - cake_tuples[j][0]] + cake_tuples[j][1])

    return dp[W]