class Node:
    """
    A node class is a class that represents a node in a graph.
    Each node have a name, a list of children nodes, a list of parents nodes and Object to set de value of the node.
    """

    def __init__(self, name: str, values: dict, parents: list, children: list, number_states: int):
        self.name = name
        self.values = values
        self.parents = parents
        self.children = children
        self.number_states = number_states
        self.lambda_value = {}  # Dict with the values of all lambda value: EX: {a1: 1, a2: 1, a3: 1}
        self.lambda_message = {}  # Dict with the values of all lambda message: EX: {a1: 1, a2: 1, a3: 1}
        self.pi_messages = {}  # Dict with the values of all pi message: EX: {a1: 1, a2: 1, a3: 1}
        self.pi_value = {}  # Dict with the values of all pi value: EX: {a1: 1, a2: 1, a3: 1}

    def get_name(self) -> str:
        return self.name

    def get_values(self) -> dict:
        return self.values

    def get_parents_string(self) -> str:
        if len(self.parents) == 0:
            return "[]"
        else:
            res = "["
            for parent in self.parents:
                res += parent.get_name() + ", "
            # Return the list removing the last comma and adding a closing bracket
            return res[:-2] + "]"

    def get_children_string(self) -> str:
        if len(self.children) == 0:
            return "[]"
        else:
            res = "["
            for child in self.children:
                res += child.get_name() + ", "
            # Return the list removing the last comma and adding a closing bracket
            return res[:-2] + "]"

    def get_parents(self) -> list:
        return self.parents

    def get_children(self) -> list:
        return self.children

    def get_lambda_value(self):
        res = "Lambda Values:[\n"
        for i in range(self.number_states):
            res += "\t" + self.name+str(i) + ": " + str(self.lambda_value.get(self.name + str(i))) + "\n"
        res += "]"
        return res

    def get_lambda_message(self):  # {B(a1): 1, B(a2): 1, B(a3): 1..... | {str(child(parent)): int(value)}
        if len(self.get_parents()) != 0:
            res = "Lambda Message[\n"
            for parent in self.parents:
                for j in range(parent.number_states):
                    res += "\t" + self.name + "(" + parent.get_name() + str(j) + ")" + ": " + \
                           str(self.lambda_message.get(self.name + "(" + parent.get_name() + str(j) + ")")) + "\n"
                res += "]"
            return res
        else:
            return "This node is a root node"

    def get_pi_messages(self):  # TODO: Change this to get the pi message of a specific node
        return self.pi_messages

    def get_pi_value(self):  # TODO: Change this to get the pi value of a specific node
        res = "Pi Values[\n"
        for i in range(self.number_states):
            res += "\t" + self.name + str(i) + ": " + str(self.pi_value.get(self.name + str(i))) + "\n"
        res += "]"
        return res

    def get_number_states(self):
        return self.number_states

    def set_name(self, name: str):
        self.name = name

    def set_values(self, values: dict):
        self.values = values

    def set_parents(self, parents: list):
        self.parents = parents

    def set_children(self, children: list):
        self.children = children

    def set_lambda_value(self, lambda_value):
        self.lambda_value.update(lambda_value)

    def set_lambda_message(self, lambda_message):
        self.lambda_message.update(lambda_message)

    def set_pi_messages(self, pi_messages):
        self.pi_messages.update(pi_messages)

    def set_pi_value(self, pi_value):
        self.pi_value.update(pi_value)

    def __str__(self):
        return "Node: " + self.get_name() + " | Values: " + str(self.get_values()) + " \n\t\tChildren: " + str(
            self.get_children_string()) + " Parents: " + str(self.get_parents_string())
