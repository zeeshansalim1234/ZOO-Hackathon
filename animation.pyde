#def parkinglot():
size(1920,1080)
background(26,183,79)
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

for i in range(0,30):
    
    if(i<5):
        
        if(i==0):
            x=115
        
        y=335
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
    
        
        
