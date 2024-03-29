# -*- coding: utf-8 -*-
"""BOJ_1260.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fgmVSoz5C1wLucN7nLnzjAxW8M97SpfW
"""

from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)

def dfs(graph, start, visited):
  visited[start] = True
  print(start, end=' ')
  for i in graph[start]:
    if not visited[i]:
      dfs(graph, i, visited)

if __name__ == '__main__':
  N, M, V = map(int, input().split())
  graph = [[] for _ in range(N+1)]
  # 정점 번호와 인덱스를 맞추기 위해 N+1로 함. 인덱스0은 비우려고.

  # 그래프 만들기 (배열표현-파이썬리스트)
  for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  for i in graph: # 각 정점의 배열을 정렬(번호순서대로 접근할수있도록)
    i.sort()

  # dfs
  visited = [False] * (N +1)
  dfs(graph, V, visited)     # 연결된그래프라고 가정한다.

  print() # dfs 후 bfs를 출력할 것이므로 줄바꿈되도록

  # bfs
  visited_2 = [False] * (N +1)
  bfs(graph, V, visited_2)   # 연결된그래프라고 가정한다.