import time
import balls
import graph
import numpy as np





def potential(state,x,y):
    summa=0
    for x1,y1,mass in state:
        denominator = np.sqrt( (x-x1)**2 + (y-y1)**2 )
        if denominator < 10**(-10):
            denominator = 10**(-10)
        summa+= mass/denominator
    return summa  #Detta är ett fält med olika värden beroende på hur många bollaR är nära
        










def show(half_size,count):
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig, ax = plt.subplots()

    
    gridsize = 1

    
    
    def animate(frame):
        ax.clear()
        ax.set_aspect('equal')
        plt.xlim([-half_size,half_size])
        plt.ylim([-half_size,half_size])

        f = lambda x, y, F=frame: potential(F, x, y) - 1

        artists = []
        
        for (x1,y1,x2,y2) in graph.segments(-half_size,half_size,half_size,-half_size,gridsize,f):
             ln = ax.plot([x1, x2], [y1, y2], color='red', linewidth=2)
             artists.append(ln)
        return artists
                        
    anim = animation.FuncAnimation(fig, animate, balls.balls(half_size,count),
                                   interval=10, blit=False)
    plt.show()

show(10,4)


