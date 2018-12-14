from time import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def main():

    numbers = [(1963309, 2265973), (2030677, 3814172),
                (1551645, 2229620), (2039045, 2020802)]

    # Example 1         
    start = time()
    results = list(map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))

    # Example 2
    start = time()
    pool = ThreadPoolExecutor(max_workers=2)
    results = list(pool.map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))

    # Example 3
    start = time()
    pool = ProcessPoolExecutor(max_workers=2)  # The one change
    results = list(pool.map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))

if __name__ == '__main__':
    main()