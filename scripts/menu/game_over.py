from scripts.menu.utils import Button
from scripts.utils import restart_level

import pygame

class Game_over:
    def __init__(self, game, joysticks):
        self.game = game
        self.joysticks = joysticks

        self.screen_size = game.screen_size
        self.screen = game.screen

        self.restart_button = Button((960-190, 245+400), 'RESTART LEVEL')
        self.exit_button = Button((960-190, 390+400), 'EXIT')

        self.joy_button = 0
        self.joy_group = 0

        self.joy_map = [
                        ['restart'],
                        ['exit'],
                       ]


        self.axis = [0,0]

        self.font = pygame.font.Font('data/fonts/Kenney Future.ttf', 36)

        self.control_pause = True
        self.clicking = False
        self.right_clicking = False

        self.interface = pygame.Surface((1920,1080), flags=pygame.SRCALPHA)


    def controller_movements(self):
        for index in range(len(self.joysticks)):
            joystick = self.joysticks[index]

            if round(joystick.get_axis(0),0) == -1:
                if self.axis[0] > 0:
                    self.axis[0] = 0
                self.axis[0] -= 1

            elif round(joystick.get_axis(0),0) == +1:
                if self.axis[0] < 0:
                    self.axis[0] = 0
                self.axis[0] += 1
            
            else: self.axis[0] = 0



            if abs(self.axis[0]) == 15:
                self.axis[0] = 0



            if round(joystick.get_axis(1),0) == -1:
                if self.axis[1] > 0:
                    self.axis[1] = 0
                self.axis[1] -= 1

            elif round(joystick.get_axis(1),0) == +1:
                if self.axis[1] < 0:
                    self.axis[1] = 0
                self.axis[1] += 1
            
            else: self.axis[1] = 0



            if abs(self.axis[1]) == 15:
                self.axis[1] = 0
            
            if self.axis[1] == 1:
                self.joy_group = (self.joy_group+1) % len(self.joy_map) 
            elif self.axis[1] == -1:
                self.joy_group = (self.joy_group-1) % len(self.joy_map)

            if self.axis[0] == 1:
                self.joy_button = (self.joy_button+1) % len(self.joy_map[self.joy_group]) 
            elif self.axis[0] == -1:
                self.joy_button = (self.joy_button-1) % len(self.joy_map[self.joy_group])
            
            
    def get_mpos(self):
            RENDER_SCALE = self.screen_size[0]/1920
            mpos = pygame.mouse.get_pos()
            mpos = (mpos[0] / RENDER_SCALE, mpos[1] / RENDER_SCALE)

            return [int(mpos[0]), int(mpos[1])]
    
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.control_pause = False

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    for index in range(len(self.joysticks)):
                        joystick = self.joysticks[index]
                        if joystick.get_button(0):
                            self.clicking = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:       # LEFT CLICK
                    self.clicking = True
                elif event.button == 3:     # RIGHT CLICK
                    self.right_clicking = True


            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:       # LEFT CLICK
                    self.clicking = False
                elif event.button == 3:     # RIGHT CLICK
                    self.right_clicking = False

            elif event.type == pygame.QUIT:
                pygame.quit()
        
    def render(self):
        surf = self.interface
        m_pos = self.get_mpos()
        clicking = self.clicking

        text = self.font.render('GAME OVER!', True, (255,255,255))
        text_rect = text.get_rect(center=(1920/2,500))
        surf.blit(text, text_rect)
        
        # surf.blit(restart_image('logo.png'), (1920/2-384/2,20))
    
        if len(self.joysticks) != 0: 
            self.controller_movements()
            
            if self.joy_group == 0:
                m_pos = (960-190, 245+400)
            
            elif self.joy_group == 1:
                m_pos = (960-190, 390+400)
            

        
        if self.restart_button.update(surf, m_pos, clicking):
            restart_level(self.game, restart_lives=True)
            self.control_pause = False

        if self.exit_button.update(surf, m_pos, clicking):
            pygame.quit()
        
    def run(self, surf):
        surf.fill((0,0,0,125))
        self.game.screen.blit(pygame.transform.scale(surf, self.game.screen_size), (0,0))
        pygame.display.update()
        self.control_pause = True
        self.clicking = False
        while self.control_pause:
            self.process_events()

            self.render()

            self.screen.blit(pygame.transform.scale(self.interface, self.screen_size), (0,0))
            pygame.display.update()
