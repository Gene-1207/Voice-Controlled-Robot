import math

class path():
    route = [0 for i in range(10)]
    distance = 0
    distGraph = [[0]]
    def addroute(x):
        route[x[0]] = x[1]
        route[x[1]] = x[0]
        distance += distGraph[x[0]][x[1]]
        return
 
class Tsp():
    def all_pairs(self,lst):
        if len(lst) < 2:
            yield lst
            return
        a = lst[0]
        for i in range(1,len(lst)):
            pair = (a,lst[i])
            for rest in self.all_pairs(lst[1:i]+lst[i+1:]):
                yield [pair] + rest

def justStitch(path,x):
    for i in x:
        path.addroute(i)
    return
def stitch(path,y):
    
def dist(x,y):
    return math.sqrt(math.pow(x[0]-y[0],2) + math.pow(x[1]-y[1],2))
minpath = path()
def main():
    global minpath
    nowpath = path()
    ts=Tsp()
    inp = [(2,3),(9,0),(-12,4),(0,0)]
    distGraph = [[dist(inp[i],inp[j]) for j in range(len(inp))] for i in range(len(inp))]
    minpath.distance = 1000000000
    nowpath.distGraph = distGraph
    count = 0
    lst=[0,1,2,3,4]
    def recursive(l):
        nonlocal count
        if(len(l) > 3):
            for y in ts.all_pairs(l):
                stitch(nowpath,y)
                recursive(y)
        else:
            print("_____" , l)
            count += 1
    for x in ts.all_pairs(lst):
        juststitch(nowpath,x)
        recursive(x)
    print(count)
        


if __name__=='__main__':
    main()
