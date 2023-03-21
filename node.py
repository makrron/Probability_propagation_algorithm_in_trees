"""
This module contains the Node class.

A node class is a class that represents a node in a graph.
Each node have a name, a list of children nodes, a list of parents nodes and Object to set de value of the node.
"""


class Node:
    def __init__(self, name: str, values: dict, parents: list, children: list):
        self.name = name
        self.values = values
        self.parents = parents
        self.children = children
        self.lambda_value = None
        self.lambda_message = None
        self.pi_messages = None
        self.pi_value = None

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
        return self.lambda_value

    def get_lambda_message(self):
        return self.lambda_message

    def get_pi_messages(self):
        return self.pi_messages

    def get_pi_value(self):
        return self.pi_value

    def set_name(self, name: str):
        self.name = name

    def set_values(self, values: dict):
        self.values = values

    def set_parents(self, parents: list):
        self.parents = parents

    def set_children(self, children: list):
        self.children = children

    def set_lambda_value(self, lambda_value):
        self.lambda_value = lambda_value

    def set_lambda_message(self, lambda_message):
        self.lambda_message = lambda_message

    def set_pi_messages(self, pi_messages):
        self.pi_messages = pi_messages

    def set_pi_value(self, pi_value):
        self.pi_value = pi_value





    def __str__(self):
        return "Node: " + self.get_name() + " Value: " + str(self.get_values()) + " Children: " + str(
            self.get_parents_string()) + " Parents: " + str(self.get_children_string())

