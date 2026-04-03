import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_torio(deposito):

    st.markdown("### ☢️ Características do Tório")

    col1, col2 = st.columns(2)

    # Verificação de segurança
    if not deposito:
        st.warning("Por favor, seleciona um tipo de depósito para visualizar as características.")
        return

    if isinstance(deposito, list):
        deposito = ", ".join(deposito)
    
    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- **Propriedades Físicas Elevadas:** Metal prateado com densidade de 11,72 g/cm³, alto ponto de fusão (1750 °C) e ebulição (4790 °C).")
        st.write("- **Radioatividade e Dominância:** O isótopo 232Th representa quase 100% da abundância natural e possui uma meia-vida de 1,39 x 10¹⁰ anos.")
        st.write("- **Natureza Litófila:** Forte afinidade pelo oxigénio, formando preferencialmente minerais de óxido em vez de sulfuretos.")
        st.write("- **Elemento Incompatível:** Concentra-se em magmas residuais tardios (como granitos alcalinos e pegmatitos) durante os processos magmáticos.")
        st.write("- **Inércia Geoquímica:** No estado Th4+ é inerte à superfície e tem baixa solubilidade, sendo transportado mecanicamente (ex: monazite).")

    with col2:

        st.info("**Importância Económica e Energética**")

        st.write("- **Combustível Nuclear do Futuro:** O 232Th pode ser transmutado em 233U (material físsil de alta eficiência).")
        st.write("- **Abundância e Segurança:** É cerca de 3 a 4 vezes mais abundante na crosta continental do que o urânio.")
        st.write("- **Vantagens de Processamento:** Como é quase inteiramente 232Th, não exige processos dispendiosos de enriquecimento isotópico.")
        st.write("- **Reatores Seguros e Limpos:** Oferece maior segurança (ex: Reatores de Sal Fundido), menos resíduos de vida longa e resistência à proliferação de armas.")
        st.write("- **Aplicações Tecnológicas Diversas:** Utilizado em ligas aeroespaciais de alta temperatura, catalisadores, cerâmicas e elétrodos de soldadura.")
    
    st.divider()

    # =========================================================
    # ESPAÇO PARA AS CARACTERÍSTICAS ESPECÍFICAS DOS DEPÓSITOS
    # =========================================================
    
    # Tal como no Urânio, aqui podes colocar a lógica dos "if" para mostrar 
    # informação detalhada consoante o depósito que o utilizador selecionou.
    
    # Exemplo (podes apagar ou modificar consoante os teus depósitos no menu):
    # if "Placers" in deposito or "Areias" in deposito:
    #     st.markdown("## Depósitos de Placers (Areias Minerais)")
    #     st.success("Detalhes sobre a acumulação mecânica da monazite...")
    #     st.divider()


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_torio():

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

def quiz_torio():

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

def checklist_torio():

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

def mapa_torio():

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

def referencias_torio():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- IAEA – Uranium Resources and Production")
    st.write("- OECD NEA – Uranium Reports (Red Book)")
    st.write("- World Nuclear Association")
    st.write("- Dahlkamp – Uranium Deposits of the World")
    st.write("- USGS – Uranium and Thorium Resources")

    st.caption("Fontes científicas e institucionais sobre urânio e tório.")
