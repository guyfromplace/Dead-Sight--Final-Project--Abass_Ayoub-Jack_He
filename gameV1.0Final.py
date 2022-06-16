#Dead Sight- Top Down Shooter
#Final Project
#June 16, 2014
#Abbass Ayoub and Jack He

from pygame import *
from random import *
from pygame.locals import *
from math import*
import math
import sys
import os
font.init()
mixer.init()

##global mx,my,mb,boss,playerpos,enemies,deadenemies,allchars,wave,totenemies,pointtot,credit

overheated = False      #Work In Progress
overcount = 0

init()
size = width, height= 780, 740
screen = display.set_mode(size)
display.set_caption("Dead Sight!")

cameraX, cameraY = 0,0
mx,my = 0,0
mb = mouse.get_pressed()

spawnlocs = [[-50,-50,10,1470],        #Enemy spawn locations. Prevents enemies from spawning in the base                 
             [-50,-50,10,1470],
             [520,1040,-50,-50],
             [520,1040,1530,1530],
             [1610,1610,10,1470],
             [1610,1610,10,1470]]

##chalwaves = [generateDDWave(wave,totenemies,spawnlocs),generateDHWave(wave,totenemies,spawnlocs),generateWWave(wave,totenemies,spawnlocs),generateSWave(wave,totenemies,spawnlocs),generateFWave(wave,totenemies,spawnlocs),generateBWave(wave,totenemies,spawnlocs)]

def hypot(x,y):
    return (x**2+y**2)**0.5


##LOAD PICTURES---------------------------------------------------------------------------------

walkermovepics = []
for i in range(8):
    walkermovepics.append(image.load("zombie sprites\\walkermove\\walker" + str(i) + ".png"))

bossmovepics=[]
for i in range(8):
    bossmovepics.append(image.load("zombie sprites\\bossmove\\boss" + str(i) + ".png"))

bossatkpics=[]
for i in range(8):
    bossatkpics.append(image.load("zombie sprites\\bossatk\\bossatk" + str(i) + ".png"))

herolegpics=[]
for i in range(8):
    herolegpics.append(image.load("zombie sprites\\herolegs\\leg" + str(i) + ".png"))

sprintermovepics=[]
for i in range(9):
    sprintermovepics.append(image.load("zombie sprites\\sprintermove\\sprintermove" + str(i) + ".png"))

fatmovepics=[]
for i in range(8):
    fatmovepics.append(image.load("zombie sprites\\fatmove\\fatmove" + str(i) + ".png"))
    
  
##--IMAGES--
staminaPic= image.load("zombie sprites\\StaminaSymbol.png")
ammo = image.load("zombie sprites\\ammo.png")
smgclipHUD = image.load("zombie sprites\\smgcliphud.png")


Map = image.load("zombie sprites\\finalmap.png")
GameMap = image.load("zombie sprites\\finalmap.png")
Treecover = image.load("zombie sprites\\treecoverfinal.png")
wallrubble95x29 = image.load("zombie sprites\\wallrubble95x29.png")
wallrubble30x26 = image.load("zombie sprites\\wallrubble30x26.png")

deadWalkpic= image.load('zombie sprites\\deadwalker.png')
deadFatpic= image.load('zombie sprites\\deadfatso.png')
deadSprintpic= image.load('zombie sprites\\deadsprinter.png')
deadBosspic= image.load('zombie sprites\\deadboss.png')

reloadPic = image.load("zombie sprites\\reloadpic.png")
pheroPic = image.load("zombie sprites\\pHero.png")
smgheroPic = image.load("zombie sprites\\smgHero.png")
arheroPic = image.load("zombie sprites\\arHero.png")
sgheroPic = image.load("zombie sprites\\sgHero.png")
lasheroPic = image.load("zombie sprites\\lasHero.png")

fcredit = image.load("zombie sprites\\credits.png")
finstructions = image.load("zombie sprites\\tutorial.png")
tscreen = image.load("zombie sprites\\Title Screen.png")

playerbutton= image.load("zombie sprites\\playerbutton.png")
pistolbutton= image.load("zombie sprites\\pistolbutton.png")
smgbutton= image.load("zombie sprites\\smgbutton.png")
arbutton= image.load("zombie sprites\\arbutton.png")
sgbutton= image.load("zombie sprites\\sgbutton.png")
lasbutton= image.load("zombie sprites\\lasbutton.png")
basebutton= image.load("zombie sprites\\basebutton.png")

rbuttons= [playerbutton,pistolbutton,smgbutton,arbutton,sgbutton,lasbutton,basebutton]

shopmain = image.load("zombie sprites\\shopmain.png")
playermain=image.load("zombie sprites\\playermain.png")
Pistolmain=image.load("zombie sprites\\pistolmain.png")
SMGmain=image.load("zombie sprites\\smgmain.png")
ARmain=image.load("zombie sprites\\armain.png")
SGmain=image.load("zombie sprites\\sgmain.png")
Lasmain=image.load("zombie sprites\\lasmain.png")
basemain=image.load("zombie sprites\\basemain.png")

upammobutton=image.load("zombie sprites\\upammobutton.png")
buyammobutton=image.load("zombie sprites\\buyammobutton.png")

bbuttons=[buyammobutton,upammobutton]

unlockbutton=image.load("zombie sprites\\unlockbutton.png")

healbutton=image.load("zombie sprites\\healbutton.png")
uphealbutton=image.load("zombie sprites\\uphealbutton.png")
upstambutton=image.load("zombie sprites\\upstambutton.png")
upacbutton=image.load("zombie sprites\\upacbutton.png")

pbuttons=[healbutton,uphealbutton,upstambutton,upacbutton]

##-----------------------------------------------------------

tsong= mixer.music.load("Title Screen Song.mp3")

psound= mixer.Sound("pistol1 shot.wav")
preload= mixer.Sound("pistol reload.wav")

smgsound= mixer.Sound("smg1 shot.wav")
smgreload= mixer.Sound("smg reload.wav")

arsound= mixer.Sound("ar1 shot.wav")
arreload= mixer.Sound("ar reload.wav")

sgsound= mixer.Sound("sg1 shot.wav")
sgreload= mixer.Sound("sg reload.wav")

lasersound= mixer.Sound("las shot.wav")
lasreload= mixer.Sound("laser reload.wav")


##OBJECT CLASSES----------------------------------------------------------------------------------------------------------
class wall(sprite.Sprite):
    def __init__(self, x, y, rect, brokeimage):

        self.x = x
        self.y = y
        self.rect = rect
        self.health = 1000
        self.tothealth = 1000
        self.brokeimage = brokeimage
        self.broken = False

    def checkhealth(self):
        if self.health<=0:
            self.broke()
        else:
            self.broken=False
            
    def broke(self):
        self.broken = True

    def draw(self,GameMap):
        GameMap.blit(self.brokeimage,(self.x,self.y))
            


wall1= wall(652, 652, Rect(633,632,135,70), wallrubble95x29)         #Top left horizontal rect
wall2= wall(652, 681, Rect(633,661,70,66), wallrubble30x26)          #Top left vertical rect
wall3= wall(811, 652, Rect(792,632,135,69), wallrubble95x29)         #Top right horizontal rect
wall4= wall(875, 681, Rect(856,661,70,66), wallrubble30x26)          #Top right vertical rect
wall5= wall(652, 797, Rect(633,778,135,70), wallrubble95x29)         #Bottom left horizontal rect
wall6= wall(652, 771, Rect(633,751,70,47), wallrubble30x26)          #Bottom left vertical rect
wall7= wall(811, 797, Rect(792,778,104,70), wallrubble95x29)         #Bottom right horizontal rect
wall8= wall(875, 771, Rect(856,751,70,77), wallrubble30x26)          #Bottom right vertical rect

walls= [wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8]


class gun(sprite.Sprite):
    def __init__(self,DMG,srd,clip,ammo,coolcnt,rSound):

        self.cooldown = 0
        self.DMG = DMG
        self.srd = srd
        self.clip = clip
        self.totclip = clip
        self.ammo = ammo
        self.totammo = ammo*3
        self.coolcnt = coolcnt
        self.rSound = rSound                         #Reload sound
        self.overheated = False                       #only for Laser Rifle
        self.heatlimit = 750
        self.overcnt = 0

    def greload(self):                          #Gunreload
        if self.totclip>self.ammo:
            self.clip=self.ammo
            self.ammo=0
        else:
            amt = self.totclip-self.clip
            self.clip = self.totclip
            self.ammo -= amt
            
                
Pistol = gun(35,10,10,80,600,preload)
SMG = gun(15,40,45,135,150,smgreload)
AR = gun(40,20,30,60,200,arreload)
SG = gun(80,30,4,24,600,sgreload)
Laser = gun(40,0,1,1,20,lasreload) 

def dealDamage(att,vic):
    select = player.gType           #Selected weapon does selected damage
    vic.health -= select.DMG

def SGblast(sx,sy,cx,cy):
    select= player.gType
    fcx,fcy= (cx+randint(int(-1*player.acmod*select.srd),int(player.acmod*select.srd))),(cy+randint(int(-1*player.acmod*select.srd),int(player.acmod*select.srd)))
    gdx,gdy= fcx-sx,sy-fcy
    if gdx==0:
        angle=math.radians(90)
    else:
        angle=math.atan2(gdy,gdx)
    drawSGshot(checkHit(sx,sy,fcx,fcy),checkHit(sx,sy,fcx+25*math.sin(angle),fcy-25*math.cos(angle)),checkHit(sx,sy,fcx-25*math.sin(angle),fcy+25*math.cos(angle)),checkHit(sx,sy,fcx+50*math.sin(angle),fcy-50*math.cos(angle)),checkHit(sx,sy,fcx-50*math.sin(angle),fcy+50*math.cos(angle)))

def singleShot(sx,sy,cx,cy):
    select=player.gType
    fcx,fcy=(cx+randint(int(-1*player.acmod*select.srd),int(player.acmod*select.srd))),(cy+randint(int(-1*player.acmod*select.srd),int(player.acmod*select.srd)))
    if select == Pistol:
        drawPshot(checkHit(sx,sy,fcx,fcy))
    elif select == SMG:
        drawSMGshot(checkHit(sx,sy,fcx,fcy))
    elif select == AR:
        drawARshot(checkHit(sx,sy,fcx,fcy))
    

def checkHit(sx,sy,fcx,fcy):
    select=player.gType
    gdx,gdy=fcx-sx,sy-fcy
    if gdx==0:
        angle=math.radians(90)
        if fcy>sy:
            for i in range(1480-int(fcy)):
                gx= player.x
                gy= int(player.y + i)
                for wall in walls:
                    if wall.rect.collidepoint(gx,gy) and wall.broken==False:
                        wall.health -= select.DMG
                        return (gx,gy)
                for e in enemies:
                    if e.rect.collidepoint(gx,gy):
                        dealDamage(player,e)
                        return (gx,gy)
            return (gx,gy) 
        if fcy<sy:
            for i in range(int(fcy)):
                gx= player.x
                gy= int(player.y - i)
                for wall in walls:
                    if wall.rect.collidepoint(gx,gy) and wall.broken==False:
                        wall.health -= select.DMG
                        return (gx,gy)
                for e in enemies:
                    if e.rect.collidepoint(gx,gy):
                        dealDamage(player,e)
                        return (gx,gy)
            return (gx,gy)
    else:
        angle=math.atan2(gdy,gdx)
    if fcx<=sx:
        for i in range(int(sx)):
            gx= int(player.x - i)
            gy= int(player.y + i*math.tan(angle))
            for wall in walls:
                if wall.rect.collidepoint(gx,gy) and wall.broken==False:
                    wall.health -= select.DMG
                    return (gx,gy)
            for e in enemies:
                    if e.rect.collidepoint(gx,gy):
                        dealDamage(player,e)
                        return (gx,gy)
        return(gx,gy)   
    for i in range(1560-int(sx)):
        gx= int(player.x + i)
        gy= int(player.y - i*math.tan(angle))
        for wall in walls:
            if wall.rect.collidepoint(gx,gy)and wall.broken==False:
                wall.health -= select.DMG
                return (gx,gy)
        for e in enemies:
                    if e.rect.collidepoint(gx,gy):
                        dealDamage(player,e)
                        return (gx,gy)
    return (gx,gy)

##--DRAW GUN SHOTS--

def drawPshot(endpos):
    draw.line(GameMap,(255,255,0),(playerpos),(endpos),1)
    psound.play()

def drawSMGshot(endpos):
    draw.line(GameMap,(255,255,0),(playerpos),(endpos),1)
    smgsound.play()

def drawARshot(endpos):
    draw.line(GameMap,(255,255,0),(playerpos),(endpos),1)
    arsound.play()

def drawSGshot(endpos1,endpos2,endpos3,endpos4,endpos5):
    draw.line(GameMap,(255,255,0),(playerpos),(endpos1),1)
    draw.line(GameMap,(255,255,0),(playerpos),(endpos2),1)
    draw.line(GameMap,(255,255,0),(playerpos),(endpos3),1)
    draw.line(GameMap,(255,255,0),(playerpos),(endpos4),1)
    draw.line(GameMap,(255,255,0),(playerpos),(endpos5),1)
    sgsound.play()

def drawLasshot(endpos):
    draw.line(GameMap,(0,0,255),(playerpos),(endpos),3)
    lasersound.play()
    

class Zombie(sprite.Sprite):
    def __init__(self, x, y, ang, movelist, atklist, deadimage, zType, health, mvspd, dmg, cooldown, cdRate, money, exp):

        self.x = x
        self.y = y
        self.ang = ang
        self.movelist = movelist
        self.omovelist = movelist      #Original movelist
        self.atklist = atklist
        self.deadimage = deadimage
        self.movframe = 0
        self.rect = 0

        self.zType = zType
        self.health = health
        self.mvspd = mvspd
        self.dmg = dmg
        self.cooldown = cooldown     #Attack cooldown
        self.cdRate = cdRate         #Rate of attack cooldown reset

        self.money = money
        self.exp = exp

#-- ENEMY SPAWN COST--
        if self.zType== 'Walker':         #There is a 1000 point limit for the amount of enemies that can appear on the screen at once. 
            self.cost= 100                #Every enemy has a point value, or cost.
        if self.zType== 'Sprinter':       #This controls how many enemies can appear on the screen.
            self.cost= 150
        if self.zType== 'Fatso':
            self.cost= 150 
        if self.zType== 'Boss':
            self.cost= 500

#--MOVE ENEMIES--
            
    def move(self,target):
        global walls
        sx,sy,dist = similarTri(self,target,self.mvspd)
        self.x += sx
        self.y += sy
        self.ang = math.degrees(math.atan2(-sy, sx))                          #Enemy will face you when approaching
        for wall in walls:
            if wall.rect.collidepoint(self.x,self.y) and wall.broken== False:
                self.x -= sx
                self.y -= sy
                wall.health -= self.dmg
        if self.zType == "Walker":
            self.rect = Rect(self.x-28,self.y-24,48,48)       #Different size collision rects for every enemy, depending on their size
            #draw.rect(screen, (0,255,0), self.rect)
        if self.zType == "Sprinter":
            self.rect = Rect(self.x-28,self.y-24,48,48)       #
        if self.zType == "Fatso":
            self.rect = Rect(self.x-28,self.y-24,48,48)       #
            #draw.rect(screen, (0,255,0), self.rect)
        if self.zType == "Boss":
            self.rect = Rect(self.x-80,self.y-90,160,180)     #
            #draw.rect(screen, (0,0,255), self.rect
     
#--DRAWING MAP AND MOVING ZOMBIES--
            
    def draw(self, GameMap):
        simage = transform.rotate(self.movelist[int(self.movframe)],self.ang-90)
        GameMap.blit(simage, (self.x-simage.get_width()//2,self.y-simage.get_height()//2))        
        
##        draw.rect(GameMap, (255,0,0),wall1)
##        draw.rect(GameMap, (0,0,255),wall2)
##        draw.rect(GameMap, (255,0,0),wall3)
##        draw.rect(GameMap, (0,0,255),wall4)
##        draw.rect(GameMap, (255,0,0),wall5)
##        draw.rect(GameMap, (0,0,255),wall6)
##        draw.rect(GameMap, (255,0,0),wall7)
##        draw.rect(GameMap, (0,0,255),wall8)
        

##        if boss in enemies:
##            #draw.rect(GameMap, (0,0,0), (self.x-20, self.y+80, 40, 10), 2)             
##            #draw.rect(GameMap, (0,255,0), (self.x-20, self.y+80.5, 40, 10))
##            draw.rect(GameMap, (0,255,0), (290+cameraX, 5+cameraY, int(boss.health/5), 10))
##            
##            if boss.health <=750:
##                draw.rect(GameMap, (255,165,0), (290+cameraX, 5+cameraY, int(boss.health/5), 10))
##                
##            if boss.health <=500:
##                draw.rect(GameMap, (255,255,0), (290+cameraX, 5+cameraY, int(boss.health/5), 10))
##l
##            if boss.health <=250:
##                draw.rect(GameMap, (255,0,0), (290+cameraX, 5+cameraY, int(boss.health/5), 10))
##            
##            draw.rect(GameMap, (0,0,0), (290+cameraX, 5+cameraY, 200, 10), 1)
##            
##            for i in range(20):
##                draw.line(GameMap,(0,0,0),(290+i*10+cameraX,5+cameraY),(290+i*10+cameraX,14+cameraY))
##            
##                    
        if self.zType=='Boss':
            self.movframe += .2
            if self.movframe > 7: self.movframe = 0
        else:
            self.movframe += .25                    #Speed of animation
            if self.movframe > 7: self.movframe = 0

#--CHECKING ENEMY STATUS--
    def checkhealth(self):
        if self.health<=0:
            self.die()

    def die(self):
        deadenemies.append(self)
        enemies.remove(self)
        allchars.remove(self)
        player.money += self.money                 #player is rewarded money and xp for the death of each zombie
        player.exp += self.exp                     #
        player.totmoney += self.money
        player.totexp += self.exp

    def drawdead(self,GameMap):
        dead= transform.rotate(self.deadimage, self.ang+90)  #Dead image is blit when zombie is killed
        GameMap.blit(dead, (self.x-dead.get_width()//2, self.y-dead.get_height()//2))
        
class hero(sprite.Sprite):
    def __init__(self, pimage, smgimage, arimage, sgimage, lasimage, rimage, gType, acmod, movelist, stamina, staminaCD, CDrate):
        sprite.Sprite.__init__(self)
        self.x = 50
        self.y = 50
        self.ang = 0
        self.gType = gType            #Gun Type
        self.acmod = acmod            #Accuracy modifier
        self.kicking = False
        self.kicked = False
        self.kickcnt = 0
        self.pimage = pimage          #Weapon images
        self.smgimage = smgimage      #
        self.arimage = arimage        #
        self.sgimage = sgimage        #
        self.lasimage = lasimage      #
        self.cimage = pimage
        self.previmage = pimage
        self.rimage = rimage
        self.mvspd = 5
        self.health = 50
        self.maxhealth = 50
        self.stamina = stamina
        self.maxstamina = 125
        self.staminaCD = 500
        self.CDrate = CDrate
        self.sprinting = False
        self.movelist = movelist
        self.moveframe = 0
        self.reloading = False
        self.reloaded = False
        self.reloadcnt = 0
        self.money = 10000
        self.exp = 0
        self.omoney = 0
        self.oexp = 0
        self.totmoney = 0
        self.totexp = 0
        self.dead = False
        self.lasunlocked = False

#--MOVE HERO--
        
    def move(self):
        global cameraX, cameraY
        smx,smy = mouse.get_pos()                       #Starting mx, my
        mx,my = smx+cameraX,smy+cameraY                 #New mx, my
        select = player.gType                           #Select gun type
        self.ang = math.degrees(math.atan2(mx-56,my-48))           
        keys= key.get_pressed()
        
        if keys[K_a]:
            self.x -= self.mvspd
            cameraX -= self.mvspd
            
            for wall in walls:                                                                  #Prevent hero from walking through solid walls
                if wall.rect.collidepoint(self.x,self.y) and wall.broken == False:              #
                    self.x += self.mvspd                                                        #
                    cameraX += self.mvspd                                                       #
                    
            if cameraX <= 0: 
                cameraX = 0
                
            if cameraX >= 780 or self.x > 1170:
                cameraX = 780
                
            if self.x <= 20:                                                                    #Prevents hero from walking off of the left of the map
                self.x = 20                                                                     #
            
        if keys[K_d]:
            self.x += self.mvspd
            cameraX +=self.mvspd
        
            for wall in walls:
                if wall.rect.collidepoint(self.x,self.y) and wall.broken == False:
                    self.x -= self.mvspd
                    cameraX -= self.mvspd
                    
            if cameraX <= 0 or self.x < 390:
                cameraX = 0
                
            if cameraX >= 780: 
                cameraX = 780
                
            if self.x >= 1540:                                                                      #Prevents hero from walking off of the right of the map
                self.x = 1540                                                                       #
            
        if keys[K_w]:
            self.y -= self.mvspd
            cameraY -=self.mvspd
            
            for wall in walls:
                if wall.rect.collidepoint(self.x,self.y) and wall.broken == False:
                    self.y += self.mvspd
                    cameraY += self.mvspd
                    
            if cameraY <= 0: 
                cameraY = 0
                
            if cameraY >= 740 or self.y > 1110:
                cameraY=740
                
            if self.y <= 20:                        #Prevents hero from walking off of the top of the map
                self.y = 20                         #
            
        if keys[K_s]:
            self.y += self.mvspd
            cameraY += self.mvspd
            
            for wall in walls:
                if wall.rect.collidepoint(self.x,self.y) and wall.broken == False:
                    self.y -= self.mvspd
                    cameraY -= self.mvspd
                    
            if cameraY <= 0 or self.y < 370:
                cameraY = 0
                
            if cameraY >= 740:
                cameraY = 740
                
            if self.y >= 1460:                      #Prevents hero from walking off of the bottom of the map
                self.y = 1460                       #

        if keys[K_LSHIFT] and self.stamina > 0:     #
            self.mvspd= 7                           #Activate sprint
            self.sprinting = True                   #    

        else:
            self.mvspd = 5
            
        if keys[K_r] and self.reloading == False and select.clip < select.totclip:     #Reload weapon
            self.sreload()

        if keys[K_SPACE] and self.stamina > 25 and self.kicked == False:
            self.kick()

#-- SELECTING WEAPON--
    def select(self):
        keys= key.get_pressed()
        if keys[K_1] and self.reloading == False:
            self.gType= Pistol
            self.cimage = self.pimage
        if keys[K_2] and self.reloading == False:
            self.gType= SMG
            self.cimage = self.smgimage
        if keys[K_3] and self.reloading == False:
            self.gType= AR
            self.cimage=self.arimage
        if keys[K_4] and self.reloading == False:
            self.gType= SG
            self.cimage = self.sgimage
        if keys[K_5] and self.reloading == False and self.lasunlocked== True:
            self.gType= Laser
            self.cimage = self.lasimage
            
##--
            
    def sreload(self):
        select = self.gType
        if select != Laser:
            select.rSound.play()
            self.reloading = True
            self.reloaded = True
            self.reloadcnt = 150
            self.previmage = self.cimage
            self.cimage = self.rimage
            select.ammo += select.clip
            select.clip = 0
        
        
    def sreloading(self):
        select=self.gType
        if self.reloading == True:
            self.reloadcnt -=1
            if self.reloadcnt == 0:
                self.cimage=self.previmage
                select.greload()
                self.reloading = False

    def kick(self):
        self.kicking = True
        self.kicked = True
        self.kickcnt = 50
        
    def skicking(self):
        if self.kicking == True:
            self.kicking = False
        if self.kicked == True:
            self.kickcnt -=1
            if self.kickcnt == 0:
                self.kicked = False
                
                
#--PLAYER UPDATES--
    def updateHealth(self):
        posRect = Rect(30+cameraX,717+cameraY,100,5)      
        posCover = GameMap.subsurface(posRect).copy()           #Takes copy of a small portion of the GameMap

        
        hlthFont = font.SysFont("Gill Sans Ultra Bold", 30)
        hlthtxt = hlthFont.render(str(self.health),True,(0,0,0))
        GameMap.blit(posCover,(30+cameraX,717+cameraY))
        GameMap.blit(hlthtxt,(30+cameraX,717+cameraY))

        
    def updateStamina(self):
        if self.sprinting == True and self.stamina > 0:
            self.stamina -= 1
            self.staminaCD = 500
 
        if self.stamina <= 0:
            self.sprinting == False

        if self.kicking == True:
            self.stamina -= 25
            self.staminaCD = 500
                         
        staminaFont = font.SysFont("Gill Sans Ultra Bold", 30)
        staminatxt= staminaFont.render(str(self.stamina),True,(0,0,0))        
        GameMap.blit(staminatxt, (100+cameraX,715+cameraY))
        GameMap.blit(staminaPic, (70+cameraX, 715+cameraY))

    def updateEXP(self):
        expFont = font.SysFont("Gill Sans Ultra Bold", 25)
        exptxt= expFont.render(str(self.exp)+ " xp" ,True,(255,255,0))        
        GameMap.blit(exptxt, (10+cameraX,10+cameraY))

    def updateMoney(self):
        moneyFont = font.SysFont("Gill Sans Ultra Bold", 25)
        moneytxt= moneyFont.render("$" + str(self.money),True,(255,255,0))        
        GameMap.blit(moneytxt, (10+cameraX,35+cameraY))

    def die(self):
        self.dead = True
##---------------------------------------------------------------------------------        

    def inRange(self, enemy):
        if distance(self.x, self.y, enemy.x, enemy.y) < 55:
            return True
        else:
            return False
        
##--DRAW HERO--
        
    def draw(self, GameMap):
        smx,smy = mouse.get_pos()                                   #Camera and mouse move in sync
        mx,my = smx+cameraX,smy+cameraY                             #
        angle = math.degrees(math.atan2(mx-self.x,my-self.y))
        keys= key.get_pressed()
        
        if keys[K_a] or keys[K_d] or keys[K_w] or keys[K_s]:                                #Move hero legs when move is initiated
            legs = transform.rotate(self.movelist[int(self.moveframe)], angle)
            GameMap.blit(legs, (self.x-legs.get_width()//2, self.y-legs.get_height()//2))
            
            if self.sprinting == True:                                                      #Increase animation speed when sprint it activated
                self.moveframe += .1                                                        #
            self.moveframe += .15                                                           #
            if self.moveframe > 7: self.moveframe = 0
            
        torso= transform.rotate(self.cimage, angle)                                         #Hero upperbody
        GameMap.blit(torso, (self.x-torso.get_width()//2,self.y-torso.get_height()//2))     #
        
##------------------------------------------------------------------------------------------------------------------     
    
def distance(x1, y1 , x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

##--CHECK DISTANCE BETWEEN HERO AND ZOMBIES--

def checkRange(enemies, player):
    global walls
    for enemy in enemies:
        if enemy.zType=='Boss':
            if distance(enemy.x,enemy.y,player.x,player.y) <150:
                enemy.movelist = enemy.atklist
                if enemy.cooldown <= 0:
                    player.health -= enemy.dmg
                    enemy.cooldown = 500
            else:
                enemy.movelist=enemy.omovelist
                
            
        elif player.inRange(enemy)and enemy.cooldown <= 0:
            player.health -= enemy.dmg
            enemy.cooldown = 500
            
        if player.health <= 0:
            player.die()

        if distance(enemy.x,enemy.y,player.x,player.y) <100 and player.kicking == True:
            enemy.health -= 50
            if player.x < enemy.x:
                enemy.x+= 30
            else:
                enemy.x-=30
            if player.y < enemy.x:
                enemy.y+= 30
            else:
                enemy.y-=30

##-------------------------------------------------------------------------------------------------            

def cooldowns():
    for enemy in enemies:                                   #Cooldown is decreased by cdRate, when cooldown hits
        enemy.cooldown -= enemy.cdRate                      #zero, enemy will attack again

    if player.stamina < player.maxstamina and player.sprinting == False and player.staminaCD > 0:  #If stamina falls below its max and the player is not using any stamina,
        player.staminaCD -= player.CDrate                                            #it will initiate the cooldown timer before stamina regenerates
        
        if player.staminaCD <= 0 and player.stamina <= 250:                          #Stamina regenerates, the cooldown is reset
           player.stamina += 1                                                       #
           player.staminaCD = 25                                                     #
    
          
def drawMoving(GameMap, enemies, player):
    for corpse in deadenemies:
        corpse.drawdead(GameMap)
    for enemy in enemies:
        enemy.draw(GameMap)
    player.draw(GameMap)

def drawTrees(GameMap, treecover):               #Tree cover is a unique attribute of the map that blocks the player's vision when he is
    GameMap.blit(Treecover, (0,0))               #beneath several trees, rendering him incapable of seeing incoming zombies

def drawCrosshair(player):
    select = player.gType
    if select == Laser:
        draw.circle(GameMap,(255,0,0),(mx,my),int(5),1)
    else:
        draw.circle(GameMap,(255,0,0),(mx,my),int(player.acmod*2*select.srd),1)   #Crosshair is changed depending on a weapons accuracy

def updateWave(GameMap, wave):
    waveFont = font.SysFont("Gill Sans Ultra Bold", 25)
    if wave % 5== 0:
        wavetxt= waveFont.render(" WAVE %s" %(wave),True,(255,0,0))
    else:
        wavetxt= waveFont.render(" WAVE %s" %(wave),True,(255,255,0))
    GameMap.blit(wavetxt, (10+cameraX,55+cameraY))
    

##--SHOOTING----------------------
def heroshoot(player):
    select=player.gType
    if select == Laser:
        if select.overheated==True:
                select.overcnt -= 1
                if select.overcnt <= 0:
                    select.overheated= False
                if select.overcnt%5==0:
                    select.rSound.play()
        
    if mb[0]==1:
        if select==SG and select.cooldown<=0 and select.clip>0:
            SGblast(player.x,player.y,mx,my)
            select.cooldown+=select.coolcnt
            select.clip-=1
        
        elif select==Laser:
            if select.cooldown > select.heatlimit and select.overheated==False:
                select.overheated = True
                select.overcnt = 300
            elif select.cooldown < select.heatlimit and select.overheated==False:
                drawLasshot(checkHit(player.x,player.y,mx,my))
                select.cooldown+=15
                
        elif select.cooldown<=0 and select.clip>0:
            singleShot(player.x,player.y,mx,my)
            select.cooldown+=select.coolcnt
            select.clip-=1
                
##--DRAW AMMO AND CLIP COUNTER--
def ammocnt(player):                                                      
    select= player.gType
    ammofont= font.SysFont('Gill Sans Ultra Bold',30)
    text= ammofont.render(str(select.clip),True,(0,0,0))
    ammotext= ammofont.render(str(select.ammo),True,(0,0,0))
    GameMap.blit(ammo,(65+cameraX,675+cameraY))
    GameMap.blit(smgclipHUD,(5+cameraX,660+cameraY))
    GameMap.blit(smgclipHUD,(11+cameraX,660+cameraY))
    GameMap.blit(smgclipHUD,(17+cameraX,660+cameraY))
    GameMap.blit(text,(30+cameraX,680+cameraY))
    GameMap.blit(ammotext,(100+cameraX,680+cameraY))
    
##---
    
def Guncooldowns():
    Pistol.cooldown -= 10
    SMG.cooldown -= 25
    AR.cooldown -= 25
    SG.cooldown -= 10
    Laser.cooldown -= 5

def gunreset():
    if mb[0]==0:
        Pistol.cooldown = 0
        SMG.cooldown = 0
        AR.cooldown = 0
    if SG.cooldown<0:
        SG.cooldown= 0
    if Laser.cooldown<0:
        Laser.cooldown= 0

def moveEnemies(enemies, player):
    for enemy in enemies:
        enemy.move(player)
    for a in allchars:
        push(a,allchars)
        
##--UPDATES ON MAP--
def EnemiesUpdate(enemies):
    global pointtot
    pointtot=0
    for enemy in enemies:
        enemy.checkhealth()
        pointtot+=enemy.cost
        
def playerpos():
    global pointtot
    pointtot = 0
    for enemy in enemies:
        enemy.checkhealth()
        pointtot += enemy.cost

def wallsUpdate(walls):
    for wall in walls:
        wall.checkhealth()

def drawRubble(Gamemap,walls):
    for wall in walls:
        if wall.broken==True:
            wall.draw(GameMap)
        
##--HEALTH CROSS SYMBOL--
def drawCross():
    draw.line(GameMap,(255,0,0),(15+cameraX,725+cameraY),(25+cameraX,725+cameraY),5)
    draw.line(GameMap,(255,0,0),(15+cameraX,725+cameraY),(5+cameraX,725+cameraY),5)
    draw.line(GameMap,(255,0,0),(15+cameraX,725+cameraY),(15+cameraX,715+cameraY),5)
    draw.line(GameMap,(255,0,0),(15+cameraX,725+cameraY),(15+cameraX,735+cameraY),5)

def drawScene(screen):
    view = Rect(0 +cameraX,0 +cameraY,780,740)    
    screen.blit(GameMap.subsurface(view),(0,0))
                     
init()
size = width, height= 780, 740
screen = display.set_mode(size)
display.set_caption("Dead Sight!")

cameraX, cameraY = 0,0             #Start position of camera
mx,my = 0,0
mb = mouse.get_pressed()

player = hero(pheroPic, smgheroPic, arheroPic, sgheroPic, lasheroPic, reloadPic, Pistol, 1, herolegpics, 125, 250, 5)
wave = 0
enemies = []
deadenemies = []
totenemies = []

##--PREVENT ENEMY AND HERO OVERLAP--
def push(guy,badGuys):                              #Mr.Mckenzie code
    for bg in badGuys:
        if guy is not bg:
            sx,sy,dist = similarTri(guy,bg,1)
            if dist < 40:
                amount = 40 - dist
                bg.x += sx * amount**.5 
                bg.y += sy * amount**.5

def similarTri(p1,p2,size):
    bigX = p2.x-p1.x
    bigY = p2.y-p1.y
    dist = hypot(bigX,bigY)
    dist = max(1,dist)
    sx = bigX * size/dist
    sy = bigY * size/dist
    return sx,sy,dist
##----------------------------------

##--WAVE MECHANIC--
def waveSelect(wave):
    if wave%5 == 0:
        chosen=randint(0,6)
        if chosen == 0:
            generateDDWave(wave,totenemies,spawnlocs)
        elif chosen == 1:
           generateDHWave(wave,totenemies,spawnlocs)
        elif chosen == 2:
           generateWWave(wave,totenemies,spawnlocs)
        elif chosen == 3:
           generateSWave(wave,totenemies,spawnlocs)
        elif chosen == 4:
           generateFWave(wave,totenemies,spawnlocs)
        elif chosen == 5:
           generateDDWave(wave,totenemies,spawnlocs)
    else:
         generateNWave(wave,totenemies,spawnlocs)

def generateNWave(wave,totenemies,spawnlocs):
    for w in range(randint(3,5)*wave//3):
        spawnloc=choice(spawnlocs)
        walker = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,walkermovepics,walkermovepics,deadWalkpic,"Walker",250,1,5,0,5,10,25)
        totenemies.append(walker)
    for s in range(randint(1,3)*wave//3):
        spawnloc=choice(spawnlocs)
        sprinter = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,sprintermovepics,sprintermovepics,deadSprintpic,"Sprinter",200,2,3,0,5,25,50)
        totenemies.append(sprinter)
    for f in range(randint(1,3)*wave//3):
        spawnloc=choice(spawnlocs)
        fatso = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,fatmovepics,fatmovepics,deadFatpic,"Fatso",350,.75,8,0,5,50,75)
        totenemies.append(fatso)
    for b in range(randint(0,2)*wave//10):
        spawnloc=choice(spawnlocs)
        boss = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]), 0, bossmovepics, bossatkpics, deadBosspic,"Boss",2000,.5,15,0,5,100,100)
        totenemies.append(boss)

def generateDDWave(wave,totenemies,spawnlocs):
    for w in range(randint(3,5)*wave//3):
        spawnloc=choice(spawnlocs)
        walker = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,walkermovepics,walkermovepics,deadWalkpic,"Walker",250,1,5*2,0,5,10,25)
        totenemies.append(walker)
    for s in range(randint(1,3)*wave//3):
        spawnloc=choice(spawnlocs)
        sprinter = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,sprintermovepics,sprintermovepics,deadSprintpic,"Sprinter",200,2,3*2,0,5,25,50)
        totenemies.append(sprinter)
    for f in range(randint(1,3)*wave//3):
        spawnloc=choice(spawnlocs)
        fatso = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,fatmovepics,fatmovepics,deadFatpic,"Fatso",350,.75,8*2,0,5,50,75)
        totenemies.append(fatso)
    for b in range(randint(0,2)*wave//10):
        spawnloc=choice(spawnlocs)
        boss = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,bossmovepics, bossatkpics, deadBosspic,"Boss",2000,.5,15*2,0,5,100,100)
        totenemies.append(boss)

def generateDHWave(wave,totenemies,spawnlocs):
    for w in range(randint(3,5)*wave//3):
        spawnloc=choice(spawnlocs)
        walker = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,walkermovepics,walkermovepics,deadWalkpic,"Walker",250*2,1,5,0,5,10,25)
        totenemies.append(walker)
    for s in range(randint(1,3)*wave//3):
        spawnloc=choice(spawnlocs)
        sprinter = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,sprintermovepics,sprintermovepics,deadSprintpic,"Sprinter",200*2,2,3,0,5,25,50)
        totenemies.append(sprinter)
    for f in range(randint(1,3)*wave//3):
        spawnloc=choice(spawnlocs)
        fatso = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,fatmovepics,fatmovepics,deadFatpic,"Fatso",350*2,.75,8,0,5,50,75)
        totenemies.append(fatso)
    for b in range(randint(0,2)*wave//10):
        spawnloc=choice(spawnlocs)
        boss = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,bossmovepics, bossatkpics, deadBosspic,"Boss",2000*2,.5,15,0,5,100,100)
        totenemies.append(boss)

def generateWWave(wave,totenemies,spawnlocs):
    for w in range(randint(15,25)*wave//3):
        spawnloc=choice(spawnlocs)
        walker = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,walkermovepics,walkermovepics,deadWalkpic,"Walker",250,1,5,0,5,10,25)
        totenemies.append(walker)

def generateSWave(wave,totenemies,spawnlocs):
    for s in range(randint(9,15)*wave//3):
        spawnloc=choice(spawnlocs)
        sprinter = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,sprintermovepics,sprintermovepics,deadSprintpic,"Sprinter",200,2,3,0,5,25,50)
        totenemies.append(sprinter)

def generateFWave(wave,totenemies,spawnlocs):  
    for f in range(randint(9,15)*wave//3):
        spawnloc=choice(spawnlocs)
        fatso = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0,fatmovepics,fatmovepics,deadFatpic,"Fatso",350,.75,8,0,5,50,75)
        totenemies.append(fatso)

def generateBWave(wave,totenemies,spawnlocs):
    for b in range(randint(3,6)*wave//10 + 5):
        spawnloc=choice(spawnlocs)
        boss = Zombie(randint(spawnloc[0],spawnloc[1]),randint(spawnloc[2],spawnloc[3]),0, bossmovepics, bossatkpics, deadBosspic,"Boss",2000,.5,15,0,5,100,100)
        totenemies.append(boss)

def spawnWave():
    global pointtot,totenemies
    while pointtot<1500:
        if len(totenemies)>0:
            mook=choice(totenemies)
            enemies.append(mook)
            allchars.append(mook)
            totenemies.remove(mook)
            pointtot+=mook.cost
        if len(totenemies)==0 and pointtot<1500:
            break
##---------------------------------------------------------------------------------

##--MAIN GAME LOOP--       
def game():
    global mx,my,mb,boss,playerpos,enemies,deadenemies,allchars,wave,totenemies,pointtot

    GameMap.blit(Map,(0,0))
    player.omoney,player.oexp = player.money,player.exp
    totenemies= []
    enemies= []
    deadenemies= []
    wave+=1
    pointtot=0
    waveSelect(wave)
    allchars=[]
    allchars.append(player)
    spawnWave()
    myClock = time.Clock()
    mouse.set_visible(False)

    running = True
    while running:
        for e in event.get():
            if e.type == QUIT:
                return 'exit'
            if e.type == KEYUP:
                player.sprinting = False 
            
        if pointtot < 1500:                         #Check to see if more enemies need to be spawned
            spawnWave() 
        if len(enemies)== 0:
            running = False                         #Ends wave when all enemies are dead
        if player.dead== True:
            return 'lose'
        keys=key.get_pressed()
        if keys[K_ESCAPE]:
            return 'menu'
        
        smx,smy = mouse.get_pos()
        mx,my = smx+cameraX,smy+cameraY 
        mb = mouse.get_pressed()
        playerpos=(player.x,player.y)

       

        GameMap.blit(Map, (0,0))                     #Clears previous map

#BEHIND THE SCENES CACLULATIONS-------------------------------------
        
        moveEnemies(enemies, player)
        checkRange(enemies, player)
        EnemiesUpdate(enemies)
        wallsUpdate(walls)

##PLAYER INPUT-------------------------------------------------------
        
        player.move()
        checkRange(enemies, player)
        player.select()
        heroshoot(player)
        if player.reloading==True:
            player.sreloading()
            
            
#GAME MAP AND HUD UPDATES--------------------------------------------------

        drawRubble(GameMap, walls)
        drawMoving(GameMap, enemies, player)
        drawTrees(GameMap,Treecover)
        
        drawCrosshair(player)
        drawCross()
        ammocnt(player)
        player.updateHealth()
        player.updateStamina()
        player.updateEXP()
        player.updateMoney()

##END OF LOOP CALCULATIONS-----------------------------------------------

        cooldowns()
        Guncooldowns()
        gunreset()
        updateWave(GameMap, wave)

#FINAL DRAW TO SCREEN----------------------------------------------------
        drawScene(screen)

        if player.kicked == True:
            player.skicking()
        
        myClock.tick(50)
        display.flip()
    return 'win'

##--MENU AND SHOP--
def menu():
    mixer.music.play()
    mouse.set_visible(True)
    playRect= Rect(67,168,85,32)
    insRect= Rect(65,245,215,32)
    credRect= Rect(65,323,130,36)
    running = True
    myClock = time.Clock()
    buttons = [playRect, insRect, credRect]
    vals = ["game","instructions","credit"]
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"

        mpos = mouse.get_pos()
        mb = mouse.get_pressed()
        
        screen.blit(tscreen,(0,0))

        for r,v in zip(buttons,vals):
            if r.collidepoint(mpos):
                draw.rect(screen,(255,255,255),r,2)
                if mb[0]==1:
                    for i in range(255,0,-1):
                        screen.fill((0,0,0))
                        tscreen.set_alpha(i)
                        screen.blit(tscreen,(0,0))
                        tscreen.set_alpha(255)
                        display.flip()
                    time.wait(25)
                    if v == 'game':
                        mixer.music.stop()
                    return v
            
                
        display.flip()

def shop():
    global player, Pistol, SMG, AR, SG, Laser, walls, rbuttons, bbuttons
    shoppage = 'smain'

    while shoppage != "exit":
        if shoppage == "smain":
            shoppage = smain()
        if shoppage == "splayer":
            shoppage = splayer()
        if shoppage == "sPistol":
            shoppage = sPistol()    
        if shoppage == 'sSMG':
            shoppage = sSMG()    
        if shoppage == 'sAR':
            shoppage = sAR()    
        if shoppage == 'sSG':
            shoppage = sSG()
        if shoppage == 'sLaser':
            shoppage= sLaser()
        if shoppage == 'sbase':
            shoppage= sbase()
            
    return 'game'

def smain():
    mouse.set_visible(True)
    screen.blit(shopmain,(0,0))
    smainfont= font.SysFont("Gill Sans Ultra Bold", 16)
    mtxt= smainfont.render('MONEY : %s' %(player.money),True,(255,7,7))
    etxt= smainfont.render('EXP : %s' %(player.exp),True,(255,7,7))
    running = True
    myClock = time.Clock()
    buttons = [Rect(200,y*50+200,100,30) for y in range(7)]
    vals = ["splayer","sPistol",'sSMG','sAR','sSG','sLaser','sbase']
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"

        mtxt= smainfont.render('MONEY : %s' %(player.money),True,(0,0,0))
        etxt= smainfont.render('EXP : %s' %(player.exp),True,(0,0,0))    
        screen.blit(shopmain,(0,0))
        screen.blit(mtxt,(100,150))
        screen.blit(etxt,(680,150))
        
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        keys=key.get_pressed()
        if keys[K_KP_ENTER]:
            return 'exit'
        
        for r,v,b in zip(buttons,vals,rbuttons):
            screen.blit(b,(r.x,r.y))
            if r.collidepoint(mpos):
                draw.rect(screen,(255,255,255),r,2)
                if mb[0]==1:
                    return v
                           
        display.flip()

def splayer():
    screen.blit(playermain,(0,0))
    splayerfont= font.SysFont("Gill Sans Ultra Bold", 16)
    mtxt= splayerfont.render('MONEY : %s' %(player.money),True,(255,7,7))
    etxt= splayerfont.render('EXP : %s' %(player.exp),True,(255,7,7))
    clicked = False
    buttons = [Rect(200,y*50+300,100,30) for y in range(4)]
    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
            
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        keys=key.get_pressed()
        if keys[K_RETURN]:
            return 'smain'
        
        screen.blit(playermain,(0,0))
        mtxt= splayerfont.render('MONEY : %s' %(player.money),True,(255,7,7))
        etxt= splayerfont.render('EXP : %s' %(player.exp),True,(255,7,7))
        screen.blit (mtxt,(100,150))
        screen.blit (etxt,(680,150))

        htxt= splayerfont.render('HEALTH : %s  HEAL COST : $500' %(player.health),True,(255,7,7))
        screen.blit (htxt,(200,285))

        mhtxt= splayerfont.render('MAX HEALTH : %s  UPGRADE COST : %s' %(player.maxhealth,(((player.maxhealth-50)//25)+1)*1000),True,(255,7,7))
        screen.blit (mhtxt,(200,335))

        htxt= splayerfont.render('MAX STAMINA : %s  UPGRADE COST : %s' %(player.maxstamina,(((player.maxstamina-125)//25)+1)*750),True,(255,7,7))
        screen.blit (htxt,(200,385))

        atxt= splayerfont.render('ACMOD : %s  UPGRADE COST : 2000' %(player.acmod),True,(255,7,7))
        screen.blit (atxt,(200,435))

        for r,b in zip(buttons,pbuttons):
            screen.blit(b,(r.x,r.y))
            if r.collidepoint(mpos):
                draw.rect(screen,(255,255,255),r,2)
                
        if mb[0]==1:
            if clicked ==False:
                if buttons[0].collidepoint(mpos):
                    if player.health < player.maxhealth and player.money > 500:
                        player.health = player.maxhealth
                        player.money-=500
                if buttons[1].collidepoint(mpos):
                    if player.exp > ((player.maxhealth-50)//25+1)*1000:
                        player.maxhealth+= 25
                        player.exp -= ((player.maxhealth-50)//25+1)*1000
                if buttons[2].collidepoint(mpos):
                    if player.exp > ((player.maxstamina-125)//25+1)*750:
                        player.maxstamina += 25
                        player.exp -= ((player.maxstamina-125)//25+1)*750
                if buttons[3].collidepoint(mpos):
                    if player.exp > 2000 and player.acmod>0.25:
                        player.acmod -= 0.05
                        safe= round(player.acmod,2)
                        player.acmod = safe
                        player.exp -= 2000
            clicked = True
        if mb[0]==0: 
            clicked =False
                
        display.flip()
        
def sPistol():
    screen.blit(Pistolmain,(0,0))
    sPistolfont= font.SysFont("Gill Sans Ultra Bold", 16)
    mtxt= sPistolfont.render('MONEY : %s' %(player.money),True,(255,7,7))
    clicked=False
    buttons = [Rect(200,y*50+200,100,30) for y in range(2)]

    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
            
        screen.blit(Pistolmain,(0,0))
        mtxt= sPistolfont.render('MONEY : %s' %(player.money),True,(255,7,7))
        screen.blit (mtxt,(390,150))
        
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        ctxt = sPistolfont.render('AMMO : %s  COST(10) : $5' %(Pistol.ammo),True,(255,7,7))
        screen.blit(ctxt,(200, 180))
                                   
        uptxt= sPistolfont.render('MAX AMMO : %s   COST  : $%s' %(Pistol.totammo,((Pistol.totammo-200)//50+1)*500),True,(255,7,7))
        screen.blit(uptxt,(200, 300))
        
        keys=key.get_pressed()
        if keys[K_RETURN]:
            return 'smain'


        for r,b in zip(buttons,bbuttons):
            screen.blit(b,(r.x,r.y))
            if r.collidepoint(mpos):
                draw.rect(screen,(255,255,255),r,2)
        if mb[0]==1:
            if clicked ==False:
                if buttons[0].collidepoint(mpos):
                    if Pistol.ammo < Pistol.totammo and player.money > 5:
                        Pistol.ammo+= 10
                        player.money-=5
                        if Pistol.ammo > Pistol.totammo:
                            Pistol.ammo = Pistol.totammo
                if buttons[1].collidepoint(mpos):
                    if player.money > ((Pistol.totammo-200)//50+1)*500:
                        Pistol.totammo+= 50
                        player.money -= ((Pistol.totammo-200)//50+1)*500
            clicked= True
        if mb[0]==0: 
            clicked=False
                           
        display.flip()

def sSMG():
    screen.blit(SMGmain,(0,0))
    sSMGfont= font.SysFont("Gill Sans Ultra Bold", 16)
    mtxt= sSMGfont.render('MONEY : %s' %(player.money),True,(255,7,7))
    clicked=False
    buttons = [Rect(200,y*50+200,100,30) for y in range(2)]

    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
            
        screen.blit(SMGmain,(0,0))
        mtxt= sSMGfont.render('MONEY : %s' %(player.money),True,(255,7,7))
        screen.blit (mtxt,(390,150))
        
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        ctxt = sSMGfont.render('AMMO : %s  COST(45) : $75' %(SMG.ammo),True,(255,7,7))
        screen.blit(ctxt,(200, 180))
                                   
        uptxt= sSMGfont.render('MAX AMMO : %s   COST  : $%s' %(SMG.totammo,((SMG.totammo-270)//90+1)*500),True,(255,7,7))
        screen.blit(uptxt,(200, 300))
        
        keys=key.get_pressed()
        if keys[K_RETURN]:
            return 'smain'


        for r,b in zip(buttons,bbuttons):
            screen.blit(b,(r.x,r.y))
            if r.collidepoint(mpos):
                draw.rect(screen,(255,255,255),r,2)
        if mb[0]==1:
            if clicked ==False:
                if buttons[0].collidepoint(mpos):
                    if SMG.ammo < SMG.totammo and player.money > 15:
                        SMG.ammo+= 45
                        player.money-=75
                        if SMG.ammo > SMG.totammo:
                            SMG.ammo = SMG.totammo
                if buttons[1].collidepoint(mpos):
                    if player.money > ((SMG.totammo-270)//90+1)*500:
                        SMG.totammo+= 90
                        player.money -= ((SMG.totammo-270)//90+1)*500
            clicked= True
        if mb[0]==0: 
            clicked=False
                           
                           
        display.flip()
        
def sAR():
    screen.blit(ARmain,(0,0))
    sARfont= font.SysFont("Gill Sans Ultra Bold", 16)
    mtxt= sARfont.render('MONEY : %s' %(player.money),True,(255,7,7))
    clicked=False
    buttons = [Rect(200,y*50+200,100,30) for y in range(2)]

    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
            
        screen.blit(ARmain,(0,0))
        mtxt= sARfont.render('MONEY : %s' %(player.money),True,(255,7,7))
        screen.blit (mtxt,(390,150))
        
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        ctxt = sARfont.render('AMMO : %s  COST(30) : $105' %(AR.ammo),True,(255,7,7))
        screen.blit(ctxt,(200, 180))
                                   
        uptxt= sARfont.render('MAX AMMO : %s   COST  : $%s' %(AR.totammo,((AR.totammo-210)//60+1)*500),True,(255,7,7))
        screen.blit(uptxt,(200, 300))
        
        keys=key.get_pressed()
        if keys[K_RETURN]:
            return 'smain'


        for r,b in zip(buttons,bbuttons):
            screen.blit(b,(r.x,r.y))
            if r.collidepoint(mpos):
                draw.rect(screen,(255,255,255),r,2)
        if mb[0]==1:
            if clicked==False:
                if buttons[0].collidepoint(mpos):
                    if AR.ammo < AR.totammo and player.money > 5:
                        AR.ammo+= 30
                        player.money-=105
                        if AR.ammo > AR.totammo:
                            AR.ammo = AR.totammo
                if buttons[1].collidepoint(mpos):
                    if player.money > ((AR.totammo-210)//60+1)*500:
                        AR.totammo+= 60
                        player.money -= ((AR.totammo-210)//60+1)*500
            clicked= True
        if mb[0]==0: 
            clicked=False
                                                      
        display.flip()
        
def sSG():
    screen.blit(SGmain,(0,0))
    sSGfont= font.SysFont("Gill Sans Ultra Bold", 16)
    mtxt= sSGfont.render('MONEY : %s' %(player.money),True,(255,7,7))
    clicked=False
    buttons = [Rect(200,y*50+200,100,30) for y in range(2)]

    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
            
        screen.blit(SGmain,(0,0))
        mtxt= sSGfont.render('MONEY : %s' %(player.money),True,(255,7,7))
        screen.blit (mtxt,(390,150))
        
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        ctxt = sSGfont.render('AMMO : %s  COST(4) : $40' %(SG.ammo),True,(255,7,7))
        screen.blit(ctxt,(200, 180))
                                   
        uptxt= sSGfont.render('MAX AMMO : %s   COST  : $%s' %(SG.totammo,((SG.totammo-80)//16+1)*500),True,(255,7,7))
        screen.blit(uptxt,(200, 300))
        
        keys=key.get_pressed()
        if keys[K_RETURN]:
            return 'smain'


        for r,b in zip(buttons,bbuttons):
            screen.blit(b,(r.x,r.y))
            if r.collidepoint(mpos):
                draw.rect(screen,(255,255,255),r,2)
        if mb[0]==1:
            if clicked ==False:
                if buttons[0].collidepoint(mpos):
                    if SG.ammo < SG.totammo and player.money > 5:
                        SG.ammo+= 4
                        player.money-=40
                        if SG.ammo > SG.totammo:
                            SG.ammo = SG.totammo
                if buttons[1].collidepoint(mpos):
                    if player.money > ((SG.totammo-80)//16+1)*500:
                        SG.totammo+= 16
                        player.money -= ((SG.totammo-80)//16+1)*500
            clicked= True
        if mb[0]==0: 
            clicked=False
                           
        display.flip()
def sLaser():
    screen.blit(Lasmain,(0,0))
    sLaserfont= font.SysFont("Gill Sans Ultra Bold", 16)
    mtxt= sLaserfont.render('MONEY : %s' %(player.money),True,(255,7,7))
    clicked=False
    unlock = Rect(200,200,100,30)
    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
            
        screen.blit(Lasmain,(0,0))
        mtxt= sLaserfont.render('MONEY : %s' %(player.money),True,(255,7,7))
        screen.blit (mtxt,(390,150))
        
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        keys=key.get_pressed()
        if keys[K_RETURN]:
            return 'smain'

        utxt = sLaserfont.render('UNLOCK COST : $10 000',True,(255,7,7))
        screen.blit(utxt,(200, 180))

        screen.blit(unlockbutton,(unlock.x,unlock.y))
        if mb[0]==1:
            if unlock.collidepoint(mpos) and player.money > 10000 and player.lasunlocked==False :
                    player.lasunlocked=True
                    player.money-=10000
        display.flip()                         

def sbase():
    mouse.set_visible(True)
    screen.blit(basemain,(0,0))
    sbasefont= font.SysFont("Gill Sans Ultra Bold", 16)
    mtxt= sbasefont.render('MONEY : %s' %(player.money),True,(255,7,7))
    clicked=False
    running = True
    myClock = time.Clock()
    repair= Rect(200,400,100,30)
    build=Rect(600,400,100,30)
    buttons = [Rect(200,y*50+200,100,30) for y in range(7)]
    vals = ["splayer","sPistol",'sSMG','sAR','sSG','sLaser','sbase']
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"
            
        screen.blit(basemain,(0,0))
        mtxt= sbasefont.render('MONEY : %s' %(player.money),True,(255,7,7))
        screen.blit (mtxt,(390,150))
        
        mpos = mouse.get_pos()
        mb = mouse.get_pressed()

        for i in range(8):
            wtxt= sbasefont.render('WALL%s HEALTH : %s' %(i,walls[i].health),True,(255,7,7))
            screen.blit(wtxt,(100, 150 + 20*i))
                                   
        maxtxt= sbasefont.render('MAX WALL HEALTH : %s' %(walls[1].tothealth),True,(255,7,7))
        screen.blit(maxtxt,(100, 330))
        
        keys=key.get_pressed()
        if keys[K_RETURN]:
            return 'smain'
        
        reptxt= sbasefont.render('REPAIR COST: $500',True,(255,7,7))
        screen.blit(reptxt,(repair.x,repair.y-20))

        buildtxt= sbasefont.render('UPGRADE COST: %s' %(2000*((walls[i].tothealth-1000)//1000+1)),True,(255,7,7))
        screen.blit(buildtxt,(build.x,build.y-20))

        draw.rect(screen,(255,7,7),repair)
        draw.rect(screen,(255,7,7),build)
        if mb[0]==1:
            if clicked==False:
                if repair.collidepoint(mpos) and player.money > 500:
                    for wall in walls:
                        wall.health= wall.tothealth
                    player.money-= 500
                if build.collidepoint(mpos) and player.money > 2000*((walls[i].tothealth-1000)//1000 + 1):
                    for wall in walls:
                        wall.tothealth+=1000
                        wall.health= wall.tothealth
                    player.money-= 2000*((walls[i].tothealth-1000)//1000 + 1)
            clicked= True
             
        if mb[0]==0: 
            clicked=False
            
        display.flip()

def instructions():
    mouse.set_visible(True)
    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"

        keys=key.get_pressed()
        if keys[K_ESCAPE]:
            return 'menu'

        screen.blit(finstructions,(0,0))
        
                
        display.flip()
                
        display.flip()
    
def credit():
    mouse.set_visible(True)
    
    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"

        keys=key.get_pressed()
        if keys[K_ESCAPE]:
            return 'menu'

        screen.blit(fcredit,(0,0))     
        display.flip()

def lose():
    global wave,player
    mouse.set_visible(True)
    screen.fill((0,0,0))
    lbfont=  font.SysFont("Gill Sans Ultra Bold", 56)
    losetitle = lbfont.render('You Survived %s Waves' %(str(wave-1)),True,(255,7,7))
    screen.blit(losetitle,(100,100))
    lsfont = font.SysFont("Gill Sans Ultra Bold", 48)
    score = player.totmoney+player.totexp
    scoretxt = lsfont.render('Your final score was %s ' %(str(score)),True,(255,7,7))
    screen.blit(scoretxt,(100,300))
    player = hero(pheroPic, smgheroPic, arheroPic, sgheroPic, lasheroPic, reloadPic, Pistol, 0.5, herolegpics, 250, 250, 5)
    wave = 0
    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"

        keys=key.get_pressed()
        if keys[K_ESCAPE]:
            return 'menu'
        
        display.flip()

def win():
    global wave,player
    mouse.set_visible(True)
    screen.fill((0,0,0))
    wbfont=  font.SysFont("Gill Sans Ultra Bold", 56)
    wintitle = wbfont.render('You Survived Wave %s ' %(str(wave)),True,(255,7,7))
    screen.blit(wintitle,(100,100))
    wsfont = font.SysFont("Gill Sans Ultra Bold", 48)
    scoretxt = wsfont.render('You earned $%s  and %s EXP ' %(player.money-player.omoney,player.exp-player.oexp),True,(255,7,7))
    screen.blit(scoretxt,(100,300))
    cont= wsfont.render(('PRESS ENTER TO CONTINUE'),True,(255,7,7))
    screen.blit(cont,(100,500))
    running = True
    myClock = time.Clock()
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                return "exit"

        keys=key.get_pressed()
        if keys[K_RETURN]:
            return 'shop'
        
        display.flip()

#global mx,my,mb,boss,playerpos,enemies,deadenemies,allchars,wave,totenemies,pointtot,reloading
        
running=True
page = "menu"
mixer.music.play()
for i in range(255):
    screen.fill((0,0,0))
    tscreen.set_alpha(i)
    screen.blit(tscreen,(0,0))
    display.flip()
time.wait(25)
while page != "exit":
    if page == "menu":
        page = menu()
    if page == "game":
        page = game()    
    if page == "instructions":
        page = instructions()    
    if page == "shop":
        page = shop()    
    if page == "credit":
        page = credit()
    if page == "lose":
        page= lose()
    if page == 'win':
        page= win()
    

#END OF MENU AND SHOP LOOP -----------------------------------------------------------------------------------------               
quit()
