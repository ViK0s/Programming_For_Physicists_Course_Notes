#Simple platformer made using pygame




import pygame
import random




class rect:
    def __init__(self,x1,y1,x2,y2,color):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.color=color
    def draw(self,window):
        pygame.draw.rect(window, self.color,#np:(0,   0, 255) or "blue",
        [self.x1, self.y1, self.x2-self.x1, self.y2-self.y1], 0#no outline
        )





class bohater(rect):
    def __init__(self,xc,yc):
        self.a=10
        self.b=15
        self.xc=xc
        self.yc=yc
        rect.__init__(self,self.xc-self.a,self.yc-self.b,self.xc+self.a,self.yc+self.b,"blue")
        self.status="alive"#alive,dead,won
        self.speed=300
    def change(self,xc,yc):
        self.xc=xc
        self.yc=yc
        self.x1=self.xc-self.a
        self.x2=self.xc+self.a
        self.y1=self.yc-self.b
        self.y2=self.yc+self.b
    def touch(self,other):
        return ((abs(self.xc-other.xc)<self.a+other.a) and self.yc==other.yc)
    def touch_platform(self,other):
        if other.type == "platforma":
            return ((abs(self.xc-other.xc)<self.a+other.a) and self.yc<other.yc)
    def check_status(self,listofenemies):
        touched=False
        for i in listofenemies:
            touched=touched or self.touch(i)
        if touched:
            self.status="dead"
    def check_status_platform(self, listofplatforms):
        touched=False
        a = 0
        for i in listofplatforms:
            touched=touched or self.touch_platform(i)
            a+=1
        if touched:
            self.status="on_platform"
            return a

        





class wrog(rect):
    def __init__(self,xc,yc):
        self.a=10
        self.b=15
        self.xc=xc
        self.yc=yc
        rect.__init__(self,self.xc-self.a,self.yc-self.b,self.xc+self.a,self.yc+self.b,"red")
    def change(self,xc,yc):
        self.xc=xc
        self.yc=yc
        self.x1=self.xc-self.a
        self.x2=self.xc+self.a
        self.y1=self.yc-self.b
        self.y2=self.yc+self.b

class moneta(rect):
    def __init__(self, xc, yc):
        self.a=10
        self.b=10
        self.xc=xc
        self.yc=yc
        rect.__init__(self,self.xc-self.a,self.yc-self.b,self.xc+self.a,self.yc+self.b,"yellow")
        self.status="notcollected"#notcollected,collected
    def touch(self,other):
        return ((abs(self.xc-other.xc)<self.a+other.a) and self.y2>=other.y1)
    def check_status(self,hero):
        touched = False
        touched = touched or self.touch(hero)
        if touched:
            self.status="collected"

class platforma(rect):
    def __init__(self, xc, yc):
        self.a=100
        self.b=3
        self.xc=xc
        self.yc=yc
        rect.__init__(self,self.xc-self.a,self.yc-self.b,self.xc+self.a,self.yc+self.b,"green")
        self.type = "platforma"


#while GenerateEnemies and GenerateCoins do the same thing, and could be made into one function, there's some limitation because of pygame that causes some of the objects
#to not have the correct coordinates, probably because of the draw function?


def GenerateEnemies(amount):
    templist = []
    for i in range(amount):
        e = 260 + (i*200)
        templist.append(wrog(random.randint(e,1260), 360))
    return templist


def GenerateCoins(amount):
    templist = []
    for i in range(amount):
        e = 260 + (i*100)
        templist.append(moneta(random.randint(e,1260), random.randint(300, 340)))
    return templist

def GeneratePlatforms(amount):
    templist = []
    for i in range(amount):
        e = 660 + (i*200)
        templist.append(platforma(random.randint(e,1260), 340))
    return templist

def DrawListOfObjects(list):
    for i in list:
        i.draw(screen)
def CheckStatusOfCoins(list_of_objects, play_object, score):
    a = 0
    for i in list_of_objects:
        i.check_status(play_object)
        if i.status == "collected":
            list_of_objects.pop(a)
            score += 50
        a += 1
    return score


def MoveEnemies(list):
    for i in list:
        move(i, dt, 0, random.randint(-50, -1))


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

def move(hero,dt,speedy, speed):
    hero.change(hero.xc+speed*dt,min(360,hero.yc-speedy*dt))
speedx = 50
speedy=0
dude=bohater(120,360)



list_of_coins = GenerateCoins(5)
lw=GenerateEnemies(5)
list_of_platforms = GeneratePlatforms(2)
score = 0
font = pygame.font.Font(None, 64)

g = 30
t=0
t2=0
while running:
    t+=dt
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
     
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dude.yc==360:
        dt2=dt
        speedy = 50 
    if speedy > 0 or dude.yc!=360:
        speedy -= g*dt

    score_text = font.render("Score:" + str(score), True, (5, 5, 5))
    score_text_pos = score_text.get_rect(centerx=100, y=10)
    screen.blit(score_text, score_text_pos)
    DrawListOfObjects(lw)
    DrawListOfObjects(list_of_coins)
    DrawListOfObjects(list_of_platforms)

    dude.draw(screen)    
    dude.check_status(lw)
    dude.check_status_platform(list_of_platforms)
    score = CheckStatusOfCoins(list_of_coins, dude, score)



    if dude.status=="dead":
        text = font.render("Game over", True, (10, 10, 10))
        textpos = text.get_rect(centerx=640, y=10)
        screen.blit(text, textpos)
        pygame.display.flip()
        pygame.time.delay(1000*2)
        running=False

    if dude.status=="on_platform":
        speedy=0
        dude.yc = 325 
    
    if dude.xc >= 1280:
        text = font.render("You win!", True, (10, 10, 10))
        textpos = text.get_rect(centerx=640, y=10)
        screen.blit(text, textpos)
        pygame.display.flip()
        pygame.time.delay(1000*2)
        running=False
    

    MoveEnemies(lw)
    move(dude,dt,speedy, speedx)
    # flip() the display to put your work on screen
    pygame.display.flip()
    

    dt = clock.tick(60) / 1000  # limits FPS to 60
    dude.status = "alive"
pygame.quit()

