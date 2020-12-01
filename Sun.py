#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:05:51 2020

@author: dpetrovykh
"""
import math
import matplotlib.pyplot as plt

class Sun:
    def __init__(self, R, theta, s= 300, speed = 0.01):
        self.R = R  #radius of sun's trajectory
        self.theta = theta #[rad] Angular position of sun. CCW from <1,0>
        self.s = s #size of sun
        self.speed = speed #[rad/step] rotational speed of sun
    
    @property
    def x(self):
        return self.R*math.cos(self.theta)
        
    @property
    def y(self):
        return self.R*math.sin(self.theta)
        
    @property
    def pos(self):
        return (float(self.x), float(self.y))
    
    def inc_theta(self):
        self.theta += self.speed
    
    def update(self):
        self.inc_theta()
    
    def draw(self):
        plt.scatter(self.x, self.y, s= self.s, color= "yellow")
    