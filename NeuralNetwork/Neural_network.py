
import Neuron as n
import numpy as np


class Neuron_layer:
    n_neurons: int

    def __init__(self,N_neurons,N_input = 2):
        self.n_neurons = N_neurons
        self.n_input = N_input

        self.neurons = []
        self.setup_neurons()
        self.previous_layer = None
        self.posterior_layer = None
        self.is_output_layer = True



    def feed(self,Input):
        shape = Input.shape
        output = np.empty([shape[0],self.n_neurons])
        # for i in range(shape[0]):
        for j in range(self.n_neurons):
            output[:,[j]] = self.neurons[j].feed(Input)

        if self.is_output_layer:
            return output
        else:
            return self.posterior_layer.feed(output)

    def add_prev_layer(self,Prev_layer):
        if type(Prev_layer) == Neuron_layer:
            self.previous_layer = Prev_layer
            self.previous_layer.is_output_layer = False
        else:
            raise TypeError

    def add_post_layer(self, Posterior_layer):
        if type(Posterior_layer) == Neuron_layer:
            self.posterior_layer = Posterior_layer
            self.is_output_layer = False
        else:
            raise TypeError

    def setup_neurons(self):
        for i in range(self.n_neurons):
            self.neurons.append(n.Neuron_sigmoid(self.n_input))

    def setup_learning_rate(self,LR):
        for i in range(self.n_neurons):
            self.neurons[i].set_learing_rate(LR)


# nn = Neuron_layer(4,N_input=3)
# # print(nn.neurons[0].weights)
# input = np.array([[1,2,3],[-1,-2,-3]])
# out = nn.feed(input)
# print("out: \n",out)

input = np.array([[1, 2, 3], [0, 0, 0], [-1, -2, -3]])
net = Neuron_layer(4,3)
for i in range(3):
    net.neurons[i].weights = np.ones([3])
    net.neurons[i].biases = 0
result = net.feed(input)
print(result)