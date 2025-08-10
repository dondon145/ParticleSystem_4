import particle
import random

# colors 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Emitter():

    # FILL PARTICLE POOL
    def fill_particle_pool(self):
        for i in range(self.pool_size):
            self.particle_pool.append([particle.Particle(30, 30, RED, 400, 400, 1.5, 5, random.randrange(0,30), 90), "alive"])
    

    # KILL and RECOVER particles
    def declare_dead(self):
        for i in range(self.pool_size -1):
            life_val = self.particle_pool[i][0].life
            if life_val < 0:
                self.particle_pool[i][1] = "dead"    
    def recover_dead(self):
        for i in range(self.pool_size-1):
            life_val = self.particle_pool[i][0].life
            if life_val < 0:
                self.particle_pool[i][0].recover()
                self.particle_pool[i][1] = "alive"


    # REQUESTED PARTICLES
    def set_requested_amount(self, val):
        self.requested_amount = val
    def request_amount(self):
        return self.requested_amount
    def check_available_amount(self):
        
        available_amount = 0
        for i in range(self.pool_size-1):
            if self.particle_pool[i][1] == "alive":
                available_amount += 1

        return available_amount
    def get_emitt_amount(self):
        
        request_amount = self.request_amount()
        available_amount = self.check_available_amount()

        if request_amount > available_amount:
            return available_amount
        else:
            return request_amount
    

    # SORT POOL
    def find_alive_index(self):
        for i in range(self.pool_size-1):
            if i == 0:
                state = self.particle_pool[0][1]
                if state == "alive":
                    return i
            else :
                state = self.particle_pool[-i][1]
                if state == "alive":
                    return -i                    
    def find_dead_index(self):
        for i in range(self.pool_size):
            state = self.particle_pool[i][1]
            if state == "dead":
                return i
    def compare_and_switch_dead_and_alive_indexes(self):
        
        alive_index = self.find_alive_index()
        dead_index = self.find_dead_index()

        if alive_index != None and dead_index != None:
            if -alive_index > dead_index :
                self.particle_pool[alive_index], self.particle_pool[dead_index] = self.particle_pool[dead_index], self.particle_pool[alive_index]


    # EMITTING
    def set_emitting_state(self, val):
        self.isEmitting = val
    def emitt_particle(self, index):
        self.group.add(self.particle_pool[index][0])
    def emitt_requested_amount(self):
        emitt_amount = self.get_emitt_amount()

        for i in range(emitt_amount-1):
            self.emitt_particle(i)


    # DELAY between every emission
    def set_delay(self, val):
        self.delay = val
    def set_delay_counter(self, val):
        self.delay_counter = val
    def count_to_delay(self, val):
        self.delay_counter += val

        return self.delay_counter


    # UPDATE
    def update(self):
        self.emitt_requested_amount()
        self.declare_dead()
        self.compare_and_switch_dead_and_alive_indexes()
        for i in range(self.pool_size-1):
            print(self.particle_pool[i][1])
            


    def __init__(self, pool_size, group, requested_amount, delay):
        # PARTICLE POOL AND GROUP
        self.particle_pool = []
        self.pool_size = pool_size
        self.group = group
        self.requested_amount = requested_amount

        # STATE
        self.isEmitting = False
        self.delay = delay
        self.delay_counter = 0

        # FUNCTIONS
        self.fill_particle_pool()