def problem_E(arr, left, right):
    if left > right:
        return
    
    mid = (left + right) // 2
    print(arr[mid], end=" ")
    problem_E(arr, left, mid - 1)
    problem_E(arr, mid + 1, right)

n = int(input())
arr = list(map(int, input().split()))
problem_E(arr, 0, n - 1)