def loop_function(multi_array_list,index):
  row = 0
  for x in multi_array_list:
    row = row + x[index]
  return row
matrix = [
      [2, 4, 6],
      [9, 5, 7],
      [3, 8, 1]
    ]
index = 1
print(loop_function(matrix,index))
