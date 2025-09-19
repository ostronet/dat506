import time 
import random as rm
import sys




def trajectory(x,y,dx,dy,halfsize,mass=None):
    yield x,y
    while True:
        x += dx
        y += dy
        yield x,y
    
        if x >= halfsize or x <= -halfsize: 
            dx = -dx
        if y >= halfsize or y <= -halfsize:
            dy = -dy
    
def prep_trajectories(halfsize,N):

    speed = 1
    
    trajs = []
    for n in range(N):
        trajs.append(trajectory(rm.random()*10, rm.random()*10, rm.random()*speed, rm.random()*speed, halfsize))
                                #x          y                      dx          dy

    return trajs


def balls(halfsize,N):
    trajectories = zip(*prep_trajectories(halfsize,N))
    return trajectories


def show(half_size,count):
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig, ax = plt.subplots()

    def animate(coords):
        ax.clear()
        ax.set_aspect('equal')
        plt.xlim([-half_size,half_size])
        plt.ylim([-half_size,half_size])

        dots = []
        for coord in coords:
            dot, = ax.plot([coord[0]], [coord[1]], marker="o")
            dots.append(dot)
        return dots

    anim = animation.FuncAnimation(fig, animate, balls(half_size,count),
                                   interval=10, blit=True)
    plt.show()




if "--help" in sys.argv:
    print("arg1: halfsize \n arg2: ball count")
    sys.exit(0)

    
if __name__ == "__main__":

    show(half_size=int(sys.argv[1]), count=int(sys.argv[2]))
