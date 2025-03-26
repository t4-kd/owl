import requests
from bs4 import BeautifulSoup
import random

def scrape_natgeo_owl_facts():
    url = "https://www.nationalgeographic.com/animals/birds/facts/owls"
    headers = {
        "User-Agent": "Mozilla/5.0"  # pretend to be a browser
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all <p> tags inside the article
    paragraphs = soup.find_all("p")
    facts = []

    for p in paragraphs:
        text = p.get_text().strip()
        if "owl" in text.lower() and len(text.split()) > 6:
            facts.append(text)

    return facts

def get_natgeo_fact():
    facts = scrape_natgeo_owl_facts()
    return random.choice(facts) if facts else "Couldn’t fetch a NatGeo hoot 🦉"
