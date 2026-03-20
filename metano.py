import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_metano(deposito):

    st.markdown("### 🔥 Características do Metano")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- Fórmula química: CH₄")
        st.write("- Gás incolor e inodoro")
        st.write("- Baixa densidade")
        st.write("- Alta inflamabilidade")
        st.write("- Principal componente do gás natural")

    with col2:

        st.info("**Importância Energética**")

        st.write("- Fonte energética global relevante")
        st.write("- Menor emissão de CO₂ que carvão e petróleo")
        st.write("- Utilizado em geração elétrica")
        st.write("- Base para produção de hidrogénio (SMR)")

    st.divider()

    if "Hidratos" in deposito:

        st.markdown("### 🧊 Hidratos de Metano")

        st.write("**Características principais:**")
        st.write("- Estruturas cristalinas (clatratos)")
        st.write("- Metano aprisionado em gelo")
        st.write("- Estáveis a alta pressão e baixa temperatura")
        st.write("- Encontrados em sedimentos marinhos e permafrost")

        st.write("**Ambientes típicos:**")
        st.write("- Margens continentais")
        st.write("- Taludes oceânicos")
        st.write("- Regiões árticas")

    elif "Não Convencionais" in deposito:

        st.markdown("### ⚙️ Recursos Não Convencionais de Metano")

        st.write("**Tipos principais:**")
        st.write("- Shale gas")
        st.write("- Coalbed methane (CBM)")
        st.write("- Tight gas")

        st.write("**Características principais:**")
        st.write("- Baixa permeabilidade")
        st.write("- Necessidade de fraturação hidráulica")
        st.write("- Produção tecnicamente exigente")

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_metano():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("Existem várias confusões frequentes no estudo do metano.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. Metano vs Gás Natural**")
        st.write("- Metano: composto específico (CH₄)")
        st.write("- Gás natural: mistura (metano dominante)")

        st.markdown("**2. Hidratos vs Gelo Comum**")
        st.write("- Hidratos: estrutura cristalina com gás")
        st.write("- Gelo: apenas H₂O")

        st.markdown("**3. Convencional vs Não Convencional**")
        st.write("- Convencional: fácil extração")
        st.write("- Não convencional: requer tecnologia avançada")

        st.markdown("**4. Metano Biogénico vs Termogénico**")
        st.write("- Biogénico: origem microbiana")
        st.write("- Termogénico: origem térmica profunda")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_metano():

    st.markdown("### 🧠 Quiz Interativo: Metano")

    st.write("Testa os teus conhecimentos 👇")

    pergunta1 = st.radio(
        "1️⃣ Onde são encontrados hidratos de metano?",
        [
            "Desertos quentes",
            "Taludes oceânicos",
            "Rochas ígneas profundas",
            "Atmosfera"
        ],
        key="m_q1"
    )

    if st.button("Responder Pergunta 1"):

        if pergunta1 == "Taludes oceânicos":
            st.success("Correto! ✅")
        else:
            st.error("Incorreto ❌")

    st.divider()

    pergunta2 = st.radio(
        "2️⃣ Qual é o principal componente do gás natural?",
        [
            "CO₂",
            "H₂",
            "CH₄",
            "O₂"
        ],
        key="m_q2"
    )

    if st.button("Responder Pergunta 2"):

        if pergunta2 == "CH₄":
            st.success("Exato! ✅")
        else:
            st.error("Resposta incorreta ❌")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_metano():

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado na prospeção de metano:")

    st.checkbox("Identificar bacias sedimentares")
    st.checkbox("Avaliar matéria orgânica")
    st.checkbox("Determinar maturação térmica")
    st.checkbox("Mapear estruturas geológicas")
    st.checkbox("Analisar dados sísmicos")
    st.checkbox("Medir emissões de gás")
    st.checkbox("Avaliar pressão e temperatura")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_metano():

    st.markdown("### 🌍 Mapa Global de Ocorrências de Metano")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="metano_map"
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
                <b>Local:</b> {row.get('Field Name','N/A')}<br>
                <b>País:</b> {row.get('Country','N/A')}<br>
                <b>Tipo:</b> {row.get('Type','N/A')}
                """

                folium.CircleMarker(
                    [row["Latitude"], row["Longitude"]],
                    radius=5,
                    color="green",
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

def referencias_metano():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- Kvenvolden – Gas Hydrates: Geological Perspective")
    st.write("- USGS – Methane Hydrates Research")
    st.write("- IPCC Reports – Methane Emissions")
    st.write("- Sloan – Clathrate Hydrates of Natural Gases")
    st.write("- AAPG – Unconventional Gas Resources")

    st.caption("Fontes científicas relevantes para metano e hidratos.")