import pygame

pygame.init()

hauteur, largeur = 1600, 800

screen = pygame.display.set_mode((hauteur, largeur))
clock = pygame.time.Clock()

running = True
camx = 0
camy = 0
zoom = 1
list_cubes = []

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
                mouse_pos_add = []
                mouse_pos_add.append(int((pygame.mouse.get_pos()[0]+(camx*grid))//(grid)))
                mouse_pos_add.append(int((pygame.mouse.get_pos()[1]+(camy*grid))//(grid)))
                for i in range(len(list_cubes)):
                    if list_cubes[i] == mouse_pos_add:
                        del list_cubes[i]
                        break
                else:
                    list_cubes.append(mouse_pos_add)
    
    def verif():
        global list_cubes
        
        a_sup = []
        cubes_add_principale = []
        a_add_plus = []
        all_temp = []
        form = []
        
        #verif les cubes à moins de 2 ou a plus de 3 cubes de voisins
        for i in range(len(list_cubes)):
            num = 0
            coo_a_verif = [[1, 1], [1, 0], [0, 1], [-1, -1], [-1, 0], [0, -1], [1, -1], [-1, 1]]
            for o in range(len(coo_a_verif)):
                for a in range(len(list_cubes)):
                    if list_cubes[i][0] == list_cubes[a][0] + coo_a_verif[o][0] and list_cubes[i][1] == list_cubes[a][1] + coo_a_verif[o][1]:
                        num += 1
            
            #met dans la variable 'a_sup' les cubes faux pour la régle
            if num != 3 and num != 2:
                a_sup.append(list_cubes[i])
        
        #######################################################
        for i in range(len(list_cubes)):
            coo_a_verif = [[1, 1], [1, 0], [0, 1], [-1, -1], [-1, 0], [0, -1], [1, -1], [-1, 1]]
            for o in range(len(coo_a_verif)):
                form = []
                form.append(list_cubes[i][0] + coo_a_verif[o][0])
                form.append(list_cubes[i][1] + coo_a_verif[o][1])
                all_temp.append(form)

        for j in range(len(all_temp)):
            if all_temp.count(all_temp[j]) == 3:
                a_add_plus.append(all_temp[j])
                
        for element in a_add_plus:
            if element not in cubes_add_principale and element not in list_cubes:
                cubes_add_principale.append(element)
        
        #sup les cubes dont les coo sont dans la variable 'a_sup'
        for b in range(len(a_sup)):
            for c in range(len(list_cubes)):
                if list_cubes[c] == a_sup[b]:
                    del list_cubes[c]
                    break
        #add les cubes dans la variable "cubes_add_prin"
        for y in range(len(cubes_add_principale)):
            list_cubes.append(cubes_add_principale[y])

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
        verif()
    if keys[pygame.K_h]:
        print("zoom", zoom, "    camy", camy, "    camx", camx, "\n", list_cubes)
    
    #afficher les lignes
    for i in range(int(largeur//(grid))):
        pygame.draw.rect(screen, "black", (0, (i+1)*(grid), 1600, 1.5))
    for i in range(int(hauteur//(grid))):
        pygame.draw.rect(screen, "black", ((i+1)*(grid), 0, 1.5, 800))
    
    #affiche les cubes qui sont dans la variable list_cubes et gère leurs mouvements
    for i in range(len(list_cubes)):
        pygame.draw.rect(screen, "black", ((list_cubes[i][0]*grid) - camx*grid
                                            , (list_cubes[i][1]*grid) - camy*grid
                                            , grid, grid))
    
    pygame.display.flip()
    clock.tick(20)
            
pygame.quit()