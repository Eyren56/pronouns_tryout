import streamlit as st

st.title("Pronoun Tryouts!")
st.subheader("Enter your pronouns!")


col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input(
        "Your name",
        label_visibility="visible",
        disabled=False,
        placeholder="e.g. Ari - Their name is Ari",
    )

with col2:
    nomi = st.text_input(
        "Nominative Pronoun",
        label_visibility="visible",
        disabled=False,
        placeholder="e.g. they - They sit on the chair",
    )

with col3:
    accu = st.text_input(
        "Accusative/Dative Pronoun",
        label_visibility="visible",
        disabled=False,
        placeholder="e.g. them - Is that them?",
    )

col4, col5, col6 = st.columns(3)

with col4:
    possDet = st.text_input(
        "Possessive Determiner",
        label_visibility="visible",
        disabled=False,
        placeholder="e.g. their - Their bag was blue.",
    )
    
with col5:
    possPro = st.text_input(
        "Possesive Pronoun",
        label_visibility="visible",
        disabled=False,
        placeholder="e.g. theirs - Is this bag theirs?",
    )


with col6:
    reflexive = st.text_input(
        "Reflexive Form",
        label_visibility="visible",
        disabled=False,
        placeholder="e.g. themself - I hope they take care of themself.",
    )

context = st.radio(
    "Would your pronoun make more sense in a singular or plural context?",
    ["Singular", "Plural"],
    captions=[
        "would make sense in place of she/her or he/him",
        "would make sense in place of they/them",
    ],
)