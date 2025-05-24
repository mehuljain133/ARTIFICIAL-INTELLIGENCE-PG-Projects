# Unit-III Intelligent Agents: Introduction to Intelligent Agents, Rational Agent, their structure, , reflex, model-based, goal-based, and utility-based agents, behavior and environment in which a particular agent operates.

# === ARTIFICIAL INTELLIGENCE - UNIT III: INTELLIGENT AGENTS ===
# Topics: Intelligent Agents, Rationality, Types of Agents, Agent-Environment Interaction

from abc import ABC, abstractmethod

print("=== Intelligent Agents Demo ===")

# --- Environment Class ---
class SimpleEnvironment:
    def __init__(self, state):
        self.state = state  # Example: "dirty", "clean", "goal_reached", etc.

    def update(self, action):
        if action == "clean":
            self.state = "clean"
        elif action == "move to goal":
            self.state = "goal_reached"
        elif action == "explore":
            self.state = "unknown"
        print(f"Environment updated: state = {self.state}")

# --- Base Agent Class ---
class Agent(ABC):
    def __init__(self, env):
        self.env = env

    @abstractmethod
    def act(self):
        pass

# --- Reflex Agent ---
class ReflexAgent(Agent):
    def act(self):
        if self.env.state == "dirty":
            print("ReflexAgent: Perceives dirty -> Action: clean")
            return "clean"
        else:
            print("ReflexAgent: Perceives clean -> Action: do nothing")
            return "do nothing"

# --- Model-Based Agent ---
class ModelBasedAgent(Agent):
    def __init__(self, env):
        super().__init__(env)
        self.model = {"location": "room", "status": "unknown"}

    def act(self):
        self.model["status"] = self.env.state
        if self.model["status"] == "dirty":
            print("ModelBasedAgent: Uses internal model -> Action: clean")
            return "clean"
        else:
            print("ModelBasedAgent: Status is clean -> Action: do nothing")
            return "do nothing"

# --- Goal-Based Agent ---
class GoalBasedAgent(Agent):
    def __init__(self, env, goal_state):
        super().__init__(env)
        self.goal_state = goal_state

    def act(self):
        if self.env.state != self.goal_state:
            print("GoalBasedAgent: Goal not reached -> Action: move to goal")
            return "move to goal"
        else:
            print("GoalBasedAgent: Goal reached -> Action: rest")
            return "rest"

# --- Utility-Based Agent ---
class UtilityBasedAgent(Agent):
    def utility(self, state):
        # Assigning scores to states
        scores = {
            "dirty": -10,
            "clean": 10,
            "unknown": 0,
            "goal_reached": 20
        }
        return scores.get(state, 0)

    def act(self):
        current_utility = self.utility(self.env.state)
        print(f"UtilityBasedAgent: Current utility = {current_utility}")
        if self.env.state == "dirty":
            return "clean"
        elif self.env.state != "goal_reached":
            return "move to goal"
        else:
            return "rest"

# --- Simulation of Agents in Different Environments ---
def simulate_agent(agent_class, initial_state, *args):
    print(f"\n--- Simulating {agent_class.__name__} ---")
    env = SimpleEnvironment(initial_state)
    agent = agent_class(env, *args) if args else agent_class(env)
    for _ in range(2):  # Run 2 perception-action cycles
        action = agent.act()
        env.update(action)

# --- Simulate All Agent Types ---
simulate_agent(ReflexAgent, "dirty")
simulate_agent(ModelBasedAgent, "dirty")
simulate_agent(GoalBasedAgent, "unknown", "goal_reached")
simulate_agent(UtilityBasedAgent, "dirty")

# --- Summary ---
print("\nAgent types:")
print("- Reflex Agent: Acts only on current percepts")
print("- Model-Based Agent: Uses internal memory of past states")
print("- Goal-Based Agent: Chooses actions based on a goal")
print("- Utility-Based Agent: Chooses actions that maximize utility")
