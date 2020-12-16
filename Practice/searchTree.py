# 3 different approaches to solve the Knapsack problem
# reference: mit 6.0002
def maxVal(toConsider: list, avail: int):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider.getUnits() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getUnits())
        withVal += nexItem.getValue()
        withOutVal, withOutToTake = maxVal(toConsider[1:], avail)
        if withVal > withOutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withOutVal, withOutToTake)
    return result


def fastmaxVal(toConsider: list, avail: int, memo={}):
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider.getUnits() > avail:
        # explore right only
        result = fastmaxVal(toConsider[1:], avail, memo)
    else:
        # explore left
        nextItem = toConsider[0]
        withVal, withToTake = fastmaxVal(
            toConsider[1:], avail - nextItem.getUnits(), memo
        )
        withVal += nexItem.getValue()
        withOutVal, withOutToTake = fastmaxVal(toConsider[1:], avail, memo)
        # choose better branch
        if withVal > withOutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withOutVal, withOutToTake)
    memo[(len(toConsider), avail)] = result
    return result


def greedy(items, maxCost, keyFunction):
    copy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0, 0
    for i in range(len(items)):
        if items[i].getUnits() + totalCost > maxCost:
            break
        else:
            result.append(items[i])
            totalVal += items[i].getValue()
            totalCost += items[i].getUnits()
    return (totalValue, result)
