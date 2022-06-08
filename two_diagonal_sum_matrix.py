def loop_function(multi_array_list):
  row=0
  for x in range(len(multi_array_list)):
    for i in range(len(multi_array_list[x])):
      if x == i:
        row = row + multi_array_list[x][i]
        break
  sum=0
  for j in range(len(matrix)):
    sum +=matrix[j][-1-j]
    if len(matrix) % 2 != 0:
      u = len(matrix)//2
      f = matrix[u][u]
      sum1=sum - f
    else:
      row + sum1
  return row + sum1
matrix=[[2,4,6],
        [9,5,7],
        [3,8,1]
        ]
print(loop_function(matrix))
print(2+5+1+6+3)
