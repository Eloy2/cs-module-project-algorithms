'''
Input: a List of integers
Returns: a List of integers
'''
# DONE
# def moving_zeroes(arr):
#     left = []
#     right = []
#     for i in arr:
#         if i == 0:
#             right.append(i)
#         else:
#             left.append(i)
#     left.extend(right)
#     return left
def moving_zeroes(arr):
    final = []
    for i in arr:
        if i == 0:
            final.append(i)
        else:
            final.insert(0,i)
    return final

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")