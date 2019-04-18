import random


# P.S WITH THE DEACTIVATED #PRINTS IN THE CODE; YOU CAN CHECK THE PROCESSES OF THE ALGORITHM BY GETTNG ACTIVATED

# SELECTION OF THE TWO OF BEST PARENTS IN THE SELECTION SIZED MATRIX FOR BREEDING TWO CHILD

class SelectionStrategies:
    def sort_by_fitness(self, population, fitness_functions):
        # Sort the population by fitness
        fitness_functions, population = zip(*sorted(zip(fitness_functions, population)))
        fitness_functions, population = (list(t) for t in zip(*sorted(zip(fitness_functions, population))))

        # print(fitness_functions)

        return [population, fitness_functions]

    def best_selection(self, population):  # Tournament Size

        selection_size = 10
                                                        # Choose a breeding point from the best members
        # FOR ELITISM : CHANGE THE START INDEX POINT

        index1 = random.randint(1, selection_size)      # Choosing the position of the route in population
        index2 = random.randint(1, selection_size)
        while (index1 == index2):
            index1 = random.randint(1, selection_size)
            index2 = random.randint(1, selection_size)
        # print (index1, index2)
        parent1 = population[index1]  # Getting Parent1
        parent2 = population[index2]  # Getting Parent2
        # print(parent1)
        # print(parent2)

        return parent1, parent2  # these two will reproduce
