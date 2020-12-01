#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:39:30 2020

@author: dpetrovykh
"""
'''TODO:
    
'''

import matplotlib.pyplot as plt



class Tree:
    def __init__(self, root_node):
        self.root = root_node
    
    def update(self):
        root = self.root
        for node in root.depth_first():
            node.update_x_y()
    
    def visualize(self):
        ax = plt.axes()
        #starting at head, look through each node
        root = self.root
        for node in root.depth_first():
            #plot node location
            plt.plot(node.x, node.y, 'ro')
            #plot connection to node from parent
            parent = node.get_parent()
            if parent != None:
                ax.arrow(parent.x, parent.y, node.dx, node.dy, head_width=0.1)
        plt.xlim(-5,5)
        plt.ylim(0,5)
        plt.show()