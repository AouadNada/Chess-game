import pygame

from button import Button

pygame.init()

WD = 100
HG = 120
WIDTH = 640
SQ_SIZE = WIDTH // 8

SCREEN = pygame.display.set_mode((WIDTH, WIDTH))
# le nom de la fenêtre
pygame.display.set_caption("Chess game")

# img de l'arrière-plan du bouton
img = pygame.transform.smoothscale(pygame.image.load("assets/Play Rect.png"), (WD, 50))


def get_font(size):  # responsable d'afficher l'écriture sous la taille choisie (size)
    return pygame.font.Font(None, size)


# fonction qui affiche les choix des pièces auxquelles le pion sera promu et retourne le type de la pièce
def promotion(row, col):
    running = True
    # variable qui reçoit la pièce de promotion {N: knight,B: Bishop,R: Rook,Q: Queen}
    piece_promo = ""
    clock = pygame.time.Clock()
    while running:
        clock.tick(60)

        # cette partie concerne la position du menu au niveau de l'écran
        if row == 0:
            VALUE = 0
        else:
            VALUE = WIDTH

        if col < 4:
            VALUE2 = col * SQ_SIZE + 1.4 * WD
        else:
            VALUE2 = col * SQ_SIZE - WD // 2

        # la position de la souris
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # la taille du texte afficher
        size = 30
        # bouton du choix du cavalier
        Knight = Button(img, pos=(VALUE2, abs(VALUE - 25)),
                        text_input="Knight", font=get_font(size), base_color="#d7fcd4", hovering_color="White")
        # bouton du choix du fou
        Bishop = Button(img, pos=(VALUE2, abs(VALUE - 80)),
                        text_input="Bishop", font=get_font(size), base_color="#d7fcd4", hovering_color="White")
        # bouton du choix de la dame
        Queen = Button(img, pos=(VALUE2, abs(VALUE - 135)),
                       text_input="Queen", font=get_font(size), base_color="#d7fcd4", hovering_color="White")
        # bouton du choix de la tour
        Rook = Button(img, pos=(VALUE2, abs(VALUE - 190)),
                      text_input="Rook", font=get_font(size), base_color="#d7fcd4", hovering_color="White")

        # respensable du changement de la couleur quand la souris est sur l'élément
        for button in [Knight, Bishop, Queen, Rook]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        # piece promo reçoit le type de la pièce choisie par l'utilisateur
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if Knight.checkForInput(MENU_MOUSE_POS):
                        piece_promo = "N"
                        running = False
                    elif Bishop.checkForInput(MENU_MOUSE_POS):
                        piece_promo = "B"
                        running = False
                    elif Queen.checkForInput(MENU_MOUSE_POS):
                        piece_promo = "Q"
                        running = False
                    elif Rook.checkForInput(MENU_MOUSE_POS):
                        piece_promo = "R"
                        running = False
        pygame.display.update()
    return piece_promo
