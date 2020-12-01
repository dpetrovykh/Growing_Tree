#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:02:10 2020

@author: dpetrovykh
"""
import math
from Tree import Tree
from Node import Limb
from Node import Leaf


def Tree_Generator():
    root = Limb(0,0)
    layers = len(limb_children)
    old_nodes = [root]
    #for each layer:
    for i in range(layers):
        #create empty list of nodes in next layer
        new_nodes = []
        #for each node in old node list:
        for node in old_nodes:
            #generate limbs
            #add limbs to parent node
            #add limbs to list of new nodes
            #generate leaves
        #

if __name__ = "__main__":
    limb_children = (2,2,2,0)
    limb_lengths = (4,2,1,1)
    leaf_children = (0,0,0,5)
    leaf_spacing = 0.5
    sep_angle = math.radians(45)
    tree = Tree_Generator(limb_children, limb_lengths, leaf_children, leaf_spacing, sep_angle)