# find the subsets of an array that will give a minimum distance

def minimum_partition(arr, n, sum_calculated, sum_total):

    if n == 0:
        return abs((sum_total-sum_calculated) - sum_calculated)

    return min(minimum_partition(arr, n - 1, sum_calculated + arr[n - 1], sum_total),
               minimum_partition(arr, n - 1, sum_calculated, sum_total))

arr = [1, 6, 11]
sum_total = sum(arr)

print minimum_partition(arr, len(arr), 0.0, sum_total)
