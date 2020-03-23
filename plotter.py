#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt 

file = open('', 'r')

x1 = []
for line in file:
    x1.append(line)

file.close()
y1 = range(1, len(x1))
  
plt.plot(y1, x1)
  
# naming the x axis 
plt.xlabel('Packet Number') 
# naming the y axis 
plt.ylabel('Response Time') 
   
plt.title('For single instance server') 
  
plt.show() 
