from secrets import compare_digest

my_input = input("Enter your password: ")
password = "password1"

print(compare_digest(my_input, password)) # this is more secure than regular if statement comparsion
