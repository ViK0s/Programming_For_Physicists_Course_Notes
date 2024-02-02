"""
A simulation of gravity of two bodies with mass
"""


import pygame
import numpy as np

g = 6.647 * 10**(-11)

class circle:
    def __init__(self, xc, yc, r, color):
        self.xc=xc
        self.yc=yc
        self.color=color
        self.r = r
    def draw(self,window):
        pygame.draw.circle(window, self.color,#np:(0,   0, 255) or "blue",
        [self.xc, self.yc], self.r#no outline
        )

class massObject(circle):
    def __init__(self,xc,yc, r, color, mass, v):
        self.r=r
        self.xc=xc
        self.yc=yc
        self.color = color
        self.mass = mass
        self.v = v
        
        self.es = circle.__init__(self,xc,yc,self.r,color)
    def SimulateGravity(self, obj, dt):
        templst = [self.xc, self.yc]
        templst2 = [obj.xc, obj.yc]
        vctr = np.array(templst)
        vctrobj = np.array(templst2)
        mag = np.linalg.norm(vctrobj-vctr)
        
        self.a = g*(obj.mass/((mag)**3))*((vctrobj-vctr))
        self.v += self.a
        #scaling of v
        if self.v[0] >= 3 or self.v[1] >= 3: 
            self.v *= 0.5
        
        


        self.xc += self.v[0]
        self.yc += self.v[1]




pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
objekt = massObject(680, 320, 5, "blue", 20000000000000, [0,0])
objekt2 = massObject(100, 200, 5, "red", 1000000000000,[1,-1])
dt = 0
while running:
    screen.fill("white")
    objekt.draw(screen)
    objekt2.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    objekt.SimulateGravity(objekt2, dt)
    objekt2.SimulateGravity(objekt, dt)
    #object position debugging
    font = pygame.font.Font(None, 64)
    text = font.render("x:" + str(int(objekt.xc)) + " y: "+ str(int(objekt.yc)) + " v: " + str(round(objekt.v[0], 2))+ " " + str(round(objekt.v[1], 2)), True, (10, 10, 10))
    textpos = text.get_rect(centerx=640, y=10)
    screen.blit(text, textpos)
    #end of debugging
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
