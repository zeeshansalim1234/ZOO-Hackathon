#def parkinglot():
x=0
y=0

rand=int(random(1,5))

    

def setup():
    

    size(1920,1080)
    background(26,183,79)
    p1.parking()


def draw():
    
    delay(100)
    s1.street_design()
    obj.body() 
    o1.stall()
    m1.moving()
    



def mousePressed():
    
    b=0
    if(b==0):
        b=1
    else:
        b=0
        
    print(b)
       

value=1

class parkinglot:
    
    def parking(self):
        
        fill(255)
        rect(80,300,1750,550)
        fill(155)
        rect(90,310,1730,530)
        x=0
        y=0
        
        for i in range(0,6):        #Creating parking spaces
        
            if(i<3):                #left rectangles
            
                if(i==0):
                    y=330
                    
                x=110
                fill(255)
                rect(x,y,800,120)
                y+=175
                
            else:                   #right rectangles
                
                if(i==3):
                    y=330
                    
                x=1000
                fill(255)
                rect(x,y,800,120)
                y+=175
        

p1=parkinglot()


class Gate:
    
    #stat = True
    #sp = 0
    def __init__(self, s, status):
        self.stat = status
        self.sp = s

    #space = str(sp)
    
    def body(self):
        
        textSize(15)
        fill(255)
        strokeWeight(2)
        rect(805, 300, 100, 20)
        rect(805, 320, 100, 20)
        rect(805, 825, 100, 20)
        rect(805, 845, 100, 20)
        fill(100)
        text("Entry", 825, 315)
        text("Exit", 825, 840)
        text("Spaces:"+ str(self.sp), 825, 335)
        
        if(self.stat == True):
            strokeWeight(8)
            line(910, 320, 995, 350)
            line(910, 835, 995, 855)
        else:
            strokeWeight(8)
            line(910, 330, 995, 330) 
            line(910, 835, 995, 835)   
            
        
        strokeWeight(1)
        
obj = Gate(20,False)

class street:
    
    def street_design(self):
        
        strokeWeight(1)
        
        fill(255)   

        rect(0,270,1920,10)
        
        rect(0,870,1920,10)
        
        rect(0,960,1920,10)   
                
        fill(155)
        
        rect(0,200,1920,70)
        
        rect(0,880,1920,80)
        
        noStroke()

        rect(910,270,90,615)  
        
        stroke(1)
        
        fill(255)
        
        rect(0,0,1920,200)
    
        
        fill(26,183,79)
        
        rect(0,0,1920,190)
        
        
        
        fill(216,208,208)
        
        rect(30,20,800,150)
        
        fill(0)
        
        textSize(30)
        
        text("Parking Rates:",50,50)
        
        text("North City Street",840,250)
        
        text("South City Street",840,930)
        
        textSize(25)
        
        text("$3.00 / Hour            Mon - Fri                       8AM to 6PM", 50,80)
        
        text("$2.00 / Hour            Mon - Fri                       8AM to 6PM", 50,115)
        
        text("$1.50 / Hour            Mon - Fri                       8AM to 6PM", 50,150)
        
        fill(216,208,208)
        
        rect(890,20,250,150)
        
        
        
        rect(1200,20,450,150)
        
        fill(0)
        
        rect(1690,40,200,150)
        
        
s1=street()
        
class parkingstall:
    
    def stall(self):
        
        for i in range(0,30):
            
            if(i<5):
                
                rand=int(random(1,6))
                if(i==0):
                    x=115
                
                y=335
                if(i==(rand-1)):
                    fill(234,21,21)
                else:
                    fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
            elif(i<10):
                
                if(i==5):
                    x=115
                    
                y=395
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
            elif(i<15):
                
                if(i==10):
                    x=115
                    
                y=510
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
            elif(i<20):
                
                if(i==15):
                    x=115
                    
                y=570
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
            elif(i<25):
                
                if(i==20):
                    x=115
                    
                y=685
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
            else:
                
                if(i==25):
                    x=115
                    
                y=745
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
        
            
            
                
        for i in range(0,30):
            
            if(i<5):
                
                if(i==0):
                    x=1005
                
                y=335
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
            elif(i<10):
                
                if(i==5):
                    x=1005
                    
                y=395
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
            elif(i<15):
                
                if(i==10):
                    x=1005
                    
                y=510
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
            elif(i<20):
                
                if(i==15):
                    x=1005
                    
                y=570
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
            elif(i<25):
                
                if(i==20):
                    x=1005
                    
                y=685
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
            else:
                
                if(i==25):
                    x=1005
                    
                y=745
                fill(37,216,98)
                rect(x,y,150,50)
                x+=160
                
                
o1=parkingstall()

        
class move:
    
    
    def __init__(self,x1,y1,x2,y2,counter):
        
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.counter=counter
    
    
    def moving(self):
        
        fill(31,222,220)
        
        if(self.x1>1900):  
                  
            self.x1=0
            
        if(self.x1==950):
            choice=int(random(1,3))
            if(choice==2):
                self.x1=0
                self.counter+=1
                

            
        rect(self.x1,self.y1,80,60)
        self.x1+=50
    
    
        if(self.x2>1900):  
                  
            self.x2=850
            
        rect(self.x2,self.y2,80,60)
        self.x2+=50
        fill(255)
        
        print("NUMBER OF CARS:",self.counter)
        
        
    
m1=move(0,205,850,890,0)
    
