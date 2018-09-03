from keras.models import Model 
from keras import backend as K 
from keras import layers, optimizers , regularizers
class Critic:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.build_model()
      
    def build_model(self):
        states = layers.Input(shape=(self.state_size,), name='states')
        actions = layers.Input(shape=(self.action_size,), name='actions')
        
        s_net = layers.Dense(500)(states)
        s_net = layers.LeakyReLU(alpha=0.01) (s_net)
        s_net = layers.BatchNormalization()(s_net)
        s_net = layers.Dense(150)(s_net)
        s_net = layers.LeakyReLU(alpha=0.01) (s_net)
        s_net = layers.BatchNormalization()(s_net)
        
        a_net = layers.Dense(450)(actions)
        a_net = layers.LeakyReLU(alpha=0.01) (a_net)
        a_net = layers.BatchNormalization() (a_net)
        
        a_net = layers.Dense(150)(a_net)
        a_net = layers.LeakyReLU(alpha=0.01) (a_net)
        a_net = layers.BatchNormalization() (a_net)
     
        
        net = layers.Add() ([s_net, a_net])
        net = layers.LeakyReLU(alpha=0.01) (net)
        Q_value = layers.Dense(1, activation=None, kernel_initializer=layers.initializers.RandomNormal(mean=0, stddev=1, seed=101))(net)
        
        self.model = Model(inputs=[states, actions], outputs=Q_value)
        optimizer = optimizers.Adam(1e-4)
        self.model.compile(optimizer=optimizer, loss='mse')
        actions_gradients = K.gradients(Q_value, actions)
        self.get_action_gradients = K.function(inputs=[*self.model.input, K.learning_phase()],\
                                outputs=actions_gradients)
        
        