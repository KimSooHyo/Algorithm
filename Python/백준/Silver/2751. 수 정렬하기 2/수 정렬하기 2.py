import sys
input = sys.stdin.readline

n = int(input())
num_list = []
for _ in range(n):
    num = int(input())
    num_list.append(num)
    
num_list.sort()
for n in num_list:
    print(n)