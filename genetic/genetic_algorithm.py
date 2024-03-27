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


def crossover(parent1, parent2):
    # Performs crossover between two parent algorithms to create offspring
    # TODO: implement a better crossover logic
    child_parameters = {}
    for key, value in parent1.parameters.items():
        if random.random() < 0.5:
            child_parameters[key] = value
        else:
            child_parameters[key] = parent2.parameters[key]
    return TCPAlgorithm(child_parameters)


def mutate(algorithm):
    # Mutate the parameters of an algorithm with a small probability
    # TODO: implement a better mutation logic
    for key, value in algorithm.parameters.items():
        if random.random() < 0.1:
            algorithm.parameters[key] += random.uniform(-0.1, 0.1)
    return algorithm


def main():
    # Hyperparameters
    population_size = 100
    generations = 100

    # Initialise population
    population = [generate_random_algorithm() for _ in range(population_size)]

    # Evolve for generations
    for generation in range(generations):
        # Evaluate fitness
        fitness = [algorithm.simulate() for algorithm in population]

        print(
            f"Generation {generation}: Average fitness: {sum(fitness) / len(fitness)}"
        )

        # Selection
        # TODO: implement different selection algorithms here, e.g. roulette wheel selection, tournament selection
        # Good place to use a strategy pattern
        selected_parents = []
        for _ in range(int(population_size / 2)):
            # Select two parents based on their fitness
            parent1_index = fitness.index(max(fitness))
            fitness.pop(parent1_index)
            parent2_index = fitness.index(max(fitness))
            fitness.pop(parent2_index)
            selected_parents.append(population[parent1_index])
            selected_parents.append(population[parent2_index])

        # Crossover and mutation
        offspring = []
        for i in range(0, population_size, 2):
            parent1, parent2 = selected_parents[i], selected_parents[i + 1]
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            offspring.append(child1)
            offspring.append(child2)

        # Replace old population with offspring
        population = offspring

    fitness = [algorithm.simulate() for algorithm in population]
    best_algorithm = population[fitness.index(max(fitness))]
    print(f"Best algorithm: {best_algorithm.parameters}")
    print(f"Best fitness: {max(fitness)}")


if __name__ == "__main__":
    main()
