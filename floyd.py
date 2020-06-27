import numpy as np
import pandas as pd
import time
def fastestRoute(fromm, to, locationA, locationB):
  all_locations = set(fromm + to)
  n_locations = max(all_locations) + 1
  #print(n_locations)
  distance_matrix = 9999999 * pd.DataFrame(np.ones((n_locations, n_locations))- np.eye(n_locations))
  for x, y in zip(fromm, to):
    distance_matrix.iloc[x,y] = 1
    distance_matrix.iloc[y,x] = 1
  print(distance_matrix)

  # 求任意两点间的最短路径
  for k in range(n_locations):
    for i in range(n_locations):
        for j in range(n_locations):
            if distance_matrix[i][j] > distance_matrix[i][k]+distance_matrix[k][j]:
                distance_matrix[i][j] = distance_matrix[i][k]+distance_matrix[k][j]

  print(distance_matrix)
  return distance_matrix[locationA][locationB]

start = time.time()
#step = fastestRoute([0,0,1], [1,2,3], 2, 3)
#step = fastestRoute([0,1], [2,3], 0, 1)
step = fastestRoute([0,0,1,1,2,3,6], [1,2,4,5,3,5,7], 4, 7) #-1
#step = fastestRoute([0,0,1,1,2,3,6], [1,2,4,5,3,5,7], 2, 5) #2
#step = fastestRoute([5,5,1,1,2,3,6,5], [1,2,4,0,3,0,7,7], 6, 0) #4
#step = fastestRoute([6,5,10,12,1,10,8,9,5,12,10,2,11,3,9,4,11,7,8,12], [3,3,0,1,9,1,7,11,11,1,0,4,3,5,7,8,0,11,12,1], 2,6) #6
print('step:', step)
end = time.time()
print (end-start)