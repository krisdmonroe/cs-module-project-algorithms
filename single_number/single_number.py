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
    # n = len(arr)
    # res = arr[0] 
      
    # # Do XOR of all elements and return 
    # for i in range(1,n): 
    #     res = res ^ arr[i] 
      
    # return res 
    # no_dups = []
    # for x in arr:
    #     if x not in no_dups:
    #         no_dups.append(x)
    #     else:
    #         no_dups.remove(x)
    # return no_dups[0]
    # O(2 * n) ~ O(n)
    # keep track of the counts of how many times we've seen a particular number 
    # dictionaries are better at being searched 
    counts = {}

    #O(n)
    # loop through nums to tally up how many times we've seen each number 
    for x in arr:
        if x in counts: #O(1)
            del counts[x]
        else:
            counts[x] = 1

    # loop through all of the key-value pairs in counts to find the one pair
    # whose value is 1
    #O(1)
    for ar in counts:
        if counts[ar] == 1:
            return ar
            
            
           
        
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")