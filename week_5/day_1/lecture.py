import numpy as np

# array = np.array([1, 2, 3, 4, 5])
# print(array)
# print(type(array))

# double = array * 2
# print(double)

# new_array = array**2
# print(new_array)

# python_list = [1, 2, 3, 4, 5]
# print(python_list)
# print(type(python_list))
# print(python_list * 2)

# array_1d = np.array([1, 2, 3, 4, 5])
# print(array_1d.ndim)  # Output: 1
# print(array_1d.shape)  # Output: (5,)
# print(array_1d.size)  # Output: 5
# print(array_1d.dtype)  # Output: int64


# array_2d = np.array([[3, 6, 8], [5, 10.7, 200]])
# print(array_2d.ndim)
# print(array_2d.shape)
# print(array_2d.size)
# print(array_2d.dtype)

# array_2d = np.array([[3, 6, 8], [5, 10.7, 200], [234, 3465, 29873]])
# print(array_2d.ndim)
# print(array_2d.shape)
# print(array_2d.size)
# print(array_2d.dtype)

# array_2d = np.array([[3, 6, 8], [5, 10.7, 200], [234, 3465, 29873], [1, 2, 3]])
# print(array_2d.ndim)
# print(array_2d.shape)
# print(array_2d.size)
# print(array_2d.dtype)


# array_nd = np.array(
#     [
#         [[[457, 28, 32], [5, 6, 7], [4, 7, 9]]],
#         [[[73, 2458, 232], [5, 6, 7], [4, 7, 9]]],
#         [[[7, 28, 32], [5, 6, 7], [4, 7, 9]]],
#         [[[4, 7, 9], [5, 6, 7], [4, 7, 9]]],
#     ]
# )
# print(array_nd.ndim)  # 4
# print(array_nd.shape)  # (4, 1, 3, 3)
# # Inside of each purple, 4 sets of blue
# # Inside of each blue, 1 set of yellow
# # Inside of each yellow, 3 sets of pink
# # Inside of each pink, 3 values
# print(array_nd.size)  # 4x1x3x3 = 36
# print(array_nd.dtype)  # int64 because we only have integers

# array_empty = np.empty((1, 5, 7))
# print(array_empty)
# print(array_empty.dtype)
# array_int64 = array_empty.astype("int64")
# print(array_int64)
# print(array_int64.dtype)

# array_ex_1d = np.arange(
#     10,
#     21,
# )
# print(array_ex_1d)
# print(f"Ndim:  {array_ex_1d.ndim}")
# print(f"Shape: {array_ex_1d.shape}")
# print(f"Size:  {array_ex_1d.size}")
# print(f"Dtype: {array_ex_1d.dtype}")
# print(f"-------------------------------------")
# array_ex_1d_float = np.arange(21, 10, -0.5, dtype=np.float64)
# # array_ex_1d_float = array_ex_1d_float.astype("float64")
# array_ex_1d_float *= 2
# print(array_ex_1d_float)
# print(f"Ndim:  {array_ex_1d_float.ndim}")
# print(f"Shape: {array_ex_1d_float.shape}")
# print(f"Size:  {array_ex_1d_float.size}")
# print(f"Dtype: {array_ex_1d_float.dtype}")
# print(f"-------------------------------------")

# # python_list = list(range(21, 10, -1))
# # print(python_list)
# print(f"First element is: {array_ex_1d_float[0]}")
# print(f"Eighth element is: {array_ex_1d_float[7]}")
# print(f"4th to 6th element is: {array_ex_1d_float[3:6]}")
# print(
#     f"4th to 10th element, skipping every other element is: {array_ex_1d_float[3:10:2]}"
# )
# print(f"-------------------------------------")
# array_4d = np.array(
#     [
#         [[[457, 28, 32], [5, 6, 7], [4, 7, 9]]],
#         [[[73, 2458, 232], [5, 6, 7], [4, 7, 9]]],
#         [[[7, 28, 32], [5, 6, 7], [4, 7, 9]]],
#         [[[4, 7, 9], [5, 6, 7], [4, 4567, 9]]],
#     ]
# )
# print(f"If Vincent is not crazy, we're gonna get 457: {array_4d[0, 0, 0, 0]}")
# print(f"If Vincent is not crazy, we're gonna get 6: {array_4d[0, 0, 1, 1]}")
# print(f"If Himanish is not crazy, we're gonna get 4567: {array_4d[3, 0, 2, 1]}")
# print(f"If everyone is not crazy, we're slicing: {array_4d[:, :, :, :2]}")

# sequence = np.linspace(0, 100, 17)
# print(sequence)

# sequence = np.linspace(-8, 52, 23)
# print(sequence.ndim)
# print(sequence.shape)
# print(sequence.size)
# print(sequence.dtype)


# random_numbers = np.random.rand(5)  # Between 0(inclusive) and 1(exclusive)
# print(random_numbers)

# # 0 - 1
# # * 9
# # 0 - 9
# # + 10
# # 10 - 19

# random_numbers_10_19 = (
#     np.random.rand(100) * 9
# ) + 10  # Between 10(inclusive) and 19(exclusive)
# print(random_numbers_10_19)

# # Sequence 20 to 30 using arange()
# print(np.arange(20, 31))

# # Sequence 20 to 30 using arange() but only the even numbers
# print(np.arange(20, 31, 2))

# # 40 random int between 1(in) and 10(ex)
# print(np.random.randint(1, 10, 40))

# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(matrix)
# print(matrix.reshape((6, 2)))

random_seq = np.random.randint(1, 10, 20)
print(random_seq)
# reshaped_seq = random_seq.reshape((2, -1, 10))
# print(reshaped_seq)
# print(reshaped_seq.shape)

# print(np.eye(10))
# random_seq = random_seq.reshape(1, -1)
# print(random_seq)
# mean = random_seq.mean(axis=1, keepdims=True)
# print(mean)
# print(random_seq.std())
# print(random_seq.max())
# print(random_seq.min())
# print(np.median(random_seq))
# mean_subtracted = random_seq - mean
# print(mean_subtracted)
# print(f"Square root: {np.sqrt(random_seq)}")
# print(f"Add togther: {random_seq + random_seq}")

# sorted_matrix = random_seq[random_seq.argsort()]
sorted_matrix = np.sort(random_seq)
print(sorted_matrix)

# matrix = np.array([[1, 3, 2], [4, 1, 5], [7, 9, 8], [10, 5, 11]])

# print("Original matrix:")
# print(matrix)
# sorted_matrix = matrix[matrix[:, 1].argsort()]

# print("\nMatrix sorted by second column:")
# print(sorted_matrix)
# random_seq = random_seq.reshape(-1, 2)
# print(random_seq)
# random_seq[[0, 1]] = random_seq[[1, 0]]
# print(random_seq)

# matrix = np.array([[6, 1, 5], [4, 2, 3], [7, 9, 8]])
# print(matrix)
# matrix[[1, 2]] = matrix[[2, 1]]
# print(matrix)


# array = np.array([1, 0, 2, 0, 3, 0, 4, 5])

# # indices = np.nonzero(array)
# indices = np.where(array == 5)[0]

# print(indices)


# array = np.array([0, 2, 2, 6, 5])
# print(array)
# count = np.bincount(array)
# print(count)

# recreated_array = np.repeat(np.arange(len(count)), count)
# same_array = array


# array[1] = 100
# print(array)  # Original
# print(
#     recreated_array
# )  # Clone is a separate array that will not be modified with the original
# print(same_array)  # Copy will be modified with the original
