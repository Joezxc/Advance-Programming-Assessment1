# original array
a = [20,23,82,40,32,15,67,52]

# find the indices of even numbers
even_indices = [i for i, x in enumerate(a) if x % 2 == 0]
print(even_indices)

# sort the array
a.sort()
print(a)

# slice elements from index 3 to the end of the array
slice_from_3 = a[3:]
print(slice_from_3)

# slice elements from index 0 to index 4
slice_from_0_to_4 = a[:5]
print(slice_from_0_to_4)

# print [32 15 67] using negative slicing
slice_negative = a[-7:-4]
print(slice_negative)