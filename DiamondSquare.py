import random

def avg(*args):
    final = 0
    for val in args:
        final += val
    return final / len(args)

class Grid():
    def __init__(self, n):
        self.n = n
        self.size = 2**self.n+1
        self.data = []
        for row in range(self.size):
            curRow = []
            for col in range(self.size):
                curRow.append(None)
            self.data.append(curRow)
        self.data[0][0]   = .5
        self.data[0][-1]  = .5
        self.data[-1][0]  = .5
        self.data[-1][-1] = .5

        self.Diamond(self.size-1)
        self.Refit(0.,255.)

    def __str__(self):
        final = "[\n\n"
        for row in range(self.size):
            vals = ['[']
            for col in range(self.size):
                if(self.data[row][col]==None):
                    vals.append("     ")
                else:
                    vals.append('%.3f' % self.data[row][col])
                vals.append(',')
            vals[-1]=']'
            final += "\t"+"".join(vals)+"\n\n\n"
        final += "]"
        return final

    def Max(self):
        biggest = -float("inf")
        for row in self.data:
            biggest = max(biggest,max(row))
        return biggest

    def Min(self):
        biggest = float("inf")
        for row in self.data:
            biggest = min(biggest,min(row))
        return biggest

    def Sample(self,y,x):
        if(x<0):
            x-=1
        if(y<0):
            y-=1
        return self.data[y%self.size][x%self.size]

    def Refit(self,NewMin,NewMax):
        OldMin = self.Min()
        OldMax = self.Max()
        for y in range(self.size):
            for x in range(self.size):
                self.data[y][x] = (((self.data[y][x] - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin

    def Doppelganger(self,y,x):
        if(y==0 or x == 0 or y == self.size-1 or x == self.size-1):
            if(y==0):
                y+=self.size-1
            if(x==0):
                x+=self.size-1
            if(y==self.size-1):
                y=0
            if(x==self.size-1):
                x=0
            return self.data[y][x]
        return None


    def Diamond(self, stepSize):
        half = stepSize/2
        if(half < 1.):
            return
        half = int(half)
        y = half
        while(y<self.size):
            x = half
            while(x<self.size):
                doppelganger = self.Doppelganger(y,x)
                if(doppelganger is not None):
                    self.data[y][x] = doppelganger
                else:
                    self.data[y][x] = avg(self.data[y+half][x+half],self.data[y+half][x-half],self.data[y-half][x+half],self.data[y-half][x-half])
                    self.data[y][x] += (random.random()-0.5)*(stepSize/(self.size))
                x+=stepSize
            y+=stepSize
            
        self.Square(stepSize)

    def Square(self, stepSize):
        half = stepSize/2
        half = int(half)
        y = 0
        yIter = 1
        while(y<self.size):
            x = (yIter%2) * half
            while(x<self.size):
                doppelganger = self.Doppelganger(y,x)
                if(doppelganger is not None):
                    self.data[y][x] = doppelganger
                else:
                    self.data[y][x] = avg(self.Sample(y+half,x),self.Sample(y-half,x),self.Sample(y,x+half),self.Sample(y,x-half))
                    self.data[y][x] += (random.random()-0.5)*(stepSize/(self.size*1.41421356))
                x+=stepSize
            y+=half
            yIter += 1
            
        self.Diamond(half)