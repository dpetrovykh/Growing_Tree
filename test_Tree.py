#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:27:45 2020

@author: dpetrovykh
"""

from Node import Node
from Tree import Tree

node_A = Node(0,0)
node_B = Node(-1,2)
node_C = Node(2,1)
node_A.add_child(node_B)
node_A.add_child(node_C)
node_B.gen_child(-0.5,0.5)
node_B.gen_child(0.5,0.5)
node_C.gen_child(-0.5,0.5)
node_C.gen_child(0.5,0.5)

tree = Tree(node_A)
tree.update()
tree.visualize()