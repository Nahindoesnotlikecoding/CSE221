class problem_A:
    def __init__(self, inv_count=0):
        self.inv_count = inv_count
    
    def merge(self, arr):
        if len(arr)>1:
            mid = len(arr)//2
            left_arr = arr[:mid]
            right_arr = arr[mid:]

            self.merge(left_arr)
            self.merge(right_arr)

            i=0
            j=0
            k=0

            while i<len(left_arr) and j<len(right_arr):
                if left_arr[i]<right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    self.inv_count += len(left_arr)-i
                    arr[k] = right_arr[j]
                    j += 1
                k += 1
            
            while i<len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
            
            while j<len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
            
        return arr

t = int(input())
arr = list(map(int, input().split(" ")))
fun = problem_A()
res = fun.merge(arr)
print(fun.inv_count)
for i in res:
    print(i, end=" ")