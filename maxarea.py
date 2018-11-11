def max_area(H):
    l = 0
    r = len(H) - 1
    area = 0

    while l < r:
        # Calculating max area 
        area = max(area, min(H[l], H[r]) * (r - l))
        if H[l] < H[r]:
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