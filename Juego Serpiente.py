import pygame
import random
import time
import os

def load_image(name):
    path= os.path.join('C:\MARTYN\Cursos Varios\Phyton\JuegoSerpiente 2.0' , name)
    return pygame.image.load(path).convert()


pygame.init()

icono= pygame.image.load("icon.png")
pygame.display.set_icon(icono)

#Colores
Blanco= (255, 255, 255)
Negro= (0, 0, 0)
Rojo= (255, 0, 0)
Azul= (0,0,255)
Verde= (0,128,0)
Naranjo= (255,127,0)
Lila= (182,149,192)


#Dimensiones
ancho = 800
altura = 400


superficie = pygame.display.set_mode((ancho,altura))
pygame.display.set_caption('Snake 2.0')

reloj = pygame.time.Clock()

serp_tamano = 20

#Letra
font = pygame.font.SysFont("Times New Roman", 35)


def pausa():
    pausado= True
    
    while pausado:
        
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    pausado= False      
                elif event.key== pygame.K_q:
                    pygame.quit()
                    quit()

        background= load_image('25.jpg')
        superficie.blit(background,[0,0])
        message_to_screen("Pausa",Negro,-100)
        message_to_screen("Tomate un descanso",Verde,-60)
        pygame.display.update()
        reloj.tick(5)


def puntos(score):
    text = font.render("Puntos: "+str(score), True, Blanco)
    superficie.blit(text, [370,0])

def mostrarVelocidad(v):
    text = font.render("Velocidad: "+str(v), True, Rojo)
    superficie.blit(text, [0,0])


def intro_juego():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    intro= False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        superficie.fill(Blanco)
        message_to_screen("Damas y caballeros", Negro, -180)
        message_to_screen("Les presento una nueva version de snake", Azul,-150)
        message_to_screen("teclas fichas de movimiento para comer manzanas", Azul,-120)
        message_to_screen("Al tocar os bordes o si se toca a si misma pierde", Negro,-90)
        message_to_screen("Al tocar la manzana roja aumenta el puntaje", Rojo,-60)
        message_to_screen("y cada tres puntos aumenta la velocidad", Rojo,-30)
        message_to_screen("Al tocar la manzana lila se alarga 10 veces", Lila,0)
        message_to_screen("Al tocar la la manzana verde su velocidad aumenta", Verde,30)
        message_to_screen("Para pausar partida, presiona la tecla P", Azul,60)
        message_to_screen("Para continuar partida, presiona la tecla X", Azul,90)
        message_to_screen("Para terminar de jugar y salir, presiona la teca Q", Negro,120)
        message_to_screen("Estas preparado?", Negro,155)
        pygame.display.update()
        reloj.tick(15)


def serpiente(serp_tamano, listaSerpiente):
    for i in listaSerpiente:
        pygame.draw.rect(superficie, Blanco, (i[0],i[1], serp_tamano, serp_tamano))


def text_objetos(text,color):
    textSuperficie= font.render(text,True,color)
    return textSuperficie, textSuperficie.get_rect()


def message_to_screen(msg, color, y_displace=0):
    textSur, textRect= text_objetos(msg,color)
    textRect.center=(ancho/2),(altura/2)+ y_displace
    superficie.blit(textSur,textRect)


def gameOver(puntaje):
    gameOver= True
    
    pulsar_sonidoPerdedor= pygame.mixer.Sound("musicaPerdedor.ogg")
    pulsar_sonidoPerdedor.set_volume(0.50)
    pulsar_sonidoPerdedor.play(18)
    
    while gameOver: #si es true es game over
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
                elif event.key== pygame.K_x:
                    pulsar_sonidoPerdedor.stop()
                    gameLoop()

        backgroundPerdedor= load_image('per.jpg')
        backgroundPerdedor= pygame.transform.scale(backgroundPerdedor,(ancho,altura))
        superficie.blit(backgroundPerdedor,[0,0])
        message_to_screen("Game Over :(", Rojo,30)
        message_to_screen("Para continuar presione C. Para terminar presione Q",Negro,80)
        message_to_screen("Tu puntaje fue de "+ str(puntaje),Negro,120)
        pygame.display.update()
        reloj.tick(5)


def gameLoop():
    gameExit = False
    CPS= 15

    mover_x = 500
    mover_y = 300

    velocidad=1

    mover_x_cambio = 0
    mover_y_cambio = 0

    listaSerpiente = []
    largoSerpiente = 1

    contToquesManzanaRoja=0

    #Manzana1
    azarManzanaX1 = round(random.randrange(0, ancho - 20)/20.0)*20.0
    azarManzanaY1 = round(random.randrange(0, altura - 20)/20.0)*20.0

    #Manzana2
    azarManzanaX2 = round(random.randrange(0, ancho - 20)/20.0)*20.0
    azarManzanaY2 = round(random.randrange(0, altura - 20)/20.0)*20.0

    #Manzana3
    azarManzanaX3 = round(random.randrange(0, ancho - 20)/20.0)*20.0
    azarManzanaY3 = round(random.randrange(0, altura - 20)/20.0)*20.0

    background= load_image('serpiente.jpg')
    background= pygame.transform.scale(background,(ancho,altura))

    pulsar_sonido= pygame.mixer.Sound("musicaFondo.ogg")
    pulsar_sonido.set_volume(0.50)
    pulsar_sonido.play(18)

    

    while not gameExit: ##si es true sale del juego

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                gameExit= True
                    
            if event.type == pygame.KEYDOWN:

                if event.key== pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key==pygame.K_p:
                    pulsar_sonido.set_volume(0.0)
                    pausa()
                    pulsar_sonido.set_volume(0.50)
                        
                if event.key == pygame.K_LEFT:
                    mover_x_cambio = -serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    mover_x_cambio = serp_tamano
                    mover_y_cambio = 0
                        
                elif event.key == pygame.K_UP:
                    mover_y_cambio = -serp_tamano
                    mover_x_cambio = 0
                elif event.key == pygame.K_DOWN:
                    mover_y_cambio = serp_tamano
                    mover_x_cambio = 0


        if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y < 0:
            pulsar_sonido.stop()
            gameOver(largoSerpiente-1)
            
           

        mover_x += mover_x_cambio
        mover_y += mover_y_cambio
        superficie.blit(background,[0,0])
        
        pygame.draw.rect(superficie,Lila,(azarManzanaX1, azarManzanaY1, 20,20))
        pygame.draw.rect(superficie,Rojo,(azarManzanaX2, azarManzanaY2, 20,20))
        pygame.draw.rect(superficie,Verde,(azarManzanaX3, azarManzanaY3, 20,20))
        
        cabezaSerpiente = []
        cabezaSerpiente.append(mover_x)
        cabezaSerpiente.append(mover_y)
        listaSerpiente.append(cabezaSerpiente)
        if len(listaSerpiente) > largoSerpiente:
            del listaSerpiente[0]

        for eachSegment in listaSerpiente[:-1]:
            if eachSegment== cabezaSerpiente:
                pulsar_sonido.stop()
                gameOver(largoSerpiente-1)


        serpiente(serp_tamano, listaSerpiente)
        puntos(largoSerpiente-1)
        mostrarVelocidad(velocidad)
        pygame.display.update()


        #Interseccion Manzana Lila
        if mover_x == azarManzanaX1 and mover_y == azarManzanaY1:
            azarManzanaX1 = round(random.randrange(0, ancho - 20)/20.0)*20.0
            azarManzanaY1 = round(random.randrange(0, altura - 20)/20.0)*20.0
            largoSerpiente += 10

        #Interseccion Manzana Roja
        if mover_x == azarManzanaX2 and mover_y == azarManzanaY2:
            azarManzanaX2 = round(random.randrange(0, ancho - 20)/20.0)*20.0
            azarManzanaY2 = round(random.randrange(0, altura - 20)/20.0)*20.0
            largoSerpiente += 1
            contToquesManzanaRoja +=1

            if contToquesManzanaRoja == 3:
                CPS+=1
                velocidad += 1
                contToquesManzanaRoja=0

    
        #Interseccion Manzana verde
        if mover_x == azarManzanaX3 and mover_y == azarManzanaY3:
            azarManzanaX3 = round(random.randrange(0, ancho - 20)/20.0)*20.0
            azarManzanaY3 = round(random.randrange(0, altura - 20)/20.0)*20.0
            largoSerpiente += 1
            velocidad += 1
            CPS += 1
        
    
        reloj.tick(CPS)
        
intro_juego()
gameLoop()





    

    
