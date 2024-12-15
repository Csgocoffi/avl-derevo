class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1  # Высота узла

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Выполняем ротацию
        x.right = y
        y.left = T2
        
        # Обновляем высоты
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Выполняем ротацию
        y.left = x
        x.right = T2

        # Обновляем высоты
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, node, key):
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Обновляем высоту узла
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Получаем баланс
        balance = self.get_balance(node)

        # Выполняем ротации
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def pre_order(self, node):
        if node is not None:
            print("{0} ".format(node.key), end="")
            self.pre_order(node.left)
            self.pre_order(node.right)

# Пример использования
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = tree.insert(root, key)

    print("obhod avl dereva")
    tree.pre_order(root)
