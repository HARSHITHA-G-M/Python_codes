lst = [int(x) for x in input("Enter numbers: ").split()]
if lst == sorted(lst):
    print("List is sorted")
else:
    print("List is not sorted")

