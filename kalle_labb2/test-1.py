import itertools
import importlib.util
from os.path import exists

pass_tests = 0
fail_tests = 0

def test(f,x,y):
    global pass_tests, fail_tests

    z = f(*x)

    if y == z:
        pass_tests = pass_tests + 1
    else:
        print(f.__name__+repr(x)+" is expected to return:")
        print("   "+str(y))
        print("but got:")
        print("   "+str(z))
        fail_tests = fail_tests + 1

def test_cond(cond,msg):
    global pass_tests, fail_tests

    if cond:
        pass_tests = pass_tests + 1
    else:
        print(msg)
        fail_tests = fail_tests + 1

def test_gen(f,x,y):
    global pass_tests, fail_tests

    z = f(*x)
    z = list(itertools.islice(z, len(y)))

    if y == z:
        pass_tests = pass_tests + 1
    else:
        print(f.__name__+repr(x)+" is expected to yield:")
        print("   "+str(y))
        print("but got:")
        print("   "+str(z))
        fail_tests = fail_tests + 1

def test_balls(f,half_size,count):
    for state in itertools.islice(f(half_size,count), 30):
        if not isinstance(state,tuple) or len(state) != count:
            print("balls"+str((half_size,count))+" must yeld tuples of size "+str(count))
            print("but got:")
            print("   "+str(state))
            return
        for x in state:
            if not (isinstance(x,tuple) and len(x) == 3):
                print("for each ball there should a triple of numbers")
                return
            if not (isinstance(x[0],float) and isinstance(x[1],float) and isinstance(x[2],float)):
                print("the triple for each ball must contain only real numbers")
                return
            if not (-half_size < x[0] < half_size and -half_size < x[1] < half_size):
                print("the coordinates for every ball must always be inside located inside the box")
                return


def run(src_path="."):
    if exists(src_path+"/balls.py"):
        spec = importlib.util.spec_from_file_location("balls", src_path+"/balls.py")
        balls = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(balls)

        if hasattr(balls, "trajectory"):
            test_gen(balls.trajectory,(0,0,2,1,5,10),[(0, 0, 5), (2, 1, 5), (4, 2, 5), (6, 3, 5), (8, 4, 5), (10, 5, 5), (8, 6, 5), (6, 7, 5), (4, 8, 5), (2, 9, 5)])
            test_gen(balls.trajectory,(4,1,1,0,5,10),[(4, 1, 5), (5, 1, 5), (6, 1, 5), (7, 1, 5), (8, 1, 5)])
        else:
            print("trajectory is not implemented yet")
        if hasattr(balls, "balls"):
            test_balls(balls.balls,10,20)
        else:
            print("balls is not implemented yet")
    else:
        print("balls.py doesn't exist yet")

    if exists(src_path+"/graph.py"):
        spec = importlib.util.spec_from_file_location("graph", src_path+"/graph.py")
        graph = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(graph)
        
        if hasattr(graph, "cells"):
            test_gen(graph.cells,(-10,10,10,-10,5), [(-10, -5, -5, -10), (-10, 0, -5, -5), (-10, 5, -5, 0), (-10, 10, -5, 5), (-5, -5, 0, -10), (-5, 0, 0, -5), (-5, 5, 0, 0), (-5, 10, 0, 5), (0, -5, 5, -10), (0, 0, 5, -5), (0, 5, 5, 0), (0, 10, 5, 5), (5, -5, 10, -10), (5, 0, 10, -5), (5, 5, 10, 0), (5, 10, 10, 5)])
            test_gen(graph.cells,(0,4,7,1,3), [(0, 4, 3, 1), (3, 4, 6, 1), (6, 4, 9, 1)])
        else:
            print("cells is not implemented yet")

        if hasattr(graph, "interpolate"):
            f = lambda x,y: (2*x+3*y)
            x,y = graph.interpolate(8,6,4,-6,f)
            test_cond(abs(f(x,y)) < 1e-14, "The interpolation doesn't find a close-enough point")

        if hasattr(graph, "get_case"):
            f = lambda x,y: (x**2+y**2)-40**2
            test(graph.get_case,(f,(-50, -45, -45, -50)), 0)
            test(graph.get_case,(f,(15, -35, 20, -40)),1)
            test(graph.get_case,(f,(-40, -15, -35, -20)),2)
            test(graph.get_case,(f,(-25, -30, -20, -35)),3)
            test(graph.get_case,(f,(-40, 20, -35, 15)),4)
            test(graph.get_case,(f,(-40, -10, -35, -15)),6)
            test(graph.get_case,(f,(-35, -15, -30, -20)),7)
            test(graph.get_case,(f,(15, 40, 20, 35)),8)
            test(graph.get_case,(f,(30, -20, 35, -25)),9)
            test(graph.get_case,(f,(15, -30, 20, -35)),11)
            test(graph.get_case,(f,(-25, 35, -20, 30)),12)
            test(graph.get_case,(f,(15, 35, 20, 30)),13)
            test(graph.get_case,(f,(-35, 20, -30, 15)),14)
            test(graph.get_case,(f,(-35, -10, -30, -15)),15)

        if hasattr(graph, "segments"):
            test_gen(graph.segments,(-20,20,20,-20,10,lambda x,y: (2*x+3*y)), [(-15.0, 10.0, -10.0, 6.666666666666667), (-20.0, 13.333333333333334, -15.0, 10.0), (0.0, 0.0, 0.0, 0.0), (-10.0, 6.666666666666667, 0.0, 0.0), (0.0, 0.0, 10.0, -6.666666666666666), (15.0, -10.0, 20.0, -13.333333333333332), (10.0, -6.666666666666666, 15.0, -10.0)])
        else:
            print("segments is not implemented yet")

    else:
        print("graph.py doesn't exist yet")

    if exists(src_path+"/metaballs.py"):
        spec = importlib.util.spec_from_file_location("metaballs", src_path+"/metaballs.py")
        metaballs = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(metaballs)
        if hasattr(metaballs, "potential"):
            test(metaballs.potential,([],10,10),0)
            test(metaballs.potential,([(0,0,1)],10,10),0.07071067811865475)
            test(metaballs.potential,([(0,0,1)],0.001,0.001),707.1067811865476)
        else:
            print("potential is not implemented yet")

    else:
        print("metaballs.py doesn't exist yet")

    print(str(pass_tests)+" out of "+str(pass_tests+fail_tests)+" passed.")


if __name__ == "__main__":
    run()
