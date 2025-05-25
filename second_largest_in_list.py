lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique_lst = list(set(lst))
unique_lst.sort()
print("Second largest number is", unique_lst[-2])

