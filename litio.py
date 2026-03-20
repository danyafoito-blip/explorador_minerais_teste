import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_litio(deposito):

    st.markdown("### 🔋 Características do Lítio")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- Elemento químico: Li")
        st.write("- Metal alcalino leve")
        st.write("- Alta reatividade química")
        st.write("- Baixa densidade")
        st.write("- Elevada mobilidade em fluidos")

    with col2:

        st.info("**Importância Económica e Energética**")

        st.write("- Essencial para baterias (íon-lítio)")
        st.write("- Transição energética")
        st.write("- Armazenamento de energia")
        st.write("- Indústria eletrónica e automóvel")

    st.divider()

    if "Pegmatitos" in deposito:

        st.markdown("### 🪨 Lítio em Rocha Dura (Pegmatitos)")

        st.write("**Minerais principais:**")
        st.write("- Espodumena")
        st.write("- Lepidolita")
        st.write("- Petalita")

        st.write("**Características:**")
        st.write("- Origem magmática")
        st.write("- Cristais de grande dimensão")
        st.write("- Extração mineira convencional")
        st.write("- Teores relativamente elevados")

    elif "Salmouras" in deposito:

        st.markdown("### 🌊 Lítio em Salmouras Continentais")

        st.write("**Ambiente típico:**")
        st.write("- Bacias endorreicas")
        st.write("- Climas áridos (salars)")

        st.write("**Características:**")
        st.write("- Lítio dissolvido em salmouras")
        st.write("- Extração por evaporação")
        st.write("- Custos mais baixos")
        st.write("- Forte dependência climática")

    elif "Argilas" in deposito:

        st.markdown("### 🧱 Lítio em Argilas")

        st.write("**Características principais:**")
        st.write("- Associado a minerais argilosos")
        st.write("- Processamento mais complexo")
        st.write("- Potencial crescente")
        st.write("- Tecnologias ainda em desenvolvimento")

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_litio():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("O lítio é frequentemente mal interpretado em contexto geológico.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. Lítio ≠ Terra Rara**")
        st.write("- Lítio não pertence ao grupo das terras raras")

        st.markdown("**2. Rocha Dura vs Salmouras**")
        st.write("- Rocha dura: mineração tradicional")
        st.write("- Salmouras: evaporação e processamento químico")

        st.markdown("**3. Recurso vs Reserva**")
        st.write("- Recurso: quantidade total estimada")
        st.write("- Reserva: economicamente viável")

        st.markdown("**4. Extração Simples?**")
        st.write("- Processamento pode ser complexo e intensivo")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_litio():

    st.markdown("### 🧠 Quiz Interativo: Lítio")

    st.write("Testa os teus conhecimentos 👇")

    pergunta1 = st.radio(
        "1️⃣ Qual mineral é uma fonte importante de lítio em pegmatitos?",
        [
            "Quartzo",
            "Espodumena",
            "Calcite",
            "Pirite"
        ],
        key="l_q1"
    )

    if st.button("Responder Pergunta 1"):

        if pergunta1 == "Espodumena":
            st.success("Correto! ✅")
        else:
            st.error("Incorreto ❌")

    st.divider()

    pergunta2 = st.radio(
        "2️⃣ Onde são típicas as salmouras ricas em lítio?",
        [
            "Regiões polares",
            "Bacias áridas (salars)",
            "Zonas vulcânicas profundas",
            "Oceanos abertos"
        ],
        key="l_q2"
    )

    if st.button("Responder Pergunta 2"):

        if pergunta2 == "Bacias áridas (salars)":
            st.success("Exato! ✅")
        else:
            st.error("Resposta incorreta ❌")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_litio():

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado na prospeção de lítio:")

    st.checkbox("Identificar pegmatitos graníticos")
    st.checkbox("Mapear bacias sedimentares evaporíticas")
    st.checkbox("Analisar mineralogia (espodumena, lepidolita)")
    st.checkbox("Amostragem geoquímica")
    st.checkbox("Avaliar condições climáticas (evaporação)")
    st.checkbox("Caracterizar salmouras")
    st.checkbox("Avaliar viabilidade económica")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_litio():

    st.markdown("### 🌍 Mapa Global de Depósitos de Lítio")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="litio_map"
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Base de dados carregada com sucesso")
        st.dataframe(df.head())

        mapa = folium.Map(
            location=[20, 0],
            zoom_start=2
        )

        Fullscreen().add_to(mapa)

        for _, row in df.iterrows():

            if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):

                popup = f"""
                <b>Depósito:</b> {row.get('Field Name','N/A')}<br>
                <b>País:</b> {row.get('Country','N/A')}<br>
                <b>Tipo:</b> {row.get('Type','N/A')}
                """

                folium.CircleMarker(
                    [row["Latitude"], row["Longitude"]],
                    radius=5,
                    color="purple",
                    fill=True,
                    fill_opacity=0.8,
                    popup=popup
                ).add_to(mapa)

        st_folium(mapa, use_container_width=True, height=600)

    else:
        st.info("Carregue um ficheiro CSV para visualizar os dados.")


# ===============================
# 6. REFERÊNCIAS
# ===============================

def referencias_litio():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- USGS – Lithium Statistics and Information")
    st.write("- Kesler et al. – Global Lithium Resources")
    st.write("- Bradley et al. – Lithium Brine Deposits")
    st.write("- London – Pegmatites")
    st.write("- IEA – Global EV Outlook")

    st.caption("Fontes científicas e institucionais sobre lítio.")