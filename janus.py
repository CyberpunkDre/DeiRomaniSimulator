'''

janus.py

This object's role in the simulation is to track time.
It will coordinate the actions and time scale of Minerva and Mercury.
'''

import time

class Janus(object):

    def __init__(self, sim_rate = 1e-11, sample_rate = 1e-9, duration = 2e-6):
        self.start_time = time.time()
        self.sim_time = 0
        self.sample_time = 0
        self.sim_rate = sim_rate
        self.sample_rate = sample_rate
        self.duration = duration
        self.sample = False
        self.end = False
        print("Janus Online.")

    def tick(self):
        self.sim_time += sim_rate
        self.sample_time += sim_rate # Intentional, this will reset. Assume sample_rate < 2 * sim_rate (Nyquist or else!!)
        if(self.sample_time >= self.sample_rate):
            self.sample = True
            self.sample_time = 0
        if(self.sim_time >= self.duration):
            self.end = True
        
    def now(self):
        return self.sim_time

    def sample_now(self):
        if(self.sample):
            self.sample = False
            return True
        return False

    def finished(self):
        return self.end

def main():
    print("You are in a little maze of twisty passages, all alike")

if __name__ == "__main__":
    main()