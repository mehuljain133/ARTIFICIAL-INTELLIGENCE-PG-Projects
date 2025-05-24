# Unit-VIII Understanding Natural Languages: Components and steps of communication, contrast between formal and natural languages in the context of grammar, parsing, and semantics, Parsing Techniques, Context-Free and Transformational Grammars.

# === ARTIFICIAL INTELLIGENCE - UNIT VIII: UNDERSTANDING NATURAL LANGUAGES ===

print("=== UNIT VIII - Understanding Natural Languages ===")

# ---------------- COMPONENTS & STEPS OF COMMUNICATION ----------------
print("\n--- Communication Components ---")
communication = {
    "Sender": "Speaker",
    "Message": "Encoded Sentence",
    "Medium": "Sound/Written Text",
    "Receiver": "Listener/Reader",
    "Decoding": "Understanding via Grammar/Semantics"
}
for k, v in communication.items():
    print(f"{k}: {v}")

# ---------------- FORMAL vs NATURAL LANGUAGES ----------------
print("\n--- Formal vs Natural Languages ---")
comparison = {
    "Grammar Strictness": "Strict (formal) vs Flexible (natural)",
    "Ambiguity": "None (formal) vs High (natural)",
    "Parsing": "Deterministic (formal) vs Contextual & probabilistic (natural)"
}
for k, v in comparison.items():
    print(f"{k}: {v}")

# ---------------- PARSING TECHNIQUES ----------------
print("\n--- Parsing Techniques ---")
print("Common: Top-down, Bottom-up, Recursive descent, Shift-reduce")

# ---------------- CONTEXT-FREE GRAMMAR PARSING ----------------
import nltk
from nltk import CFG
from nltk.parse.generate import generate

print("\n--- CFG Parsing Example ---")
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog'
V -> 'chased' | 'saw'
""")

print("Generated sentences (CFG):")
for sentence in generate(grammar, n=5):
    print(" ".join(sentence))

# ---------------- TRANSFORMATIONAL GRAMMAR (Conceptual Only) ----------------
print("\n--- Transformational Grammar (Conceptual Example) ---")
deep_structure = "the cat chased the dog"
transformations = [
    lambda s: " ".join(s.split()),  # identity (deep structure)
    lambda s: "was " + s + " by the dog",  # passive (basic)
]
for i, transform in enumerate(transformations):
    print(f"Structure {i+1}: {transform(deep_structure)}")

# ---------------- END OF UNIT VIII ----------------
