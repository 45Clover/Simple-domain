import pygame
import math 


pygame.init()

wscreen = 1200
hscreen = 500

win = pygame.display.set_mode((wscreen, hscreen))


class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color


#A static method is a type of method in a class that doesn't operate on an instance of the class (i.e., it doesn't access or modify the instance's attributes). Instead, it belongs to the class itself and can be called without creating an instance of the class.
    def draw(self,win):
        pygame.draw.circle(win, (0,0,0), (self.x,self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius-1)
#angles are in radians
#velocity = vel
    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        velx = math.cos(ang) * power
        vely = math.sin(ang) * power

        distX = velx * time
        distY = (vely * time) - ((9.81 * (time)**2) / 2)



        newx = round(distX + startx)
        newy = round(starty - distY)

        return newx, newy
    


def redrawindow():
    win.fill((64,64,64))
    golfBall.draw(win)
    pygame.draw.line(win, (255,255,255), line[0], line[1])
    pygame.display.update()
#takes position of golfball and mouse and tangent to find line
#its like convertig radians into angle 
def findAngle(pos):
    sX = golfBall.x
    sY = golfBall.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle - math.pi / 2
#direction of shot or quadrant located in 
    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi = abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle 

    return angle 








#(x, y, radius,(color))
golfBall = ball(300, 494, 5, (255,255,255))



#where ball was shot from
x = 0
y = 0
time = 0
power = 0
angle = 0
shoot = False








run = True
while run:
    if shoot:
        if golfBall.y < 500 - golfBall.radius:
            time += 0.05
            po = ball.ballPath(x,y,power,angle,time)
            golfBall.x = po[0]
            golfBall.y = po[1]
        else:
            shoot = False
            golfBall.y = 494


    pos = pygame.mouse.get_pos()
    line = [(golfBall.x, golfBall.y), pos]
    redrawindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not shoot:
                    shoot = True
                    x = golfBall.x
                    y = golfBall.y
                    time = 0
                    power = math.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2) / 8
                    angle = findAngle(pos)    

        
pygame.quit()



