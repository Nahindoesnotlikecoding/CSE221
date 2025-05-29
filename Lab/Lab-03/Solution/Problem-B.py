def maximum_subarray(arr, left, right):
    max_sum = 0
    i = left
    j = 1
    while j<right+1:
        sum = arr[i]+(arr[j]**2)
        max_sum = max(sum, max_sum)
        if arr[i]<arr[j]:
            i = j
        j += 1
    return max_sum


def problem_B(t, arr, left, right):
    if left==right:
        return arr[left]
    else:
        mid = (left+right)//2

        left_arr = problem_B(t, arr, left, mid)
        right_arr = problem_B(t, arr, mid+1, right)
        max_sum_arr = maximum_subarray(arr, left, right)
        return max(left_arr, right_arr, max_sum_arr)


t = int(input())
arr = list(map(int, input().split(" ")))
res = problem_B(t, arr, 0, len(arr)-1)
print(res)