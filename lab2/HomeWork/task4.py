from BinaryTree import BinaryTree
from Product import Product

if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(Product(1, 12))
    tree.add(Product(2, 13))
    tree.add(Product(3, 14))
    tree.add(Product(4, 15))
    tree.add(Product(5, 16))
    tree.add(Product(6, 17))
    tree.add(Product(7, 18))
    tree.add(Product(8, 19))
    tree.printBinaryTree()

    try:
        print('input CODE and COUNT-> ')
        userArgs = [int(v) for v in input().split()]
        if len(userArgs) != 2:
            raise ValueError('input only 2 digits')
        if not(isinstance(i, int) for i in userArgs):
            raise TypeError('input int')
        price = int(tree.find(userArgs[0]).price)
        print(price * userArgs[1])
    except Exception as ve:
        print(ve)
