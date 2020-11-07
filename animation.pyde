#def parkinglot():
x=0
y=0
colorselector_row=0
colorselector_col=0
vacant_lot=0
occupied=[]
a=False
b=0
no_of_customers=0
earning=0
w1=15
w2=65
w3=2000
w4=2000
gate_condition=False
exit_condition=False

def setup():
    
    smooth()
    frameRate(60)
    size(1920,1080)
    background(26,183,79)
    p1.parking()


def draw():
    
    delay(100)
    s1.street_design()
    obj.body() 
    m1.moving()
    o1.stall()
    



def mousePressed():
    
    global b
    
    if(b==0):
        noLoop()
        b=1
    else:
        loop()
        b=0
       

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
        
        global gate_condition
        textSize(15)
        fill(255)
        strokeWeight(2)
        fill(51,158,222)
        rect(805, 300, 100, 20)
        fill(255)
        rect(805, 320, 100, 20)
        rect(805, 825, 100, 20)
        rect(805, 845, 100, 20)
        fill(0)
        text("Entry", 825, 315)
        text("Exit", 825, 840)
        text("Spaces:"+ str(60-len(occupied)/2), 825, 335)
        
        if(gate_condition):
            strokeWeight(8)
            line(910, 320, 995, 350)
        
        else:
            strokeWeight(8)
            line(910, 330, 995, 330) 
         
            
        if(exit_condition):
            strokeWeight(8)
            line(910, 835, 995, 855)
            
        else:
            strokeWeight(8)
            line(910, 835, 995, 835)
            
        
        strokeWeight(1)
        
obj = Gate(20,True)

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
        
        text("$2.00 / Hour            Saturday                        8AM to 6PM", 50,115)
        
        text("$1.50 / Hour            All Other Times                    ", 50,150)
        

        
        fill(216,208,208)
        
        rect(890,20,250,150)
        
        rect(1200,20,450,150)
        
        if(len(occupied)==60):
            fill(252,13,13)
            
        else:            
            fill(255,168,36)
            
        rect(1690,20,200,150)
        fill(216,208,208)
        
        fill(255)
        textSize(30)
        text(" SPACES ",1730,70)
        text(60-len(occupied)/2,1770,130)    
        fill(216,208,208)
    
    
        strokeWeight(3)
        circle(1010,95,130)
        strokeWeight(1)
        
        fill(0)
        triangle(988,58,988,128,1054,95)
        noFill()
        
        
        rect(1200,20,450,150)
        
        fill(0)
    
        textSize(22)
        text("Simulation Values",1320,50)
        textSize(20)
        text("Total number of customers :",1250,85)
        text(no_of_customers,1540,85)
        
        global earning
        
        if(len(occupied)>0):
            earning=earning+0.003*(len(occupied)/2)
            
        text("Net Revenue :                 $",1250,115)
        
        text(earning,1400,115)
        
        text("Current number of cars parked :",1250,145)
        
        text(len(occupied)/2,1570,145)
            
        
        
        
    
        
        
s1=street()
        
        
        
class parkingstall:
    
    def stall(self):
        
        y=335
        
        for i in range (0,6):
            
            x=115
            
            for j in range(0,10):
                
    
                fill(37,216,98)
                
                for k in range(1,len(occupied)+2,2):
                    
                    if(len(occupied)>2 and occupied[len(occupied)-k]==j and occupied[len(occupied)-(k+1)]==i):
                        fill(245,35,35)
                    
                    elif(len(occupied)!= 0 and occupied[0]==i and occupied[1]==j):
                        fill(245,35,35)  
                                  
                    
                rect(x,y,150,50)
                if(j==4):
                    x+=250
                else:
                    x+=160
                    
            if(i%2!=0):
                y+=115
            else:
                y+=60
                            
                
o1=parkingstall()

        
class move:
    
    
    def __init__(self,x1,y1,x2,y2,counter):
        
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.counter=counter
    
    
    def moving(self):
        
        global gate_condition,exit_condition
        
        global no_of_customers,w1,w2,w3,w4
        
        fill(31,222,220)
        
        if(self.x1>1900):  
                  
            self.x1=0
            w1=15
            w2=65
            gate_condition=False
            exit_condition=False
            
        if(self.x1==950):
            choice=int(random(1,3))
            
            if(choice==1):

                gate_condition=True
                no_of_customers+=1
                self.x1=0
                w1=15
                w2=65
                self.counter+=1
                global colorselector_row
                colorselector_row=int(random(0,6))
                global colorselector_col
                colorselector_col=int(random(0,10)) 
                global occupied
                occupied.append(colorselector_row)
                occupied.append(colorselector_col)
                print(occupied)
            
                
        
            
                 
        rect(self.x1,self.y1,100,60)
        self.x1+=50
        fill(0)
        rect(w1,210,20,45)
        w1+=50
        rect(w2,210,20,45)
        w2+=50
        
        global vacant_lot
        vacant_lot=int(random(0,90))
        
        fill(31,222,220)
    
        rect(self.x2,self.y2,100,60)
        fill(0)  
        rect(w4,895,20,45)
        rect(w3,895,20,45)
    
        if(self.x2>1900 and vacant_lot==2 and len(occupied)>0):  
                  
            self.x2=850
            w3=865
            w4=910
            occupied=occupied[2:]
            exit_condition=True
        
        self.x2+=50
        w3+=50
        w4+=50
        fill(255)
    
        

    
m1=move(0,205,2000,890,0)
