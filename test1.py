import pygame

pygame.init()

hauteur, largeur = 1600, 800

screen = pygame.display.set_mode((hauteur, largeur))
clock = pygame.time.Clock()

running = True
camx = 0
camy = 0
zoom = 1
list_cubes = set()  # Utilisation d'un ensemble pour stocker les cellules vivantes

while running:
    grid = 25//zoom
    screen.fill("gray")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                zoom = zoom / 1.1
            elif event.button == 5:
                zoom = zoom * 1.1
            elif event.button == 1:
                mouse_pos_add = ((pygame.mouse.get_pos()[0]+(camx*grid))//(grid),
                                (pygame.mouse.get_pos()[1]+(camy*grid))//(grid))
                if mouse_pos_add in list_cubes:
                    list_cubes.remove(mouse_pos_add)
                else:
                    list_cubes.add(mouse_pos_add)

    # Fonction pour vérifier les règles du jeu de la vie et mettre à jour les cellules vivantes
    def update_game():
        global list_cubes
        
        new_list_cubes = set()
        neighbors_count = {}
        
        # Compter les voisins de chaque cellule vivante
        for x, y in list_cubes:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    neighbor = (x + dx, y + dy)
                    neighbors_count[neighbor] = neighbors_count.get(neighbor, 0) + 1
        
        # Appliquer les règles du jeu de la vie pour chaque cellule et mettre à jour new_list_cubes
        for cell, count in neighbors_count.items():
            if count == 3 or (count == 2 and cell in list_cubes):
                new_list_cubes.add(cell)
        
        list_cubes = new_list_cubes

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
        update_game()

    for i in range(int(largeur//(grid))):
        pygame.draw.rect(screen, "black", (0, (i+1)*(grid), 1600, 1.5))
    for i in range(int(hauteur//(grid))):
        pygame.draw.rect(screen, "black", ((i+1)*(grid), 0, 1.5, 800))

    for x, y in list_cubes:
        pygame.draw.rect(screen, "black", ((x*grid) - camx*grid, (y*grid) - camy*grid, grid, grid))

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
