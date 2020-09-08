from typing import List, Union
import numpy as np
from numpy.core.multiarray import ndarray



import Activation_function as af


class Neuron:
    
    activation: af.Activation_function
    weights: Union[ndarray, float]
    bias: int
    learning_rate: float

    def __init__(self,N_Weigths = 2):
        self.weights = np.random.normal(size=[N_Weigths])
        self.bias = 0
        self.learning_rate = 0.1
        self.setUpNeuron()


    def setUpNeuron(self):
        self.activation = af.Activation_function()
        # print("Base neuron")

    # def activation(self, Output):
    #     return Output

    def feed(self,Inputs):
        z = np.empty([len(Inputs),1])
        for i in range(len(Inputs)):
            # result = np.matmul(Inputs[i,:],self.weights)+self.bias
            z[i,0] = self.activation(np.matmul(Inputs[i,:],self.weights)+self.bias)
        return z

    def train(self,Input, Desired_output):
        assert len(Input)==len(Desired_output),"Wrong dimensiones for Input {:d} and Output {:d}".format(len(Input), len(Desired_output))
        output = self.feed(Input)
        dif = Desired_output-output
        derivative = self.activation.derivative(Input)
        for i in range(len(Input)):
            for j in range(len(self.weights)):
                # print("DIF",dif[i,0])
                # print("IN: ",Input[i,j])
                self.weights[j] += self.learning_rate*dif[i,0]*derivative[i,0]*Input[i,j]
            self.bias += (self.learning_rate*dif[i])[0]



    def set_weights(self,Values):
        assert len(Values) == len(self.weights),"Invalid Length of weights."
        for i,val  in enumerate(Values):
            self.weights[i] = val

    def get_weights(self):
        return self.weights

    def set_bias(self,Value):
        assert type(Value)==int, "Invalid data type"
        self.bias = Value

    def get_bias(self):
        return self.bias

    def set_learing_rate(self, Value):
        if type(Value)==int or type(Value) == float:
            self.learning_rate = Value



class Perceptron(Neuron):

    def __init__(self,N_Weigths = 2):
        super().__init__(N_Weigths)
    # def feed(self,Inputs):
    #     z = np.empty([len(Inputs), 1])
    #     for i in range(len(Inputs)):
    #         result = np.matmul(Inputs[i, :], self.weights) + self.bias
    #         if result > 0:
    #             z[i, 0] = 1
    #         else:
    #             z[i, 0] = 0
    #     return z
    def setUpNeuron(self):
        # print("Perceptro setup")
        self.activation = af.Activation_step()

    # def activation(self, Output):
    #     if Output > 0:
    #         return 1
    #     else:
    #         return 0

class Neuron_sigmoid(Neuron):
    def __init__(self,N_Weigths = 2):
        super().__init__(N_Weigths)

    def setUpNeuron(self):
        # print("Perceptro setup")
        self.activation = af.Activation_sigmoid()



    # def activation(self, Output):
    #     return 1 / (1 + np.exp(-Output))



# neuron = Perceptron()
# input_data = np.array([[1,1],[0,1],[0,0],[1,0]])#generar and method
# desired_output = np.array([[1],[0],[0],[0]])
# print("Before \n",neuron.feed(input_data))
# for i in range(20):
#     # print("Weigths: ",neuron.weights)
#     neuron.train(input_data,desired_output)
#     # print("Weigths: ",neuron.weights)
# print("After: \n",neuron.feed(input_data))






# print(input_data)
# neuron.set_weights(np.array([1,-1]))
# neuron.set_bias(0)
# print(neuron.feed(input_data))
# z = np.random.random([100,100])
# result = neuron.feed(z)
# print(result)

