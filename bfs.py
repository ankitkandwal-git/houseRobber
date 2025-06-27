from collections import deque

def bfs(n, adj):
    q = deque([0])
    visited = [False] * n
    visited[0] = True
    ans = []
    
    while q:
        cur = q.popleft()
        ans.append(cur)
        for k in adj[cur]:
            if not visited[k]:
                q.append(k)
                visited[k] = True
    return ans

"""
if __name__ == "__main__":
    n, e = map(int, input().split())  
    adj = [[] for _ in range(n)]  

    for _ in range(e):
        f, t = map(int, input().split())
        adj[f].append(t)
        adj[t].append(f)
    result = bfs(n, adj)
    print(' '.join(map(str, result)))
"""