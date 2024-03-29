# -*- coding: utf-8 -*-
"""BOJ_1012.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FqCJLiioRYKHxsChXtdtBH-J7hExwagY
"""

from collections import deque

def bfs(x, y, graph, r_size, f_size):

  graph[x][y] = 0
  queue = deque([(x, y)])
  while queue:
    x, y = queue.popleft()

    if x > 0:
      if graph[x-1][y] == 1:
        queue.append((x-1, y))
        graph[x-1][y] = 0
    if y < f_size - 1:
      if graph[x][y+1] == 1:
        queue.append((x, y+1))
        graph[x][y+1] = 0
    if x < r_size - 1:
      if graph[x+1][y] == 1:
        queue.append((x+1, y))
        graph[x+1][y] = 0
    if y > 0:
      if graph[x][y-1] == 1:
        queue.append((x, y-1))
        graph[x][y-1] = 0

# dfs는 런타임에러(recurrsion에러)나서 bfs로 함.
def dfs(x, y, graph, r_size, f_size):
  graph[x][y] = 0
  if x > 0:
    if graph[x-1][y] == 1:
      dfs(x-1, y, graph, r_size, f_size)
  if y < f_size - 1:
    if graph[x][y+1] == 1:
      dfs(x, y+1, graph, r_size, f_size)
  if x < r_size - 1:
    if graph[x+1][y] == 1:
      dfs(x+1, y, graph, r_size, f_size)
  if y > 0:
    if graph[x][y-1] == 1:
      dfs(x, y-1, graph, r_size, f_size)

if __name__ == '__main__':
  test_num = int(input())

  for _ in range(test_num):
    r_size, f_size, l_num = map(int, input().split())

    graph = []
    l_list = []
    for _ in range(r_size):
      graph.append([0] * f_size)

    for _ in range(l_num):
      x, y = map(int, input().split())
      graph[x][y] = 1
      l_list.append((x, y))

    worm_cnt = 0

    for x, y in l_list:
      if graph[x][y] == 1:
        worm_cnt += 1
        bfs(x, y, graph, r_size, f_size)
    print(worm_cnt)