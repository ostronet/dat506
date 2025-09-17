import sys
from random import random

def trajectory(x,y,dx,dy,mass,half_size):
	
	while True:
		
		if x>half_size or x<-half_size:
			dx=-dx
		if y>half_size or y<-half_size:
			dy=-dy
		
		x=x+dx
		y=y+dy

		yield (x,y,mass)
		
def balls(half_size, N):
		
	trajectories=[]
	
	for i in range(N):
		x=(2*random()-1)*half_size
		y=(2*random()-1)*half_size
		dx=(2 * random() - 1)
		dy=(2 * random() - 1)
		mass=1
		
		trajectories.append(trajectory(x,y,dx,dy,mass,half_size))
		
	for ball in zip(*trajectories):
		yield ball
		
		
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
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python balls.py <half_size> <N>")
        sys.exit(1)

    half_size = float(sys.argv[1])   
    N = int(sys.argv[2]) 
    show(half_size,N)            

			
	