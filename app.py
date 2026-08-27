import streamlit as st

st.title("Calculadora de Tinta 🎨")

largura = st.number_input("Digite a largura da parede (m)", min_value=0.0)
altura = st.number_input("Digite a altura da parede (m)", min_value=0.0)

if st.button("Calcular"):
    area = largura * altura
    tinta = area / 2
    st.success(f"A área é {area:.2f} m² e precisa de {tinta:.2f} litros de tinta.")
