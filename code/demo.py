import random

def load_facts_from_file(path="owl_facts.txt"):
    with open(path, "r") as f:
        facts = [line.strip() for line in f if line.strip()]
    return facts

def get_file_fact():
    return random.choice(load_facts_from_file())
