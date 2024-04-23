numbers = input("Enter numbers: ")
numbers_list = [float(num) for num in numbers.split(",")]
max_number = max(numbers_list)
print("The maximum number is:", max_number)