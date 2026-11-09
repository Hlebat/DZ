a = [2, 5, 8, 11, 14, 18, 21, 25, 30]
b = 1 # искомое число
left = 0
right = len(a) - 1
result = -1
while left <= right:
    mid = (left + right) // 2
    if a[mid] == b:
        result = mid
        break
    elif a[mid] < b:
        left = mid + 1
    else:
        right = mid - 1
print(result)