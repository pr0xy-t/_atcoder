import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [0] * n
        self.rank = [0] * n
        for i in range(n):
            self.parent[i] = i

    def find_root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find_root(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

if __name__ == "__main__":
    uf1 = UnionFind(5)
    uf1.unite(2,3)
    print(*uf1.parent)
    print(*[ uf1.find_root(i) for i in range(5)])

