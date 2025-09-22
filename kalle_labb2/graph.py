import sys

                #1 = x^2 + y^2

def cells(x1,y1,x2,y2,gridsize):        #x1 är lägsta x, längst till vänster, y1 är högsta y, längst upp
    xc1 = x1
    xc2 = x1 + gridsize
    yc1 = y2 + gridsize
    yc2 = y2

    while xc2 <= x2 and yc1 <= y1:
        yield (xc1,yc1,xc2,yc2)
        yc1 += gridsize
        yc2 += gridsize
        if yc1 == y1:
            yield (xc1,yc1,xc2,yc2)
            yc1 = y2 + gridsize
            yc2 = y2
            xc1 += gridsize
            xc2 += gridsize
            
        
def get_case(f,c):
    bool_tuple = (f(c[0],c[3]) < 0,f(c[2],c[3]) < 0,f(c[2],c[1]) < 0,f(c[0],c[1]) < 0)
    """
    binary = bool_tuple*1
    decimal = binary[0]*8*binary[1]*4+binary[2]*2+binary[3]
    print(decimal)
    return decimal """
    
    bool_cases = {
                0:(False,False,False,False),
                1:(False,False,False,True),
                2:(False,False,True,False),
                3:(False,False,True,True),
                4:(False,True,False,False),
                5:(False,True,False,True),
                6:(False,True,True,False),
                7:(False,True,True,True),
                8:(True,False,False,False),
                9:(True,False,False,True),
                10:(True,False,True,False),
                11:(True,False,True,True),
                12:(True,True,False,False),
                13:(True,True,False,True),
                14:(True,True,True,False),
                15:(True,True,True,True),
                }

    Case = next(k for k, v in bool_cases.items() if v == bool_tuple)
    return Case

def interpolate(x1,y1,x2,y2,f):

    f1 = f(x1,y1)
    f2 = f(x2,y2)
    
    x = x1 - (f1/(f2-f1)) * (x2-x1)
    y = y1 - (f1/(f2-f1)) * (y2-y1)
    return x,y

     

#cell är en tuple cell = (x1,y1,x2,y2) 

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


def segments(x1,y1,x2,y2,gridsize,f):
    for c in cells(x1,y1,x2,y2,gridsize): 
           #Fall är en tuple (1,2,0,1,3,3,0,1,1)
        fall = get_case(f,c) 
        
        if fall != 0 and fall != 15: 
            #for tuples in table[fall]:                      #Få ett fall
            koordPos = table[fall][0] 
                         #Kolla upp vilka hörn från table
            
            xin1 = c[koordPos[0]]
            yin1 = c[koordPos[1]]

            xin2 = c[koordPos[2]]
            yin2 = c[koordPos[3]]

            xin3 = c[koordPos[4]]
            yin3 = c[koordPos[5]]

            xin4 = c[koordPos[6]]
            yin4 = c[koordPos[7]]
            
            kord1 = interpolate(xin1,yin1,xin2,yin2,f)
            kord2 = interpolate(xin3,yin3,xin4,yin4,f)
            
            a = kord1[0]
            b = kord1[1]
            c = kord2[0]
            d = kord2[1]
            
            yield (a,b,c,d)



def show(x1,y1,x2,y2,gridsize,f):
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for (x1,y1,x2,y2) in segments(x1,y1,x2,y2,gridsize,f):
        plt.plot([x1, x2], [y1, y2], color="red")
    plt.show()



def circle(x,y):
    return x**2 + y**2  - 5**2

def line(x,y):
    return x+y

def cardioid(x,y):
    return (x**2+y**2)**2 + 4*10*x*(x**2+y**2) - 4*10**2*y**2

def lemniscate(x,y):
    return (x**2 +y**2)**2 - 40**2*(x**2-y**2)

str_to_func = {
    "line":line,
    "circle":circle,
    "cardioid":cardioid,
    "lemniscate":lemniscate
}


def main(): 
    show(-100,100,100,-100,1,str_to_func[sys.argv[1]])
    

if "--help" in sys.argv:
    print("x1,y1,x2,y2,gridsize,(f)") 

    sys.exit(0)

if __name__ == "__main__":
    main()

