#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:59:47 2020

@author: dpetrovykh
"""

class NoChildrenError(Exception):
    '''No children present'''
    pass

class Node:
    def __init__(self, dx, dy, parent= None, x=None, y=None):
        self.parent = parent
        self.dx = dx
        self.dy = dy
        self.children = []
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Node({self.dx}, {self.dy}, has_parent = {bool(self.parent)})"
    
    def __iter__(self):
        return iter(self.children)
    
    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent):
        self.parent = parent
    
    def get_children(self):
        if self.children:
            return self.children
        else:
            raise NoChildrenError
        #return
        
    def gen_child(self, dx, dy):
        child = Node(dx, dy, self)
        self.children.append(child)
        #return
    
    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.set_parent(self)
        
    def update_x_y(self):
        if self.parent:
            self.x = self.parent.x + self.dx
            self.y = self.parent.y + self.dy
        else:
            self.x = self.dx
            self.y = self.dy
            
    def depth_first(self):
        yield self
        for child in self:
            yield from child.depth_first()