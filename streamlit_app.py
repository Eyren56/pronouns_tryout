pronounS = []

import random


NameLength = False
nomi = " "
accu = " "
possDet = " "
possPro = " "
reflexive = " "
context = " "
location = " "
wasWere = " "
personal =" "
interests = " "


import streamlit as st

st.title("Pronoun Tryouts")
st.subheader("Welcome! We have a few preset pronoun options or you can custom enter your own.")

st.write("Please only select one pronoun at a time, I'm working on it but currently it just gets confused.")


name = st.text_input(
    "Your name",
    key=111,
    label_visibility="visible",
    disabled=False 
    )
if len(name) < 1:
    st.caption("Names must be at least 1 character")
    NameLength = False
else:
    NameLength = True



col1, col2, col3 = st.columns(3)

#they/them
with col1:
    they = st.checkbox("they/them")

    if they:
        pronounS = ["they", "them", "their", "theirs", "themself"]
        nomi = pronounS[0]
        accu = pronounS[1]
        possDet = pronounS[2]
        possPro = pronounS[3]
        reflexive = pronounS[4]
        context = "Plural"

#she/her
with col2:
    she = st.checkbox("she/her")

    if she:
        pronounS = ["she", "her", "her", "hers", "herself"]
        nomi = pronounS[0]
        accu = pronounS[1]
        possDet = pronounS[2]
        possPro = pronounS[3]
        reflexive = pronounS[4]
        context = "Singular"


#he/him
with col3:
    he = st.checkbox("he/him")

    if he:
        pronounS = ["he", "him", "his", "his", "himself"]
        nomi = pronounS[0]
        accu = pronounS[1]
        possDet = pronounS[2]
        possPro = pronounS[3]
        reflexive = pronounS[4]
        context = "Singular"

        

col4, col5, col6 =st.columns(3)

#it/its
with col4:
    it = st.checkbox("it/its")

    if it:
        pronounS = ["it", "it", "its", "its", "itself"]
        nomi = pronounS[0]
        accu = pronounS[1]
        possDet = pronounS[2]
        possPro = pronounS[3]
        reflexive = pronounS[4]
        context = "Singular"

#xe/xem
with col5:
    xe = st.checkbox("xe/xem/xyr")

    if xe:
        pronounS = ["xe", "xem", "xyr", "xyrs", "xemself"]
        nomi = pronounS[0]
        accu = pronounS[1]
        possDet = pronounS[2]
        possPro = pronounS[3]
        reflexive = pronounS[4]
        context = "Plural"


#fae/faer
with col6:
    fae = st.checkbox("fae/faer")

    if fae:
        pronounS = ["fae", "faer", "faers", "faers", "faeself"]
        nomi = pronounS[0]
        accu = pronounS[1]
        possDet = pronounS[2]
        possPro = pronounS[3]
        reflexive = pronounS[4]
        context = "Singular"

col1 = st.columns(1)
custom = st.checkbox("Custom Pronouns")

if custom:

    col1, col2, col3 = st.columns(3)

    with col1:
        nomi = st.text_input(
            "Nominative Pronoun",
            label_visibility="visible",
            disabled=False,
            placeholder="e.g. they - They sit on the chair",
        )
        pronounS.append(nomi)

    with col2:
        accu = st.text_input(
            "Accusative/Dative Pronoun",
            label_visibility="visible",
            disabled=False,
            placeholder="e.g. them - Is that them?",
        )
        pronounS.append(accu)

    with col3:
        possDet = st.text_input(
            "Possessive Determiner",
            label_visibility="visible",
            disabled=False,
            placeholder="e.g. their - Their bag was blue.",
        )
        pronounS.append(possDet)

    col4, col5 = st.columns(2)

    with col4:
        possPro = st.text_input(
            "Possesive Pronoun",
            label_visibility="visible",
            disabled=False,
            placeholder="e.g. theirs - Is this bag theirs?",
        )
        pronounS.append(possPro)

    with col5:
        reflexive = st.text_input(
            "Reflexive Form",
            label_visibility="visible",
            disabled=False,
            placeholder="e.g. themself - I hope they take care of themself.",
        )
        pronounS.append(reflexive)


    context = st.radio(
        "Would your pronoun make more sense in a singular or plural context?",
        ["Singular", "Plural"],
        captions=[
            "would make sense in place of she/her or he/him e.g. xe is here",
            "would make sense in place of they/them e.g. xe are here",
        ],
        )


        
st.divider() 

if context == "Singular":
    wasWere = "was"
elif context == "Plural":
    wasWere = "were"


personal = st.toggle("Personalised Text")
st.write("By default you get a randomly generated text, take a small quiz to customise it to be more accurate to you")

if personal:
    with st.form("my_form"):
        st.subheader("Text Customisation")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Where might you be most likely to meet a new friend?")
            cafe = st.checkbox("A  cafe")
            party = st.checkbox("A party")
            college = st.checkbox("College/School")
            work = st.checkbox("Work")


        if cafe:
            location = "at a cafe"
            because = "a sticker on"
            device = "laptop"
        elif party:
            location = "at a party"
            because = "a photo in"
            device = "phonecase"
        elif college:
            location = "on campus"
            because = "a sticker on"
            device = "laptop"
        elif work:
            location = "at work"
            because = "a photo in"
            device = "phonecase"

        with col2:
            st.write("What migt you talk about?")
            craft = st.checkbox("Craft")
            sports = st.checkbox("Sports")
            games = st.checkbox("Games")
            place2 = st.checkbox("placeholder2")
            place = st.checkbox("placeholder")
        submitted = st.form_submit_button("Submit")

        if craft:
            interests = "crafts"
            presents = "projects"
            invite = "craft fair"
        elif sports:
            interests = "sports" 
            presents = "photos from matches" 
            invite = "match"
        elif interest == 2:
            interests = "gaming"
            presents = "some picture of a game"
            invite = "a small gaming event in a local cafe"
        
            

    if (fae or he or she or they or it or xe) and submitted and NameLength:     
        st.write("I met", name, location, "the other day.", nomi.title(), wasWere, "lovely! We got to talking about", interests,"because of", because, possDet, device + ".", nomi.title(), "showed me some", presents, "of", possPro + ", they were really good! We talked for a while. Before", nomi, "left", name, " told me about a", invite, nomi, "would be at next weekend. It sounded like something I might enjoy so I think I might go - I wonder if I’ll see", accu, "there.")


elif (fae or he or she or they or it or xe) and NameLength:
    st.divider()
    area = random.randint(0,3)

    if area == 1:
        location = "at a cafe"
        because = "a sticker on"
        device = "laptop"
    elif area == 2:
        location = "at a party"
        because = "a photo on"
        device = "phonecase"
    elif area == 3:
        location = "on campus"
        because = "a sticker on"
        device = "laptop"
    elif area == 0:
        location = "at work"
        because = "a photo in"
        device = "phonecase"
    
    interest = random.randint(0,2)
    if interest == 0:
            interests = "crafts"
            presents = "projects"
            invite = "craft fair"
    elif interest == 1:
        interests = "sports" 
        presents = "photos from matches" 
        invite = "match"
    elif interests == 2:
        interests = "gaming"
        presents = "some picture of a game"
        invite = "a small gaming event in a local cafe"
        
    st.write("I met", name, location, "the other day.", nomi.title(), wasWere, "lovely! We got to talking about", interests,"because of", because, possDet, device + ".", nomi.title(), "showed me some", presents, "of", possPro + ", they were really good! We talked for a while and before", nomi, "left", name, " told me about a", invite, nomi, "would be at next weekend. It sounded like something I might enjoy so I think I might go - I wonder if I’ll see", accu, "there.")

 



#foot notes
st.divider()

st.caption("Pronoun presets were chosen based on the results of the Gender Census 2024 https://www.gendercensus.com/")
st.caption("For more info, suggestions or error reports contact us on the discord! https://discord.gg/NssMXUAeup")
st.caption("Buy me a kofi and support upkeep https://ko-fi.com/cerulean163")


