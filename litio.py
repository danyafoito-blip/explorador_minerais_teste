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

# ===============================
# 2. CONFUSÕES COMUNS E DISTINÇÕES
# ===============================

def mostrar_confusoes_litio(deposito=""):

    st.markdown("### ⚠️ Pontos de Distinção e Confusão: Lítio")

    st.markdown("#### 🌍 5 Pontos Gerais de Distinção")

    with st.expander("🔍 Ver pontos gerais", expanded=True):
        st.markdown("**1. Estado Físico do Recurso:** A principal distinção reside entre o lítio em estado sólido, fixado em redes cristalinas de minerais (pegmatitos e argilas), e o lítio em estado líquido, dissolvido como ião em águas hipersalinas (salmouras).")
        st.markdown("**2. Ambiente Tectónico e Climático:** Os pegmatitos formam-se em cinturões orogénicos (zonas de colisão de placas), enquanto as salmouras e muitas argilas dependem de bacias fechadas em climas áridos com atividade vulcânica recente.")
        st.markdown("**3. Mineralogia e Química:** Cada depósito tem \"minerais indicadores\": a espodumena para rocha dura, a hectorite para argilas e o cloreto de lítio dissolvido para salmouras.")
        st.markdown("**4. Método de Extração:** Pegmatitos exigem mineração convencional, moagem e ustulação a altas temperaturas; salmouras utilizam evaporação solar ou adsorção direta; argilas requerem lixiviação ácida.")
        st.markdown("**5. Idade Geológica:** Os depósitos de rocha dura abrangem desde o Arqueico ao Mioceno, enquanto quase todos os depósitos de salmoura economicamente viáveis são do Quaternário.")

    st.divider()

    if deposito:
        st.markdown(f"#### 🔎 Distinções Específicas: {deposito}")

        if "pegmatito" in deposito.lower() or "rocha dura" in deposito.lower():
            st.markdown("- **Composição Mineral:** O lítio está concentrado em silicatos como a espodumena, petalite e lepidolite, frequentemente ocorrendo em cristais de dimensões excecionais dentro de diques graníticos.")
            st.markdown("- **Génese:** Resultam do fracionamento extremo de magmas graníticos peraluminosos (Tipo S) ou da fusão parcial da crosta, geralmente a menos de 10 km do plutão progenitor.")
            st.markdown("- **Zonamento:** Apresentam um zonamento mineralógico característico, onde o lítio tende a acumular-se nas zonas intermédias ou distais em relação ao granito de origem.")

        elif "salmoura" in deposito.lower():
            st.markdown("- **Acumulação em Bacias Fechadas:** Encontram-se em bacias endorreicas onde a água flui para o interior, mas só sai por evaporação, concentrando sais ao longo de milhões de anos.")
            st.markdown("- **Fonte Vulcânica:** O lítio provém da lixiviação de rochas vulcânicas circundantes (como ignimbritos) e de aportes de fluidos hidrotermais que alimentam a bacia.")
            st.markdown("- **Desafio das Impurezas:** A viabilidade económica depende do rácio Magnésio/Lítio; rácios elevados dificultam a precipitação do lítio devido à similaridade química entre os dois iões.")

        elif "argila" in deposito.lower():
            st.markdown("- **Mineralogia Específica:** O lítio está hospedado em minerais de argila do grupo da esmectite, principalmente a hectorite (rica em magnésio e lítio) ou em ilites alteradas.")
            st.markdown("- **Ambiente de Formação:** Formam-se tipicamente em lagos de caldeiras vulcânicas, onde cinzas e vidros vulcânicos sofrem alteração hidrotermal ou reagem com fluidos ricos em lítio.")
            st.markdown("- **Facilidade de Mineração:** Por serem depósitos mais \"macios\", permitem a extração por céu aberto sem necessidade de explosivos, embora a separação química do lítio da estrutura da argila exija processamento ácido intensivo.")
            
    else:
        st.info("Selecione um tipo de depósito na barra lateral para ver as distinções específicas.")

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
