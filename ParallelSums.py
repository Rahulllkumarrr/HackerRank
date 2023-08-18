"""
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
"""


# Code starts here
def isEvenSets(subset):
    if subset:
        if len(subset) % 2 == 0:
            return True
    return False


def part(arr, expected_sum, left=[], right=[]):
    if arr:
        selected_int = arr[-1]
        if selected_int > expected_sum:
            return None, None
        # print("SELECTED INT => ", selected_int, arr)
        fake_left = left + [selected_int]
        fake_right = right + [selected_int]
        # print(left,right)
        if sum(fake_left) == expected_sum == sum(right + arr[:-1]):
            if isEvenSets(fake_left):
                # print("LEFT HAS PASSED")
                right.extend(arr[:-1])
                return fake_left, right
        elif sum(fake_right) == expected_sum == sum(left + arr[:-1]):
            if isEvenSets(fake_right):
                # print("RIGHT HAS PASSED")
                left.extend(arr[:-1])
                return left, fake_right
        else:
            # if sum(fake_left) > expected_sum:
            if sum(fake_left) < expected_sum:
                l, r = part(arr[:-1], expected_sum, fake_left, right)
                if isEvenSets(l):
                    # print("L and R 1 -> ", arr[:-1], "----------", left, " &&& ",right)
                    if l and r and sum(l) == sum(r):
                        return l, r
            if sum(fake_right) < expected_sum:
                l, r = part(arr[:-1], expected_sum, left, fake_right)
                if isEvenSets(l):
                    # print("    L and R 2 -----> ",arr[:-1], "----------", left, " &&& ",right)
                    if l and r and sum(l) == sum(r):
                        return l, r
        return None, None
    else:
        if left and right and sum(left) == sum(right) and isEvenSets(left):
            return left, right
        else:
            return None, None


def sortSubArrays(left, right):
    if min(left) <= min(right):
        return sorted(left), sorted(right)
    elif min(left) > min(right):
        return sorted(right), sorted(left)


def split_array(arr):
    expected_sum = sum(arr) // 2
    left, right = part(arr, expected_sum)
    if left and right and sum(left) == sum(right):
        left, right = sortSubArrays(left, right)
        left.extend(right)
        res = ",".join([str(item) for item in left])
        return res
    else:
        return -1


def ParallelSums(arr):
    return split_array(arr)


arr = [16, 22, 35, 8, 20, 1, 21, 11]
res = ParallelSums(arr)

print(res == "1,11,20,35,8,16,21,22")
