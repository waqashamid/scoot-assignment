def max_area(H):
    l = 0
    r = len(H) - 1
    area = 0

    # Algorithm/Idea:
    # (arr_size-1)*(min(H1, Hn) has the maximum base length
    # If some other rectangle beats the above area that becomes the greater rectangle and so on.
    # Since (arr_size -1) is a constant, min(H1, Hn) dictates the chosen rectangle/area.
    # 1. Take 2 pointers l at 0 and r at n-1, where n is length of H.
    # 2. Calculate the area and compare with previous area and update accordingly
    # 3. If H[l] < H[r], this means l, if moved to the right can lead to a bigger rectangle and vice versa for r.
    # Now, this is important:
    # Consider H1 < Hn, we cannot build a bigger rectangle using H1, so the problem reduces to the same for
    # H2 to Hn. So at every step, the lesser of H[l] and H[r] needs to be forgotten to achieve a greater rectangle.

    # Below is the implementation for the same
    while l < r:
        # Calculating max area 
        area = max(area, min(H[l], H[r]) * (r - l))
        if H[l] <= H[r]:
            l += 1
        else:
            r -= 1
    return area

def main():
    # Test data
    y = [3, 1, 2, 4, 5]
    print(max_area(y))
    
if __name__=='__main__':
    main()

# Time complexity: O(n) where n is the length of input array