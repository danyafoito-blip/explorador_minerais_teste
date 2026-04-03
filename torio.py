import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


import streamlit as st

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

    # Correção: Converter a variável para string minúscula (resolve o NameError!)
    if isinstance(deposito, list):
        deposito_str = " ".join(deposito).lower()
    else:
        deposito_str = str(deposito).lower()
    
    # --- PARTE 1: CARACTERÍSTICAS GERAIS ---
    with col1:
        st.success("**Propriedades Físicas e Geoquímicas**")
        st.write("- Propriedades Físicas Elevadas")
        st.write("- Radioatividade e Dominância Isotópica")
        st.write("- Baixa Solubilidade")
        st.write("- Comportamento de Elemento Incompatível")
        st.write("- Inércia Geoquímica à Superfície")

    with col2:
        st.info("**Importância Económica e Energética**")
        st.write("- Combustível Nuclear do Futuro")
        st.write("- Abundância e Segurança de Suprimento")
        st.write("- Vantagens Económicas no Processamento")
        st.write("- Reatores mais Seguros e Limpos")
        st.write("- Aplicações Tecnológicas Diversas")
    
    st.divider()

    # --- PARTE 2: CARACTERÍSTICAS ESPECÍFICAS DOS DEPÓSITOS ---
    
    # 1. Carbonatitos e Complexos Alcalinos
    if "carbonatitos" in deposito_str or "alcalinos" in deposito_str:
        st.markdown("## Carbonatitos e Complexos Alcalinos")
        
        st.markdown("### Génese e Formação")
        st.success(
            "O tório é um elemento incompatível que se enriquece nos estágios tardios da "
            "diferenciação magmática. Nestes sistemas, fluidos carbonatíticos alcalinos ricos em voláteis (como F, Cl e CO₂) "
            "possuem uma elevada capacidade de transportar e concentrar o tório e elementos de terras raras (REE). "
            "A mineralização ocorre frequentemente na zona de contacto entre o carbonatito e o soco (ex: Bayan Obo, China) ou controlada por falhas regionais."
        )
        
        st.divider()
        
        st.markdown("### Exploração e Processamento")
        st.info(
            "O tório nestes depósitos é quase sempre explorado como um subproduto "
            "da extração de REE ou nióbio. O processamento envolve a recuperação de minerais como a bastnaesite e a monazite. "
            "Nestes depósitos, a monazite costuma ter teores de ThO₂ relativamente baixos (geralmente <2%), o que é uma "
            "vantagem para a extração química das terras raras, reduzindo a contaminação radioativa."
        )
        st.divider()

    # 2. Placeres e Paleoplaceres
    if "placeres" in deposito_str or "paleoplaceres" in deposito_str or "sedimentares" in deposito_str:
        st.markdown("## Placeres e Paleoplaceres (Depósitos Sedimentares de Superfície)")
        
        st.markdown("### Génese e Formação")
        st.success(
            "Devido à inércia geoquímica do Th⁴⁺ e à estabilidade da rede cristalina dos seus minerais "
            "(especialmente a monazite), o tório resiste à meteorização química. Através da meteorização mecânica, "
            "estes minerais densos e resistentes acumulam-se em aluviões, rios e zonas costeiras, formando depósitos de 'areias negras' ou prazeres."
        )
        
        st.divider()
        
        st.markdown("### Exploração e Processamento")
        st.info(
            "Estes constituem a principal fonte mundial de tório. A exploração foca-se "
            "em áreas de margem continental e bacias estáveis. O processamento utiliza a elevada densidade da monazite (>5 g/cm³) "
            "para a separação gravítica, seguida de métodos magnéticos e eletrostáticos para purificar o concentrado antes da lixiviação química."
        )
        st.divider()

    # 3. Terrenos e Sistemas Metamórficos
    if "metamórficos" in deposito_str or "metamorficos" in deposito_str:
        st.markdown("## Terrenos e Sistemas Metamórficos")
        
        st.markdown("### Génese e Formação")
        st.success(
            "O tório apresenta mobilidade durante o metamorfismo, tal como o potássio e o urânio. "
            "Os depósitos podem ser sedimentar-metamórficos ou de contacto-metassomático (skarns), onde o tório se concentra "
            "em migmatitos, gnaisses e xistos. A mineralização distribui-se frequentemente ao longo de planos de foliação, fraturas ou de forma disseminada."
        )
        
        st.divider()
        
        st.markdown("### Exploração e Processamento")
        st.info(
            "Estes recursos são menos desenvolvidos comercialmente do que os prazeres. "
            "Um exemplo notável de processamento histórico ocorreu em Steenkampskraal (África do Sul), onde se extraíram "
            "concentrados de monazite com teores entre 3,3% e 7,6% de Th."
        )
        st.divider()

    # 4. Granitos Evoluídos e Pegmatitos
    if "granitos" in deposito_str or "pegmatitos" in deposito_str:
        st.markdown("## Granitos Evoluídos e Pegmatitos")
        
        st.markdown("### Génese e Formação")
        st.success(
            "O tório concentra-se em magmas residuais tardios (leucogranitos e pegmatitos) "
            "devido ao seu grande raio iónico e carga elevada, que o impedem de entrar na estrutura dos minerais comuns de silicato. "
            "Nestes sistemas de alta temperatura, o tório e o urânio são frequentemente enriquecidos em simultâneo (sincronismo geoquímico)."
        )
        
        st.divider()
        
        st.markdown("### Exploração e Processamento")
        st.info(
            "Embora contenham grandes reservas, a maioria destes depósitos não tem "
            "importância comercial imediata, funcionando como reservas estratégicas para o futuro. O tório ocorre disseminado "
            "em minerais como a uraninite, thorite e monazite."
        )
        st.divider()

    # 5. Perfis de Alteração Residual
    if "alteração residual" in deposito_str or "alteracao" in deposito_str or "weathering" in deposito_str:
        st.markdown("## Perfis de Alteração Residual (Weathering Crusts)")
        
        st.markdown("### Génese e Formação")
        st.success(
            "Resultam da meteorização química intensa de rochas primárias (como carbonatitos) em climas tropicais. "
            "Enquanto elementos móveis como Ca e Mg são removidos, o tório e as terras raras permanecem concentrados no resíduo laterítico. "
            "Formam-se agregados porosos de monazite secundária e outros fosfatos."
        )
        
        st.divider()
        
        st.markdown("### Exploração e Processamento")
        st.info(
            "O depósito de Mt. Weld (Austrália) é o exemplo mais proeminente, sendo um "
            "dos depósitos de REE de maior teor no mundo. O processamento envolve a exploração a céu aberto, flotação para concentrar os minerais "
            "e, posteriormente, processos complexos de calcinação, conversão cáustica, lixiviação ácida e extração por solventes "
            "(geralmente utilizando extratantes organofosforados como o CYANEX 923)."
        )
        st.divider()

# ===============================
# 2. CONFUSÕES E MITOS
# ===============================

def mostrar_confusoes_torio():

    st.markdown("### ❌ Confusões e Mitos Frequentes")

    # Mito 1
    st.error("**Mito: O tório não é radioativo.**")
    st.success(
        "**Realidade:** O tório é um elemento radioativo natural de vida longa. Embora a sua radioatividade seja "
        "por vezes considerada 'ligeira', as preocupações com as emissões gama e os produtos de decaimento "
        "(como o 232U) são obstáculos significativos à sua utilização comercial e requerem manuseamento especializado."
    )
    
    st.divider()

    # Mito 2
    st.error("**Mito: O tório é físsil e pode ser usado diretamente como combustível.**")
    st.success(
        "**Realidade:** O tório (232Th) não é físsil, o que significa que não pode sustentar uma reação em cadeia por si só. "
        "Ele é um material fértil: precisa de absorver neutrões (geralmente de uma fonte externa de urânio ou plutónio) "
        "para se transmutar em 233U, que é o verdadeiro material físsil que gera energia."
    )
    
    st.divider()

    # Mito 3
    st.error("**Mito: A tecnologia nuclear de tório já está implementada à escala global.**")
    st.success(
        "**Realidade:** Atualmente, não existem reatores nucleares à escala industrial que utilizem tório em operação comercial "
        "no mundo. Embora tenham existido protótipos experimentais desde meados do século XX e a Índia continue a operar "
        "reatores experimentais e a desenvolver o seu programa, a tecnologia ainda é considerada emergente e de fase de pesquisa "
        "em muitos países."
    )
    
    st.divider()

    # Mito 4
    st.error("**Mito: O tório não tem outras aplicações além da energia nuclear.**")
    st.success(
        "**Realidade:** Apesar de o seu potencial nuclear ser o mais discutido, o tório tem sido utilizado há muito tempo "
        "em diversas indústrias de ponta. Ele é empregado no fabrico de ligas aeroespaciais de alta temperatura, "
        "catalisadores químicos, elétrodos de soldadura e cerâmicas resistentes ao calor. Historicamente, também foi "
        "fundamental na produção de mantas para lanternas incandescentes."
    )


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
