class GameLogic:
    def update(self, pacman, ghost):
        # update on the ghost behavior based on pacmans position
        ghost.update((pacman.x, pacman.y))
