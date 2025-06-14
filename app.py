import streamlit as st
from computador import Computador

st.title("Simulador de Computador")

marca = st.text_input("Marca do computador")
memoria_ram = st.number_input("Memória RAM (GB)", min_value=1, max_value=128, step=1)
armazenamento = st.number_input("Armazenamento (GB)", min_value=64, max_value=2000, step=64)

if st.button("Criar Computador"):
    pc = Computador(marca, memoria_ram, armazenamento)

    st.success("Computador criado com sucesso!")

    st.subheader("Informações do Computador:")
    st.write("Marca:", pc.get_marca())
    st.write("Memória RAM:", pc.get_memoria_ram(), "GB")
    st.write("Armazenamento:", pc.get_armazenamento(), "GB")

    if st.button("Ligar Computador"):
        st.info(pc.ligar_computador())
