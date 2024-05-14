import streamlit as st
from src.discrete_models import bernoulli_page, binomial_page, geometric_page, poisson_page


@st.cache_data
def model_function(model: str):
    discrete_models = {
        "Bernoulli": bernoulli_page,
        "Binomial": binomial_page,
        "Geométrico": geometric_page,
        "Poisson": poisson_page,
    }
    if discrete_models.get(model):
        return discrete_models[model]

st.subheader("Modelos de probabilidades discretos")
option = st.selectbox(
    "Selecione um modelo",
    ("Bernoulli", "Binomial", "Geométrico", "Poisson")
)

model_function(option)()
st.divider()

st.page_link("https://mthsolon.github.io/blog/Estat%C3%ADstica/Modelos-de-probabilidade-discretos", label="Clique aqui para saber mais sobre os modelos.")
