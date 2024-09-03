from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7]

resMax = reduce(lambda x, y : x if x>y else y, numbers) ##maior valor da lista
resMin = reduce(lambda x, y : x if x<y else y, numbers) ##menor valor da lista

print(resMax, resMin)