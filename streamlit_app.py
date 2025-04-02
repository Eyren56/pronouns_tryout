pronounS = []

import streamlit as st

st.title("Pronoun Tryouts")
st.subheader("Welcome! We have a few preset pronoun options or you can custom enter your own.")

st.write("Please only select one pronoun at a time, I'm working on it but currently it just gets confused.")


col1, col2, col3 = st.columns(3)

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



personal = st.toggle("Personalised Text")
st.write("By default you get a randomly generated text, take a small quiz to customise it to be more accurate to you")

if personal:
    st.write("Feature activated!")

st.divider()


st.caption("Pronoun presets were chosen based on the results of the Gender Census 2024 https://www.gendercensus.com/")
st.caption("For any questions, suggestions or bug reports contact us on th discord! https://discord.gg/NssMXUAeup")
st.caption("Support upkeep and fund future projects https://ko-fi.com/cerulean163")


