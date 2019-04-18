import random
from collections import Counter
from MutationStrategies import MutationStrategies

crossover_rate = 0.75

# CROSSOVER STRATEGIES

# - ORDER_1 CROSSOVER
# - CYCLE CROSSOVER

# P.S WITH THE DEACTIVATED #PRINTS IN THE CODE; YOU CAN CHECK THE PROCESSES OF THE ALGORITHM BY GETTNG ACTIVATED


class RecombinationStrategies:
    def crossover_ox1(self, parent1, parent2):

        if random.random() < crossover_rate:

            dna1 = parent1[1:-1]    #Extracting the first and last not to break the route rule
            dna2 = parent2[1:-1]
            # print(dna1, "dna1")
            # print(dna2, "dna2")

            pos1 = random.randint(0, len(dna1) - 1)
            pos2 = random.randint(0, len(dna2) - 1)

            if pos1 == pos2:
                pos2 = random.randint(0, len(dna1))

            cr_point_1, cr_point_2 = min(pos1, pos2), max(pos1, pos2)

            # For First Child

            child1_temp = []                        # Separate the genes from random points and take the fixed part
            part1 = dna1[cr_point_1:cr_point_2]     # finds and add the duplicates to temporary matrix
            temp1 = [city for city in dna2[cr_point_2:] if city not in part1]
            temp2 = [city for city in dna2[:cr_point_2] if city not in part1]
            temp_tot = temp1 + temp2
            # print(part1, "part")

            for genes in dna1:                      # Adds the temporary matrix's elements starting from second break points.
                if genes in part1:
                    child1_temp.append(genes)
                else:
                    child1_temp.append(temp_tot.pop())
                    # print(temp_tot2)

            A = child1_temp[0:cr_point_1]           # Gets another temporary matrix which has the all parts
            B = child1_temp[cr_point_2:]

            child1 = parent1[:1] + A[::-1] + part1 + B[::-1] + parent1[-1:]
                                                                          # Creates the child adding intermediate part
                                                            # start and end cities and the reverse of temporary matrix.
            # print(child1, "child1")

            # For Second Child does the same

            child2_temp = []
            part2 = dna2[cr_point_1:cr_point_2]
            temp3 = [city for city in dna1[cr_point_2:] if city not in part2]
            temp4 = [city for city in dna1[:cr_point_2] if city not in part2]
            temp_tot2 = temp3 + temp4
            # print(part2, "part2")

            for alleles in dna2:
                if alleles in part2:
                    child2_temp.append(alleles)
                else:
                    child2_temp.append(temp_tot2.pop())
                    # print(temp_tot2)

            A_2 = child2_temp[0:cr_point_1]
            B_2 = child2_temp[cr_point_2:]

            child2 = parent2[:1] + A_2[::-1] + part2 + B_2[::-1] + parent2[-1:]

            # print(child2, "child2")
            # print("Crossover occurred")

            return child1, child2

        else:
            return parent1, parent2

    def crossover_cycle(self, parent1, parent2):

        if random.random() < crossover_rate:

            dna1 = parent1[1:-1]                            #Extracting the first and last not to break the route rule
            dna2 = parent2[1:-1]
            dna3 = parent1[1:-1]
            dna4 = parent2[1:-1]

            # print(parent1, "Parent1 Before Crossover")
            # print(parent2, "Parent2 Before Crossover")

            child1_temp = dna1                              # Creates temporary child matrixes.
            child2_temp = dna4

            i = random.randint(0, len(dna1) - 1)   # Performs cyclic for both children same time. The i'th gene
            start_i = i                            # of parent1 is replaced by i'th gene of parent2. Then this gene set
            j = i                                  # to be index of the same value in parent2. This repeated until i
            stop = False                           # i gets the same value with start.

            while not stop:
                replaced = child1_temp[i]
                replaced2 = child2_temp[j]
                # print(replaced, "replaced")
                # print(replaced2, "replaced2")
                child1_temp[i] = dna2[i]
                child2_temp[j] = dna3[j]
                i = dna2.index(replaced)
                j = dna3.index(replaced2)
                stop = i == start_i
                # print(i, " Indexes of Cycle")

            child1 = parent1[:1] + child2_temp + parent1[-1:]   # The child1 born from parent2-parent1
            child2 = parent1[:1] + child1_temp + parent1[-1:]   # The child2 born from parent1-parent2

            # print(child1)
            # print(child2)
            # print("Crossover Occured")

            return child1, child2
        else:
            return parent1, parent2
