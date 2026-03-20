import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_uranio(deposito):

    st.markdown("### ☢️ Características do Urânio e Tório")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- Elementos radioativos (U, Th)")
        st.write("- Elevada densidade")
        st.write("- Emissão de radiação ionizante")
        st.write("- Mobilidade controlada por condições redox")
        st.write("- Ocorrência em minerais como uraninita")

    with col2:

        st.info("**Importância Energética**")

        st.write("- Combustível para energia nuclear")
        st.write("- Produção de eletricidade de base")
        st.write("- Baixas emissões de CO₂")
        st.write("- Tório como alternativa emergente")

    st.divider()

    if "unconformity" in deposito.lower():

        st.markdown("### 🪨 Depósitos tipo Unconformity")

        st.write("**Características principais:**")
        st.write("- Altos teores de urânio")
        st.write("- Associados a discordâncias geológicas")
        st.write("- Interação entre fluidos oxidantes e redutores")
        st.write("- Exemplos: Canadá, Austrália")

    elif "arenitos" in deposito.lower():

        st.markdown("### 🏜️ Depósitos em Arenitos")

        st.write("**Características principais:**")
        st.write("- Hospedados em bacias sedimentares")
        st.write("- Controlo por fluxo de fluidos")
        st.write("- Formação de roll-fronts")
        st.write("- Extração por lixiviação in situ (ISR)")

    elif "hidrotermais" in deposito.lower():

        st.markdown("### 🌋 Depósitos Hidrotermais")

        st.write("**Características principais:**")
        st.write("- Associados a fluidos quentes")
        st.write("- Relação com atividade magmática")
        st.write("- Mineralização em veios e brechas")
        st.write("- Variabilidade de teores")

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_uranio():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("O urânio e o tório são frequentemente mal compreendidos.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. Urânio vs Tório**")
        st.write("- Urânio: amplamente utilizado atualmente")
        st.write("- Tório: potencial futuro, menos explorado")

        st.markdown("**2. Radioatividade ≠ Perigo imediato**")
        st.write("- Depende da concentração e exposição")

        st.markdown("**3. Depósitos ≠ Reatores nucleares**")
        st.write("- Depósitos são naturais, reatores são artificiais")

        st.markdown("**4. Energia nuclear ≠ Energia renovável**")
        st.write("- É de baixa emissão, mas não renovável")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_uranio():

    st.markdown("### 🧠 Quiz Interativo: Urânio e Tório")

    st.write("Testa os teus conhecimentos 👇")

    pergunta1 = st.radio(
        "1️⃣ Onde são comuns depósitos tipo unconformity?",
        [
            "Oceanos profundos",
            "Discordâncias geológicas",
            "Atmosfera",
            "Desertos arenosos"
        ],
        key="u_q1"
    )

    if st.button("Responder Pergunta 1"):

        if pergunta1 == "Discordâncias geológicas":
            st.success("Correto! ✅")
        else:
            st.error("Incorreto ❌")

    st.divider()

    pergunta2 = st.radio(
        "2️⃣ Qual método é comum em depósitos em arenitos?",
        [
            "Exploração submarina",
            "Fraturação hidráulica",
            "Lixiviação in situ (ISR)",
            "Fusão nuclear"
        ],
        key="u_q2"
    )

    if st.button("Responder Pergunta 2"):

        if pergunta2 == "Lixiviação in situ (ISR)":
            st.success("Exato! ✅")
        else:
            st.error("Resposta incorreta ❌")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_uranio():

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado na prospeção de urânio e tório:")

    st.checkbox("Identificar bacias sedimentares")
    st.checkbox("Mapear discordâncias geológicas")
    st.checkbox("Medir radioatividade (gamma)")
    st.checkbox("Analisar condições redox")
    st.checkbox("Identificar minerais uraníferos")
    st.checkbox("Avaliar circulação de fluidos")
    st.checkbox("Verificar segurança radiológica")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_uranio():

    st.markdown("### 🌍 Mapa Global de Depósitos de Urânio e Tório")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="uranio_map"
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
                    color="orange",
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

def referencias_uranio():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- IAEA – Uranium Resources and Production")
    st.write("- OECD NEA – Uranium Reports (Red Book)")
    st.write("- World Nuclear Association")
    st.write("- Dahlkamp – Uranium Deposits of the World")
    st.write("- USGS – Uranium and Thorium Resources")

    st.caption("Fontes científicas e institucionais sobre urânio e tório.")