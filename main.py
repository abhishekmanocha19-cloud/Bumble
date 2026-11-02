# Write your reference solution here
n=int(input("enter num: "))

s = 0
i = 1

if n == 0:
    print("Sum: 0")
    print("Average: 0.00")

while i<=n:
    s = s + i
    i = i + 1
avg = round(s/n,2)

print("Sum:",s)
print("Average:", avg)