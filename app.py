
import streamlit as st

st.title("Aplicação desenvolvida por ZedeckDev 🐍")

# Menu lateral
opcao = st.sidebar.selectbox(
    "Escolha a aplicação:",
    ["Calculadora de Tinta", "Calculadora de Desconto"]
)

# --- Calculadora de Tinta ---
if opcao == "Calculadora de Tinta":
    st.header("🎨 Calculadora de Tinta")
    largura = st.number_input("Digite a largura da parede (m)", min_value=0.0)
    altura = st.number_input("Digite a altura da parede (m)", min_value=0.0)

    if st.button("Calcular tinta"):
        area = largura * altura
        tinta = area / 2
        st.success(f"A área é {area:.2f} m²")
        st.info(f"Quantidade de tinta necessária: {tinta:.2f} litros")

# --- Calculadora de Desconto ---
elif opcao == "Calculadora de Desconto":
    st.header("🛒 Calculadora de Desconto")
    preco = st.number_input("Digite o preço do produto (R$)", min_value=0.0)

    if st.button("Calcular desconto"):
        desconto = preco * 0.05
        novo_preco = preco - desconto
        st.success(f"Preço original: R$ {preco:.2f}")
        st.info(f"Desconto de 5%: R$ {desconto:.2f}")
        st.success(f"Novo preço: R$ {novo_preco:.2f}")

