# Unit-VI Planning: Basic representation for planning, symbolic-centralized vs reactive-distributed, partial order planning algorithm.

# === ARTIFICIAL INTELLIGENCE - UNIT VI: PLANNING ===

print("=== UNIT VI - Planning ===")

# ---------------- BASIC REPRESENTATION FOR PLANNING ----------------
class Action:
    def __init__(self, name, preconds, effects):
        self.name = name
        self.preconds = set(preconds)
        self.effects = set(effects)

    def is_applicable(self, state):
        return self.preconds.issubset(state)

    def apply(self, state):
        return (state - self.preconds) | self.effects

    def __str__(self):
        return self.name

# Sample Actions
actions = [
    Action("cook", ["hungry", "has_ingredients"], ["not_hungry", "has_meal"]),
    Action("buy", ["has_money"], ["has_ingredients"]),
    Action("earn", [], ["has_money"])
]

initial_state = {"hungry"}
goal_state = {"has_meal"}

# ---------------- SYMBOLIC-CENTRALIZED PLANNING ----------------
print("\n--- Symbolic Centralized Planning (Forward State Space Search) ---")

def forward_search(state, goal, actions, plan=[]):
    if goal.issubset(state):
        return plan
    for action in actions:
        if action.is_applicable(state):
            new_state = action.apply(state)
            if action not in plan:
                result = forward_search(new_state, goal, actions, plan + [action])
                if result: return result
    return None

plan = forward_search(initial_state, goal_state, actions)
print("Plan found:" if plan else "No plan found.")
if plan:
    for step in plan:
        print("-", step)

# ---------------- REACTIVE-DISTRIBUTED PLANNING (Mock) ----------------
print("\n--- Reactive Distributed Planning (Conceptual Mock) ---")
agents = {
    "chef": {"can_do": ["cook"]},
    "shopper": {"can_do": ["buy"]},
    "worker": {"can_do": ["earn"]}
}
for name, props in agents.items():
    print(f"{name} can perform: {props['can_do']}")

# ---------------- PARTIAL ORDER PLANNING ----------------
print("\n--- Partial Order Planning (Simplified) ---")

class PartialPlan:
    def __init__(self):
        self.steps = []
        self.ordering = []  # tuples (a, b): a before b

    def add_step(self, action):
        self.steps.append(action)

    def add_ordering(self, before, after):
        self.ordering.append((before, after))

    def __str__(self):
        result = "Steps:\n"
        for s in self.steps:
            result += f"  {s.name}\n"
        result += "Orderings:\n"
        for a, b in self.ordering:
            result += f"  {a.name} → {b.name}\n"
        return result

# Example actions
a1 = Action("earn", [], ["has_money"])
a2 = Action("buy", ["has_money"], ["has_ingredients"])
a3 = Action("cook", ["has_ingredients", "hungry"], ["has_meal"])

partial_plan = PartialPlan()
partial_plan.add_step(a1)
partial_plan.add_step(a2)
partial_plan.add_step(a3)
partial_plan.add_ordering(a1, a2)
partial_plan.add_ordering(a2, a3)

print(partial_plan)

# --- End of UNIT VI ---
