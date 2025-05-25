lst = list(map(int, input("Enter numbers: ").split()))
lst.sort()
n = len(lst)
mid = n // 2

if n % 2 == 0:
    median = (lst[mid - 1] + lst[mid]) / 2
else:
    median = lst[mid]

print("Median is:", median)

