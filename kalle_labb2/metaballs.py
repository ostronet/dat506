import time
import balls
import graph
import numpy as np





def potential(state,x,y):
    return  obj[2] / np.sqrt( (x-obj[0])**2 + (y-obj[1])**2 ) - 5 #detta är en funktion








def show(x1,y1,x2,y2,gridsize,f):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for (x1,y1,x2,y2) in graph.segments(x1,y1,x2,y2,gridsize,f):
        plt.plot([x1, x2], [y1, y2], color="red")
    plt.show()

def f(x,y):
    mass = 1
    y0 = 1
    x0 = 1
    denominator = np.sqrt( (x0-x)**2 + (y0-y)**2 )
    if denominator < 10**(-10):
        denominator = 10**(-10)
    ans = mass / np.sqrt( (x0-x)**2 + (y0-y)**2 ) - 5
    return ans

def g(x,y):
    return x**2+y**2 - 40**2
    
show(-10,10,10,-10,10,f)
