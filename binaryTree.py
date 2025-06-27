class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def main():
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

if __name__ == "__main__":
    main()