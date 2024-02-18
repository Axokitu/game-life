import pygame
import os
import random

pygame.init()

hauteur, largeur = 1600, 800

screen = pygame.display.set_mode((hauteur, largeur))
clock = pygame.time.Clock()

running = True

camx = 0
camy = 0
zoom = 1

pix = [[3, 3]]

while running:
    grid = 25//zoom
    screen.fill("gray")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #zoom de la cam
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                zoom -= 0.1
            elif event.button == 5:
                zoom += 0.1
            
            #le click pour add ou sup des cubes
            elif event.button == 1:
                mouse_pos_add = []
                mouse_pos_add.append(int((pygame.mouse.get_pos()[0]+(camx*grid))//(grid)))
                mouse_pos_add.append(int((pygame.mouse.get_pos()[1]+(camy*grid))//(grid)))
                for i in range(len(pix)):
                    if pix[i] == mouse_pos_add:
                        del pix[i]
                        break
                else:
                    pix.append(mouse_pos_add)
    
    #mouvement de la cam
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        camy -= 1
    if keys[pygame.K_q]:
        camx -= 1
    if keys[pygame.K_s]:
        camy += 1
    if keys[pygame.K_d]:
        camx += 1
    if keys[pygame.K_h]:
        print("zoom", zoom, "    camy", camy, "    camx", camx, "\n", pix)
    
    #afficher les lignes
    for i in range(int(largeur//(grid))):
        pygame.draw.rect(screen, "black", (0, (i+1)*(grid), 1600, 1.5))
    for i in range(int(hauteur//(grid))):
        pygame.draw.rect(screen, "black", ((i+1)*(grid), 0, 1.5, 800))
    
    #affiche les cubes qui sont dans la variable pix et gère leurs mouvements
    for i in range(len(pix)):
        pygame.draw.rect(screen, "black", ((pix[i][0]*grid) - camx*grid
                                            , (pix[i][1]*grid) - camy*grid
                                            , grid, grid))
    
    
    #pygame.draw.rect(screen, "black", ((75//zoom)-camx, (75//zoom)-camy, 25//zoom, 25//zoom))
    
    
    pygame.display.flip()
    clock.tick(20)
            
pygame.quit()
