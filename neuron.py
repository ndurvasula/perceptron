class Neuron:
    def __init__(self, _bias, _weights):
        self.bias = _bias
        self.weights = _weights

    def __activation(self, x):
        if (x < 0):
            return 0
        return 1

    # 
    def n_apply(self, in_vec):
        accum = self.bias
        for i in xrange(len(in_vec)):
            accum += in_vec[i] * self.weights[i]

        return self.__activation(accum)
    
    # adjust neuron based on error
    # inp is list of inputs to this neuron
    # partial is the partial derivative of error with respect to weighted input
    # lr is learning rate
    def adjust(self, inp, partial, lr):
        for i in xrange(len(ins)):
            self.weights[i] += inp[i] * partial * lr
        self.bias += partial * lr
