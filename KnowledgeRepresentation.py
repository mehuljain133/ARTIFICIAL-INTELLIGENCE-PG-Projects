# Unit-V Knowledge Representation: Introduction to First Order Predicate Calculus, Resolution Principle, Unification, Semantic Nets, Conceptual Dependencies, semantic networks, Frames system, Production Rules, Conceptual Graphs, Ontologies.

# === ARTIFICIAL INTELLIGENCE - UNIT V: KNOWLEDGE REPRESENTATION ===

print("=== UNIT V - Knowledge Representation ===")

# ---------------- FIRST ORDER PREDICATE LOGIC ----------------
class Predicate:
    def __init__(self, name, args):
        self.name = name
        self.args = args  # list of variables/constants

    def __str__(self):
        return f"{self.name}({', '.join(self.args)})"

def unify(x, y, subs={}):
    if x == y:
        return subs
    elif isinstance(x, str) and x.islower():
        subs[x] = y
        return subs
    elif isinstance(y, str) and y.islower():
        subs[y] = x
        return subs
    elif isinstance(x, Predicate) and isinstance(y, Predicate):
        if x.name != y.name or len(x.args) != len(y.args):
            return None
        for a, b in zip(x.args, y.args):
            subs = unify(a, b, subs)
            if subs is None:
                return None
        return subs
    return None

print("\n--- First Order Logic & Unification ---")
p1 = Predicate("loves", ["john", "X"])
p2 = Predicate("loves", ["john", "mary"])
subs = unify(p1, p2, {})
print(f"Unify {p1} and {p2} =>", subs)

# ---------------- RESOLUTION PRINCIPLE ----------------
def resolution_demo():
    print("\n--- Resolution Principle (Example) ---")
    print("Clause 1: A ∨ B")
    print("Clause 2: ¬B ∨ C")
    print("Resolve on B → New Clause: A ∨ C")

resolution_demo()

# ---------------- SEMANTIC NETWORKS ----------------
print("\n--- Semantic Network ---")
semantic_net = {
    "bird": {"is_a": "animal", "can": ["fly"]},
    "penguin": {"is_a": "bird", "can": ["swim"], "cannot": ["fly"]},
}
for concept, props in semantic_net.items():
    print(f"{concept}: {props}")

# ---------------- CONCEPTUAL DEPENDENCIES ----------------
print("\n--- Conceptual Dependency (Simplified) ---")
cd = {
    "actor": "John",
    "action": "eat",
    "object": "apple",
    "instrument": "mouth"
}
print(cd)

# ---------------- FRAME SYSTEM ----------------
print("\n--- Frame System ---")
frame = {
    "Car": {
        "wheels": 4,
        "engine": "internal combustion",
        "methods": ["start", "drive"]
    },
    "ElectricCar": {
        "parent": "Car",
        "engine": "electric",
        "methods": ["charge"]
    }
}
print(frame)

# ---------------- PRODUCTION RULES ----------------
print("\n--- Production Rules ---")
facts = {"hungry"}
rules = [
    {"if": ["hungry"], "then": "eat"},
    {"if": ["eat"], "then": "happy"}
]
inferred = set()
for rule in rules:
    if all(f in facts for f in rule["if"]):
        inferred.add(rule["then"])
print("Inferred actions:", inferred)

# ---------------- CONCEPTUAL GRAPHS ----------------
print("\n--- Conceptual Graph ---")
graph = [
    ("John", "agent", "eat"),
    ("eat", "object", "apple"),
    ("eat", "instrument", "fork")
]
for triple in graph:
    print(f"{triple[0]} --{triple[1]}--> {triple[2]}")

# ---------------- ONTOLOGY EXAMPLE ----------------
print("\n--- Ontology (Simple Taxonomy) ---")
ontology = {
    "Animal": {"subclass": ["Mammal", "Bird"]},
    "Mammal": {"subclass": ["Dog", "Cat"]},
    "Bird": {"subclass": ["Penguin", "Sparrow"]},
}
for entity, props in ontology.items():
    print(f"{entity}: {props}")

# --- End of UNIT V ---
