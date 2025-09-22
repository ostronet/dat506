import sys
import graph

def iterate(x,y,n):
    z = 0
    c = x+y*1j
    for i in range(n):
        z = z**2 + c
    return z

def mandelbrot(x1,y1,x2,y2,gridsize,min,max):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    for n in range(min,max+1):
        f = lambda x,y: abs(iterate(x/50,y/50,n))-2
        for (sx1,sy1,sx2,sy2) in graph.segments(x1,y1,x2,y2,gridsize,f):
            c = (n-min+1)/(max-min+1)
            plt.plot([sx1, sx2], [sy1, sy2], color=(c,0,0,c))
    plt.show()

if len(sys.argv) == 3:
    min,max = int(sys.argv[1]),int(sys.argv[2])
    mandelbrot(-100,100,100,-100,1,min,max)
elif len(sys.argv) == 2:
    n = int(sys.argv[1])
    mandelbrot(-100,100,100,-100,1,n,n)
else:
    print("SYNTAX: mandelbrot.py min max")
    print("      | mandelbrot.py n")
