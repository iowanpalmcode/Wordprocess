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
# Remove any non alphabetic characters from the input
Node = []
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
            scores["fly" if word in flysim else ("run" if word in runsim else "swim")] += 1
                    # I had to find that but don't worry that's my only pasted code. <--- This was from like 3 days ago. Ignore it.
        elif 33 <= full.index(word) < 66: 
            scores["climb" if word in climbsim else ("jump" if word in jumpsim else "crawl")] += 1
        elif 66 <= full.index(word) < 99:
            scores["hide" if word in hidesim else ("hunt" if word in huntsim else "sleep")] += 1
        else:
            scores["communicate"] += 1
def decide():
    global decidea, decideb, decidec
    ranked_categories = sorted(scores, key=scores.get, reverse=True)
    decidea = ranked_categories[0]
    decideb = ranked_categories[1]
    decidec = ranked_categories[2]


def rank_animals():
    global category_dicts, weights, animal_scores
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