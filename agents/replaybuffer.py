import random 
from collections import deque, namedtuple 


class ReplayBuffer:
    def __init__(self, memory_size=10000, batch_size=64):
        self.batch_size = batch_size
        self.memory = deque(maxlen=memory_size)
        self.experience = namedtuple("Experience", field_names=["state", "action","reward", "next_state", "done"])
        
    def add(self, state, action, reward, next_state, done):
        self.memory.append(self.experience(state, action, reward, next_state, done))
        
    def sample(self):
        return random.sample(self.memory, k=self.batch_size)
    
    
    def __len__(self):
        return len(self.memory)
    
