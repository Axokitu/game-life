import pygame

pygame.init()

hauteur, largeur = 1600, 800

screen = pygame.display.set_mode((hauteur, largeur))
clock = pygame.time.Clock()

running = True
camx = 0
camy = 0
zoom = 1
go = 0
list_cubes = [[23, 18], [23, 19], [29.0, 19.0], [30.0, 19.0], [30.0, 18.0], [30.0, 20.0], [31.0, 20.0], [31.0, 19.0], [31.0, 18.0], [33.0, 17.0], [33.0, 16.0], [34.0, 17.0], [33.0, 21.0], [33.0, 22.0], [34.0, 21.0], [22.0, 18.0], [22.0, 19.0], [44.0, 20.0], [45.0, 20.0], [46.0, 19.0], [47.0, 18.0], [47.0, 17.0], [47.0, 16.0], [46.0, 15.0], [45.0, 14.0], [44.0, 14.0], [56.0, 16.0], [56.0, 17.0], [57.0, 17.0], [57.0, 16.0]]

while running:
    grid = 25//zoom
    screen.fill("gray")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #zoom de la cam
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                zoom = zoom / 1.1
            elif event.button == 5:
                zoom = zoom * 1.1
            
            #le click pour add ou sup des cubes
            elif event.button == 1:
                mouse_pos_add = [((pygame.mouse.get_pos()[0]+(camx*grid))//(grid)),
                                ((pygame.mouse.get_pos()[1]+(camy*grid))//(grid))]
                for i in range(len(list_cubes)):
                    if list_cubes[i] == mouse_pos_add:
                        del list_cubes[i]
                        break
                else:
                    list_cubes.append(mouse_pos_add)
    
    def verif():
        global list_cubes
        
        cubes_sup_principale = []
        cubes_add_principale = []
        a_add_plus = []
        coo_a_verif = [[1, 1], [1, 0], [0, 1], [-1, -1], [-1, 0], [0, -1], [1, -1], [-1, 1]]
        all_temp = []
        
        #verif les cubes à moins de 2 ou a plus de 3 cubes de voisins
        for i in range(len(list_cubes)):
            num = 0
            for o in range(len(coo_a_verif)):
                for a in range(len(list_cubes)):
                    if list_cubes[i][0] == list_cubes[a][0] + coo_a_verif[o][0] and list_cubes[i][1] == list_cubes[a][1] + coo_a_verif[o][1]:
                        num += 1
            
            #met dans la variable 'cubes_sup_principale' les cubes faux pour la régle
            if num != 3 and num != 2:
                cubes_sup_principale.append(list_cubes[i])
        
        #######################################################
        for a in range(len(list_cubes)):
            for b in range(len(coo_a_verif)):
                all_temp.append([list_cubes[a][0] + coo_a_verif[b][0], list_cubes[a][1] + coo_a_verif[b][1]])
                
        for c in range(len(all_temp)):
            if all_temp.count(all_temp[c]) == 3:
                a_add_plus.append(all_temp[c])
                
        for d in a_add_plus:
            if d not in cubes_add_principale and d not in list_cubes:
                cubes_add_principale.append(d)
        
        #sup les cubes dont les coo sont dans la variable 'cubes_sup_principale'
        for e in range(len(cubes_sup_principale)):
            for f in range(len(list_cubes)):
                if list_cubes[f] == cubes_sup_principale[e]:
                    del list_cubes[f]
                    break
                
        #add les cubes dans la variable "cubes_add_principale"
        for g in range(len(cubes_add_principale)):
            list_cubes.append(cubes_add_principale[g])

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
    if keys[pygame.K_SPACE]:
        verif()
    if keys[pygame.K_n]:
        if go == 0:
            go = 1
        else:
            go = 0
    if keys[pygame.K_h]:
        print("zoom", zoom, "    camy", camy, "    camx", camx, "\n", list_cubes)
        
    
    #afficher les lignes
    if zoom < 5:
        for i in range(int(largeur//(grid))):
            pygame.draw.rect(screen, "black", (0, (i+1)*(grid), 1600, 1.5))
        for i in range(int(hauteur//(grid))):
            pygame.draw.rect(screen, "black", ((i+1)*(grid), 0, 1.5, 800))
    
    #affiche les cubes qui sont dans la variable list_cubes et gère leurs mouvements
    for i in range(len(list_cubes)):
        pygame.draw.rect(screen, "black", ((list_cubes[i][0]*grid) - camx*grid
                                            , (list_cubes[i][1]*grid) - camy*grid
                                            , grid, grid))
    
    if go == 0:
        verif()
    
    pygame.display.flip()
    clock.tick(20)
    print(clock.get_fps())
            
pygame.quit()