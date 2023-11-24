
class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        # image insérée dans l'arrière-plan du bouton
        self.image = image
        # positions du bouton
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        # le font et la taille du texte
        self.font = font
        # la couleur de base et celle du hovering
        self.base_color, self.hovering_color = base_color, hovering_color
        # le texte à afficher sur bouton
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        # au cas il n'y pas de bouton
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    # mise à jour du bouton
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    # changer la couleur quand la souris est positionnée sur le bouton
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
