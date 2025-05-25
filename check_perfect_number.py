num = int(input("Enter a number: "))
sum_div = sum(i for i in range(1, num) if num % i == 0)
if sum_div == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")

