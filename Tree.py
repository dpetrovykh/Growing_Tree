#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:39:30 2020

@author: dpetrovykh
"""
'''TODO:
    
'''

#import  plotting functions


class NoChildrenError(Exception):
    '''No children present'''
    pass

class Tree:
    def __init__(self, head_node):
        self.head_node = head_node
        
    def DFS():
        #traverses tree in depth first search and yields one node at a time
        #yield node
        pass
    
class Node:
    def __init__(self, x, y, parent= None):
        self.parent = parent
        self.x = x
        self.y = y
        self.children = []
    
    def __repr__(self):
        return f"Node({self.x}, {self.y}, has_parent = {bool(self.parent)})"
    
    def __iter__(self):
        return iter(self.children)
    
    def get_children(self):
        if self.children:
            return self.children
        else:
            raise NoChildrenError
        #return
        
    def add_child(self, x, y):
        child = Node(x, y, self)
        self.children.append(child)
        #return
    
    def depth_first(self):
        yield self
        for child in self:
            yield from child.depth_first()
    
def Visualize_Tree(tree):
    
    pass    