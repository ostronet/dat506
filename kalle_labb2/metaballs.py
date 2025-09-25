import time
import balls
import graph
import numpy as np
import sys




def potential(state,x,y):
    summa=0
    for x1,y1,mass in state:
        denominator = np.sqrt( (x-x1)**2 + (y-y1)**2 )
        if denominator < 10**(-10):
            denominator = 10**(-10)
        summa+= mass/denominator
    return summa  #Detta är ett fält med olika värden beroende på hur många bollaR är nära
        




def show(half_size,gridsize,count):
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig, ax = plt.subplots()
    

    
    
    def animate(frame):
        ax.clear()
        ax.set_aspect('equal')
        plt.xlim([-half_size,half_size])
        plt.ylim([-half_size,half_size])

        f = lambda x, y, F=frame: potential(F, x, y) - 5

        artists = []
        
        for (x1,y1,x2,y2) in graph.segments(-half_size,half_size,half_size,-half_size,gridsize,f):
             ln = ax.plot([x1, x2], [y1, y2], color='k', linewidth=2)
             artists.append(ln)
        return artists
                   
    anim = animation.FuncAnimation(fig, animate, balls.balls(half_size,count),
                                   interval=10, blit=False)
    plt.show()


def show_w_gif(half_size,gridsize,count,file_name,frame_count):
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig, ax = plt.subplots()
    

    
    def animate(frame):
        
        ax.clear()
        ax.set_aspect('equal')
        plt.xlim([-half_size,half_size])
        plt.ylim([-half_size,half_size])

        f = lambda x, y, F=frame: potential(F, x, y) - 5

        artists = []
        
        for (x1,y1,x2,y2) in graph.segments(-half_size,half_size,half_size,-half_size,gridsize,f):
             ln = ax.plot([x1, x2], [y1, y2], color='k', linewidth=2)
             artists.append(ln)
        return artists
        
                   
    anim = animation.FuncAnimation(fig, animate, balls.balls(half_size,count),
                                   interval=10, blit=False, save_count=frame_count)
    anim.save(file_name, writer=animation.PillowWriter(fps=60))


def main():
    if "animation.gif" in sys.argv:
        show_w_gif(int(sys.argv[1]), int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5]))
        
        
    else:   
        show(int(sys.argv[1]), int(sys.argv[2]),int(sys.argv[3]))


if "--help" in sys.argv:
    print("arg1 = halfsize arg2 = gridsize arg3 = count")

if __name__ == "__main__":
    main()


