import random

def main():
	size = 10
	lr = .1
	num_data = 10
	data_size = 1

	layer1 = []
	for i in range(size):
		bias = random.random()
		weights = [random.random() for i in range(data_size)]
		layer1.append(Neuron(bias, weights))

	
