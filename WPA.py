# Word Processing Agent (kinda..)
import streamlit as st
from categories import climb, swim, run, fly, jump, crawl, hide, hunt, sleep, communicate
from sim import flysim, runsim, swimsim, climbsim, jumpsim, crawlsim, hidesim, huntsim, sleepsim, communicatesim, negators
full = flysim + runsim + swimsim + climbsim + jumpsim + crawlsim + hidesim + huntsim + sleepsim + communicatesim
skip = False

st.title("Word Processing Agent")
st.write("A simple(ish) word processing agent that tries to guess what animal you're thinking of based on the words you give.")
st.write("The current categories are: climb, swim, run, fly, jump, crawl, hide, hunt, sleep, communicate. Try to give words that relate to those categories and the animal you're thinking of. For example, if you're thinking of a monkey, you might say 'climb', 'jump', 'swing', etc.")
Basetext = st.text_input("Give me a string of words relating to an animal: ").strip().lower().split()
Node, Unique = [], []
for word in Basetext:
    cleaned_word = ''.join(filter(str.isalpha, word))
    if cleaned_word and cleaned_word in full or cleaned_word in negators:
        Node.append(cleaned_word)
        
analyze = st.button("Analyze")
raw = st.button("Raw Data")
scores = {"climb": 0, "swim": 0, "run": 0, "fly": 0, "jump": 0, "crawl": 0, "hide": 0, "hunt": 0, "sleep": 0, "communicate": 0}
# New idea
for word in Node:
    if skip:
        skip = False
        continue
    if word in negators:
        skip = True
    else: 
        if full.index(word) < 33:
            if word in flysim and "fly" not in Unique:
                scores["fly"] += 1; Unique.append("fly")
            elif word in runsim and "run" not in Unique:
                scores["run"] += 1; Unique.append("run")
            elif word in swimsim and "swim" not in Unique:
                scores["swim"] += 1; Unique.append("swim")
        elif 33 <= full.index(word) < 66:
            if word in climbsim and "climb" not in Unique:
                scores["climb"] += 1; Unique.append("climb")
            elif word in jumpsim and "jump" not in Unique:
                scores["jump"] += 1; Unique.append("jump")
            elif word in crawlsim and "crawl" not in Unique:
                scores["crawl"] += 1; Unique.append("crawl")
        elif 66 <= full.index(word) < 99:
            if word in hidesim and "hide" not in Unique:
                scores["hide"] += 1; Unique.append("hide")
            elif word in huntsim and "hunt" not in Unique:
                scores["hunt"] += 1; Unique.append("hunt")
            elif word in sleepsim and "sleep" not in Unique:
                scores["sleep"] += 1; Unique.append("sleep")
        else:
            if word in communicatesim and "communicate" not in Unique:
                scores["communicate"] += 1; Unique.append("communicate")         
def decide():
    global decidea, decideb, decidec
    ranked_categories = sorted(scores, key=scores.get, reverse=True)
    decidea = ranked_categories[0]
    decideb = ranked_categories[1]
    decidec = ranked_categories[2]
    
def rank_animals():
    global category_dicts, weights, animal_scores
    category_dicts = {
        "climb": climb, "swim": swim, "run": run, "fly": fly, "jump": jump, "crawl": crawl, "hide": hide, "hunt": hunt, "sleep": sleep, "communicate": communicate}
    if len(Node) >= 3:
        weights = {decidea: 1.0, decideb: 0.8, decidec: 0.6}
    elif len(Node) == 2:
        weights = {decidea: 1.0, decideb: 0.8}
    else:
        weights = {decidea: 1.0}
    animal_scores = {}
    for category_name, weight in weights.items():
        for animal, value in category_dicts[category_name].items():
            animal_scores[animal] = animal_scores.get(animal, 0) + value * weight
    return sorted(animal_scores, key=animal_scores.get, reverse=True)[:3]
decide()

top_animals = rank_animals()
if analyze and len(Node) > 0:
    if len(Unique) >= 3:
        st.write("The amount of categories being taken note of in calculations are:", 3)
    else:
        st.write("The amount of categories being taken note of in calculations are:", len(Unique))
    st.write("The 3 most likely categories you could be thinking of are:",decidea, decideb, decidec)
    st.write("Top 3 animals in relation to the categories:", *top_animals)
    
if raw and len(Node) > 0:
        st.write("Scores for each category:")
        for category, score in scores.items():
            st.write(f"- {category}: {score}")    # score for all animals as well
        st.write("Animal Scores:")
        for animal, score in animal_scores.items():
            st.write(f"- {animal}: {score:.2f}")
        st.write("Top 3 animals in relation to the categories:", *top_animals)
        st.balloons()
elif len(Basetext) == 0:
    st.write("Please enter some words to analyze.")
elif len(Node) == 0 and len(Basetext) != 0:
    st.write("Please enter valid words that relate to the categories.")