if __name__ == "__main__":
   n, e = map(int, input().split())
   adj = [[] for _ in range(n+1)]
   for _ in range(e):
       f, t = map(int, input().split())
       adj[f].append(t)
       adj[t].append(f)
   for i in range(1, n+1):
       print(f"{i} -> {' '.join(map(str, adj[i]))}")