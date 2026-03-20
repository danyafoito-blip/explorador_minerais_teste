import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium

# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_hidrogenio(deposito):

    st.markdown("### ⚛️ Características do Hidrogénio")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- Molécula: H₂ (diatómica)")
        st.write("- Densidade extremamente baixa")
        st.write("- Alta difusividade")
        st.write("- Elevada reatividade química")
        st.write("- Baixa viscosidade")

    with col2:

        st.info("**Importância Energética**")

        st.write("- Vetor energético limpo")
        st.write("- Produção de eletricidade (fuel cells)")
        st.write("- Armazenamento de energia")
        st.write("- Descarbonização industrial")

    st.divider()

    if "Natural" in deposito:

        st.markdown("### 🌍 Hidrogénio Natural (Geológico)")

        st.write("**Processos de geração:**")
        st.write("- Serpentinização (reação água-rocha)")
        st.write("- Radiolise da água")
        st.write("- Degaseificação mantélica")

        st.write("**Ambientes geológicos típicos:**")
        st.write("- Rochas ultramáficas (peridotitos)")
        st.write("- Zonas de rifte")
        st.write("- Crátons antigos")
        st.write("- Sistemas hidrotermais")

    else:

        st.markdown("### 🏗️ Armazenamento Geológico de Hidrogénio")

        st.write("**Tipos de reservatórios:**")
        st.write("- Cavidades salinas (salt caverns)")
        st.write("- Aquíferos profundos")
        st.write("- Reservatórios exauridos de gás/petróleo")

        st.write("**Desafios principais:**")
        st.write("- Fugas devido à alta mobilidade")
        st.write("- Reações geoquímicas")
        st.write("- Consumo microbiano")
        st.write("- Integridade do selo (cap rock)")

# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_hidrogenio():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("Classificações incorretas são frequentes no estudo do hidrogénio.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. Hidrogénio Natural vs Industrial**")
        st.write("- Natural: ocorre no subsolo (white hydrogen)")
        st.write("- Industrial: produzido artificialmente")

        st.markdown("**2. Hidrogénio Branco vs Verde vs Azul**")
        st.write("- Branco: geológico")
        st.write("- Verde: eletrólise com renováveis")
        st.write("- Azul: gás natural com captura de CO₂")

        st.markdown("**3. Armazenamento ≠ Ocorrência Natural**")
        st.write("- Um reservatório pode armazenar H₂ sem o gerar")

        st.markdown("**4. Hidrogénio vs Metano**")
        st.write("- H₂: mais leve, mais difusivo")
        st.write("- CH₄: mais estável e comum")

# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_hidrogenio():

    st.markdown("### 🧠 Quiz Interativo: Hidrogénio")
    st.write("Teste os teus conhecimentos 👇")

    if "corrigido_h2" not in st.session_state:
        st.session_state.corrigido_h2 = False

    corretas = [
        "Serpentinização",
        "Fugas devido à elevada mobilidade"
    ]

    pergunta1 = st.radio(
        "1️⃣ Qual processo gera hidrogénio natural?",
        [
            "Combustão de carvão",
            "Serpentinização",
            "Refinação de petróleo",
            "Fotossíntese"
        ],
        key="q1",
        index=None
    )

    if st.session_state.corrigido_h2:
        if pergunta1 == corretas[0]:
            st.success("Correto ✅")
        elif pergunta1 is not None:
            st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

    st.divider()

    pergunta2 = st.radio(
        "2️⃣ Qual é o principal desafio no armazenamento de H₂?",
        [
            "Cor do gás",
            "Alta densidade",
            "Fugas devido à elevada mobilidade",
            "Baixa reatividade"
        ],
        key="q2",
        index=None
    )

    if st.session_state.corrigido_h2:
        if pergunta2 == corretas[1]:
            st.success("Correto ✅")
        elif pergunta2 is not None:
            st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

    if st.button("Corrigir Quiz"):
        st.session_state.corrigido_h2 = True

    if st.session_state.corrigido_h2:
        respostas = [pergunta1, pergunta2]
        score = sum([r == c for r, c in zip(respostas, corretas)])
        st.markdown(f"### 🎯 Pontuação: {score}/2")

# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_hidrogenio():

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado em prospeção de hidrogénio geológico:")

    st.checkbox("Identificar rochas ultramáficas")
    st.checkbox("Mapear falhas e fraturas")
    st.checkbox("Avaliar presença de água")
    st.checkbox("Medir emissões gasosas (H₂, CH₄)")
    st.checkbox("Analisar mineralogia (serpentina, olivina)")
    st.checkbox("Verificar selos geológicos")
    st.checkbox("Avaliar atividade microbiana")

# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_hidrogenio():

    st.markdown("### 🌍 Mapa Global de Ocorrências de Hidrogénio")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="hidrogenio_map"
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Base de dados carregada com sucesso")
        st.dataframe(df.head())

        mapa = folium.Map(
            location=[20, 0],
            zoom_start=2,
            tiles="OpenStreetMap"
        )

        Fullscreen(
            position="topright",
            title="Expandir mapa",
            title_cancel="Sair do fullscreen",
            force_separate_button=True
        ).add_to(mapa)

        for _, row in df.iterrows():

            if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):

                popup = f"""
                <b>Local:</b> {row.get('Field Name','N/A')}<br>
                <b>País:</b> {row.get('Country/Region','N/A')}<br>
                <b>Tipo:</b> {row.get('Type','N/A')}<br>
                <b>Status:</b> {row.get('Status','N/A')}
                """

                folium.CircleMarker(
                    location=[row["Latitude"], row["Longitude"]],
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

def referencias_hidrogenio():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- USGS – Natural Hydrogen Studies")
    st.write("- IEA – Global Hydrogen Review")
    st.write("- Zgonnik (2020) – The occurrence and geoscience of natural hydrogen")
    st.write("- Prinzhofer et al. – Natural Hydrogen Systems")
    st.write("- Truche et al. – Hydrogen exploration models")

    st.caption("Fontes científicas e institucionais relevantes para hidrogénio geológico.")