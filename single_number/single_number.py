'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
     # Hacky version
    # remove = [1, 4, 5, 3, 0]
    # arr = [i for i in arr if i not in remove]
    # return arr
    n = len(arr)
    res = arr[0] 
      
    # Do XOR of all elements and return 
    for i in range(1,n): 
        res = res ^ arr[i] 
      
    return res 
    
    
            
            
           
        
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")