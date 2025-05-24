# Unit-IV Problem Solving and Search Techniques: Problem Characteristics, Production Systems, Control Strategies, Breadth First Search, Depth First Search, iterative deepening, uniform cost search, Hill climbing and its Variations, simulated annealing, genetic algorithm search. Heuristics Search Techniques: Best First Search, A* algorithm, AO* algorithm, Minmax & game trees, refining minmax, Alpha – Beta pruning, Constraint Satisfaction Problem, Means-End Analysis.

# === ARTIFICIAL INTELLIGENCE - UNIT IV: PROBLEM SOLVING & HEURISTIC SEARCH ===

import heapq, random, math
from collections import deque, defaultdict

print("=== UNIT IV - ALL-IN-ONE DEMO ===")

# ---------------- BASIC PROBLEM DEFINITION ----------------
class Problem:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

    def actions(self, state):
        return [state + 1, state - 1]  # Simplified

    def goal_test(self, state):
        return state == self.goal

    def cost(self, a, b):
        return abs(a - b)

# ---------------- UNINFORMED SEARCHES ----------------
def bfs(problem):
    frontier = deque([problem.start])
    explored = set()
    while frontier:
        state = frontier.popleft()
        print("BFS:", state)
        if problem.goal_test(state): return state
        explored.add(state)
        for neighbor in problem.actions(state):
            if neighbor not in explored and neighbor not in frontier:
                frontier.append(neighbor)

def dfs(problem):
    frontier = [problem.start]
    explored = set()
    while frontier:
        state = frontier.pop()
        print("DFS:", state)
        if problem.goal_test(state): return state
        explored.add(state)
        for neighbor in problem.actions(state):
            if neighbor not in explored:
                frontier.append(neighbor)

def iterative_deepening(problem, limit=10):
    def dls(state, depth):
        print(f"IDDFS: {state} at depth {depth}")
        if problem.goal_test(state): return True
        if depth == 0: return False
        for neighbor in problem.actions(state):
            if dls(neighbor, depth - 1): return True
        return False
    for d in range(limit):
        if dls(problem.start, d): return

def uniform_cost_search(problem):
    frontier = [(0, problem.start)]
    visited = set()
    while frontier:
        cost, state = heapq.heappop(frontier)
        print("UCS:", state)
        if problem.goal_test(state): return state
        visited.add(state)
        for neighbor in problem.actions(state):
            if neighbor not in visited:
                heapq.heappush(frontier, (cost + problem.cost(state, neighbor), neighbor))

# ---------------- HEURISTIC SEARCHES ----------------
def best_first_search(problem, heuristic):
    frontier = [(heuristic(problem.start), problem.start)]
    visited = set()
    while frontier:
        _, state = heapq.heappop(frontier)
        print("BestFS:", state)
        if problem.goal_test(state): return state
        visited.add(state)
        for neighbor in problem.actions(state):
            if neighbor not in visited:
                heapq.heappush(frontier, (heuristic(neighbor), neighbor))

def a_star(problem, heuristic):
    frontier = [(heuristic(problem.start), 0, problem.start)]
    visited = set()
    while frontier:
        f, cost, state = heapq.heappop(frontier)
        print("A*:", state)
        if problem.goal_test(state): return state
        visited.add(state)
        for neighbor in problem.actions(state):
            if neighbor not in visited:
                g = cost + problem.cost(state, neighbor)
                h = heuristic(neighbor)
                heapq.heappush(frontier, (g + h, g, neighbor))

# ---------------- AO* ALGORITHM (Simple Mock) ----------------
def ao_star():
    print("AO* (Mock): Applied for AND/OR graph problems. Complex, typically used in planning.")

# ---------------- HILL CLIMBING + SIMULATED ANNEALING ----------------
def hill_climbing(problem, heuristic):
    current = problem.start
    while True:
        neighbors = problem.actions(current)
        next_state = max(neighbors, key=heuristic)
        if heuristic(next_state) <= heuristic(current): break
        current = next_state
        print("Hill:", current)
    print("Final:", current)

def simulated_annealing(problem, heuristic, temp=1000, decay=0.95):
    current = problem.start
    while temp > 1:
        next_state = random.choice(problem.actions(current))
        delta = heuristic(next_state) - heuristic(current)
        if delta > 0 or random.random() < math.exp(delta / temp):
            current = next_state
        print(f"SA: {current} at temp {temp:.1f}")
        temp *= decay
    print("Final:", current)

# ---------------- GENETIC ALGORITHM ----------------
def genetic_algorithm(goal, pop_size=6, generations=10):
    def fitness(x): return -abs(goal - x)
    population = [random.randint(0, 20) for _ in range(pop_size)]
    for g in range(generations):
        population = sorted(population, key=fitness, reverse=True)
        print(f"Gen{g}:", population)
        if population[0] == goal: return population[0]
        next_gen = population[:2]
        while len(next_gen) < pop_size:
            p1, p2 = random.choices(population[:4], k=2)
            child = (p1 + p2) // 2
            if random.random() < 0.1:
                child += random.choice([-1, 1])
            next_gen.append(child)
        population = next_gen

# ---------------- MINIMAX + ALPHA-BETA ----------------
def minimax(state, depth, maximizing):
    if depth == 0: return state
    if maximizing:
        return max(minimax(state - 1, depth - 1, False),
                   minimax(state + 1, depth - 1, False))
    else:
        return min(minimax(state - 1, depth - 1, True),
                   minimax(state + 1, depth - 1, True))

def alpha_beta(state, depth, alpha, beta, maximizing):
    if depth == 0:
        return state
    if maximizing:
        max_eval = -float("inf")
        for child in [state + 1, state - 1]:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha: break
        return max_eval
    else:
        min_eval = float("inf")
        for child in [state + 1, state - 1]:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha: break
        return min_eval

# ---------------- CONSTRAINT SATISFACTION (Simple) ----------------
def csp():
    variables = ['X', 'Y']
    domains = {'X': [1, 2], 'Y': [2, 3]}
    constraints = lambda x, y: x != y
    for x in domains['X']:
        for y in domains['Y']:
            if constraints(x, y):
                print(f"CSP Solution: X={x}, Y={y}")

# ---------------- MEANS-END ANALYSIS ----------------
def means_end(start, goal):
    print(f"Start: {start}, Goal: {goal}")
    while start != goal:
        diff = goal - start
        step = 1 if diff > 0 else -1
        start += step
        print("Step to:", start)

# ---------------- DEMO EXECUTION ----------------
p = Problem(2, 7)
heuristic = lambda x: -abs(x - p.goal)

print("\n--- BFS ---")
bfs(p)
print("\n--- DFS ---")
dfs(p)
print("\n--- Iterative Deepening ---")
iterative_deepening(p)
print("\n--- Uniform Cost Search ---")
uniform_cost_search(p)
print("\n--- Best First Search ---")
best_first_search(p, heuristic)
print("\n--- A* Search ---")
a_star(p, heuristic)
print("\n--- Hill Climbing ---")
hill_climbing(p, heuristic)
print("\n--- Simulated Annealing ---")
simulated_annealing(p, heuristic)
print("\n--- Genetic Algorithm ---")
genetic_algorithm(p.goal)
print("\n--- Minimax (starting at 3, depth 3) ---")
print("Minimax result:", minimax(3, 3, True))
print("\n--- Alpha-Beta (starting at 3, depth 3) ---")
print("Alpha-Beta result:", alpha_beta(3, 3, -math.inf, math.inf, True))
print("\n--- Constraint Satisfaction Problem ---")
csp()
print("\n--- Means-End Analysis ---")
means_end(2, 7)
print("\n--- AO* (Not implemented, theory only) ---")
ao_star()
