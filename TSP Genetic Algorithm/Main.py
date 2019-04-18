from Population import Population
from SelectionStrategies import SelectionStrategies
from RecombinationStrategies import RecombinationStrategies
from MutationStrategies import MutationStrategies
from ReinsertionStrategies import ReinsertionStrategies


# MAIN SCRIPT FOR GENETIC ALGORITHM. IMPORTS ALL THE MODULES AND APPLIES IN A ROW

# P.S WITH THE DEACTIVATED #PRINTS IN THE CODE; YOU CAN CHECK THE PROCESSES OF THE ALGORITHM BY GETTNG ACTIVATED

class Engine_TSP_GA:
    def main(self):
        run = 100
        child = 20  # Replicates "2 x child" children

        for j in range(run):

            prov = Population(100)
            selection = SelectionStrategies()
            recombination = RecombinationStrategies()
            mutation = MutationStrategies()
            reinsertion = ReinsertionStrategies()
            prov.main()
            generations = 10000
            fitness_values = prov.fitness_values
            population = prov.population

            for count in range(generations):

                for children in range(child):

                    population, fitness_values = selection.sort_by_fitness(population, fitness_values)  # 1. STEP
                    # print(fitness_values, "Sorting")
                    parent1, parent2 = selection.best_selection(population)  # 2. STEP
                    # You can choose "order1" or "cycle" crossovers .
                    child1, child2 = recombination.crossover_ox1(parent1, parent2)  # 3. STEP
                    # child1, child2 = recombination.crossover_cycle(parent1, parent2)
                    # You can choose "displacement" or "swap".
                    child1, child2 = mutation.mutation_dm(child1, child2)  # 4.STEP
                    # child1, child2 = mutation.mutation_swap(child1, child2)
                    fitness_of_child1 = prov.get_total_distance(child1, prov.city_names, prov.routes)  # 5.STEP
                    fitness_of_child2 = prov.get_total_distance(child2, prov.city_names, prov.routes)
                    # print(fitness_of_child1, "Fitness Of Child1")
                    # print(fitness_of_child2, "Fitness of Child2")
                    population, fitness_values = reinsertion.tournament(child1, child2, population, fitness_values,
                                                                        fitness_of_child1, fitness_of_child2)  # 6.STEP
                    # print(fitness_values, "After Insertation")


            print(' -> '.join(population[0]), "Best Route")
            print(fitness_values[0])


if __name__ == '__main__':
    object_Engine_TSP_GA = Engine_TSP_GA()
    object_Engine_TSP_GA.main()
