
# Sum of even numbers should be divisible by 8 within a given range
# Given a range, find the sum of all even numbers in it.
# Examples:
# Input : 2 4
# Output : 6
# Explanation : 2 + 4 = 6
def sum_of_even_numbers_divisible_by_8(start, end):
    sum = 0
    for i in range(start, end+1):
        if i % 2 == 0 and i % 8 == 0:
            sum += i
    return sum

start_range = int(input("Enter the start range: "))
end_range = int(input("Enter the end range: "))

result = sum_of_even_numbers_divisible_by_8(start_range, end_range)
print("The sum of even numbers divisible by 8 is",result)



