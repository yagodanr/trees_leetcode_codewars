from queue import Queue


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n



def tree_by_levels(node: Node) -> list:
    l = []

    s =  Queue()
    s.put(node)
    while not s.empty():
        cur = s.get()
        if cur is None:
            continue

        s.put(cur.left)
        s.put(cur.right)
        l.append(cur.value)

    return l