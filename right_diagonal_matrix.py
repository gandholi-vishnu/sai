matrix=[[2,4,6],
        [9,4,7],
        [7,6,3]
       ]
sum=0
for j in range(len(matrix)):
  sum +=matrix[j][-1-j]
print(sum)
