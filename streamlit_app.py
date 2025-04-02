pronounS = []
name = " "

nomi = " "
accu = " "
possDet = " "
possPro = " "
reflexive = " "
compelment  = " "




import streamlit as st

st.title("Pronoun Tryouts")
st.subheader("Welcome! We have a few preset pronoun options or you can custom enter your own.")

st.write("Please only select one pronoun at a time, I'm working on it but currently it just gets confused.")



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
        name = st.text_input(
            "Your name ",
            label_visibility="visible",
            disabled=False,
        )

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
        name = st.text_input(
            "Your name  ",
            label_visibility="visible",
            disabled=False,
        )

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
        name = st.text_input(
            "Your name   ",
            label_visibility="visible",
            disabled=False,
        )
        

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
        name = st.text_input(
            "Your name    ",
            label_visibility="visible",
            disabled=False,
        )

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
        context = "Singular"
        name = st.text_input(
            "Your name     ",
            label_visibility="visible",
            disabled=False
        )

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
        name = st.text_input(
            "Your name     ",
            label_visibility="visible",
            disabled=False
        )



custom = st.checkbox("Custom Pronouns")

if custom:

    col1, col2, col3 = st.columns(3)

    with col1:
        name = st.text_input(
            "Your name",
            label_visibility="visible",
            disabled=False
        )

    with col2:
        nomi = st.text_input(
            "Nominative Pronoun",
            label_visibility="visible",
            disabled=False,
            placeholder="e.g. they - They sit on the chair",
        )
        pronounS.append(nomi)

    with col3:
        accu = st.text_input(
            "Accusative/Dative Pronoun",
            label_visibility="visible",
            disabled=False,
            placeholder="e.g. them - Is that them?",
        )
        pronounS.append(accu)

    col4, col5, col6 = st.columns(3)

    with col4:
        possDet = st.text_input(
            "Possessive Determiner",
            label_visibility="visible",
            disabled=False,
            placeholder="e.g. their - Their bag was blue.",
        )
        pronounS.append(possDet)

    with col5:
        possPro = st.text_input(
            "Possesive Pronoun",
            label_visibility="visible",
            disabled=False,
            placeholder="e.g. theirs - Is this bag theirs?",
        )
        pronounS.append(possPro)

    with col6:
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

if context == "Singular":
    wasWere = "was"
elif context == "Plural":
    wasWere = "were"


personal = st.toggle("Personalised Text")
st.write("By default you get a randomly generated text, take a small quiz to customise it to be more accurate to you")

if not personal:
    st.write("I met", name, "in a cafe the other day.", nomi.title(), wasWere "lovely! We got to talking about crafts because of a sticker on", possDet, "laptop.", nomi.title(), "showed me some projects of", possPro, ", they were really”, compliment, ”! We talked for a while. Before", nomi, "left", name, " told me about a craft fair next weekend. It sounded like something I might enjoy so I think I might go - I wonder if I’ll see", accu, "there.")


#foot notes
st.divider()

st.caption("Pronoun presets were chosen based on the results of the Gender Census 2024 https://www.gendercensus.com/")
st.caption("For more info, suggestions or error reports contact us on the discord! https://discord.gg/NssMXUAeup")
st.caption("Buy me a kofi and support upkeep https://ko-fi.com/cerulean163")


