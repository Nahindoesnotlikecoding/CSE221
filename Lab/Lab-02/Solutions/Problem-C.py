def problem_C():
    inp = list(map(int, input().split(" ")))
    n, k = inp[0], inp[1]
    arr = list(map(int, input().split(" ")))
    i = 0
    j = 0
    cur_sum = arr[0]
    max_length = 0
    cur_length = 1
    while i<len(arr) or j<len(arr):
        if cur_sum <= k:
            j += 1
            if j>=len(arr):
                max_length = max(cur_length, max_length)
                break
            else:
                cur_sum += arr[j]
                max_length = max(cur_length, max_length)
                cur_length += 1
        else:
            cur_length -= 1
            cur_sum -= arr[i]
            i += 1
        
        
    
    print(max_length)

problem_C()
    