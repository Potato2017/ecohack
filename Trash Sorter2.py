# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:09:39 2021

@author: apeng
"""

import pygame
import os, sys
from pygame import mixer
import random

pygame.font.init()



WIDTH, HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SmartSorter")
BIN_FONT = pygame.font.SysFont('comicsans', 30)


WHITE = (255,255,255)
GREEN = (0,192,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREY = (128,128,128)
SILVER = (192,192,192)
PURPLE = (75,0,130)

BACKGROUND = pygame.image.load((os.path.join('Assets','field3.png'))) #house 

FPS = 60

RECYCLE_BIN = pygame.image.load(os.path.join('Assets','RECYCLING BIN.png'))
RECYCLE_BIN = pygame.transform.scale(RECYCLE_BIN, (125,140))
TRASH_BIN = pygame.image.load(os.path.join('Assets','TRASH BIN.png'))
TRASH_BIN = pygame.transform.scale(TRASH_BIN, (110,150))
COMPOST_BIN = pygame.image.load(os.path.join('Assets','COMPOST BIN.png'))
COMPOST_BIN = pygame.transform.scale(COMPOST_BIN, (110,153))

RECYCLE_BIN_X_ORI = 185
RECYCLE_BIN_Y_ORI = 103
TRASH_BIN_X_ORI = 400
TRASH_BIN_Y_ORI = 100
COMPOST_BIN_X_ORI = 600
COMPOST_BIN_Y_ORI = 100

SMALL_BONES = pygame.image.load(os.path.join('Assets','SmallBones.png'))
PLASTIC = pygame.image.load(os.path.join('Assets','Non-Foods.png'))

def load_sprite(path, image_filename, xsize, ysize):
    sprite = pygame.image.load(os.path.join('Assets/' + path, image_filename))
    sprite = pygame.transform.scale(sprite, (xsize ,ysize))
    return sprite

item = ''
whichbin =''
RECYCLEBIN = ['cardboardbox','cerealbox','magazines','milk','newspaper','shampoo','sodacan','waterbottle','winebottle','fabricsoftener']
TRASHBIN = ['candywrapper','chipbag','cup','takeoutbox','ketchup','straws','plasticbag','plasticplate','napkin','shoppingbag']
COMPOSTBIN = ['bananapeel', 'leaf','apple','leftovers','pizzabox','pizzacrust','sandwich','stick','eggcarton','toiletpaperroll']
#sprite = pygame.image.load(os.path.join('Assets/' + whichbin,item + '.png'))


def randomNum():
    binType = random.randint(1,3)

    itemType = random.randint(0,9)
    if binType == 1:
        whichbin = 'recycle'
        item = RECYCLEBIN[itemType]
    elif binType == 2:
        whichbin = 'trash'
        item = TRASHBIN[itemType]
    else:
        whichbin = 'compost'
        item = COMPOSTBIN[itemType]
    return item, whichbin
    
def gameEnd(score):
    print(score)
    if score >= 75:
        sprite = load_sprite('', 'youwin.jpg', 200, 200)
    elif score <= -25:
        sprite = load_sprite('', 'youlose.jpg', 200, 200)
    else:
        return score

    WIN.fill(BLACK)

    print('here')
    #draw lose or win screens
    WIN.blit(sprite, (350, 100))

    pygame.display.update()
    pygame.time.wait(3000)

    score = 0
    return score

def scoring(item,whichbin, score):
    if check(item, whichbin):
        score = score + 10
    else:
        score = score - 5
    return score

#    score_text = BIN_FONT.render(str(score+n), 1, 'BLACK')
#    WIN.blit(score_text,(420,25))
#    pygame.display.update()


def addScore(score,n):
#    score_text = BIN_FONT.render(str(score+n), 1, 'BLACK')
#    WIN.blit(score_text,(420,25))
#    pygame.display.update()

    return score+n

def check(item,whichbin):
    if whichbin == 'recycle':
        if item in RECYCLEBIN:
            return True
        else:
            return False
    if whichbin == 'trash':
        if item in TRASHBIN:
            return True
        else:
            return False
    if whichbin == 'compost':
        if item in COMPOSTBIN:
            return True
        else:
            return False


def soundEffect(item, whichbin):
    if check(item, whichbin) == True:
        
        mixer.init()
        correct = os.path.join('Assets', 'correct.mp3')
        mixer.music.load(correct)
        mixer.music.set_volume(0.7)
        mixer.music.play()
    else:
        mixer.init()
        wrong = os.path.join('Assets','wrong.mp3')
        mixer.music.load(wrong)
        mixer.music.set_volume(0.7)
        mixer.music.play()

    


def draw_window2(x, y, trash_sprite, score, item):

    #WIN.fill(SILVER)
    WIN.blit(BACKGROUND, (0,0))

    #draw bins
    WIN.blit(RECYCLE_BIN, (RECYCLE_BIN_X_ORI,RECYCLE_BIN_Y_ORI))
    WIN.blit(TRASH_BIN, (TRASH_BIN_X_ORI,TRASH_BIN_Y_ORI))
    WIN.blit(COMPOST_BIN, (COMPOST_BIN_X_ORI,COMPOST_BIN_Y_ORI))

    #make label
    sprite_text = BIN_FONT.render(item,1, PURPLE)
    WIN.blit(sprite_text, (50,450))

    #label bins
    recycling_text = BIN_FONT.render("Recycling", 1, BLUE)
    trash_text = BIN_FONT.render("Landfill", 1, GREY)
    compost_text = BIN_FONT.render("Compost", 1, GREEN)
    WIN.blit(recycling_text, (215,75))
    WIN.blit(trash_text, (420,75))
    WIN.blit(compost_text, (615,75))

    #draw trash
    WIN.blit(trash_sprite, (x, y))

    # display score
    score_text = BIN_FONT.render('Score: ' + str(score), 1, 'PURPLE')
    WIN.blit(score_text, (420, 25))

    pygame.display.update()

def isInBins(trash_sprite, bin_sprite, xdrop, ydrop, x_bin, y_bin):

    xs_trash, ys_trash, xe_trash, ye_trash = trash_sprite.get_rect()
    xs_bin, ys_bin, xe_bin, ye_bin = bin_sprite.get_rect()

    xIsIn = (xdrop > x_bin and xdrop < x_bin + xe_bin) or (xdrop + xe_trash > x_bin and xdrop + xe_trash < x_bin + xe_bin)
    yIsIn = (ydrop > y_bin and ydrop < y_bin + ye_bin) or (ydrop + ye_trash > y_bin and ydrop + ye_trash < y_bin + ye_bin)
    if xIsIn and yIsIn:
        return True
    else:
        return False

def main():
    clock = pygame.time.Clock()

    run = True
    
    dragging = False
    x = 400
    y = 400
    xdrop_ori = x
    ydrop_ori = y
    xdrop = x
    ydrop = y

    score = 0

   # trash_sprite = SMALL_BONES
    item, whichbin = randomNum()
    trash_sprite = load_sprite(whichbin, item + '.png', 70, 90)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mx, my = event.pos
                    xstart, ystart, xend, yend = trash_sprite.get_rect()

                    if mx < xdrop + xend and mx > xdrop and my < ydrop + yend and my > ydrop: # picked the trash

                        dragging = True
                        mx, my = event.pos
                        x, y = xdrop, ydrop
                        off_x = x - mx
                        off_y = y - my
    #                    print(off_x, off_y)
                        
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
                    xdrop = x
                    ydrop = y

                    # check if trash is in any one the bins
                    isInRecycle = isInBins(trash_sprite, RECYCLE_BIN, xdrop, ydrop, RECYCLE_BIN_X_ORI, RECYCLE_BIN_Y_ORI)
                    isInTrash = isInBins(trash_sprite, TRASH_BIN, xdrop, ydrop, TRASH_BIN_X_ORI, TRASH_BIN_Y_ORI)
                    isInCompost = isInBins(trash_sprite, COMPOST_BIN, xdrop, ydrop, COMPOST_BIN_X_ORI, COMPOST_BIN_Y_ORI)

                    if isInRecycle:
                        whichbin = 'recycle'
                    elif isInTrash:
                        whichbin = 'trash'
                    elif isInCompost:
                        whichbin = 'compost'



#                    print(isInCompost)
#                    print(isInTrash)
#                    print(isInRecycle)

                    if isInRecycle or isInTrash or isInCompost:
                        soundEffect(item, whichbin)
                        score = scoring(item, whichbin, score)

                        score = gameEnd(score)

#                        if check(item, whichbin):
#                            score = score + 10
#                        else:
#                            score = score - 5
                        item, whichbin = randomNum()
                        trash_sprite = load_sprite(whichbin, item + '.png', 70, 90)
                        x = xdrop_ori
                        y = ydrop_ori

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    mx, my = event.pos
                    x = mx + off_x
                    y = my + off_y
#                    print(x, y)
                    
        #draw_window()
        draw_window2(x, y, trash_sprite, score, item)

    pygame.quit()
    
    
if __name__ == "__main__":
    main()
    
    
            
