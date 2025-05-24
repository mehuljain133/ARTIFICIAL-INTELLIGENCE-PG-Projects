# Unit-IV Problem Solving and Search Techniques: Problem Characteristics, Production Systems, Control Strategies, Breadth First Search, Depth First Search, iterative deepening, uniform cost search, Hill climbing and its Variations, simulated annealing, genetic algorithm search.

# === ARTIFICIAL INTELLIGENCE - UNIT IV: SEARCH TECHNIQUES ===
# Topics: Problem Solving, Production Systems, Control Strategies, Various Search Algorithms

import math, random, heapq
from collections import deque

print("=== Search Techniques Demo ===")

# --- Problem Definition (8-Puzzle Simplified to Numbers) ---
class Problem:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def actions(self, state):
        # Actions: +1, -1 (Just for demo simplicity)
        return [state + 1, state - 1]

    def goal_test(self, state):
        return state == self.goal

    def cost(self, a, b):
        return abs(a - b)

# --- Breadth-First Search (BFS) ---
def bfs(problem):
    frontier = deque([problem.start])
    explored = set()
    while frontier:
        state = frontier.popleft()
        print(f"BFS visiting: {state}")
        if problem.goal_test(state):
            print("Goal found!")
            return
        explored.add(state)
        for neighbor in problem.actions(state):
            if neighbor not in explored and neighbor not in frontier:
                frontier.append(neighbor)

# --- Depth-First Search (DFS) ---
def dfs(problem):
    frontier = [problem.start]
    explored = set()
    while frontier:
        state = frontier.pop()
        print(f"DFS visiting: {state}")
        if problem.goal_test(state):
            print("Goal found!")
            return
        explored.add(state)
        for neighbor in problem.actions(state):
            if neighbor not in explored and neighbor not in frontier:
                frontier.append(neighbor)

# --- Iterative Deepening DFS ---
def iddfs(problem, depth_limit=10):
    def dls(state, depth):
        print(f"Visiting {state} at depth {depth}")
        if problem.goal_test(state):
            print("Goal found!")
            return True
        if depth == 0:
            return False
        for neighbor in problem.actions(state):
            if dls(neighbor, depth - 1):
                return True
        return False
    for depth in range(depth_limit):
        print(f"\nDepth level: {depth}")
        if dls(problem.start, depth):
            return

# --- Uniform Cost Search ---
def uniform_cost_search(problem):
    frontier = [(0, problem.start)]
    explored = set()
    while frontier:
        cost, state = heapq.heappop(frontier)
        print(f"UCS visiting: {state} with cost {cost}")
        if problem.goal_test(state):
            print("Goal found!")
            return
        explored.add(state)
        for neighbor in problem.actions(state):
            if neighbor not in explored:
                total_cost = cost + problem.cost(state, neighbor)
                heapq.heappush(frontier, (total_cost, neighbor))

# --- Hill Climbing ---
def hill_climbing(problem, heuristic):
    current = problem.start
    while True:
        neighbors = problem.actions(current)
        if not neighbors:
            break
        next_state = max(neighbors, key=heuristic)
        if heuristic(next_state) <= heuristic(current):
            break
        current = next_state
        print(f"Hill Climbing: moving to {current}")
    print("Final state:", current)

# --- Simulated Annealing ---
def simulated_annealing(problem, heuristic, temp=1000, decay=0.95):
    current = problem.start
    while temp > 1:
        neighbors = problem.actions(current)
        next_state = random.choice(neighbors)
        delta_e = heuristic(next_state) - heuristic(current)
        if delta_e > 0 or random.random() < math.exp(delta_e / temp):
            current = next_state
        print(f"SA state: {current} at temp {temp:.2f}")
        temp *= decay
    print("Final state:", current)

# --- Genetic Algorithm (Demo) ---
def genetic_algorithm(goal, population_size=6, generations=20):
    def fitness(individual):
        return -abs(goal - individual)

    population = [random.randint(0, 20) for _ in range(population_size)]
    for gen in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        print(f"Gen {gen}: {population}")
        if population[0] == goal:
            print("Goal found!")
            return
        next_gen = population[:2]  # Elitism
        while len(next_gen) < population_size:
            parent1, parent2 = random.choices(population[:4], k=2)
            child = (parent1 + parent2) // 2
            if random.random() < 0.1:  # Mutation
                child += random.choice([-1, 1])
            next_gen.append(child)
        population = next_gen
    print("Best individual:", population[0])

# --- Demo Run ---
demo_problem = Problem(start=2, goal=7)

print("\n--- BFS ---")
bfs(demo_problem)

print("\n--- DFS ---")
dfs(demo_problem)

print("\n--- Iterative Deepening ---")
iddfs(demo_problem)

print("\n--- Uniform Cost Search ---")
uniform_cost_search(demo_problem)

print("\n--- Hill Climbing ---")
hill_climbing(demo_problem, heuristic=lambda x: -abs(x - demo_problem.goal))

print("\n--- Simulated Annealing ---")
simulated_annealing(demo_problem, heuristic=lambda x: -abs(x - demo_problem.goal))

print("\n--- Genetic Algorithm ---")
genetic_algorithm(goal=demo_problem.goal)
