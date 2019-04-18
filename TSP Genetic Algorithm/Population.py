import csv, random, os.path


# POPULATION.py has the functions that GA uses for initializing and doing main calculations for algorithm.

# P.S WITH THE DEACTIVATED #PRINTS IN THE CODE; YOU CAN CHECK THE PROCESSES OF THE ALGORITHM BY GETTNG ACTIVATED

class Population:
    # INITIALIZING---------------------------------------------------------------------------

    def __init__(self, population_size):
        self.routes = []
        self.city_names = []
        self.population = []
        self.fitness_values = []
        self.population_size = population_size

        # READS THE CSV FILE -----------------------------------------------------------------

    def get_raw_data(self, filename, delim):
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=delim)
            data = []
            for row in reader:
                data.append(row)
                # print(data)
            return data

            # CALCULATES THE DISTANCE BETWEEN TWO CITIES-------------------------------------------

    def get_route_distance(self, A, B, list_of_city_names, list_of_routes):

        # print (list_of_routes, "list of routes")
        # print (list_of_city_names, "list of routes")

        # Get the index of the destination city and refer to it by its index from here on
        index_of_B = list_of_city_names.index(B)

        # Now find the distance between A and B
        for row in list_of_routes:
            if row[0] == A:
                distance = row[index_of_B + 1]
                return int(distance)
        print("At least one of the cities you entered is invalid, returning 0!")
        return 0

        # FUNCTION OF THE CALCULATOR OF THE FITNESS VALUE(TOTAL DISTANCE)-----------------------

    def get_total_distance(self, individual, list_of_city_names, list_of_routes):

        number_of_cities = len(individual)
        total_distance = 0

        for count in range(0, number_of_cities - 1):
            origin = individual[count]  # The city you are at
            destination = individual[count + 1]  # The city you are travelling to next
            # Fitness Value
            total_distance += self.get_route_distance(origin, destination, list_of_city_names, list_of_routes)
            # print(total_distance)

        return total_distance

        # INITIAL RANDOM POPULATIONS---------------------------------------------------------------

    def set_first_generation(self, list_of_city_names):

        # Using a list of all the cities, generate a random population of ten individuals
        # The first city in the list should be the "head" and "tail" node of each individual
        # It has to start and end in the same city

        f = open('first_generation.csv', 'w')
        size = self.population_size  # Size of the population
        for count in range(size):
            items = list_of_city_names[1:-1]
            random.shuffle(items)  # Shuffles the order of the cities, excluding the first and last city
            individual = list_of_city_names[:1] + items + list_of_city_names[-1:]  # Loop Travelling
            string = ''
            for element in individual:
                string = string + ',' + element
            f.write(string[1:])
            f.write('\n')

        f.close()

    def get_first_generation(self):  # An initial population has already been created simply read it
        population = self.get_raw_data('first_generation.csv', ',')
        return population

        # MAIN CALCULATIONS FOR GENETIC ALGORITHM --------------------------------------------------

    def main(self):

        routes = self.get_raw_data('distances.csv', ',')  # Reading Data
        list_of_city_names = routes[0]  # Cities and Distances, first element of the list icities
        # print(routes)
        del routes[0]

        print("generating first_generation.csv")
        self.set_first_generation(list_of_city_names)
        population = self.get_first_generation()  # Number of initial random population you can see the file generated

        # Puts all fitness values of population togather

        fitness_values = []

        for individual in population:  # Calculate the total distance for every route
            total_distance = self.get_total_distance(individual, list_of_city_names, routes)
            fitness_values.append(total_distance)

        # print(fitness_values, "Fitness Values of First Populations")

        self.routes = routes
        self.city_names = list_of_city_names
        self.population = population
        self.fitness_values = fitness_values

    if __name__ == "__main__":
        main()
