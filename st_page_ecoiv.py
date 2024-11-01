import streamlit as st

st.set_page_config(page_title="Notas interactivas de Economía IV", page_icon="ecoiv.png")

curso = st.Page("curso.py", title = "Curso", default= True)
eqg = st.Page("eqg.py", title = "Equilibrio general", default= False)
mono = st.Page("mono.py", title = "Monopolio", default = False)
gt = st.page("gt.py", title = "Teoría de juegos", default = False)

pg = st.navigation(
    {
        "Curso": [curso],
        "Equilibrio general": [eqg],
        "Monopolio y monopsonio": [mono],
        "Teoría de juegos": [gt],
    }
)
pg.run()