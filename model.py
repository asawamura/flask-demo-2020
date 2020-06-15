import random
import requests

def name_randomizer(username):
    # find first char of name input by user
    firstchar = username[:1].lower()
    
    # select correct list of alternative names by first char
    if firstchar == 'a':
        names = ['Alexandra', 'Alexis', 'Arnoldo', 'Angelica', 'Anita']
    elif firstchar == 'b':
        names = ['Billy', 'Barbara', 'Bella', 'Bartolomeo', 'Bashir']
    elif firstchar == 'c':
        names = ['Cassandra', 'Clarissa', 'Camila', 'Coltrane', 'Christian']
    elif firstchar == 'd':
        names = ['Don', 'Diego', 'Damien', 'Delilah','Daphne']
    elif firstchar == 'e':
        names = ['Elias', 'Ephraim', 'Elison', 'Edmund', 'Eliza']
    elif firstchar == 'f':
        names = ['Fatima', 'Florencia', 'Fabiano', 'Faith', 'Farrah']
    elif firstchar == 'g':
        names = ['Gabriella', 'Gavin', 'Ganesh', 'Gesualdo', 'Gary']
    elif firstchar == 'h':
        names = ['Hassan', 'Hannah', 'Harold', 'Hagan', 'Hadrian']
    elif firstchar == 'i':
        names = ['Icarus', 'Inez', 'Ivy', 'Isaac', 'Ignatius']
    elif firstchar == 'j':
        names = ['Juliana', 'Jerome', 'Jacqueline', 'Jacques', 'Jonathan']
    elif firstchar == 'k':
        names = ['Kayla', 'Kareem', 'Karla', 'Kit', 'Karl']
    elif firstchar == 'l':
        names = ['Lorenzo', 'Liliana', 'Lancelot', 'Lafayette', 'Lamar']
    elif firstchar == 'm':
        names = ['Marianne', 'Malika', 'Michelle', 'Mabel', 'Marcus']
    elif firstchar == 'n':
        names = ['Nicolas', 'Nicole', 'Norman', 'Nadine', 'Nancy']
    elif firstchar == 'o':
        names = ['Orpheus', 'Omar', 'Ophelia','Olaf', 'Oliver']
    elif firstchar == 'p':
        names = ['Phillip','Paulette', 'Pauline', 'Pierre', 'Patrick']
    elif firstchar == 'q':
        names = ['Quinton', 'Quinn', 'Quinby', 'Quigley', 'Quimby']
    elif firstchar == 'r':
        names = ['Raul', 'Rashad', 'Raina', 'Rafael', 'Rosalia']
    elif firstchar == 's':
        names = ['Sabra', 'Shana', 'Sebastian','Samantha','Sofia']
    elif firstchar == 't':
        names = ['Theodore', 'Tristan', 'Tabitha', 'Tadashi', 'Taylor']
    elif firstchar == 'u':
        names = ['Uriel', 'Umberto', 'Ulysses', 'Upton', 'Urbano']
    elif firstchar == 'v':
        names = ['Vivian', 'Valdemar', 'Valeria', 'Ventura', 'Valentino']
    elif firstchar == 'w':
        names = ['Winston', 'Walden', 'Wagner', 'Wanda', 'Willow']
    elif firstchar == 'x':
        names = ['Xavier', 'Xena', 'Xenon', 'Xerxes', 'Xenophon']
    elif firstchar == 'y':
        names = ['Yvette', 'Yoko', 'Yvonne', 'Yolanda', 'Yarnell']
    elif firstchar == 'z':
        names = ['Zoe', 'Zara', 'Zelda', 'Zander', 'Zacharias']
    else:
        names = ['Elimir', 'Wadsworth', 'Tabitha', 'Florencia', 'Samantha']
    
    # choose random name from list
    random.shuffle(names)
    newname=names[0]
    return newname

def topic_thesaurus(topic):
    # find synonyms for topic
    listoftopics = requests.get(f"https://api.datamuse.com/words?ml={topic}").json()
    
    # randomize word choice
    random.shuffle(listoftopics)

    # store topic synonyms in variables
    topic1 = listoftopics[0]['word']
    topic2 = listoftopics[1]['word']
    return topic1 and topic2

def mood_thesaurus(mood):
    # find synonyms for mood
    listofmoods = requests.get(f"https://api.datamuse.com/words?ml={mood}").json()
    
    # randomize word choice
    random.shuffle(listofmoods)
    mood1=listofmoods[0]['word']
    mood2=listofmoods[1]['word']
    mood3=listofmoods[2]['word']
    return mood1 and mood2 and mood3

def descriptor_thesaurus():
    # generate random descriptive synonyms
    listofdescriptors = requests.get(f"https://api.datamuse.com/words?ml=astonishing").json()
    random.shuffle(listofdescriptors)
    descriptor1=listofdescriptors[0]['word']

    listofdescriptors2 = requests.get(f"https://api.datamuse.com/words?ml=interesting").json()
    random.shuffle(listofdescriptors2)
    descriptor2=listofdescriptors2[0]['word']

    listofdescriptors3 = requests.get(f"https://api.datamuse.com/words?ml=frightful").json()
    random.shuffle(listofdescriptors3)
    descriptor3=listofdescriptors3[0]['word']

    listofdescriptors4 = requests.get(f"https://api.datamuse.com/words?ml=repulsive").json()
    random.shuffle(listofdescriptors4)
    descriptor4=listofdescriptors4[0]['word']

    return descriptor1 and descriptor2 and descriptor3 and descriptor4

def trigger_thesaurus(topic):
    # generate words 'triggered by' topic
    triggerlist = requests.get(f"https://api.datamuse.com/words?rel_trg={topic}").json()
    trigger1 = triggerlist[0]['word']
    random.shuffle(triggerlist)
    trigger2 = triggerlist[0]['word']
    return trigger1 and trigger2

def poem_descriptor():
    poemlist = ["laudable limerick", "lackadaisical limerick", "vaulting verse", "obliging ode", "scintillating song", "rapturous rhyme", "sensational sonnet"]    
    random.shuffle(poemlist)
    poem=poemlist[0]
    return poem

def surprising_rhyme():
    # generate random rhyme for "surprising"
    surprisinglist = requests.get(f"https://api.datamuse.com/words?rel_rhy=surprising").json()
    random.shuffle(surprisinglist)
    surprisingrhyme = surprisinglist[0]['word']
    return surprisingrhyme

def name_rhyme(newname):
    # generate random rhyme for name2
    namerhymes = requests.get(f"https://api.datamuse.com/words?rel_rhy={newname}").json()
    random.shuffle(namerhymes)
    namerhyme = namerhymes[0]['word']
    return namerhyme