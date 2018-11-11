from itertools import chain, combinations

# generate all combinations of N items
def powerSet(items):
    s = list(items)
    # create combinations
    combo = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    for c in combo:
        yield c

def powerset_generator(i):
    for subset in chain.from_iterable(combinations(i, r) for r in range(len(i)+1)):
        yield subset

list1 = [1,2,3,4,5]
for i in powerset_generator(list1):
    print (i)