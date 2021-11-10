import pygame
from pygame.locals import *
from sys import exit
import random


branco = (255, 255, 255)
preto = (0, 0, 0)
amarelo = (255, 255, 0)
xr = 1200
yr = random.randint(0, 200)
xr2 = 1600
yr2 = random.randint(0, 200)
xr3 = 2000
yr3 = random.randint(0, 200)
m = 0
mx = 2000
my = random.randint(0, 300)


background_image_filename = 'img/Noite.png' 
correndo_image_filename = 'img/Correndo.png' 
pulando_image_filename = 'img/Pulando.png' 
inimigo1_image_filename = 'img/Inimigo1.png' 
inimigo2_image_filename = 'img/Inimigo2.png' 
bala_image_filename = 'img/Bala.png' 
bronze_image_filename = 'img/Bronze.png' 
prata_image_filename = 'img/Prata.png' 
ouro_image_filename = 'img/Ouro.png' 


pygame.init()

screen = pygame.display.set_mode((800, 380), 0, 32)
clock = pygame.time.Clock()
background = pygame.image.load(background_image_filename)
background2 = pygame.image.load(background_image_filename)
correndo = pygame.image.load(correndo_image_filename)
pulando = pygame.image.load(pulando_image_filename)
inimigo1 = pygame.image.load(inimigo1_image_filename)
inimigo2 = pygame.image.load(inimigo2_image_filename)
bala1 = pygame.image.load(bala_image_filename)
bala2 = pygame.image.load(bala_image_filename)
bronze = pygame.image.load(bronze_image_filename)
prata = pygame.image.load(prata_image_filename)
ouro = pygame.image.load(ouro_image_filename)
moedas = [bronze, prata, ouro]
moeda = moedas[m]
personagem = correndo

font = pygame.font.SysFont('sans',30)

vel_y = 20
bx = 0
bx2 = 801
x = 0
y = 325
xi1 = 710
xi2 = 710
yi1 = 100
yi2 = y
xb1 = 700
xb2 = 700
yb1 = yi1
yb2 = yi2
subir = 0
z = 0
a = 4
colisãox = 0
colisãoy = 0
pontos = 0
jump = False
queda = False
line_rect = Rect(xr,yr, 200, 10)
line_rect2 = Rect(xr2,yr2, 200, 10)
line_rect3 = Rect(xr3,yr3, 200, 10)
line_rect4 = Rect(x,y, 40, 60)
line_rect5 = Rect(mx,my, 30, 30)
line_rect6 = Rect(xb1 + 13,yb1 + 25, 40, 30)
line_rect7 = Rect(xb2 + 13,yb2 + 25, 40, 30)


while True:

    for event in pygame.event.get():        
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN and subir == 0:
            if event.key==K_SPACE:
                jump = True
                personagem = pulando 




    # Pular e Correr

    if jump:
        y -= vel_y
        vel_y -= 1
        if vel_y < -20:
            jump = False

    if jump is False:
        vel_y = 20

    if queda is True and jump is False:
        y += 10

    if jump is False and queda is False:
        personagem = correndo


    #Colisão

    top1 = line_rect.top - line_rect4.bottom
    top2 = line_rect2.top - line_rect4.bottom
    top3 = line_rect3.top - line_rect4.bottom
    
    bottom1 = line_rect.bottom - line_rect4.top
    bottom2 = line_rect2.bottom - line_rect4.top
    bottom3 = line_rect3.bottom - line_rect4.top 


    if line_rect4.colliderect(line_rect) and z == 0:
        queda = False
        z = 1
        if bottom1 <= 10:
            vel_y = 0
            

        else:
            jump = False
            

    if line_rect4.colliderect(line_rect2) and z == 0:
        queda = False
        z = 1
        if bottom2 <= 10:
            vel_y = 0

        else:
            jump = False

    if line_rect4.colliderect(line_rect3) and z == 0:
        queda = False
        z = 1
        if bottom3 <= 10:
            vel_y = 0

        else:
            jump = False

    if line_rect4.colliderect(line_rect6) or line_rect4.colliderect(line_rect7):
        print("O jogador foi atingido")
        

    if not line_rect4.colliderect(line_rect) and not line_rect4.colliderect(line_rect2)and not line_rect4.colliderect(line_rect3):
        z = 0
        queda = True


    if y > 325:
        y = 325
        jump = False
        queda = False

    

            
       


    
    #Valores após passar a tela

    if bx < -800:
        bx = 800

    if bx2 < -800:
        bx2 = 800

    if xr < - 200:
        xr = 1000
        yr = random.randint(0, 300)

    if xr2 < - 200:
        xr2 = 1000
        yr2 = random.randint(0, 300)

    if xr3 < - 200:
        xr3 = 1000
        yr3 = random.randint(0, 300)

    if yi1 < 0:
        a = a * (-1)

    if yi1 > 300:
        a = a * (-1)

    if xb1 < -150:
        xb1 = 700
        yb1 = yi1 + 10 

    if xb2 < -150:
        xb2 = 700
        yb2 = yi2 + 10

    if mx < -250:
        mx = 2000
        my = random.randint(0, 300)
        m += 1

    if m == 3:
        m = 0

    #placar

    score1 = font.render('Placar '+str(pontos), True, (amarelo))

        

    #Blits das imagens e valores de velocidade
        
    line_rect = Rect(xr,yr, 200, 10)
    line_rect2 = Rect(xr2,yr2, 200, 10)
    line_rect3 = Rect(xr3,yr3, 200, 10)
    line_rect4 = Rect(x,y, 40, 60)
    line_rect5 = Rect(mx,my, 30, 30)
    line_rect6 = Rect(xb1 + 13,yb1 + 25, 40, 30)
    line_rect7 = Rect(xb2 + 13,yb2 + 25, 40, 30)




    
    xr -= 5
    xr2 -= 5
    xr3 -= 5
    bx -= 5
    bx2 -= 5
    yi1 += a
    yi2 = y - 30
    xb1 -= 5
    xb2 -= 5
    mx -= 5
    moeda = moedas[m]

    clock.tick(60)

    pygame.draw.rect(screen, preto, line_rect4, 5)
    pygame.draw.rect(screen, preto, line_rect6, 3)
    pygame.draw.rect(screen, preto, line_rect7, 3)
    screen.blit(background, (bx,0))
    screen.blit(background2, (bx2,0))
    screen.blit(personagem, (x,y))
    screen.blit(bala1, (xb1,yb1))
    screen.blit(bala2, (xb2,yb2))
    screen.blit(inimigo1, (xi1,yi1))
    screen.blit(inimigo2, (xi2,yi2))
    screen.blit(moeda, (mx,my))
    pygame.draw.rect(screen, branco, line_rect)


    pygame.draw.rect(screen, branco, line_rect)
    pygame.draw.rect(screen, branco, line_rect2)
    pygame.draw.rect(screen, branco, line_rect3)


    screen.blit(score1, (0,0))
   
    pygame.display.update()
