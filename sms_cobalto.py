import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_sms(deposito):

    st.markdown("### 🌊⚙️ Sulfuretos Maciços Submarinos (SMS) e Crostas de Cobalto")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Geológicas e Geoquímicas**")

        st.write("- Depósitos hidrotermais submarinos")
        st.write("- Ricos em Cu, Zn, Pb, Au, Ag")
        st.write("- Associados a fluidos quentes")
        st.write("- Precipitação rápida de sulfuretos")
        st.write("- Elevada heterogeneidade")

    with col2:

        st.info("**Importância Económica**")

        st.write("- Fonte de metais críticos")
        st.write("- Cobalto essencial para baterias")
        st.write("- Potencial elevado no fundo oceânico")
        st.write("- Interesse crescente em mineração profunda")

    st.divider()

    if "Dorsais" in deposito:

        st.markdown("### 🌋 Dorsais Médio-Oceânicas")

        st.write("**Características principais:**")
        st.write("- Associadas a expansão do fundo oceânico")
        st.write("- Sistemas hidrotermais ativos (black smokers)")
        st.write("- Formação rápida de sulfuretos")
        st.write("- Alta temperatura")

    elif "Arcos" in deposito:

        st.markdown("### 🌊 Arcos Vulcânicos Submarinos")

        st.write("**Características principais:**")
        st.write("- Associados a zonas de subducção")
        st.write("- Magmatismo intenso")
        st.write("- Maior diversidade metálica")
        st.write("- Ambientes complexos")

    elif "retro-arco" in deposito.lower():

        st.markdown("### 🌊 Bacias de Retro-Arco")

        st.write("**Características principais:**")
        st.write("- Extensão tectónica atrás de arcos vulcânicos")
        st.write("- Sistemas hidrotermais ativos")
        st.write("- Depósitos economicamente relevantes")
        st.write("- Variabilidade geológica")

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_sms():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("Os depósitos SMS e crostas de cobalto são frequentemente confundidos.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. SMS vs Nódulos Polimetálicos**")
        st.write("- SMS: associados a hidrotermalismo")
        st.write("- Nódulos: crescimento lento em planícies abissais")

        st.markdown("**2. SMS vs Crostas de Cobalto**")
        st.write("- SMS: sulfuretos maciços")
        st.write("- Crostas: enriquecimento em superfícies rochosas")

        st.markdown("**3. Ativo vs Inativo**")
        st.write("- Ativo: associado a fluidos quentes")
        st.write("- Inativo: sistemas fossilizados")

        st.markdown("**4. Mineração Simples?**")
        st.write("- Ambientes profundos implicam desafios técnicos e ambientais")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_sms():

    st.markdown("### 🧠 Quiz Interativo: SMS e Cobalto")

    st.write("Testa os teus conhecimentos 👇")

    pergunta1 = st.radio(
        "1️⃣ Onde se formam os SMS?",
        [
            "Desertos",
            "Sistemas hidrotermais submarinos",
            "Atmosfera",
            "Glaciares"
        ],
        key="sms_q1"
    )

    if st.button("Responder Pergunta 1"):

        if pergunta1 == "Sistemas hidrotermais submarinos":
            st.success("Correto! ✅")
        else:
            st.error("Incorreto ❌")

    st.divider()

    pergunta2 = st.radio(
        "2️⃣ O cobalto é crítico para:",
        [
            "Produção de cimento",
            "Baterias",
            "Areia industrial",
            "Vidro comum"
        ],
        key="sms_q2"
    )

    if st.button("Responder Pergunta 2"):

        if pergunta2 == "Baterias":
            st.success("Exato! ✅")
        else:
            st.error("Resposta incorreta ❌")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_sms():

    st.markdown("### ✅ Checklist de Campo (Exploração Submarina)")

    st.write("Utilizado na exploração de depósitos SMS:")

    st.checkbox("Identificar atividade hidrotermal")
    st.checkbox("Mapear estruturas tectónicas")
    st.checkbox("Analisar plumas hidrotermais")
    st.checkbox("Amostragem de sulfuretos")
    st.checkbox("Caracterização geoquímica")
    st.checkbox("Avaliação ambiental")
    st.checkbox("Utilização de ROVs/AUVs")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_sms():

    st.markdown("### 🌍 Mapa Global de Depósitos SMS e Cobalto")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="sms_map"
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Base de dados carregada com sucesso")
        st.dataframe(df.head())

        mapa = folium.Map(
            location=[0, 0],
            zoom_start=2
        )

        Fullscreen().add_to(mapa)

        for _, row in df.iterrows():

            if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):

                popup = f"""
                <b>Local:</b> {row.get('Field Name','N/A')}<br>
                <b>Região:</b> {row.get('Region','N/A')}<br>
                <b>Tipo:</b> {row.get('Type','N/A')}
                """

                folium.CircleMarker(
                    [row["Latitude"], row["Longitude"]],
                    radius=5,
                    color="black",
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

def referencias_sms():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- Hannington et al. – Seafloor Massive Sulfides")
    st.write("- ISA (International Seabed Authority)")
    st.write("- USGS – Marine Mineral Resources")
    st.write("- Hein et al. – Cobalt-Rich Crusts")
    st.write("- Nature Reviews – Deep-Sea Mining")

    st.caption("Fontes científicas sobre mineração submarina e SMS.")