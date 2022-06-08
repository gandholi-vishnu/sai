def loop_function(multi_array_list):
  row=0
  for x in range(len(multi_array_list)):
    row +=matrix[x][x]
    row +=matrix[x][-1-x]
  if len(matrix) % 2 != 0:
    u = len(matrix)//2
    f = matrix[u][u]
    row -= f
  return row
matrix=[[2,4,6],
        [9,5,7],
        [3,8,1]
        ]
print(loop_function(matrix))
