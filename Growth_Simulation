#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:05:33 2020

@author: dpetrovykh
"""

from Node import Limb
from Sun import Sun
from Tree import Tree
import matplotlib.pyplot as plt

sun = Sun(5, 0)

node_A = Limb(0,0)
node_B = Limb(-1,2)
node_C = Limb(2,1)
node_A.add_child(node_B)
node_A.add_child(node_C)
node_B.gen_child(-0.5,0.5)
node_B.gen_child(0.5,0.5)
node_C.gen_child(-0.5,0.5)
node_C.gen_child(0.5,0.5)

for node in [*node_B.children, *node_C.children]:
    node.gen_leaf(-0.2, 0.2)
    node.gen_leaf(0.2, 0.2)

tree = Tree(node_A)
for tstep in range(0,100):
    tree.update()
    sun.update()
    #plotting
    tree.draw()
    sun.draw()
    plt.xlim(-6,6)
    plt.ylim(0,6)
    plt.title(f"Timestep= {tstep}")
    plt.show()