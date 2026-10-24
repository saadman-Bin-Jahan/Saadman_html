
import numpy as np

arr = np.arange(10)
print("Original Array:", arr)

new_arr = np.where(arr % 2 != 0, -1, arr)
print("Array with odd numbers replaced:", new_arr)
print("Original Array remains unchanged:", arr)

two_d_arr = arr.reshape(2, 5)
print("2D Array with two rows:")
print(two_d_arr)

even_sum = arr[arr % 2 == 0].sum()
print("Sum of all even numbers:", even_sum)
