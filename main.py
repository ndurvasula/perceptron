import random

def main():
    size = 10 # size of layer or number of neurons; 
	lr = .1 # learning rate; tells us how quickly we want our boundary to adjust itself 
	num_data = 10 # number of data points we can train on
	data_size = 1 # how many features each data point has

    # Creating a layer of <size> neurons
	layer1 = []
	for i in range(size):
		bias = random.random()
		weights = [random.random() for i in range(data_size)]
		layer1.append(Neuron(bias, weights))

	
