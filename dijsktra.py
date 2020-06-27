import numpy as np
import pandas as pd
import time

MAX = 999
def dijkstra(min_point, visited_locations, distance_matrix, dist):
  visited_locations.append(min_point)
  while len(visited_locations) < len(distance_matrix):
    for next_point, _ in enumerate(distance_matrix[min_point]):
      # 更新和直接相连的点的距离
      dist[next_point] = min(dist[next_point], (dist[min_point] + distance_matrix[min_point][next_point]))

    min_dist = MAX
    for next_point, _ in enumerate(dist):
      # 找直接相连的点里最近的，设为min_point供接下来的递归
      if dist[next_point] < min_dist and next_point not in visited_locations:
        min_dist = dist[next_point]
        min_point = next_point
    dijkstra(min_point, visited_locations, distance_matrix, dist)
  return dist

distance_matrix = [
	[0, 10, 5, MAX, MAX],
	[MAX, 0, 2, 1, MAX],
	[MAX, 3, 0, 9, 2],
	[MAX, MAX, MAX, 0, 4],
	[7, MAX, MAX, 6, 0]]
dist = [MAX for i in range(len(distance_matrix))]
locationA = 0
dist[locationA] = 0
visited_locations = []

start = time.time()
dist = dijkstra(locationA, visited_locations, distance_matrix, dist)
end = time.time()
print (end-start)
print(dist)