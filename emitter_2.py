import particle
import random

GREEN = [0, 255, 0]
RED = [255, 0, 0]
BLUE = [0, 0, 255]
colors = [GREEN , RED, BLUE]

class BaseEmitter():

    # FILL THE POOL
    def fill_pool(self):
        for i in range(self.pool_size):
            self.particle_pool.append([particle.Particle(10, 10, colors[random.randrange(0, 3)], 400, 400, 2, 5, random.randrange(-180,180), random.randrange(-180, 180), 0), "alive"])

    # SORT
    def sort(self):

        for i in range(self.pool_size):
            if self.particle_pool[i][0].life < 0:
                self.particle_pool[i][0].recover()
                self.particle_pool[i][1] = "alive"

            if self.particle_pool[i][1] == "dead":
                for j in range(i, self.pool_size):
                    if self.particle_pool[j][1] == "alive":
                        self.particle_pool[i], self.particle_pool[j] = self.particle_pool[j], self.particle_pool[i]
    # EMITT
    def emitt_particle(self, index):
        self.group.add(self.particle_pool[index][0])
        self.particle_pool[index][1] = "dead"
    def emitt(self):
        for i in range(self.requested_particles):
            self.emitt_particle(i)
    
    def update(self):
        self.sort()
        #for i in range(self.pool_size):
         #   print(self.particle_pool[i][1])

    def __init__(self, pool_size, group):
        self.particle_pool = []
        self.pool_size = pool_size
        self.group = group
        self.requested_particles = 5

        self.fill_pool()

class FountainEmitter(BaseEmitter):

    def fill_pool(self):
        for i in range(self.pool_size):
            self.particle_pool.append(
                [particle.Particle(10, 10, BLUE, 400, 400, 2, random.randrange(4, 9), random.randrange(80, 100), 90, 1), "alive"])

    def __init__(self, pool_size, group):
        super().__init__(pool_size, group)
        self.pool_size = pool_size
        self.particle_pool = []
        self.group = group 
        self.requested_particles = 30

        self.fill_pool()

