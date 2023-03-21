"""
test file
"""
from bayesian_network import BayesianNetwork
from node import Node

if __name__ == '__main__':
    a = Node("a", {"a1": 0.3, "a2": 0.5, "a3": 0.2}, [], [])
    b = Node("b", {"b1/a1": 0.1, "b1/a2": 0.3, "b1/a3": 0.2}, [], [])
    c = Node("c", {"c1/b1": 0.9, "c1/b2": 0.1}, [], [])
    d = Node("d", {"d1/a1": 0.9, "d1/a2": 0.7, "d1/a3": 0.3}, [], [])

    a.set_parents([])
    a.set_children([b, d])
    b.set_parents([a])
    b.set_children([c])
    c.set_parents([b])
    c.set_children([])
    d.set_parents([a])
    d.set_children([])

    network = BayesianNetwork([a, b, c, d])

    print(network.__str__())



