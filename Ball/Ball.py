import pygame
from datetime import datetime, timedelta
import math
import random
pygame.init()

display_width = 1300
display_height = 200

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('My First Pygame!')

black = (0,0,0)
white = (0,255,100)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('sball.png')
carSizeX = 101
carSizeY = 101
carRadiusX = carSizeX/2
carRadiusY = carSizeY/2
framerate = 60
carImg = pygame.transform.scale(carImg, (carSizeX, carSizeY))

def car(x,y):
    gameDisplay.blit(carImg, (x-(carRadiusX),y-carRadiusY))

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
velocity = [2,5]
last=datetime.now()
framerateMonitor = 0
dragging = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONUP:
            dragging=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseLastX,mouseLastY=pygame.mouse.get_pos()
            if(mouseLastX<x+carRadiusX and mouseLastX>x-carRadiusX and mouseLastY<y+carRadiusY and mouseLastY>y-carRadiusY):
                lastMouseMoveTime = datetime.now()
                dragging=True
    gameDisplay.fill(white)
    if(dragging==True):
        mouseX,mouseY=pygame.mouse.get_pos()
        if(mouseX-carRadiusX<0 or mouseX+carRadiusX>display_width):
            pass
        else:
            x = mouseX
        if(mouseY-carRadiusY<0 or mouseY+carRadiusY>display_height):
            pass
        else:
            y = mouseY
        xD=mouseX-mouseLastX
        yD=mouseY-mouseLastY
        now = datetime.now()
        timeElapsed = now-lastMouseMoveTime
        distanceDivisor = (timeElapsed.seconds+(timeElapsed.microseconds/10000))
        if(distanceDivisor==0):
            distanceDivisor=0.000001
        velocity[0] = (mouseX-mouseLastX)/distanceDivisor
        velocity[1] = (mouseY-mouseLastY)/distanceDivisor
        mouseLastX = mouseX
        mouseLastY = mouseY
        lastMouseMoveTime = datetime.now()
        last = datetime.now()

    else:


        now = datetime.now()
        elapsedTime = now-last
        multiplier = (elapsedTime.microseconds/10000)
        changeX,changeY = velocity[0]*multiplier, velocity[1]*multiplier
        if(x-carRadiusX+changeX<0):
            x+=0-(x-carRadiusX+changeX)
            velocity[0]=velocity[0]*-1
        elif(x+carRadiusX+changeX>display_width):
            x+=display_width-(x+carRadiusX+changeX)
            velocity[0]=velocity[0]*-1
        elif(y-carRadiusY+changeY<0):
            y+=0-(y-carRadiusY+changeY)
            velocity[1]=velocity[1]*-1
        elif(y+carRadiusY+changeY>display_height):
            y+=display_height-(y+carRadiusY+changeY)
            velocity[1]=velocity[1]*-1
        else:
           x,y = x+velocity[0]*multiplier, y+velocity[1]*multiplier

        #if(x-carRadiusX+velocity[0]<0 or x+carRadiusX+velocity[0]>display_width):
        #    velocity[0]=velocity[0]*-1
        #elif(y-carRadiusY+velocity[1]<0 or y+carRadiusY+velocity[1]>display_height):
        #    velocity[1]=velocity[1]*-1
       # else:
        #    x,y = x+velocity[0]*multiplier, y+velocity[1]*multiplier


        last = datetime.now()
    car(x,y)
        
    pygame.display.update()


    clock.tick(framerate)

pygame.quit()
quit()