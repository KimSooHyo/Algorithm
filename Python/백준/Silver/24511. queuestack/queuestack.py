import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue = deque([])
for i in range(N):
    if A[i] == 0:
        queue.append(B[i])
        
for i in range(M):
    queue.appendleft(C[i])
    print(queue.pop(), end=' ')