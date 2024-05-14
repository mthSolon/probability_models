import streamlit as st
from src.discrete_functions import bernoulli, binomial, geometric, poisson

def bernoulli_page():
    st.latex(r"P(X=x) = p^x \cdot (1-p)^{1-x}")
    prob = st.slider("Escolha a probabilidade:", 0.0, 1.0, key="bernoulli_p")
    values = bernoulli(prob)
    st.bar_chart(values)

def binomial_page():
    st.latex(r"P(X=k) = \binom{x}{k} \; \cdot \; p^k \; \cdot \; (1-p)^{x-k}")
    prob = st.slider("Escolha a probabilidade:", 0.0, 1.0, key="binomial_p")
    k = st.slider("Escolha o valor da variável aleatória k:", 0, 100, key="binomial_k")
    values = binomial(prob, k)
    if k:
        st.bar_chart(values)

def geometric_page():
    st.latex(r"P(X=k) = p(1-p)^k")
    prob = st.slider("Escolha a probabilidade:", 0.0, 1.0, key="geometric_p")
    k = st.slider("Escolha o valor da variável aleatória k:", 0, 100, key="geometric_k")
    values = geometric(prob, k)
    if k:
        st.bar_chart(values)

def poisson_page():
    st.latex(r"P(X=x) = \frac{\lambda^xe^{-\lambda}}{x!}")
    l = st.number_input("Escolha o valor de lambda:", 0.0, 100.0)
    x = st.slider("Escolha o valor da variável aleatória x:", 0, 100, key="poisson_x")
    values = poisson(l, x)
    if x:
        st.bar_chart(values)

