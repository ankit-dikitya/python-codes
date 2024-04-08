# Get input from user
arr = list(map(int, input("Enter a list of numbers separated by space: ").split()))

import numpy as np
arr = np.array(arr)
arr = np.unique(arr)
arr = arr.tolist()

# Print the list after removing duplicates
print("List after removing duplicates:", arr)