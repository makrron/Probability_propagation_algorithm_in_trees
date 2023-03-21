"""
This module contains the BayesianNetwork class.

A BayesianNetwork class is a class that represents a Bayesian Network. Composed of nodes of type Node.

This class will be able to Initialize the  probability of the Bayesian Network and update the probability by the probability propagation algorithm.
"""
from typing import Any

from node import Node


class BayesianNetwork:
    def __init__(self, nodes: list):
        self.nodes = nodes

    def get_nodes(self) -> list:
        return self.nodes

    def set_nodes(self, nodes: list):
        self.nodes = nodes

    def get_node_by_name(self, name: str) -> Node | None:
        for node in self.nodes:
            if node.get_name() == name:
                return node
        return None

    def __str__(self):
        res = "[\n"
        for Node in self.nodes:
            res += "\t" + Node.__str__() + "\n"
        # Return the list removing the last comma and adding a closing bracket
        return res + "]"
