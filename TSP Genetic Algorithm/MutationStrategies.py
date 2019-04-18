import random

mutation_rate = 0.08


# MUTATION STRATEGIES

# - SWAP MUTATION
# - DISPLACEMENT MUTATION

# P.S WITH THE DEACTIVATED #PRINTS IN THE CODE; YOU CAN CHECK THE PROCESSES OF THE ALGORITHM BY GETTNG ACTIVATED

class MutationStrategies:
    def mutation_swap(self, child1, child2):  # Swap Mutation Method

        if random.random() < mutation_rate:  # Dice
            mutation_position_1 = random.randint(1, len(child1) - 2)  # Chossing the positions of swapping
            mutation_position_2 = random.randint(1, len(child1) - 2)  # Chossing the positions of swapping
            # print(mutation_position_1, "Mutation_pos1")
            # print(mutation_position_2, "Mutation_pos2")
            if mutation_position_1 == mutation_position_2:
                mutation_position_2 = random.randint(1, len(child1) - 2)

            # FIRS CHILD

            city1 = child1[mutation_position_1]
            city2 = child1[mutation_position_2]

            child1[mutation_position_2] = city1  # Swaps the Cities
            child1[mutation_position_1] = city2
            # print("Mutation occurred")
        else:
            pass

        if random.random() < mutation_rate:  # Dice
            mutation_position_1 = random.randint(1, len(child1) - 2)  # Chossing the positions of swapping
            mutation_position_2 = random.randint(1, len(child1) - 2)  # Chossing the positions of swapping
            # print(mutation_position_1, "Mutation_pos1")
            # print(mutation_position_2, "Mutation_pos2")
            if mutation_position_1 == mutation_position_2:
                mutation_position_2 = random.randint(1, len(child1) - 2)

            # SECOND CHILD

            city1_2 = child2[mutation_position_1]
            city2_2 = child2[mutation_position_2]

            child2[mutation_position_2] = city1_2
            child2[mutation_position_1] = city2_2
            # print("Mutation occurred")
        else:
            pass

        return child1, child2  # Mutated Childs

    def mutation_dm(self, child1, child2):  # Displacement Mutation

        if random.random() <= mutation_rate:
            # print(child1)
            subtour_start = random.randint(1, int(len(child1) / 2))
            subtour_end = random.randint(1, int(len(child1) / 2))

            if subtour_end == subtour_start:
                subtour_end = random.randint(1, int(len(child1) / 2))

            subtour_start, subtour_end = min(subtour_start, subtour_end), max(subtour_start, subtour_end)
            subtour = child1[subtour_start: subtour_end]  # Chooses the subtour in the child routes
            # print(subtour, "subtour")
            child_temp = [item for item in child1 if item not in subtour]  # Substract the Subtour Temporily
            displacement_position = random.randint(1, len(child_temp) - 1)  # Chooses the new position
            child1 = child_temp[:displacement_position] + subtour + child_temp[
                                                                    displacement_position:]  # Adds the subtour to new place
            # print(child1)
            # print("Child1 Mutation occurred")
        else:
            pass

        if random.random() <= mutation_rate:
            # print(child2)
            subtour_start = random.randint(1, int(len(child2) / 2))
            subtour_end = random.randint(1, int(len(child2) / 2))

            if subtour_end == subtour_start:
                subtour_end = random.randint(1, int(len(child2) / 2))

            subtour_start, subtour_end = min(subtour_start, subtour_end), max(subtour_start, subtour_end)
            subtour2 = child2[subtour_start: subtour_end]  # Chooses the subtour in the child routes
            # print(subtour2, "subtour")
            child2_temp = [item for item in child2 if item not in subtour2]         # Substract the Subtour Temporily
            displacement_position = random.randint(1, len(child2_temp) - 1)         # Chooses the new position
            child2 = child2_temp[:displacement_position] + subtour2 + child2_temp[
                                                                      displacement_position:]  # Adds the subtour to new place
            # print(child1)
            # print("Child2 Mutation occurred")
        else:
            pass

        return child1, child2
