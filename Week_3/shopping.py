# Bryan Rodriguez-Andrade
# CS 325 F2020
# Homework 3, Problem 4(c)

# implementation of knapsack pulled from geeks for geeks https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/ & https://www.geeksforgeeks.org/printing-items-01-knapsack/
# code was then tweaked to output the required file for this problem
# geeks for geeks code was commented for my understanding
def knapsack(wt, val, W, n):
    """runs a bottom up knapsack algorithm

    Args:
        wt (array): an array of weights
        val (array): an array of values
        W (int): the maximum capacity of the knapsack
        n (int): the amount of items passed

    Returns:
        int, [array]: returns the optimized knapsack amount, and items to be taken
    """
    # multidimensional matrix used for the DP table
    K = [[0 for w in range(W + 1)]
        for i in range(n + 1)]

    # this creates the table in a bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):  # loop through both rows an columns of table
            if i == 0 or w == 0:  # sets zero values for the table
                K[i][w] = 0
            elif wt[i - 1] <= w:  # decides which item to choose
                K[i][w] = max(val[i - 1]
                            + K[i - 1][w - wt[i - 1]], K[i - 1][w])  # compares the maximum value of the solution directly above the subproblem on the table, or the value of the previous best solution in the row above with the current item's weight subtracted
            else:
                K[i][w] = K[i - 1][w]  # if neither item is taken
    result = K[n][W]
    optimized_value = result
    w = W
    optimized_items = []

    for i in range(n, 0, -1):
        if optimized_value <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if optimized_value == K[i - 1][w]:
            continue
        else:

            # This item is included.
            optimized_items.append(wt.index(wt[i - 1])+1)

            # Since this weight is included
            # its value is deducted
            optimized_value = optimized_value - val[i - 1]
            w = w - wt[i - 1]
    return result, optimized_items

# handles shopping list file and pulls necessary information, compiling together arguments to be passed to the knapsack algorithm. 
with open('shopping.txt', 'r') as infile, open('results.txt', 'a') as outfile:
    test_cases = int(infile.readline().strip())
    for case in range(test_cases):
        number_of_items = int(int(infile.readline().strip()))
        item_prices = []
        item_weights = []
        for line in range(number_of_items):
            p, w = map(int, infile.readline().strip().split())
            item_prices.append(p), item_weights.append(w)
        size_of_family = int(infile.readline().strip())
        family_member_weight_capacity = [
            int(infile.readline().strip()) for i in range(size_of_family)]

        total_value = 0
        items_taken = []
        for family_member in range(size_of_family):
            value, items = knapsack(item_weights, item_prices,
                                    family_member_weight_capacity[family_member], number_of_items)
            total_value += value
            items_taken.append(items)

        outfile.write('Test Case: %d\n' % (case + 1))
        outfile.write('Total Price: %d\nMember Items:\n' %
                    (total_value))
        for i in range(0, len(items_taken)):
            outfile.write("%d: %s\n" %
                        (i+1, " ".join(map(str, items_taken[i]))))
        outfile.write('\n')
