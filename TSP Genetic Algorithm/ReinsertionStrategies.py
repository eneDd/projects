import random

# REINSERTATION STRATEGIES

# GENERATION GAP POPULATION MODEL

# P.S WITH THE DEACTIVATED #PRINTS IN THE CODE; YOU CAN CHECK THE PROCESSES OF THE ALGORITHM BY GETTNG ACTIVATED

class ReinsertionStrategies:
    def tournament(self, child1, child2, population, fitness_functions, fitness_of_child1, fitness_of_child2):

        # Reinsert the children to the population , if their fitness values are greater then worsts of population

        length = len(population)

        if fitness_of_child1 < fitness_of_child2:

            if fitness_of_child1 < fitness_functions[length - 2]:
                population[length - 2] = child1
                fitness_functions[length - 2] = fitness_of_child1
            else:
                pass

            if fitness_of_child2 < fitness_functions[length - 1]:
                population[length - 1] = child2
                fitness_functions[length - 1] = fitness_of_child2
            else:
                pass
        else:
            pass

        if fitness_of_child1 >= fitness_of_child2:

            if fitness_of_child2 < fitness_functions[length - 2]:
                population[length - 2] = child2
                fitness_functions[length - 2] = fitness_of_child2
            else:
                pass

            if fitness_of_child1 < fitness_functions[length - 1]:
                population[length - 1] = child1
                fitness_functions[length - 1] = fitness_of_child1
            else:
                pass
        else:
            pass

        return population, fitness_functions
