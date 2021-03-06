class Node:
    def __init__(self, key):
        self.key = key
        self.pre = []
        self.succ = []

def LCAdag(root, n1, n2):
    if root is None:
        return None

    if (root.key == n1.key or root.key == n2.key):
        return root.key

    if n1.key == n2.key:
        return n1.key
    lca = []
    for i in range(len(n1.pre)):
        for j in range(len(n2.pre)):
            if (n1.pre[i].key == n2.pre[j].key):
                lca.append(n1.pre[i].key)

if (lca == []):
        if (n1.key > n2.key):lca.append(LCAdag(root, n1.pre[0], n2))
        else:lca.append(LCAdag(root, n1, n2.pre[0]))
    return max (lca) 