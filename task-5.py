import numpy as np

# Distance matrix (symmetric TSP)
d = np.array([
    [0, 10, 12, 1, 14],
    [10, 0, 13, 25, 8],
    [12, 13, 0, 9, 14],
    [11, 15, 9, 0, 16],
    [14, 8, 14, 16, 0]
])

# Parameters
iterations = 100
n_ants = 5
n_cities = 5
evaporation_rate = 0.5
alpha = 1  # Influence of pheromone
beta = 2   # Influence of visibility

# Initialize visibility (inverse of distance)
visibility = 1 / d
np.fill_diagonal(visibility, 0)

# Initialize pheromone matrix (same for all edges)
pheromone = 0.1 * np.ones((n_cities, n_cities))

# Ant route matrix (each ant gets a route of length n_cities + 1 to return to start)
routes = np.ones((n_ants, n_cities + 1), dtype=int)

for iteration in range(iterations):
    routes[:, 0] = 1  # All ants start at city 1 (index 0)

    for ant in range(n_ants):
        visited = set()
        visited.add(0)  # city 1 is index 0

        for step in range(1, n_cities):
            current_city = routes[ant, step - 1] - 1

            probabilities = np.zeros(n_cities)
            for city in range(n_cities):
                if city not in visited:
                    tau = pheromone[current_city, city] ** alpha
                    eta = visibility[current_city, city] ** beta
                    probabilities[city] = tau * eta

            if probabilities.sum() == 0:
                next_city = list(set(range(n_cities)) - visited)[0]
            else:
                probabilities /= probabilities.sum()
                next_city = np.random.choice(range(n_cities), p=probabilities)

            routes[ant, step] = next_city + 1
            visited.add(next_city)

        # Return to start city
        routes[ant, -1] = routes[ant, 0]

    # Evaluate routes
    route_costs = np.zeros(n_ants)
    for ant in range(n_ants):
        cost = 0
        for step in range(n_cities):
            from_city = routes[ant, step] - 1
            to_city = routes[ant, step + 1] - 1
            cost += d[from_city, to_city]
        route_costs[ant] = cost

    # Find best route in this iteration
    best_index = np.argmin(route_costs)
    best_route = routes[best_index].copy()
    best_cost = route_costs[best_index]

    # Pheromone evaporation
    pheromone *= (1 - evaporation_rate)

    # Pheromone update
    for ant in range(n_ants):
        for step in range(n_cities):
            from_city = routes[ant, step] - 1
            to_city = routes[ant, step + 1] - 1
            pheromone[from_city, to_city] += 1 / route_costs[ant]
            pheromone[to_city, from_city] += 1 / route_costs[ant]  # symmetric update

# Final output
print("Routes of all ants at the end:")
print(routes)
print()
print("Best path found:", best_route)
print("Cost of the best path:", int(best_cost))
