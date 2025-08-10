import pygame
import math

class Particle(pygame.sprite.Sprite):

    # KILLING and HEALING
    def reset(self):
        self.pos_x = self.original_pos_x
        self.pos_y = self.original_pos_y
        self.vel_x = self.original_vel_x
        self.vel_y = self.original_vel_y
        self.time = 0
        self.color = [0, 0, 255]

    def die(self):
        if self.life < 0:
            self.kill()
    def recover(self):
        if self.life < 0:
            self.life = 1.5
            self.reset()


    # TIME and Life changes
    def run_time(self, delta_time):
        self.time += delta_time
    def run_life(self, delta_time):
        self.life -= delta_time
    def fade(self):
        if self.alpha > 0.6:
            self.alpha = self.life/self.original_life
        else:
            self.alpha = self.life/2/self.original_life
        self.image.set_alpha(self.alpha*255)

    """def color_to_white(self, first, second):
        self.color[first] += 2.5
        self.color[second] += 2.5
        
        if self.color[0]> 255:
            self.color[0]= 255
        if self.color[1]> 255:
            self.color[1]= 255
        self.image.fill(self.color)"""

    # GRAVITY
    def velocity_with_gravity(self):
        self.vel_y -= self.acceleration* self.time

    # MOVING
    def move(self):
        self.pos_x += self.vel_x
        self.pos_y -= self.vel_y

        self.rect.center = (self.pos_x, self.pos_y)

    # UPDATE
    def update(self):
        self.die()
        self.run_time(1/60)
        self.run_life(1/60)
        self.velocity_with_gravity()
        self.move()
        self.fade()
        #self.color_to_white(0, 1)
        #print(self.color[0])

    def __init__(self, width, height, color, pos_x, pos_y, life, speed, angle_x, angle_y, acceleration):
        super().__init__()

        self.original_color = self.color = color
        self.image = pygame.Surface((width, height))
        self.image.fill(self.color)
        

        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        self.original_pos_x = self.pos_x = pos_x
        self.original_pos_y = self.pos_y = pos_y

        self.original_vel_x = self.vel_x = speed* math.cos(angle_x* math.pi/180)
        self.original_vel_y = self.vel_y = speed* math.sin(angle_y* math.pi/180)

        self.acceleration = acceleration
        self.original_life = self.life = life
        self.time = 0
        self.alpha = 1

