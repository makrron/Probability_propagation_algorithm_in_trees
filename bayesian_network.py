from node import Node


def pi_message_operation(node, child, i):
    pass


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

    def get_root_nodes(self) -> list:
        res = []
        for node in self.nodes:
            if len(node.get_parents()) == 0:
                res.append(node.get_name())
        return res

    def initialize_algorithm(self):
        # SET THE LAMBDA VALUE OF THE NODES
        for node in self.nodes:
            for i in range(node.get_number_states()):
                node.set_lambda_value({node.get_name() + str(i): 1})

        # SET THE LAMBDA MESSAGE OF THE NODES
        root = self.get_root_nodes()
        for node in self.nodes:
            if node.get_name() not in root:  # Initialize the lambda message of the nodes that are not root nodes
                if len(node.get_parents()) != 0:
                    for parent in node.get_parents():
                        # print("parent", parent.get_name())
                        for j in range(parent.get_number_states()):
                            node.set_lambda_message({str(node.get_name() + "(" + parent.get_name() + str(j) + ")"): 1})

        # SET THE PI VALUE OF THE NODES
        for node in self.nodes:
            if node.get_name() in root:
                for i in range(node.get_number_states()):
                    node.set_pi_value({node.get_name() + str(i): node.get_values().get(node.get_name() + str(i))})

        # SEND PI MESSAGE TO THE CHILDREN OF THE ROOT NODES
        for node in self.nodes: # TODO: Finish the initialization of the algorithm
            if node.get_name() in root:
                for child in node.get_children():
                    print(child.get_name())
                    for i in range(node.get_number_states()):
                        print(str(child.get_name() + "(" + node.get_name() + str(i) + ")"))
                        child.set_pi_messages({child.get_name() + "(" + node.get_name() + str(i) + ")":
                                                   pi_message_operation(node, child, i)}) # TODO: Implement this function

    def __str__(self):
        res = "Bayesian Network[\n"
        for node in self.nodes:
            res += "\t" + node.__str__() + "\n"
        return res + "]"
