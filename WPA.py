# Word Processing Agent (kinda..)
import streamlit as st
from categories import climb, swim, run, fly, jump, crawl, hide, hunt, sleep, communicate
from sim import flysim, runsim, swimsim, climbsim, jumpsim, crawlsim, hidesim, huntsim, sleepsim, communicatesim, negators
full = flysim + runsim + swimsim + climbsim + jumpsim + crawlsim + hidesim + huntsim + sleepsim + communicatesim
total = 0
skip = False
st.title("Word Processing Agent")
st.write("A simple(ish) word processing agent that tries to guess what animal you're thinking of based on the words you give.")
st.write("The current categories are: climb, swim, run, fly, jump, crawl, hide, hunt, sleep, communicate. Try to give words that relate to those categories and the animal you're thinking of. For example, if you're thinking of a monkey, you might say 'climb', 'jump', 'swing', etc.")
Node = st.text_input("Give me a string of words relating to an animal: ").strip().lower().split()
analyze = st.button("Analyze")
scores = {"climb": 0, "swim": 0, "run": 0, "fly": 0, "jump": 0, "crawl": 0, "hide": 0, "hunt": 0, "sleep": 0, "communicate": 0}
# New idea
for word in Node:
    if skip:
        skip = False
        continue
    if word in negators:
        skip = True
    else:   
        if word in full:
            if full.index(word) < 30:
                scores["climb" if word in climbsim else ("swim" if word in swimsim else "run")] += 1
                    # I had to find that but don't worry that's my only pasted code.
            elif 30 <= full.index(word) < 60: 
                scores["run" if word in runsim else ("fly" if word in flysim else "jump")] += 1
            elif 60 <= full.index(word) < 90:
                scores["crawl" if word in crawlsim else ("hide" if word in hidesim else "hunt")] += 1
            else:
                scores["sleep" if word in sleepsim else "communicate"] += 1
def decide():
    global decidea, decideb, decidec
    ranked_categories = sorted(scores, key=scores.get, reverse=True)
    decidea = ranked_categories[0]
    decideb = ranked_categories[1]
    decidec = ranked_categories[2]


def rank_animals():
    category_dicts = {
        "climb": climb,
        "swim": swim,
        "run": run,
        "fly": fly,
        "jump": jump,
        "crawl": crawl,
        "hide": hide,
        "hunt": hunt,
        "sleep": sleep,
        "communicate": communicate,
    }
    weights = {decidea: 1.0, decideb: 0.8, decidec: 0.6}
    animal_scores = {}

    for category_name, weight in weights.items():
        for animal, value in category_dicts[category_name].items():
            animal_scores[animal] = animal_scores.get(animal, 0) + value * weight

    return sorted(animal_scores, key=animal_scores.get, reverse=True)[:3]


decide()
top_animals = rank_animals()
if analyze and len(Node) > 0:
    st.write(decidea, decideb, decidec)
    st.write("Top 3 animals:", *top_animals)