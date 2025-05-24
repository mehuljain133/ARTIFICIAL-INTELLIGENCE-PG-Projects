# Unit-VII Reasoning with Uncertain Knowledge: Different types of uncertainty - degree of belief and degree of truth, various probability constructs - prior probability, conditional probability, probability axioms, probability distributions, and joint probability distributions, Bayes' rule, other approaches to modeling uncertainty such as Dempster-Shafer theory and fuzzy sets/logic.

# === ARTIFICIAL INTELLIGENCE - UNIT VII: REASONING WITH UNCERTAIN KNOWLEDGE ===

print("=== UNIT VII - Reasoning with Uncertain Knowledge ===")

# ---------------- TYPES OF UNCERTAINTY ----------------
print("\n--- Types of Uncertainty ---")
print("Degree of belief (subjective probability) vs Degree of truth (fuzzy logic)")
belief = 0.8  # example: 80% sure it's raining
truth_degree = 0.6  # example: 60% true that "the room is hot"

# ---------------- PROBABILITY THEORY ----------------
print("\n--- Probability Constructs ---")
P_rain = 0.3  # prior probability
P_traffic_given_rain = 0.9
P_traffic_given_no_rain = 0.2
P_traffic = P_rain * P_traffic_given_rain + (1 - P_rain) * P_traffic_given_no_rain

print(f"Prior P(rain): {P_rain}")
print(f"P(traffic | rain): {P_traffic_given_rain}")
print(f"P(traffic): {P_traffic:.2f}")

# ---------------- BAYES’ RULE ----------------
print("\n--- Bayes' Rule ---")
P_rain_given_traffic = (P_traffic_given_rain * P_rain) / P_traffic
print(f"P(rain | traffic): {P_rain_given_traffic:.2f}")

# ---------------- PROBABILITY DISTRIBUTIONS ----------------
print("\n--- Probability Distributions ---")
weather_probs = {"sunny": 0.5, "cloudy": 0.3, "rainy": 0.2}
print("Weather distribution:", weather_probs)

# ---------------- JOINT PROBABILITY ----------------
print("\n--- Joint Probability Distribution ---")
joint_prob = {
    ("sunny", "picnic"): 0.4,
    ("rainy", "picnic"): 0.05,
    ("cloudy", "picnic"): 0.15,
    ("rainy", "no_picnic"): 0.15,
    ("sunny", "no_picnic"): 0.1
}
for event, prob in joint_prob.items():
    print(f"P{event} = {prob}")

# ---------------- DEMPSTER-SHAFER THEORY (Simplified) ----------------
print("\n--- Dempster-Shafer Theory (Simple Example) ---")
beliefs = {
    "A": 0.6,
    "B": 0.3,
    "A_or_B": 0.1  # uncertainty
}
print("Belief mass function:", beliefs)
belief_A = beliefs["A"]
plausibility_A = beliefs["A"] + beliefs["A_or_B"]
print(f"Belief(A): {belief_A}, Plausibility(A): {plausibility_A}")

# ---------------- FUZZY LOGIC ----------------
print("\n--- Fuzzy Logic Example ---")

def fuzzy_temperature(value):
    if value <= 15:
        return {"cold": 1.0, "warm": 0.0, "hot": 0.0}
    elif 15 < value <= 25:
        return {
            "cold": (25 - value) / 10,
            "warm": (value - 15) / 10,
            "hot": 0.0
        }
    elif 25 < value <= 35:
        return {
            "cold": 0.0,
            "warm": (35 - value) / 10,
            "hot": (value - 25) / 10
        }
    else:
        return {"cold": 0.0, "warm": 0.0, "hot": 1.0}

temp = 22
fuzzy_values = fuzzy_temperature(temp)
print(f"Fuzzy values for temperature {temp}°C: {fuzzy_values}")

# --- End of UNIT VII ---
