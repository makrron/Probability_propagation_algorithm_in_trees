"""
test file
"""
from bayesian_network import BayesianNetwork
from node import Node

if __name__ == '__main__':

    a = Node("a", {"a0": 0.3, "a1": 0.5, "a2": 0.2}, [], [], 3)
    b = Node("b", {"b0/a0": 0.1, "b0/a1": 0.3, "b0/a2": 0.2}, [], [], 2)
    c = Node("c", {"c0/b0": 0.9, "c0/b1": 0.1}, [], [], 2)
    d = Node("d", {"d0/a0": 0.9, "d0/a1": 0.7, "d0/a2": 0.3}, [], [], 2)

    a.set_parents([])
    a.set_children([b, d])
    b.set_parents([a])
    b.set_children([c])
    c.set_parents([b])
    c.set_children([])
    d.set_parents([a])
    d.set_children([])

    network = BayesianNetwork([a, b, c, d])

    network.initialize_algorithm()

    """
    a = Node("a", {"a0": 0.2, "a1": 0.8}, [], [], 2)
    b = Node("b", {"b0/a0": 0.2, "b0/a1": 0.6}, [], [], 2)
    c = Node("c", {"c0/a0": 0.8, "c0/a1": 0.2, "c1/a0": 0.1, "c1/a1":0.7}, [], [], 2)

    a.set_children([b, c])
    b.set_parents([a])
    c.set_parents([a])
    network = BayesianNetwork([a, b, c])

    # print(network.__str__())

    network.initialize_algorithm()

    
    print(network.get_node_by_name("a").get_lambda_value())
    print(network.get_node_by_name("a").get_lambda_message())

    print(network.get_node_by_name("b").get_lambda_value())
    print(network.get_node_by_name("b").get_lambda_message())

    print(network.get_node_by_name("c").get_lambda_value())
    print(network.get_node_by_name("c").get_lambda_message())

    print(network.get_node_by_name("a").get_pi_value())

    print("ayuda",network.get_node_by_name("a").get_pi_messages())


   print(network.get_node_by_name("d").get_lambda_value())
     print(network.get_node_by_name("d").get_lambda_message())
    """
    print(network.get_node_by_name("b").get_pi_messages())
    print(network.get_node_by_name("d").get_pi_messages())


