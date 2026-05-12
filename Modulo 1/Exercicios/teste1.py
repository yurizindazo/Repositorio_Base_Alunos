from turtle import st

import streamlit as st

st.title("Calculadora da Soma")

numero1 = st.number_input("Digite o pimeiro numero: ", min_value=0)
numero2 = st.number_input("Digite o segundo numero: ", min_value=0)

if st.button("calcular"):
    st.sucess(f"A soma é: {numero1 + numero2}")
    st.balloons()