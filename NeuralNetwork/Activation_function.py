import numpy as np


class Activation_function:
    def __init__(self):
        pass
    def __call__(self, Value):
        return Value

    def derivative(self,Value):

        return np.ones([len(Value),1])

class Activation_step(Activation_function):
    def __call__(self, Value):
        if Value>0:
            return 1
        return 0


class Activation_sigmoid(Activation_function):
    def __call__(self, Value):
        return 1 / (1 + np.exp(-Value))

    def derivative(self,Value):
        return self(Value)*(1-self(Value))