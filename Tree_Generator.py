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
import matplotlib.pyplot as plt


def fan_angles(n, theta_bound, ref= math.pi/2):
    #Returns a list of angles which correspond to a an evenly-spaced fan of n lines within angle theta_bound, centered around ref
    assert isinstance(n, int)
    if n==0:
        return []
    elif n== 1:
        return [ref]
    else:
        return [ref + theta_bound/2 - (theta_bound/(n-1))*i for i in range(n)]
        

def Tree_Generator(limb_children, limb_lengths, leaf_children, leaf_spacing, sep_angle):
    root = Limb(0,0)
    layers = len(limb_children)
    old_limbs = [root]
    #for each layer:
    for i in range(layers):
        n_limbs = limb_children[i]
        l_limbs = limb_lengths[i]
        n_leafs = leaf_children[i]
        theta_bound = sep_angle[i]
        #create empty list of nodes in next layer
        new_limbs = []
        #for each node in old node list:
        for limb in old_limbs:
            #calculate child angles
            child_angles = fan_angles(n_limbs, theta_bound)
            #generate limbs
            for angle in child_angles:
                dx = l_limbs*math.cos(angle)
                dy = l_limbs*math.sin(angle)
                child = Limb(dx, dy)
                #link child to parent
                limb.add_child(child)
                #save limbs to new limb list
                new_limbs.append(child)
            #generate leaf angles
            leaf_angles = fan_angles(n_leafs, theta_bound)
            for angle in leaf_angles:
                dx = l_limbs*math.cos(angle)
                dy = l_limbs*math.sin(angle)
                child = Leaf(dx, dy)
                #link child to parent
                limb.add_child(child)
                #do not copy leaf to limb list
        #all limbs generated for next level
        old_limbs = list(new_limbs)
    return Tree(root)

if __name__ == "__main__":
    limb_children = (3,2,2,0)
    limb_lengths = (4,2,1,1)
    leaf_children = (0,0,0,5)
    leaf_spacing = 0.5
    sep_angle = [math.radians(deg) for deg in (70, 45, 45, 45)]
    tree = Tree_Generator(limb_children, limb_lengths, leaf_children, leaf_spacing, sep_angle)
    tree.update()
    tree.draw()
    plt.show()
    