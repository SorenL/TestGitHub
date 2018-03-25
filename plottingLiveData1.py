# -*- coding: utf-8 -*-
'''
Created on Fri Feb 09 09:20:36 2018

@author: hwcoop1
'''
import os
#import csv
import numpy as np
#import time
import matplotlib.pyplot as plt
#import matplotlib.backends.backend_pdf
#from emailResults import gmailResults
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

import matplotlib as style
#import msvcrt 
#import py-getch
'''
import msvcrt
import time
import sys
'''
'''
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)
'''
os.chdir('c:\\data\python\laser')
plt.style.use("fivethirtyeight")


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(tt):
    #raw_input('wait a minute')
    graph_data = open('livePlottxt.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1 :
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)
    print(xs, ys )
    
  
ani = animation.FuncAnimation(fig, animate, interval = 2000)
plt.show()




'''
def main():
    try:
        while True:
            ani = animation.FuncAnimation(fig, animate, interval = 1000)
            plt.show()

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

'''


'''
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated=True)
#print(ln,)

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    print(xdata, ydata, ", ")
    
    return ln,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), 
                    init_func=init, blit=True)
plt.show()

'''
