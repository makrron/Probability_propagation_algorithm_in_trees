from node import Node


class BayesianNetwork:
    """
    A BayesianNetwork class is a class that represents a Bayesian Network. Composed of nodes of type Node.

    This class will be able to Initialize the  probability of the Bayesian Network and update the probability by the
    probability propagation algorithm.
    """

    def __init__(self, nodes: list):
        self.nodes = nodes

    def get_nodes(self) -> list:
        return self.nodes

    def set_nodes(self, nodes: list):
        self.nodes = nodes

    def get_node_by_name(self, name: str) -> Node:
        for node in self.nodes:
            if node.get_name() == name:
                return node

    def initialize_algorithm(self):
        for node in self.nodes:
            for i in range(node.get_number_states()):
                node.set_lambda_value({node.get_name()+str(i): 1})
                # TODO: Continue with the initialization of the algorithm

    def __str__(self):
        res = "[\n"
        for node in self.nodes:
            res += "\t" + node.__str__() + "\n"
        # Return the list removing the last comma and adding a closing bracket
        return res + "]"
