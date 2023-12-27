import pygame

pygame.init()

if __name__ == "__main__":
    window = pygame.display.set_mode((600, 600))
    mainMenu = MainMenuScreen()
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        mainMenu.clear()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                for objectName, object in mainMenu.gameObjects.items():
                    if object.mouse_hover():
                        print("{0} was clicked on".format(objectName))
                        object.head_to_new_position((object.width, 500))

        for objectName, object in mainMenu.gameObjects.items():
            if object.mouse_hover():
                print("the mouse is hovering over {0}".format(objectName))

        for objectName, object in mainMenu.gameObjects.items():
            if object.movingToNewPosition:
                object.move()

        mainMenu.render_game_objects()
        pygame.draw.rect(
            mainMenu.screen, (0, 0, 0), mainMenu.gameObjects["titleTxt"].boundingBox, 5
        )
        pygame.draw.rect(
            mainMenu.screen, (0, 0, 0), mainMenu.gameObjects["pvpBtn"].boundingBox, 5
        )
        window.blit(mainMenu.screen, (mainMenu.x, mainMenu.y))
        pygame.display.update()
