'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # What if 0 is given
    # Cheese strat
    # if n <= 1:
    #     return 1
    # elif n == 2:
    #     return 2
    # elif n == 5:
    #     return 13
    # elif n == 10:
    #     return 274
    # 1 cookies visual [1]
    # [1]
    # 2 cookies visual [1,1], [2]
    # [2]
    #  3 cookies Visual [1,1,1], [1,2], [2,1], [3]
    # [4]
    # 4 cookies visual [1,1,1,1],[3,1],[1,3],[2,2],[2,1,1],[1,1,2],[1,2,1]
    # [7]
    # 5 cookies visual [1,1,1,1,1],[3,2],[2,3],[3,1,1],[1,1,3],[1,3,1],[2,2,1],[1,2,2],[2,1,2],[1,1,1,2],[2,1,1,1],[1,2,1,1],[1,1,2,1]
    # [13]
    if n < 0:
        return 0
    if n <= 1:
        return 1
    else:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
