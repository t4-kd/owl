from flask import Flask, request, render_template
from facts_wiki import get_wiki_fact
from gpt_facts import get_gpt_fact
from scrape_facts import get_natgeo_fact
from demo import get_file_fact
import os
import random

app = Flask(__name__)


@app.route("/")
def home():
    return "🦉 Owl Fact API — Try /fact?mode=wiki /gpt /bird /file /random or go to /hoot for frontend"

@app.route("/hoot")
def hoot_page():
    return render_template("hoot.html")

@app.route("/fact")
def get_fact():
    mode = request.args.get("mode", default="random")

    if mode == "wiki":
        return get_wiki_fact()
    elif mode == "gpt":
        return get_gpt_fact()
    elif mode == "bird":
        return get_natgeo_fact()
    elif mode == "file":
        return get_file_fact()
    elif mode == "random":
        return random.choice([
            get_wiki_fact(),
            get_natgeo_fact(),
            get_file_fact(),
            get_gpt_fact(),
        ])
    else:
        return ":( ran out of GPT creds oops pls use wikipedia, natgeo, article, or random.", 400

if __name__ == "__main__":
    app.run(debug=True)
