import random

def det_answer(x):
    return x * x < 9


def main():
    size = 10 # size of layer or number of neurons; 
    lr = .1 # learning rate; tells us how quickly we want our boundary to adjust itself 
    num_data = 10 # number of data points we can train on
    data_size = 1 # how many features each data point has

    # Creating a layer of <size> neurons
    in_layer = [Neuron(random.random(), [random.random() for i in xrange(data_size)])]

    hidden_layer = []
    for i in range(size):
            bias = random.random()
            weights = [random.random() for i in range(data_size)]
            hidden_layer.append(Neuron(bias, weights))

    out_layer = [Neuron(random.random(), [random.random() for i in xrange(size)]]

    while True:
        k = random.random() * 10
        inp = in_layer.n_apply([k])
        hp = [n.n_apply(inp) for n in hidden_layer]
        op = out_layer.n_apply(hp) 


if __name__ == '__main__':
    main()
