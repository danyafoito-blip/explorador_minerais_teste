import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_quartzo(deposito):

    st.markdown("### 💎 Características do Quartzo")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Físicas e Mineralógicas**")

        st.write("- Fórmula química: SiO₂")
        st.write("- Dureza: 7 (escala de Mohs)")
        st.write("- Alta resistência química")
        st.write("- Fratura concoidal")
        st.write("- Elevada estabilidade")

    with col2:

        st.info("**Importância Económica e Industrial**")

        st.write("- Produção de vidro")
        st.write("- Indústria eletrónica (silício)")
        st.write("- Cerâmica")
        st.write("- Construção")
        st.write("- Aplicações ópticas")

    st.divider()

    if "Veios" in deposito:

        st.markdown("### 🌋 Veios Hidrotermais")

        st.write("**Características principais:**")
        st.write("- Formação por fluidos hidrotermais")
        st.write("- Preenchimento de fraturas")
        st.write("- Alta pureza possível")
        st.write("- Associado a mineralizações metálicas")

    elif "Pegmatitos" in deposito:

        st.markdown("### 🪨 Pegmatitos")

        st.write("**Características principais:**")
        st.write("- Origem magmática")
        st.write("- Cristais de grande dimensão")
        st.write("- Associado a feldspatos e mica")
        st.write("- Importante para quartzo de alta qualidade")

    elif "Aluviais" in deposito:

        st.markdown("### 🏞️ Depósitos Aluviais")

        st.write("**Características principais:**")
        st.write("- Transporte por água")
        st.write("- Acumulação em rios e planícies")
        st.write("- Grãos arredondados")
        st.write("- Fácil extração")

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_quartzo():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("O quartzo é frequentemente confundido com outros minerais.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. Quartzo vs Feldspato**")
        st.write("- Quartzo: mais duro (Mohs 7)")
        st.write("- Feldspato: mais macio (~6)")

        st.markdown("**2. Quartzo vs Vidro**")
        st.write("- Quartzo: cristalino")
        st.write("- Vidro: amorfo")

        st.markdown("**3. Areia ≠ Apenas Quartzo**")
        st.write("- Pode conter feldspatos e outros minerais")

        st.markdown("**4. Pureza Industrial**")
        st.write("- Nem todo quartzo é adequado para eletrónica")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_quartzo():

    st.markdown("### 🧠 Quiz Interativo: Quartzo")

    st.write("Testa os teus conhecimentos 👇")

    pergunta1 = st.radio(
        "1️⃣ Qual é a fórmula química do quartzo?",
        [
            "SiO₂",
            "Al₂O₃",
            "Fe₂O₃",
            "CaCO₃"
        ],
        key="qz_q1"
    )

    if st.button("Responder Pergunta 1"):

        if pergunta1 == "SiO₂":
            st.success("Correto! ✅")
        else:
            st.error("Incorreto ❌")

    st.divider()

    pergunta2 = st.radio(
        "2️⃣ Qual é a dureza do quartzo?",
        [
            "5",
            "6",
            "7",
            "8"
        ],
        key="qz_q2"
    )

    if st.button("Responder Pergunta 2"):

        if pergunta2 == "7":
            st.success("Exato! ✅")
        else:
            st.error("Resposta incorreta ❌")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_quartzo():

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado na identificação de quartzo:")

    st.checkbox("Verificar dureza (risca vidro)")
    st.checkbox("Observar fratura concoidal")
    st.checkbox("Analisar transparência")
    st.checkbox("Identificar associação mineral")
    st.checkbox("Avaliar pureza")
    st.checkbox("Observar contexto geológico")
    st.checkbox("Recolher amostras representativas")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_quartzo():

    st.markdown("### 🌍 Mapa Global de Depósitos de Quartzo")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="quartzo_map"
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
                    color="blue",
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

def referencias_quartzo():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- Deer, Howie & Zussman – Rock-Forming Minerals")
    st.write("- USGS – Quartz Data and Industrial Uses")
    st.write("- Klein & Dutrow – Manual of Mineral Science")
    st.write("- IMA – Mineral Database")
    st.write("- Industrial Minerals Association")

    st.caption("Fontes científicas e industriais sobre quartzo.")