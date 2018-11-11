
def find_pair_sum(A=None, sum=None):
    # Let's sort the array first
    # Copying array to leave the original intact for correct indices
    array = A
    sorted(array)
    l = 0
    r = len(array) - 1

    # Traverse the array for the two elements
    temp_indices = None
    while l < r:
        if (array[l] + array[r] == sum):
            temp_indices = [l,r]
            break
        elif (array[l] + array[r] < sum):
            l += 1
        else:
            r -= 1

    # Obtain the indexes in the original array
    if temp_indices:
        indices = []
        indices.append(A.index(array[temp_indices[0]]))
        indices.append(A.index(array[temp_indices[1]]))
        return indices

    return 0

def main():

    # Test data
    array = [3, 7, 12, 18]
    sum = 10

    indexes = find_pair_sum(A=array, sum=sum)
    if not indexes:
        print("No such pair exist")
    else:
        print(indexes)

if __name__=='__main__':
    main()

# Time complexity: O(nlog(n)) assuming sorted takes O(nlog(n))
# Extra Space: O(n)