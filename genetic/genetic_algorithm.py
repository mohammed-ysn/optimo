import random


class TCPAlgorithm:
    def __init__(self, parameters):
        self.parameters = parameters

    def simulate(self):
        # For now return the sum of the parameters as the score if it is less than 5, else return 0
        # This is just a placeholder for the actual simulation
        # We should converge on an algorithm whose parameters sum to just under 5

        # TODO: hook this up to ns-3 simulation and generate a score based on the simulation results

        s = self.parameters["param1"] + self.parameters["param2"]
        return s if s < 5 else 0


def generate_random_algorithm():
    # Generate a random TCP congestion control algorithm with random parameters
    # TODO: when I have implemented a congestion control algorithm in ns-3, I can use the parameters of that algorithm and parameter ranges
    parameters = {
        "param1": random.uniform(0, 1),
        "param2": random.uniform(0, 1),
    }
    return TCPAlgorithm(parameters)


def mutate(algorithm, mutation_rate=0.1, mutation_range=(-0.1, 0.1)):
    # Mutate the parameters of an algorithm with a small probability
    # TODO: implement a better mutation logic
    for key in algorithm.parameters.keys():
        if random.random() < mutation_rate:
            mutation_amount = random.uniform(*mutation_range)
            algorithm.parameters[key] += mutation_amount
            # TODO: clamp the parameter values to a valid range
    return algorithm
