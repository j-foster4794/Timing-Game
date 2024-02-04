import pygame as pg
import random

screenwidth = 900
screenheight = 900
timer = 0
run = True
score = 0
closest = 0

pg.init()
pg.font.init()
screen = pg.display.set_mode((screenwidth,screenheight))
pg.display.set_caption("Timing Game")

font = pg.font.Font(None, 36)

first = pg.sprite.Group()
first.empty()
second = pg.sprite.Group()
second.empty()
third = pg.sprite.Group()
third.empty()
fourth = pg.sprite.Group()
fourth.empty()

class notes(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        list = [100,300,500,700]
        self.x = random.choice(list)
        image =  pg.image.load("H:\James School Work\A Level\Comp Sci\Coding\Free time coding\Timing Game\pixilart-drawing.png")
        self.surf = image
        self.rect = self.surf.get_rect(topleft = (self.x,0))
        self.speed = 5
        self.note = self

    def move(self):
      self.rect.y += self.speed

CREATENOTE = pg.USEREVENT + 1
pg.time.set_timer(CREATENOTE,1000)
all_sprites = pg.sprite.Group()

def pointcheck():
    global score, closest
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[pg.K_d] and first:
        closest = None
        a = 0
        for i in first:
            if i.rect.y > a:
                closest = i
                a = closest.rect.y
        distance = abs(((screenheight - 200)  - a + 25))
        if closest:
            if distance < 100:
                if closest.rect.y < (screenheight-200): 
                    score += (125-distance)
                    closest.note.kill()
    if keys_pressed[pg.K_f] and second:
        closest = None
        a = 0
        for i in second:
            if i.rect.y > a:
                closest = i
                a = closest.rect.y
        distance = abs(((screenheight - 200)  - a + 25))
        if closest:
            if distance < 100:
                if closest.rect.y < (screenheight-200):
                    score += (125-distance)
                    closest.note.kill()
    if keys_pressed[pg.K_j] and third:
        closest = None
        a = 0
        for i in third:
            if i.rect.y > a:
                closest = i
                a = closest.rect.y
        distance = abs(((screenheight - 200)  - a + 25))
        if closest:
            if distance < 100:
                if closest.rect.y < (screenheight-200):    
                    score += (125-distance)
                    closest.note.kill()
    if keys_pressed[pg.K_k] and fourth:
        closest = None
        a = 0
        for i in fourth:
            if i.rect.y > a:
                closest = i
                a = closest.rect.y
        distance = abs(((screenheight - 200)  - a + 25))
        if closest:
            if distance < 100:
                if closest.rect.y < (screenheight-200):
                    score += (125-distance)
                    closest.note.kill()

def drawgrid():
    screen.fill("blue4")
    for i in range(100,screenwidth,100):
        pg.draw.line(screen,'blueviolet',(i,0),(i,screenheight),3)
    pg.draw.line(screen,"blueviolet",(0,screenheight-200),(screenwidth,screenheight-200),7)

def updatenotes():
    for entity in all_sprites:
        if timer % 10 == 0:
            entity.move()
        if entity.rect.y > screenheight:
            entity.kill()
        screen.blit(entity.surf,entity.rect)


while run:
    drawgrid()
    updatenotes()
    pointcheck()
    score_text = font.render(f'Score: {score}', True, ("red3"))
    screen.blit(score_text,(10,10))
    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
        if event.type == CREATENOTE:
            note = notes()
            all_sprites.add(note)
            if note.x == 100:
              first.add(note)
            if note.x == 300:
              second.add(note)
            if note.x == 500:
              third.add(note)
            if note.x == 700:
              fourth.add(note)
    timer += 1