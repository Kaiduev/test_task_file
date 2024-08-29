"""
Test Python

Write a function that builds a tree based on a list of tuples of id (parent id, offspring id),
where None is the id of the root node.
How this should work:

Написать функцию, строящую дерево по списку пар id (id родителя, id потомка),
где None - id корневого узла.
Пример работы:

"""

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {
    'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
    'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
    'c': {'c1': {}},
}

def to_tree(source):
    tree = {}
    nodes = {}

    for parent, child in source:
        nodes[child] = nodes.get(child, {})
        if parent is None:
            tree[child] = nodes[child]
        else:
            nodes[parent] = nodes.get(parent, {})
            nodes[parent][child] = nodes[child]
    
    return tree

assert to_tree(source) == expected


