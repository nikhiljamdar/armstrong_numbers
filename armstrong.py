num = int(input("Enter number : "))
sum = 0
temp = num
count = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** count
    temp //= 10

if num == sum:
    print(f"number {num} armstrong number")

else :
    print(f"number {num} not armstrong number")
