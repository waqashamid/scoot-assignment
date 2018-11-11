
def count_ways_to_sum(n):

    counts = [0 for _ in range(n + 1)]
    counts[0] = 1

    for i in range(1, n + 1):
        counts[i] += counts[i - 1]
    for i in range(2, n + 1):
        counts[i] += counts[i - 2]
    for i in range(5, n + 1):
        counts[i] += counts[i - 5]
    for i in range(10, n + 1):
        counts[i] += counts[i - 10]

    return counts[n]

def main():
    # Test data
    n = 5

    print(count_ways_to_sum(n))

if __name__=='__main__':
    main()