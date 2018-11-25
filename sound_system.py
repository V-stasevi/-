import pygame

"""
Класс звукового сопровождения. 

Описание методов:
1. playEatSeedSound(loops) - воспроизводит звук съедания зерна. loops - количество повторений звука, по умолчанию воспроизводится 1 раз
2. playEatFruitSound(loops) - воиспроизводит звук съедания вишенки
3. playEatGhostSound(loops) - воспроизводит звук съедания привидения
4. playIntermissionSound(loops) - воспроизводит звук испуганного привидения
5. playDeathSound(loops) - Воспроизводит звук смерти пакмана
6. playExtraPacmanSound(loops) - Воспроизводит звук новой жизни пакмана
7. playIntroSound() - Воспроизводит начальную мелодию.
8. UpdateValue(volume) - обновляет уровень звука. Volume - новое значение уровня громкости, от 0 до 1
"""


class Sounds:
    def __init__(self, volume=1):
        self.eatSeedSound = pygame.mixer.Sound('sounds/pacman_chomp.wav')
        self.eatFruitSound = pygame.mixer.Sound('sounds/pacman_eatfruit.wav')
        self.eatGhostSound = pygame.mixer.Sound('sounds/pacman_eatghost.wav')
        self.extraPacmanSound = pygame.mixer.Sound('sounds/pacman_extrapac.wav')
        self.intermissionSound = pygame.mixer.Sound('sounds/pacman_intermission.wav')
        self.deathSound = pygame.mixer.Sound('sounds/pacman_death.wav')
        self.updateVolume(volume)

    def playEatSeedSound(self, loops=1):
        self.eatSeedSound.play(loops-1)

    def playEatFruitSound(self, loops=1):
        self.eatFruitSound.play(loops-1)

    def playEatGhostSound(self, loops=1):
        self.eatGhostSound.play(loops-1)

    def playExtraPacmanSound(self, loops=1):
        self.extraPacmanSound.play(loops-1)

    def playIntermissionSound(self, loops=1):
        self.intermissionSound.play(loops-1)

    def playDeathSound(self, loops=1):
        self.deathSound.play(loops-1)

    def updateVolume(self, volume):
        self.eatSeedSound.set_volume(volume)
        self.eatFruitSound.set_volume(volume)
        self.eatGhostSound.set_volume(volume)
        self.extraPacmanSound.set_volume(volume)
        self.intermissionSound.set_volume(volume)
        self.deathSound.set_volume(volume)

    def playIntroSound(self):
        pygame.mixer.music.load('sounds/pacman_beginning.wav')
        pygame.mixer.music.play()