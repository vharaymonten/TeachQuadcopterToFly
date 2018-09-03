import keras 
from keras.models import Model 
from keras import backend as K

from keras import layers, optimizers ,regularizers
import numpy as np
import random 
import os 

class Actor:
    def __init__(self, state_size, action_size, action_high, action_low):
        self.state_size = state_size
        self.action_size = action_size
        self.action_high = action_high
        self.action_low = action_low
        self.action_range = action_high - action_low 
        self.build_model()
    def build_model(self):
        states = layers.Input(shape=(self.state_size,), name='states')
        net = layers.Dense(250, activation='relu')(states)
        net = layers.BatchNormalization()(net)
        net = layers.Dense(100, activation='relu')(net)
       
        net = layers.BatchNormalization()(net)
        
        #net = layers.Dense(80, activation='relu')(net)
        #net = layers.BatchNormalization()(net)
        actions_raw = layers.Dense(self.action_size, activation='sigmoid',\
                                   kernel_initializer=layers.initializers.TruncatedNormal(mean=0, stddev=0.1, seed=101)) (net)
        
        actions = layers.Lambda(lambda x : (x*self.action_range) + self.action_low) (actions_raw)
        
        
        self.model = Model(inputs=states, outputs=actions)
        action_gradients = layers.Input(shape=(self.action_size,))
        loss = K.mean(-action_gradients * actions)
        optimizer = optimizers.Adam(1e-3)
        update_op = optimizer.get_updates(params=self.model.trainable_weights, loss=loss)
        self.train_fn = K.function(inputs=[states, action_gradients, K.learning_phase()], \
                                   outputs=[],
                                   updates=update_op)
