numbers = []
for i in range(5):
    number = int(input("Enter a number"))
    numbers.append(number)

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("the smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("the average is", sum(numbers)/float(len(numbers)))
# Jan crooks has been here
