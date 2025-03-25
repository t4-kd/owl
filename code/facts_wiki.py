import requests
import re
import random

def get_wiki_facts(limit=1):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": True,
        "titles": "Owl",
        "format": "json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Get the actual content from the Wikipedia page
    content = next(iter(data["query"]["pages"].values()))["extract"]

    # Split into sentences based on period followed by space
    sentences = re.split(r'(?<=\.)\s+', content)

    # Filter sentences that mention 'owl'
    owl_facts = [s for s in sentences if "owl" in s.lower()]

    return owl_facts[:limit]

def get_wiki_fact():
    facts = get_wiki_facts(limit=200)
    return random.choice(facts) if facts else "Couldn't fetch a fact from Wikipedia cause wiki limits oops🦉"
