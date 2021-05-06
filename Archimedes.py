import pygame,sys,time
pygame.init()
screen = pygame.display.set_mode((1000,770))
clock = pygame.time.Clock()
X, Y = 100, 100
smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('Start' , True , 'black')
text1 = smallfont.render('Stop' , True , 'black')

Q=10
x,y=[340,500,339,633,402,628,402,430,430,875],[270,370,222,305,548,650,525,650,550,350]
#images=[0]*Q
img=[0]*Q
rect=[0]*Q
#for m in range(10):
#    name='image'
#    m1=str(m)
#    ext='.png'
#    images[m]=name+m1+ext
images=['image0.png','image1.png','image2.png','image3.png','image4.png',\
        'image5.png','image6.png','image7.png','image8.png','image9.png']
background=pygame.image.load('bg_ground.png')

def base(i,scalex,scaley,angle):
    img[i]=pygame.image.load(images[i])
    img[i]=pygame.transform.scale(img[i],(scalex,scaley))
    img[i]=pygame.transform.rotate(img[i],angle)
    rect[i]=img[i].get_rect(center=(x[i],y[i]))
    screen.blit(img[i],rect[i])
delta,delta1=1,0
t,i,a,angle1,angle2=0,-1,0,-40,0
X1,Y1=480,592
plotPoints=[(480,592),(496,592.1)]

dX1=8
while True:
    screen.blit(background,(0,-30))
    pygame.draw.rect(screen,'orange', (X, Y,100,50))
    screen.blit(text,(X+10,Y+5))
    mouse=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if abs(mouse[0] - X)<50 and abs(mouse[1] - Y) <50:
                a=a+1
                angle1=-105
            if a==2:
                t,i,angle1,angle2,a=0,0,-105,0,0
                delta=1
                delta1=0
                X1,Y1=480,592
                x,y=[340,500,339,633,402,628,402,430,430,875],[270,370,222,305,548,650,525,650,550,350]
                img=[0]*Q
                rect=[0]*Q
                plotPoints=[(480,592),(496,592.1)]
                base(4,20,delta1,0)
                
    if a==1:
        if y[0]<420:
            y[0]=y[0]+delta
            y[6]=y[6]+delta
            print('y[0]=',y[0])
            y[2]=y[2]+delta
        else: delta=0
        screen.fill('white')
        pygame.draw.rect(screen,'orange', (X, Y,100,50))
        screen.blit(text1,(X+10,Y+5))
        #base(1,1000,800,0)
        
        base(1,1000,800,0)
        base(0,270,515,0)
        base(2,37,162,angle1);
        base(3,37,162,angle2)
        
        base(5,162,21,0)
        base(6,100,145,0)
        #base(9,450,293,0)
        if y[0]>340:
            if y[0]>350:
                y[5]=y[5]-delta/3
            if y[0]>350 and y[0]<420:
                angle1=angle1+1/5
                angle2=angle2-1/5
                y[4]=y[4]+delta*0.5
                delta1=delta1+delta
                base(4,20,delta1,0)
            if y[0]>419:
                base(4,21,delta1,0)
                base(7,50,50,0)
                base(8,50,50,0)
                base(9,250,307,0)
            i=i+1
            X1=X1+dX1
            Y1=592+(dX1*i)*(dX1*i)*0.002
            if i<25:
                plotPoints.append([X1,Y1])
    if y[0]<420:
        pygame.draw.lines(screen,(44,207,255),False,plotPoints,5)
    clock.tick(100)
    pygame.display.update()      