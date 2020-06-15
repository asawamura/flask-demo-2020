# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, request, redirect, render_template
import model
from random import randint


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())

# @app.route('/greeting', methods=["POST", "GET"])
# def greeting():
#     if request.method == "POST":
#         info = request.form
#         name = info['username']
#         topic = info['topic']
#         mood = info['mood']
#         newname = model.name_randomizer(name)
#         # name2 = model.name_randomizer(name)
#         topic1 = model.topic_thesaurus(topic)
#         topic2 = model.topic_thesaurus(topic)
#         mood1 = model.mood_thesaurus(mood)
#         mood2 = model.mood_thesaurus(mood)
        
#         return render_template("greeting.html", name=name, newname=newname, topic=topic, topic1=topic1, topic2=topic2, mood=mood, mood1=mood1, mood2=mood2)
#     # -- if get to the website any other way than posting, it will show this
#     else:
#         return "You are GETTING this website"

@app.route('/poem', methods=["POST", "GET"])
def poem():
    if request.method == "POST":
        info = request.form
        name = info['username']
        topic = info['topic']
        mood = info['mood']
        newname = model.name_randomizer(name)
        # name2 = model.name_randomizer(name)
        # name3 = model.name_randomizer(name)
        topic1 = model.topic_thesaurus(topic)
        topic2 = model.topic_thesaurus(topic)
        mood1 = model.mood_thesaurus(mood)
        mood2 = model.mood_thesaurus(mood)
        mood3 = model.mood_thesaurus(mood)
        descriptor1 = model.descriptor_thesaurus()
        descriptor2 = model.descriptor_thesaurus()
        descriptor3 = model.descriptor_thesaurus()
        descriptor4 = model.descriptor_thesaurus()
        trigger1 = model.trigger_thesaurus(topic)
        trigger2 = model.trigger_thesaurus(topic)
        poem = model.poem_descriptor()
        poem2 = model.poem_descriptor()
        surprisingrhyme = model.surprising_rhyme()
        namerhyme = model.name_rhyme(newname)
        return render_template("poem.html", name=name, newname=newname, topic=topic, topic1=topic1, topic2=topic2, trigger1 = trigger1, trigger2=trigger2, poem=poem, poem2=poem2, mood=mood, mood1=mood1, mood2=mood2, mood3=mood3, descriptor1 = descriptor1, descriptor2 = descriptor2, descriptor3 = descriptor3, descriptor4 = descriptor4, surprisingrhyme = surprisingrhyme, namerhyme = namerhyme)
    else:
        return render_template("index.html", time=datetime.now())