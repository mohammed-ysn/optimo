import random

from genetic_algorithm import TCPAlgorithm


class CrossoverStrategy:
    def crossover(self, parent1, parent2):
        raise NotImplementedError("Subclasses must implement this method")


class BlendCrossover(CrossoverStrategy):
    def __init__(self, alpha=0.5):
        self.alpha = alpha

    def crossover(self, parent1, parent2):
        child_parameters = {}
        for key in parent1.parameters.keys():
            p1_value = parent1.parameters[key]
            p2_value = parent2.parameters[key]
            # Alpha is the blending factor which controls the degree of exploration around the parents
            low = min(p1_value, p2_value) - self.alpha * abs(p1_value - p2_value)
            high = max(p1_value, p2_value) + self.alpha * abs(p1_value - p2_value)
            child_parameters[key] = random.uniform(low, high)
        return TCPAlgorithm(child_parameters)


class UniformCrossover(CrossoverStrategy):
    def crossover(self, parent1, parent2):
        child_parameters = {}
        for key in parent1.parameters.keys():
            if random.random() < 0.5:
                child_parameters[key] = parent1.parameters[key]
            else:
                child_parameters[key] = parent2.parameters[key]
        return TCPAlgorithm(child_parameters)


class ArithmeticCrossover(CrossoverStrategy):
    def crossover(self, parent1, parent2):
        child_parameters = {}
        for key in parent1.parameters.keys():
            child_parameters[key] = (
                parent1.parameters[key] + parent2.parameters[key]
            ) / 2
        return TCPAlgorithm(child_parameters)


class SinglePointCrossover(CrossoverStrategy):
    def crossover(self, parent1, parent2):
        child_parameters = {}
        keys = list(parent1.parameters.keys())
        split_point = random.randint(0, len(keys) - 1)
        for i, key in enumerate(keys):
            if i <= split_point:
                child_parameters[key] = parent1.parameters[key]
            else:
                child_parameters[key] = parent2.parameters[key]
        return TCPAlgorithm(child_parameters)
