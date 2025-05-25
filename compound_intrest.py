p = float(input("Principal amount: "))
r = float(input("Rate of interest (%): "))
t = float(input("Time (years): "))
n = float(input("Number of times interest applied per year: "))
ci = p * (1 + r/(100*n))**(n*t) - p
print("Compound Interest:", ci)

