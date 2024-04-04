# import re

# # Example string containing a path
# example_string = "This is a path/to/some/repo.git/ and another/path/to/another/repo.git/"

# # Regular expression pattern to match .git/
# pattern = r"\.git\/"

# # Find all occurrences of .git/
# matches = re.findall(pattern, example_string)

# # Print the results
# if matches:
#     print(f"Found {len(matches)} occurrences of '.git/' in the string.")
#     for match in matches:
#         print(match)
# else:
#     print("No occurrences of '.git/' found.")

import re

# Example string containing paths
example_string = "This is a path/to/some/repo.git/ and another/path/to/another/repo.git/"

# Regular expression pattern to match .git/ at the beginning
pattern = r"^(.*?)/\.git/"

# Find the start of the match
match = re.search(pattern, example_string)
print(match)

if match:
    start_position = match.start()
    print(f"Start position of '.git/' in the string: {start_position}")
else:
    print("No match found for '.git/' at the beginning of the string.")

