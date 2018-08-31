a = (3, 5, 6, 87, 78, 78, 9, 7, 5)


def count_elements(sequence) -> dict:
    # Tally elements from sequence
    hist = {}
    for i in sequence:
        hist[i] = hist.get(i, 0) + 1
    return hist


counted = count_elements(a)
print(counted)

# Or
from collections import Counter
counted = Counter(a)
print(counted)
