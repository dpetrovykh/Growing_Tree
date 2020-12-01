#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 10:00:58 2020

@author: dpetrovykh
"""

from Node import Node

root = Node(1,1)
root.gen_child(1,2)
root.gen_child(2,1)
for node in root.depth_first():
    print(node)
