
import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from SMS import quiz_sms, mostrar_referencias_sms


# --- 1. Configurações da Página ---

st.set_page_config(
    page_title="Explorador de Recursos Energéticos",
    layout="wide",
    page_icon="💎"
)

# --- 2. Base de Dados ---

materias_primas = [
    "Hidrogénio (Geração natural e armazenamento)",
    "Petróleo e Gás (Sistemas convencionais)",
    "Metano (Hidratos e recursos não convencionais)",
    "Lítio (Rocha dura versus salmouras)",
    "Urânio e Tório (Combustíveis nucleares)",
    "Sulfuretos maciços do fundo oceânico (SMS) e crostas de cobalto",
    "Quartzo",
    "Monazite",
    "Ortoclase"
]

depositos = {

    "Hidrogénio (Geração natural e armazenamento)": [
        "Reservatórios geológicos naturais",
        "Cavernas salinas",
        "Reservatórios de gás esgotados"
    ],

    "Petróleo e Gás (Sistemas convencionais)": [
        "Bacias sedimentares",
        "Armadilhas estruturais",
        "Armadilhas estratigráficas"
    ],

    "Metano (Hidratos e recursos não convencionais)": [
        "Hidratos de gás marinhos",
        "Folhelhos ricos em matéria orgânica (Shale)",
        "Carvões (Coalbed methane)"
    ],

    "Lítio (Rocha dura versus salmouras)": [
        "Pegmatitos (rocha dura)",
        "Salmouras continentais",
        "Argilas ricas em lítio"
    ],

    "Urânio e Tório (Combustíveis nucleares)": [
        "Depósitos tipo unconformity",
        "Depósitos em arenitos",
        "Depósitos hidrotermais"
    ],

    "Sulfuretos maciços do fundo oceânico (SMS)": [
        "Dorsais médio-oceânicas",
        "Arcos vulcânicos submarinos",
        "Bacias de retro-arco"
    ],

    "Quartzo": [
        "Veios hidrotermais",
        "Pegmatitos",
        "Depósitos aluviais"
    ],

    "Monazite": [
        "Depósitos Primários ",
        "Depósitos Secundários"
    ],

    "Ortoclase": [
        "Pegmatitos graníticos",
        "Granitos",
        "Depósitos residuais"
    ]
}

# --- 3. Sidebar ---

with st.sidebar:

    try:
        nome_imagem = "WhatsApp Image 2026-03-16 at 13.44.40.jpeg"
        st.image(nome_imagem)
    except Exception:
        st.write("*(Espaço para o Logótipo)*")

    st.markdown("<h3 style='text-align: center;'>⚙️ Painel de Controlo</h3>", unsafe_allow_html=True)

    st.divider()

    recurso_selecionado = st.selectbox(
        "Selecione a Matéria-Prima:",
        materias_primas
    )

    deposito_selecionado = st.selectbox(
        "Selecione o Tipo de Depósito:",
        depositos.get(recurso_selecionado, []),
        key=f"deposito_{recurso_selecionado}"
    )

    st.divider()

    st.info("💡 Utilize os separadores no ecrã principal para navegar.")

# --- 4. Ecrã Principal ---

st.markdown(f"## 🔎 Análise: {recurso_selecionado}")
st.caption(f"Tipo de depósito selecionado: **{deposito_selecionado}**")

st.write("")

# --- Tabs ---

tab_caract, tab_confusoes, tab_quiz, tab_check, tab_mapa, tab_ref = st.tabs([
    "📊 Características",
    "⚠️ Confusões Comuns",
    "🧠 Quiz Interativo",
    "✅ Checklist de Campo",
    "🗺️ Mapa Global",
    "📚 Referências"
])

# --- Características ---

with tab_caract:

    st.markdown("### Propriedades Principais")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Físicas**")

        st.write("- Dureza (Escala de Mohs): *A definir*")
        st.write("- Brilho: *A definir*")
        st.write("- Clivagem / Fratura: *A definir*")

    with col2:

        st.info("**Aplicações Industriais**")

        st.write("- Uso 1")
        st.write("- Uso 2")
        st.write("- Uso 3")

# --- Confusões ---

with tab_confusoes:

    st.markdown("### Minerais Semelhantes")

    st.warning("Diferenças cruciais para identificação.")

    with st.expander("Ver detalhes"):

        st.write("Conteúdo comparativo.")

# --- Quiz ---

with tab_quiz:

    if recurso_selecionado == "Sulfuretos maciços do fundo oceânico (SMS)":

        quiz_sms()

    else:

        st.info(
            f"O quiz para **{recurso_selecionado}** ainda está em desenvolvimento."
        )

# --- Checklist ---

with tab_check:

    st.checkbox("Verificar a cor e o traço")
    st.checkbox("Testar a dureza")
    st.checkbox("Observar fratura/clivagem")
    st.checkbox("Testar reação com HCl")

# --- MAPA GLOBAL 2D COM CSV ---

with tab_mapa:

    st.markdown("### 🌍 Mapa Global de Ocorrências")

    uploaded_file = st.file_uploader(
        "Carregar base de dados CSV com Latitude e Longitude",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Base de dados carregada com sucesso")

        st.dataframe(df.head())

        mapa = folium.Map(
            location=[20,0],
            zoom_start=2,
            tiles="OpenStreetMap"
        )

        for _, row in df.iterrows():

            if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):

                popup = f"""
                <b>Field:</b> {row.get('Field Name','N/A')}<br>
                <b>Country:</b> {row.get('Country/Region','N/A')}<br>
                <b>Operator:</b> {row.get('Operator','N/A')}<br>
                <b>Status:</b> {row.get('Status','N/A')}
                """

                folium.CircleMarker(
                    location=[row["Latitude"], row["Longitude"]],
                    radius=5,
                    color="red",
                    fill=True,
                    fill_opacity=0.8,
                    popup=popup
                ).add_to(mapa)

        st_folium(mapa, use_container_width=True, height=600)

    else:

        st.info("Carregue um ficheiro CSV para visualizar os dados.")

# --- Referências ---

with tab_ref:

    if recurso_selecionado == "Sulfuretos maciços do fundo oceânico (SMS)":

        mostrar_referencias_sms()

    else:

        st.markdown("### Fontes e Bibliografia")

        st.info(
            f"As referências para **{recurso_selecionado}** ainda estão em compilação."
        )

        st.caption("Organizado por: Grupo Quartzo")








