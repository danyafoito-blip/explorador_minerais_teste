import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_ortoclase(deposito):

    st.markdown("### 🪨 Características da Ortoclase")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Físicas e Mineralógicas**")

        st.write("- Fórmula química: KAlSi₃O₈")
        st.write("- Grupo: Feldspatos")
        st.write("- Dureza: ~6 (Mohs)")
        st.write("- Clivagem perfeita em 2 direções")
        st.write("- Cor: rosa, branca ou bege")

    with col2:

        st.info("**Importância Económica e Industrial**")

        st.write("- Produção de cerâmica")
        st.write("- Indústria do vidro")
        st.write("- Material de construção")
        st.write("- Uso em esmaltes")
        st.write("- Fonte de potássio")

    st.divider()

    if "Pegmatitos" in deposito:

        st.markdown("### 🪨 Pegmatitos Graníticos")

        st.write("**Características principais:**")
        st.write("- Origem magmática")
        st.write("- Cristais de grande dimensão")
        st.write("- Associado a quartzo e mica")
        st.write("- Alta pureza mineral")

    elif "Granitos" in deposito:

        st.markdown("### 🌋 Granitos")

        st.write("**Características principais:**")
        st.write("- Rocha ígnea intrusiva")
        st.write("- Ortoclase como mineral dominante")
        st.write("- Textura fanerítica")
        st.write("- Amplamente distribuído")

    elif "residuais" in deposito.lower():

        st.markdown("### 🌱 Depósitos Residuais")

        st.write("**Características principais:**")
        st.write("- Resultantes da alteração química")
        st.write("- Formação in situ")
        st.write("- Enriquecimento relativo em feldspatos")
        st.write("- Associado a solos e regolitos")

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_ortoclase():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("A ortoclase é frequentemente confundida com outros feldspatos.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. Ortoclase vs Plagioclase**")
        st.write("- Ortoclase: feldspato potássico")
        st.write("- Plagioclase: feldspato sódio-cálcico")

        st.markdown("**2. Ortoclase vs Quartzo**")
        st.write("- Ortoclase: clivagem presente")
        st.write("- Quartzo: fratura concoidal")

        st.markdown("**3. Feldspatos ≠ Minerais Raros**")
        st.write("- São os minerais mais abundantes da crosta")

        st.markdown("**4. Alteração para Argilas**")
        st.write("- Feldspatos alteram-se facilmente (caulinização)")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_ortoclase():

    st.markdown("### 🧠 Quiz Interativo: Ortoclase")

    st.write("Testa os teus conhecimentos 👇")

    pergunta1 = st.radio(
        "1️⃣ A ortoclase pertence a que grupo mineral?",
        [
            "Óxidos",
            "Feldspatos",
            "Carbonatos",
            "Sulfuretos"
        ],
        key="ort_q1"
    )

    if st.button("Responder Pergunta 1"):

        if pergunta1 == "Feldspatos":
            st.success("Correto! ✅")
        else:
            st.error("Incorreto ❌")

    st.divider()

    pergunta2 = st.radio(
        "2️⃣ Qual elemento caracteriza a ortoclase?",
        [
            "Ferro",
            "Potássio",
            "Magnésio",
            "Cálcio"
        ],
        key="ort_q2"
    )

    if st.button("Responder Pergunta 2"):

        if pergunta2 == "Potássio":
            st.success("Exato! ✅")
        else:
            st.error("Resposta incorreta ❌")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_ortoclase():

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado na identificação de ortoclase:")

    st.checkbox("Observar clivagem em 2 direções")
    st.checkbox("Testar dureza (~6 Mohs)")
    st.checkbox("Identificar cor típica (rosa/branco)")
    st.checkbox("Associar a granitos/pegmatitos")
    st.checkbox("Distinguir de quartzo")
    st.checkbox("Verificar alteração para argilas")
    st.checkbox("Recolher amostras")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_ortoclase():

    st.markdown("### 🌍 Mapa Global de Depósitos de Ortoclase")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="ortoclase_map"
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
                    color="pink",
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

def referencias_ortoclase():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- Deer, Howie & Zussman – Rock-Forming Minerals")
    st.write("- Klein & Dutrow – Manual of Mineral Science")
    st.write("- USGS – Feldspar Data")
    st.write("- British Geological Survey – Industrial Minerals")
    st.write("- IMA – Mineral Database")

    st.caption("Fontes científicas sobre feldspatos e ortoclase.")