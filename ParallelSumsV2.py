'''
Parallel Sums
Have the function ParallelSums(arr) take the array of integers stored in arr which 
will always contain an even amount of integers, and determine how they can be split
into two even sets of integers each so that both sets add up to the same number. 
If this is impossible return -1. If it's possible to split the array into two sets,
then return a string representation of the first set followed by the second set with
each integer separated by a comma and both sets sorted in ascending order. The set
that goes first is the set with the smallest first integer.

For example: if arr is [16, 22, 35, 8, 20, 1, 21, 11], then your program should 
output 1,11,20,35,8,16,21,22

Examples
Input: [1,2,3,4]
Output: 1,4,2,3
'''


def splitter(arr, left, target_sum, max_layer, layer):
    # spacing = '    ' * layer
    # print(spacing, str(arr).ljust(50, ' '), str(left).ljust(50, ' '))
    if sum(left) == target_sum and len(left) % 2 == 0:
        # print(spacing, '  1. RETURNING LEFT = ', left)
        return left
    elif sum(left) > target_sum or len(arr) == 0:
        # print(spacing, '  2. RETURNING LEFT= ', [])
        return []
    # elif layer >= max_layer:
    #     # print(spacing, '  3. RETURNING LEFT= ', [])
    #     return []
    selected = arr[0]
    new_arr = arr[1:]
    new_left = left + [selected]
    # print(spacing, 'INSIDE A:')
    a = splitter(new_arr, new_left, target_sum, max_layer, layer + 1)
    # print(spacing, 'INSIDE B:')
    b = splitter(new_arr, left, target_sum, max_layer, layer + 1)
    # print(spacing, 'RETURNING A OR B')
    # print(spacing, a or b)
    return a or b


def ParallelSums(arr):
    if sum(arr) % 2 != 0:
        return -1
    target_sum = sum(arr) // 2
    smallest_num = min(arr)
    arr.remove(smallest_num)
    output = splitter(arr, [smallest_num], target_sum, len(arr), 0)
    if output:
        left = sorted(output)
        arr.append(smallest_num)
        for item in left:
            arr.remove(item)
        right = sorted(arr)
        left.extend(right)
        return ','.join([str(item) for item in left])
    else:
        return -1


arr = [16, 22, 35, 8, 20, 1, 21, 11]
print(ParallelSums(arr))
