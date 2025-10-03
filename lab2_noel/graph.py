import sys

form='circle'
def f(x,y):
	if form=='circle':
		return x*x+y*y-40**2
	if form=='line':
		return x-y
	if form=='lemniscate':
		return (x*x+y*y)**2 - 40**2 * (x*x-y*y)
	if form=='cardioid':
		return (x*x + y*y)**2 + 40*x*(x*x + y*y) - 400*y*y

def cells(x1,y1,x2,y2,gridsize):
	x=x1 
	while x+gridsize<=x2:
		y=y2 
		while y+gridsize<=y1:
			yield (x,y,x+gridsize,y+gridsize)
			y+=gridsize
		x+=gridsize 
	
def get_case(f,c):
	max_v = f(c[0], c[3]) < 0 
	max_h = f(c[2], c[3]) < 0  
	min_h = f(c[2], c[1]) < 0  
	min_v = f(c[0], c[1]) < 0 
	
	return (8 if max_v else 0) | (4 if max_h else 0) | (2 if min_h else 0) |(1 if min_v else 0)	
	
    
	"""cases={
	0:(False, False, False, False),
	1:(False, False, False, True),
	2:(False, False, True, False),
	3:(False, False, True, True),
	4:(False, True, False, False),
	5:(False, True, False, True),
	6:(False, True, True, False),
	7:(False, True, True, True),
	8:(True, False, False, False),
	9:(True, False, False, True),
	10:(True, False, True, False),
	11:(True, False, True, True),
	12:(True, True, False, False),
	13:(True, True, False, True),
	14:(True, True, True, False),
	15:(True, True, True, True)
	}	"""
	
def interpolate(x1,y1,x2,y2,f):
	f1=f(x1,y1)
	f2=f(x2,y2)
	
	x=x1-(f1/(f2-f1))*(x2-x1)
	y=y1-(f1/(f2-f1))*(y2-y1)
	return (x,y)

table = [
  [],
  [(0,3,0,1,2,1,0,1)],
  [(0,1,2,1,2,3,2,1)],
  [(0,3,0,1,2,3,2,1)],
  [(0,3,2,3,2,1,2,3)],
  [(0,3,0,1,0,3,2,3),(0,3,0,1,0,3,2,3)],
  [(0,1,2,1,0,3,2,3)],
  [(0,3,0,1,0,3,2,3)],
  [(0,1,0,3,2,3,0,3)],
  [(2,1,0,1,2,3,0,3)],
  [(0,1,0,3,0,1,2,1),(2,3,0,3,2,3,2,1)],
  [(2,3,0,3,2,3,2,1)],
  [(0,1,0,3,2,1,2,3)],
  [(2,1,0,1,2,1,2,3)],
  [(0,1,0,3,0,1,2,1)],
  []
]

def segments(x1, y1, x2, y2, gridsize, f):
    for c in cells(x1, y1, x2, y2, gridsize):
        case = get_case(f, c)
        for i in table[case]:
            x_1 = c[i[0]]
            x_2 = c[i[2]]
            y_1 = c[i[1]]
            y_2 = c[i[3]]

            x_3 = c[i[4]]
            x_4 = c[i[6]]
            y_3 = c[i[5]]
            y_4 = c[i[7]]
            
            p = interpolate(x_1, y_1, x_2, y_2, f)
            q = interpolate(x_3, y_3, x_4, y_4, f)
            yield (p, q)
		
		
def show(x1,y1,x2,y2,gridsize,f):
  import matplotlib.pyplot as plt

  fig, ax = plt.subplots()
  ax.set_aspect('equal')

  for (p,q) in segments(x1,y1,x2,y2,gridsize,f):
  	(xa,ya)=p
  	(xb,yb)=q
  	plt.plot([xa, xb], [ya, yb], color="red")
  	
  ax.set_xlim(x1, x2)
  ax.set_ylim(y2, y1)
  
  plt.show()

if __name__ == "__main__":
	
	form=sys.argv[1]
	show(-100,100,100,-100,1,f)
	

       
    
					
	
		