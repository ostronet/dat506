import balls
import graph
import math
import random

def balls(N):
	state=[]
	
	for i in range(N):
		xi=random.uniform(-1,1)
		yi=random.uniform(-1,1)
		mi=random.uniform(0.5,1)	
		
		state.append((xi,yi,mi))
	return tuple(state)
	

def potential(state,x,y):
	
	p=0
	for i in state:
		d=(math.sqrt((x-xi)**2 + (y-yi)**2))
		if d<1e-25:
			d = 1e-25
		p+=mi/d
		
	return p

def show(half_size,count):
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    fig, ax = plt.subplots()

    def animate(state):
    	ax.clear()
    	ax.set_aspect('equal')
    	plt.xlim([-half_size,half_size])
    	plt.ylim([-half_size,half_size])
    	
    	def f(x,y):
    		f=potential(state,x,y)-5
    		return f
    		
    	state = []
    	for i in state:
    		p,= ax.plot([coord[0]], [coord[1]], marker="o")
    		state.append(p)
    	return state

	anim = animation.FuncAnimation(fig, animate, balls(half_size,count), 
	interval=10, blit=True)
    #anim.save(file_name, writer=animation.PillowWriter(fps=60))
    
	plt.show()

	
	
	
