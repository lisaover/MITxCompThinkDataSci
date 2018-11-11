'''POWER SET GENERATORS'''

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
        
items = ['book', 'computer', 'earbuds', 'lotion', 'notebook', 'snack']
#p = powerSet(items)
#p.__next__()

def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each 
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            # i>>j is same as i // 2**j so replace with i // 3 ** j
            if (i // 3**j) % 3 == 1:
                bag1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)
        
items = ['book', 'computer', 'earbuds', 'lotion', 'notebook', 'snack']
#p = yieldAllCombos(items)
#p.__next__()

# generate all combinations of N items
def powerSet2(items):
    from itertools import chain, combinations
    s = list(items)
    # create combinations
    combo = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    for c in combo:
        yield c
        
items = ['book', 'computer', 'earbuds', 'lotion', 'notebook', 'snack']
p = powerSet2(items)
#p.__next__()



'''FROM STACK OVERFLOW ABOUT POWERSET WITH ITERTOOLS'''

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

for result in powerset([1, 2, 3]):
    print(result)

results = list(powerset([1, 2, 3]))
print(results)
