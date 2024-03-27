from crossover import (
    ArithmeticCrossover,
    BlendCrossover,
    SinglePointCrossover,
    UniformCrossover,
)
from genetic_algorithm import generate_random_algorithm, mutate


def main(crossover_strategy):
    # Hyperparameters
    population_size = 100
    generations = 100

    # Initialise population
    population = [generate_random_algorithm() for _ in range(population_size)]

    # Evolve for generations
    for generation in range(generations):
        # Evaluate fitness
        fitness = [algorithm.simulate() for algorithm in population]

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
            child1 = crossover_strategy.crossover(parent1, parent2)
            child2 = crossover_strategy.crossover(parent1, parent2)
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
    blend_crossover = BlendCrossover(alpha=0.5)
    print("Blend Crossover")
    main(blend_crossover)
    uniform_crossover = UniformCrossover()
    print("Uniform Crossover")
    main(uniform_crossover)
    arithmetic_crossover = ArithmeticCrossover()
    print("Arithmetic Crossover")
    main(arithmetic_crossover)
    single_point_crossover = SinglePointCrossover()
    print("Single Point Crossover")
    main(single_point_crossover)
