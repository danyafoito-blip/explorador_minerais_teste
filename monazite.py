import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_monazite(deposito):

    st.markdown("### 🧲 Características da Monazite")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- Fosfato de terras raras (REE)")
        st.write("- Contém Ce, La, Nd e Th")
        st.write("- Elevada densidade")
        st.write("- Resistência à alteração")
        st.write("- Pode ser radioativa (tório)")

    with col2:

        st.info("**Importância Económica**")

        st.write("- Fonte de terras raras (REE)")
        st.write("- Aplicações em eletrónica")
        st.write("- Energias renováveis (ímans)")
        st.write("- Fonte potencial de tório")
        st.write("- Indústria tecnológica avançada")

    st.divider()

    if "Placer" in deposito:

        st.markdown("### 🏖️ Depósitos de Placer")

        st.write("**Características principais:**")
        st.write("- Formação por concentração mecânica")
        st.write("- Associado a minerais pesados")
        st.write("- Encontrado em praias e rios")
        st.write("- Fácil extração relativa")

    elif "ígneos" in deposito.lower():

        st.markdown("### 🌋 Depósitos Ígneos")

        st.write("**Características principais:**")
        st.write("- Origem magmática")
        st.write("- Associado a rochas graníticas")
        st.write("- Presente em pegmatitos")
        st.write("- Pode coexistir com outros REE")

    elif "metamórficos" in deposito.lower():

        st.markdown("### 🪨 Depósitos Metamórficos")

        st.write("**Características principais:**")
        st.write("- Recristalização em condições metamórficas")
        st.write("- Associado a gnaisses e xistos")
        st.write("- Redistribuição de REE")
        st.write("- Variabilidade mineralógica")

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_monazite():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("A monazite é frequentemente mal interpretada.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. Monazite vs Bastnasite**")
        st.write("- Ambos são minerais de terras raras")
        st.write("- Diferem na composição química")

        st.markdown("**2. Terras Raras ≠ Raras**")
        st.write("- São relativamente abundantes, mas dispersas")

        st.markdown("**3. Radioatividade**")
        st.write("- Presença de tório pode tornar o mineral radioativo")

        st.markdown("**4. REE vs Metais Comuns**")
        st.write("- Terras raras têm propriedades únicas tecnológicas")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_monazite():

    st.markdown("### 🧠 Quiz Interativo: Monazite")

    st.write("Testa os teus conhecimentos 👇")

    pergunta1 = st.radio(
        "1️⃣ A monazite é principalmente uma fonte de:",
        [
            "Ferro",
            "Terras raras (REE)",
            "Carbono",
            "Silício"
        ],
        key="mnz_q1"
    )

    if st.button("Responder Pergunta 1"):

        if pergunta1 == "Terras raras (REE)":
            st.success("Correto! ✅")
        else:
            st.error("Incorreto ❌")

    st.divider()

    pergunta2 = st.radio(
        "2️⃣ Em que tipo de depósito é comum encontrar monazite concentrada?",
        [
            "Placer",
            "Glaciar",
            "Atmosférico",
            "Vulcânico superficial"
        ],
        key="mnz_q2"
    )

    if st.button("Responder Pergunta 2"):

        if pergunta2 == "Placer":
            st.success("Exato! ✅")
        else:
            st.error("Resposta incorreta ❌")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_monazite():

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado na prospeção de monazite:")

    st.checkbox("Identificar minerais pesados")
    st.checkbox("Amostragem de sedimentos")
    st.checkbox("Separação por densidade")
    st.checkbox("Análise geoquímica (REE)")
    st.checkbox("Verificar radioatividade")
    st.checkbox("Mapear contexto geológico")
    st.checkbox("Avaliar viabilidade económica")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_monazite():

    st.markdown("### 🌍 Mapa Global de Depósitos de Monazite")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="monazite_map"
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
                    color="gold",
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

def referencias_monazite():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- USGS – Rare Earth Elements")
    st.write("- IAEA – Thorium Resources")
    st.write("- Gupta & Krishnamurthy – Extractive Metallurgy of REE")
    st.write("- British Geological Survey – REE Profiles")
    st.write("- Hatch – Critical Minerals Report")

    st.caption("Fontes científicas sobre monazite e terras raras.")