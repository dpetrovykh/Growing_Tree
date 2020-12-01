#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:39:30 2020

@author: dpetrovykh
"""
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
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.children = []
    
    def get_children(self):
        if self.children:
            return self.children
        else:
            raise NoChildrenError
        #return
        
    def add_child(self, value):
        child = Node(self, value)
        self.children.append(child)
        #return
    
        