import pygame, sys
from button import Button
from main import main

WIDTH = 650
HEIGHT = 680

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# le nom de la fenêtre
pygame.display.set_caption("Chess game")

# l'image de l'arrière-plan
BG = pygame.transform.smoothscale(pygame.image.load("assets/background.jpg"), (WIDTH, HEIGHT))
# l'image utilisée en arrière-plan du bouton
BUTTON_IMG = pygame.image.load("assets/Play Rect.png")


# fonction contenant la fenêtre qui sera afficher qi le joueur à sélectionner le mode contre ordinateur
def PvAI():
    pygame.init()
    while True:
        # ajout de l'image de l'arrière-plan
        SCREEN.blit(BG, (0, 0))

        # détecter la position de la souris
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # text afficher en de la fenêtre
        MENU_TEXT = get_font(100).render("Choose a color ", True, "#b68f40")
        # la position des boutons au centre de la fenêtre
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH // 2, 100))
        # le bouton pour choisir la couleur blanche
        WHITE_BUTTON = Button(image=BUTTON_IMG, pos=(WIDTH // 2, 250),
                              text_input="WHITE", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        # le bouton pour choisir la couleur noire
        BLACK_BUTTON = Button(image=BUTTON_IMG, pos=(WIDTH // 2, 400),
                              text_input="BLACK", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        # le bouton pour retourner au menu d'accueil
        BACK_BUTTON = Button(image=BUTTON_IMG, pos=(WIDTH // 2, 550),
                             text_input="BACK", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # respensable du changement de la couleur quand la souris est sur l'élément
        for button in [WHITE_BUTTON, BLACK_BUTTON, BACK_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # boucle de gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if WHITE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        main(False)
                        return
                    if BLACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        main(False, True)
                        return

                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        return
        pygame.display.update()


def get_font(size):  # responsable d'afficher l'écriture sous la taille choisie (size)
    return pygame.font.Font(None, size)


# fonction responsable de l'affichage du menu d'accueil
def main_menu():
    pygame.init()
    while True:
        # ajout de l'image de l'arrière-plan
        SCREEN.blit(BG, (0, 0))

        # détecter la position de la souris
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # détecter la position de la souris
        MENU_TEXT = get_font(100).render("Chess Game", True, "#b68f40")
        # la position des boutons au centre de la fenêtre
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH // 2, 100))

        # le bouton pour choisir le mode entre joueurs humains
        PvP_BUTTON = Button(image=BUTTON_IMG, pos=(WIDTH // 2, 250),
                            text_input="Mode Player", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        # le bouton pour choisir le mode contre l'ordinateur
        PvAI_BUTTON = Button(image=BUTTON_IMG, pos=(WIDTH // 2, 400),
                             text_input="Mode Computer", font=get_font(60), base_color="#d7fcd4",
                             hovering_color="White")
        # le bouton pour sortir du jeu
        QUIT_BUTTON = Button(image=BUTTON_IMG, pos=(WIDTH // 2, 550),
                             text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # respensable du changement de la couleur quand la souris est sur l'élément
        for button in [PvP_BUTTON, PvAI_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if PvP_BUTTON.checkForInput(MENU_MOUSE_POS):
                        main()

                    if PvAI_BUTTON.checkForInput(MENU_MOUSE_POS):
                        PvAI()

                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main_menu()
