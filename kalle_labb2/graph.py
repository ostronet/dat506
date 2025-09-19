
                #1 = x^2 + y^2
def f(x,y):
    ans = x**2 + y**2 - 1
    return ans


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

    Case = next((k for k, v in bool_cases.items() if v == bool_tuple))
    return Case

     
for c in cells(-10,10,10,-10,5):
    get_case(f,c)
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
