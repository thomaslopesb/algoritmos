from binary_tree import Binary

if __name__ == '__main__':
    tree = Binary()
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    tree.pre_order(tree.root)
    print('')
    tree.post_order(tree.root)
    print('')
    tree.in_order(tree.root)

    tree.remove(tree.root, 3)

    print('')
    tree.pre_order(tree.root)
    print('')
    tree.post_order(tree.root)
    print('')
    tree.in_order(tree.root)
