lst = list(map(int, input("Enter numbers from 1 to n with one missing: ").split()))
n = len(lst) + 1
total = n * (n + 1) // 2
print("Missing number is", total - sum(lst))

