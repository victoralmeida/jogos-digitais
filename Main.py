import pygame
from pygame.locals import *
from sys import exit
import random


branco = (255, 255, 255)
preto = (0, 0, 0)
amarelo = (255, 255, 0)
red = (255, 0, 0)
xr = 1200
yr = random.randint(200, 400)
xr2 = 1600
yr2 = random.randint(200, 400)
xr3 = 2000
yr3 = random.randint(200, 400)
m = 0
mx = 2000
my = random.randint(0, 300)

background_image_filename = 'img/Noite.png' 
correndo_image_filename = 'img/img_1.png'
correndo2_image_filename = 'img/img_2.png' 
correndo3_image_filename = 'img/img_3.png' 
correndo4_image_filename = 'img/img_4.png' 
correndo5_image_filename = 'img/img_5.png' 
correndo6_image_filename = 'img/img_6.png' 
correndo7_image_filename = 'img/img_7.png' 
correndo8_image_filename = 'img/img_8.png' 
pulando_image_filename = 'img/Pulando.png' 
inimigo1_image_filename = 'img/Inimigo1.png' 
inimigo2_image_filename = 'img/Inimigo2.png' 
bala_image_filename = 'img/Bala.png' 
bronze_image_filename = 'img/Bronze.png' 
prata_image_filename = 'img/Prata.png' 
ouro_image_filename = 'img/Ouro.png'
fim_image_filename = 'img/GameOver.png'
nome_image_filename = 'img/nome.png'
tutorial_image_filename = 'img/Tutorial.png'




pygame.init()

screen = pygame.display.set_mode((997, 480), 0, 32)
clock = pygame.time.Clock()
background = pygame.image.load(background_image_filename)
background2 = pygame.image.load(background_image_filename)
correr1 = pygame.image.load(correndo_image_filename)
correr2 = pygame.image.load(correndo2_image_filename)
correr3 = pygame.image.load(correndo3_image_filename)
correr4 = pygame.image.load(correndo4_image_filename)
correr5 = pygame.image.load(correndo5_image_filename)
correr6 = pygame.image.load(correndo6_image_filename)
correr7 = pygame.image.load(correndo7_image_filename)
correr8 = pygame.image.load(correndo8_image_filename)
pulando = pygame.image.load(pulando_image_filename)
inimigo1 = pygame.image.load(inimigo1_image_filename)
inimigo2 = pygame.image.load(inimigo2_image_filename)
bala1 = pygame.image.load(bala_image_filename)
bala2 = pygame.image.load(bala_image_filename)
bronze = pygame.image.load(bronze_image_filename)
prata = pygame.image.load(prata_image_filename)
ouro = pygame.image.load(ouro_image_filename)
GameOver = pygame.image.load(fim_image_filename)
Nome = pygame.image.load(nome_image_filename)
instrução = pygame.image.load(tutorial_image_filename)


correr1 = pygame.transform.scale(correr1, (58, 54))
correr2 = pygame.transform.scale(correr2, (58, 54))
correr3 = pygame.transform.scale(correr3, (58, 54))
correr4 = pygame.transform.scale(correr4, (58, 54))
correr5 = pygame.transform.scale(correr5, (58, 54))
correr6 = pygame.transform.scale(correr6, (58, 54))
correr7 = pygame.transform.scale(correr7, (58, 54))
correr8 = pygame.transform.scale(correr8, (58, 54))
pulando = pygame.transform.scale(pulando, (58, 54))

moedas = [bronze, prata, ouro]
moeda = moedas[m]
correndo = [correr1, correr1, correr2, correr2, correr3, correr3, correr4, correr4, correr5, correr5, correr6, correr6, correr7, correr7, correr8, correr8]



personagem = correndo[0]

font = pygame.font.SysFont('sans',30)

menu_y = 50
menu_val = 1
vel_y = 20
bx = 0
bx2 = 998
x = 0
y = 425
xi1 = 910
xi2 = 1100
yi1 = 100
yi2 = y
xb1 = 900
xb2 = 900
yb1 = yi1
yb2 = yi2
subir = 0
z = 0
a = 4
mx2 = mx + 20
my2 = my + 20
pontos = 0
double_jump = 0
fase = 1
jump = False
queda = False
game = False
final = False
click = False
menu = True
music = True
tutorial = False
line_rect = Rect(xr,yr, 200, 10)
line_rect2 = Rect(xr2,yr2, 200, 10)
line_rect3 = Rect(xr3,yr3, 200, 10)
line_rect_2 = Rect(xr,yr + 5, 200, 5)
line_rect2_2 = Rect(xr2,yr2 + 5, 200, 5)
line_rect3_2 = Rect(xr3,yr3 + 5, 200, 5)
line_rect_3 = Rect(xr + 1 ,yr + 10, 2, 5)
line_rect2_3 = Rect(xr2 + 1,yr2 + 10, 2, 5)
line_rect3_3 = Rect(xr3 + 1,yr3 + 10, 2, 5)
line_rect4 = Rect(x,y, 40, 60)
line_rect5 = Rect(mx,my, 30, 30)
line_rect6 = Rect(xb1 + 13,yb1 + 25, 40, 30)
line_rect7 = Rect(xb2 + 13,yb2 + 25, 40, 30)
line_rect8 = Rect(mx2,my2, 200, 10)

CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) 
temporizador = 120

while menu is True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button1 = pygame.Rect(800,200,150,50)
    button2 = pygame.Rect(800,270,150,50)
    button3 = pygame.Rect(420,420,150,50)
    text1 = font.render('Começar',True, amarelo)
    text2 = font.render('Instruções',True, amarelo)
    text3 = font.render('Voltar',True, amarelo)


    if button1.collidepoint((mouse_x, mouse_y)):
        if click:
            game = True

    if button2.collidepoint((mouse_x, mouse_y)):
        if click:
            tutorial = True

    if button3.collidepoint((mouse_x, mouse_y)):
        if click:
            tutorial = False

    click = False

    for event in pygame.event.get():        
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                click = True
    



    if menu_y == 60 or menu_y == 40:
        menu_val = -menu_val



    clock.tick(60)
    menu_y += menu_val

                
    screen.blit(background, (0,0))
    screen.blit(Nome, (20,20))
    screen.blit(personagem, (100,425))
    screen.blit(inimigo1, (650,menu_y))
    screen.blit(inimigo2, (850,menu_y))
    pygame.draw.rect(screen,preto,button1)
    pygame.draw.rect(screen,preto,button2)
    screen.blit(text1, (825,205))
    screen.blit(text2, (820,275))

    if tutorial is True:
        screen.blit(instrução, (20,0))
        pygame.draw.rect(screen,preto,button3)
        screen.blit(text3, (465,425))
        
    pygame.display.update()

    estadoCorrida = 0
    while game is True:

        for event in pygame.event.get():        
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == CLOCKTICK and temporizador > 0:
                temporizador = temporizador -1

            if event.type == KEYDOWN and subir == 0:


                
                if event.key==K_SPACE and double_jump < 2:
                    vel_y = 16
                    jump = True
                    personagem = pulando
                    double_jump += 1            




        # Pular e Correr

        if jump:
            y -= vel_y 
            vel_y -= 1
            if vel_y < -16:
                jump = False

        if jump is False:
            vel_y = 16
        
        

        if queda is True and jump is False:
            y += 12

        if jump is False and queda is False:
            personagem = correr1


        #Colisão




        if line_rect4.colliderect(line_rect) and z == 0 and not line_rect4.colliderect(line_rect_2):
            queda = False
            jump = False
            z += 1
            y = yr - 50
            vel_y = 0
            double_jump = 0
            

        if line_rect4.colliderect(line_rect_2) and z == 0:
            jump = False
            queda = True
            y = yr + 60
            z += 1
            vel_y = 0
            

        if line_rect4.colliderect(line_rect2) and z == 0 and not line_rect4.colliderect(line_rect2_2):
            queda = False
            jump = False
            z = 1
            y = yr2 - 50
            vel_y = 0
            double_jump = 0
        

        if line_rect4.colliderect(line_rect2_2) and z == 0:
            jump = False
            queda = True
            y = yr2 + 60
            z += 1
            vel_y = 0
            

        if line_rect4.colliderect(line_rect3) and z == 0 and not line_rect4.colliderect(line_rect3_2):
            queda = False
            jump = False
            z = 1
            y = yr3 - 50
            vel_y = 0
            double_jump = 0
            

        if line_rect4.colliderect(line_rect3_2) and z == 0:
            jump = False
            queda = True
            y = yr3 + 60
            z += 1
            vel_y = 0
        

        if line_rect4.colliderect(line_rect6) or line_rect4.colliderect(line_rect7):
            game = False
            final = True
        

        if not line_rect4.colliderect(line_rect) and not line_rect4.colliderect(line_rect2)and not line_rect4.colliderect(line_rect3) and not line_rect4.colliderect(line_rect_2) and not line_rect4.colliderect(line_rect2_2)and not line_rect4.colliderect(line_rect3_2):
            z = 0
            z2 = 0
            queda = True


        if y > 425:
            y = 425
            jump = False
            queda = False
            double_jump = 0


        if line_rect4.colliderect(line_rect8):
            mx = 2500
            my = random.randint(0, 400)
            mx2 = 2500
            my2 = my
            ganho = 10 + (10 * m)
            pontos = pontos + ganho
            m += 1
            pygame.mixer.music.load('som/catch.mp3')
            pygame.mixer.music.play(0)

        if line_rect8.colliderect(line_rect) or line_rect8.colliderect(line_rect2) or line_rect8.colliderect(line_rect3) or line_rect8.colliderect(line_rect_2) or line_rect8.colliderect(line_rect2_2) or line_rect8.colliderect(line_rect3_2):
            my = random.randint(0, 400)


        if line_rect6.colliderect(line_rect) or line_rect6.colliderect(line_rect2) or line_rect6.colliderect(line_rect3) or line_rect6.colliderect(line_rect_2) or line_rect6.colliderect(line_rect2_2) or line_rect6.colliderect(line_rect3_2):
            yb1 = -1000


        if line_rect7.colliderect(line_rect) or line_rect7.colliderect(line_rect2) or line_rect7.colliderect(line_rect3) or line_rect7.colliderect(line_rect_2) or line_rect7.colliderect(line_rect2_2) or line_rect7.colliderect(line_rect3_2):
            yb2 = -1000

        if line_rect4.colliderect(line_rect_3) or line_rect4.colliderect(line_rect2_3)or line_rect4.colliderect(line_rect3_3) and not line_rect4.colliderect(line_rect2) and not line_rect4.colliderect(line_rect) and not line_rect4.colliderect(line_rect3):
            game = False
            final = True



            
       


    
        #Valores após passar a tela

 
        if bx < -997:
            bx = 998

        if bx2 < -997:
            bx2 = 998

        if xr < - 200:
            xr = 1000
            yr = random.randint(200,400)

        if xr2 < - 200:
            xr2 = 1000
            yr2 = random.randint(200, 400)

        if xr3 < - 200:
            xr3 = 1000
            yr3 = random.randint(200, 400)

        if yi1 < 0:
            a = a * (-1)

        if yi1 > 400:
            a = a * (-1)

        if xb1 < -150:
            xb1 = 900
            yb1 = yi1 + 10 

        if xb2 < -150:
            xb2 = 900
            yb2 = yi2 + 10

        if mx < -250:
            mx = 2000
            my = random.randint(0, 300)
            m += 1

        if m == 0:
            mx2 = mx + 23

        if m == 1:
            mx2 = mx + 85

        if m == 2:
            mx2 = mx + 145

        if m == 3:
            m = 0
            mx2 = mx + 20

        #placar e tempo

        score = font.render('Placar '+str(pontos), True, (amarelo))
        placar = score

        timer1 = font.render('Tempo ' + str(temporizador), True, (amarelo))


        # Estados de fase

        if temporizador == 90:
            fase = 2

        if temporizador == 60:
            fase = 3

        if temporizador == 0:
            fase = 5


        # Detalhes de fase

        if fase == 1:
            yi1 += a
            yi2 = -200
            yb2 = -1000

        if fase == 2:
            if xi1 == 1100 and xi2 == 910:
                yi1 += -200
                yi2 = y - 30
                yi1 = -200

            else:
                xi1 += 5
                xi2 -= 5
                yi2 = y - 30
                yb1 = -1000
                yb2 = -1000

        if fase == 3:
            if xi1 == 910:
                fase = 4

            else:
                xi1 -= 5
                yi1 = 100
                yb1 = -1000
                yb2 = -1000
                yi2 = y - 30
            

            
                

        if fase == 4:
            yi1 += a
            yi2 = y - 30
        

        if fase == 5:
            yi1 = 50
            yi2 = 200
            fase = 6
            yb1 = -1000
            yb2 = -1000
            yr = - 300
            yr2 = -300
            yr3 = -300
            my = -500


        if fase == 6:
            xi1 -= 8
            xi2 -= 8
            yb1 = -1000
            yb2 = -1000
            yr = - 300
            yr2 = -300
            yr3 = -300
            my = -500


            if xi1 <= -200 and xi2 <= -200:
                fase = 7

        if fase == 7:
            x += 5
            yb1 = -1000
            yb2 = -1000
            yr = - 300
            yr2 = -300
            yr3 = -300
            my = -500

            if x > 1050:
                game = False
                final = True
        

        

        # Valores dos retangulos
        
        line_rect = Rect(xr,yr, 200, 19)
        line_rect2 = Rect(xr2,yr2, 200, 19)
        line_rect3 = Rect(xr3,yr3, 200, 19)
        line_rect_2 = Rect(xr,yr + 19, 200, 1)
        line_rect2_2 = Rect(xr2,yr2 + 19, 200, 1)
        line_rect3_2 = Rect(xr3,yr3 + 19, 200, 1)
        line_rect_3 = Rect(xr - 1 ,yr + 10, 1, 1)
        line_rect2_3 = Rect(xr2 - 1,yr2 + 10, 1, 1)
        line_rect3_3 = Rect(xr3 - 1,yr3 + 10, 1, 1)
        line_rect4 = Rect(x,y, 40, 60)
        line_rect5 = Rect(mx,my, 30, 30)
        line_rect6 = Rect(xb1 + 13,yb1 + 25, 40, 30)
        line_rect7 = Rect(xb2 + 13,yb2 + 25, 40, 30)
        line_rect8 = Rect(mx2,my2, 45, 45)
    




        # Valores de velocidade

        xr -= 5
        xr2 -= 5
        xr3 -= 5
        bx -= 5
        bx2 -= 5
        xb1 -= 7
        xb2 -= 10
        mx -= 5
        mx2 -= 5
        my2 = my + 25
        moeda = moedas[m]

        clock.tick(60)

        pygame.draw.rect(screen, branco, line_rect4, 5)
        pygame.draw.rect(screen, preto, line_rect6, 3)
        pygame.draw.rect(screen, preto, line_rect7, 3)
        pygame.draw.rect(screen, preto, line_rect8, 5)
        pygame.draw.rect(screen, preto, line_rect_3)
        pygame.draw.rect(screen, preto, line_rect2_3)
        pygame.draw.rect(screen, preto, line_rect3_3)
        screen.blit(background, (bx,0))
        screen.blit(background2, (bx2,0))

        

        
       
        if jump: 
            personagem = pulando
        else:
            
            if estadoCorrida < (len(correndo)-1):
                estadoCorrida = estadoCorrida+1
            else:
                estadoCorrida = 0

            personagem = correndo[estadoCorrida]

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
        pygame.draw.rect(screen, branco, line_rect_2)
        pygame.draw.rect(screen, branco, line_rect2_2)
        pygame.draw.rect(screen, branco, line_rect3_2)





        screen.blit(score, (0,0))
        screen.blit(timer1, (200,0))
   
        pygame.display.update()


    while final is True:
        tutorial = False
        
        pygame.mixer.music.load('som/Game_Over.mp3')
        pygame.mixer.music.play(0)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        textf = font.render('Menu',True, preto)
        screen.fill((preto))
        pygame.mixer.music.play(0)
        screen.blit(GameOver, (260,0))
        screen.blit(placar, (440,300))

        button = pygame.Rect(420,420,150,50)

        if button.collidepoint((mouse_x, mouse_y)):
            if click:
                final = False

        click = False

        for event in pygame.event.get():        
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                click = True

        pygame.draw.rect(screen,branco,button)
        screen.blit(textf, (465,425))
                
        pygame.display.flip()
