'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    
    count = 0
    # # Your code here
    # # Traverse the array. If element  
    # # encountered is non-zero, then 
    # # replace the element at index 
    # # 'count' with this element 
    for i in range(len(arr)):
        if arr[i] != 0:
            # here count is incremented 
            arr[count] = arr[i] 
            count+=1
    # # Now all non-zero elements have been 
    # # shifted to front and 'count' is set 
    # # as index of first 0. Make all  
    # # elements 0 from count to end. 
    while count < len(arr): 
        arr[count] = 0
        count += 1
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")