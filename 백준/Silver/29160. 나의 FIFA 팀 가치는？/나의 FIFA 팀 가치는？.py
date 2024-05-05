import sys, heapq
t = sys.stdin.readline
N, K = map(int, t().strip().split())
players = {x:[] for x in range(1,12)}
for _ in range(N) : 
	p, s = map(int, t().strip().split())
	heapq.heappush(players[p], -s)

choice = [0]*12
for year in range(K) : 
	for x in range(1,12) :
		if players[x] : 
			tmp = min(0, heapq.heappop(players[x]) + 1)
			heapq.heappush(players[x], tmp)
			choice[x] = players[x][0]
	
print(-sum(choice))