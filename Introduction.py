# Unit-I Introduction: Introduction to Artificial Intelligence, various definitions of AI, AI Applications and Techniques, Turing Test and Reasoning - forward & backward chaining

# === ARTIFICIAL INTELLIGENCE - UNIT I DEMO CODE ===
# Author: AI Demonstration
# Topics: Introduction, Applications, Turing Test, Reasoning (Forward/Backward Chaining)

# ---- Introduction to AI ----
print("Welcome to AI Concepts Demo")

# ---- AI Applications Example: Simple Expert System ----
knowledge_base = {
    "fever": ["flu", "covid"],
    "cough": ["flu", "covid", "cold"],
    "sore throat": ["cold"],
    "loss of smell": ["covid"]
}

def diagnose(symptoms):
    print("\n[Expert System] Diagnosing based on symptoms:", symptoms)
    possible_diseases = {}
    for symptom in symptoms:
        if symptom in knowledge_base:
            for disease in knowledge_base[symptom]:
                possible_diseases[disease] = possible_diseases.get(disease, 0) + 1
    if not possible_diseases:
        print("No matching disease found.")
        return
    max_score = max(possible_diseases.values())
    likely_diseases = [d for d, score in possible_diseases.items() if score == max_score]
    print("Likely disease(s):", likely_diseases)

# ---- Turing Test Simulation: Basic Chatbot ----
def turing_test_bot():
    print("\n[Chatbot] You can talk to the AI now. Type 'bye' to exit.")
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you": "I'm just code, but I'm functioning as expected!",
        "what is ai": "AI stands for Artificial Intelligence, simulating human thinking in machines.",
        "bye": "Goodbye! Hope to chat again."
    }
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Bot: I'm not sure how to respond to that.")

# ---- Forward Chaining Example ----
def forward_chaining(rules, facts):
    print("\n[Forward Chaining]")
    inferred = set(facts)
    added = True
    while added:
        added = False
        for (premises, conclusion) in rules:
            if premises.issubset(inferred) and conclusion not in inferred:
                inferred.add(conclusion)
                print(f"Inferred: {conclusion}")
                added = True
    return inferred

# ---- Backward Chaining Example ----
def backward_chaining(goal, rules, facts, indent=""):
    print(f"{indent}Proving: {goal}")
    if goal in facts:
        print(f"{indent}✔ {goal} is a known fact.")
        return True
    for premises, conclusion in rules:
        if conclusion == goal:
            print(f"{indent}Trying rule: {premises} => {conclusion}")
            if all(backward_chaining(p, rules, facts, indent + "  ") for p in premises):
                print(f"{indent}✔ {goal} proven by rule.")
                return True
    print(f"{indent}✘ {goal} cannot be proven.")
    return False

# === Demonstration ===
diagnose(["fever", "cough"])

turing_test_bot()

rules = [
    ({"has wings", "can fly"}, "is a bird"),
    ({"has feathers"}, "has wings"),
    ({"lays eggs"}, "can fly"),
]
facts = {"has feathers", "lays eggs"}
print("\nFacts:", facts)
inferred_facts = forward_chaining(rules, facts)
print("All inferred facts:", inferred_facts)

goal = "is a bird"
backward_chaining(goal, rules, facts)
