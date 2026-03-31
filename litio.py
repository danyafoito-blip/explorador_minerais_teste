import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_litio(deposito):

    st.markdown("### Características do Lítio")

    col1, col2 = st.columns(2)

    with col1:
        st.success("**Propriedades Físicas e Químicas**")
        st.write("- É o metal mais leve da Tabela Periódica")
        st.write("- Elevado potencial eletroquímico e calor específico")
        st.write("- Altamente reativo e inflamável (não ocorre livre na natureza)")
        st.write("- Excelente condutividade elétrica")

    with col2:
        st.info("**Importância Energética**")
        st.write("- Elemento central na transição energética global")
        st.write("- Crucial para o fabrico de baterias de iões de lítio")
        st.write("- Utilizado em ligas metálicas leves (setor aeroespacial)")
        st.write("- Aplicações importantes na indústria vidreira e cerâmica")

    st.divider()

    if "Pegmatitos (rocha dura)" in deposito:

        st.markdown("## Pegmatitos (Rocha Dura)")
    
        st.success(
            "Depósitos de rocha dura formados através da cristalização fracionada de magmas graníticos, "
            "onde o lítio se concentra nas fases finais (fluidos residuais)."
        )
    
        st.divider()
    
        st.markdown("## Mineralogia Principal")
    
        with st.container():
            st.info(
                "O lítio nestes depósitos encontra-se inserido na estrutura cristalina de minerais específicos."
            )
    
            col1, col2 = st.columns(2)
    
            with col1:
                st.markdown("**Mineral Principal:**")
                st.write("- **Espodumena:** O mineral de lítio mais comum e explorado em rocha dura.")
    
            with col2:
                st.markdown("**Outros Minerais Comuns:**")
                st.write("- Petalite")
                st.write("- Lepidolite")
    
        st.divider()
    
        st.markdown("## Génese e Formação")
    
        st.warning(
            "O lítio, sendo um elemento incompatível, não se integra facilmente nos minerais que cristalizam primeiro "
            "num magma, acumulando-se no líquido magmático residual."
        )
        
        st.write("- Ocorrem geralmente na forma de filões (veios) intrusivos em rochas encaixantes mais antigas.")
        st.write("- Associados a granitos do tipo LCT (Lítio, Césio e Tântalo).")
    
        st.divider()
    
        st.markdown("## Exploração e Processamento")
    
        st.error(
            "Requer mineração tradicional (céu aberto ou subterrânea), seguida de processamento intensivo."
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("**Vantagens:**")
            st.write("- Processamento mais rápido que as salmouras")
            st.write("- Teores de lítio geralmente mais elevados")
    
        with col2:
            st.markdown("**Desafios:**")
            st.write("- Custos operacionais (OPEX) mais elevados")
            st.write("- Processos de britagem, moagem e flotação intensivos em energia")

    elif "Salmouras continentais" in deposito:

        st.markdown("## Salmouras Continentais")
    
        st.success(
            "Depósitos líquidos onde o recurso se encontra dissolvido em águas subterrâneas hipersalinas (salmouras), "
            "geralmente localizados por baixo da crosta de sal em bacias endorreicas (salares)."
        )
    
        st.divider()
    
        st.markdown("## Génese e Formação")
    
        with st.container():
            st.info(
                "Resultam da lixiviação contínua de rochas vulcânicas ricas em lítio ao longo de milhões de anos."
            )
    
            col1, col2 = st.columns(2)
    
            with col1:
                st.markdown("**Requisitos Geológicos:**")
                st.write("- Bacias endorreicas (sem saída para o mar)")
                st.write("- Atividade vulcânica prévia/recente")
    
            with col2:
                st.markdown("**Requisitos Climáticos:**")
                st.write("- Clima extremamente árido")
                st.write("- Taxa de evaporação muito superior à precipitação")
    
        st.divider()
    
        st.markdown("## Características do Reservatório")
    
        st.warning(
            "Tal como nos hidrocarbonetos, as salmouras requerem uma rocha reservatório com porosidade e permeabilidade "
            "suficientes para permitir o bombeamento."
        )
        
        st.write("- O aquífero pode ser composto por halite fraturada, areias, cascalhos ou argilas.")
        st.write("- A dinâmica de fluidos é essencial para não diluir a salmoura com águas doces superficiais.")
    
        st.divider()
    
        st.markdown("## Exploração e Processamento")
    
        st.error(
            "Extração feita através de bombagem da salmoura para a superfície, seguida de evaporação solar."
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("**Vantagens:**")
            st.write("- Menor custo de produção (OPEX)")
            st.write("- Menor intensidade carbónica na extração inicial")
    
        with col2:
            st.markdown("**Desafios:**")
            st.write("- Tempo de processamento longo (12 a 24 meses em tanques)")
            st.write("- Desafios ambientais (consumo e gestão hídrica)")

    elif "Argilas ricas em lítio" in deposito:

        st.markdown("## Argilas Ricas em Lítio")
    
        st.success(
            "Recurso não convencional e emergente onde o lítio se encontra fixado na estrutura lamelar de minerais de argila, "
            "frequentemente depositados em bacias sedimentares de antigos lagos vulcânicos."
        )
        
        st.divider()
    
        st.markdown("## Mineralogia Principal")
    
        with st.container():
            st.info(
                "Diferente dos pegmatitos, o lítio está ligado a minerais de grão muito fino."
            )
    
            col1, col2 = st.columns(2)
    
            with col1:
                st.markdown("**Argilas Comuns:**")
                st.write("- Hectorite")
                st.write("- Esmectite")
    
            with col2:
                st.markdown("**Outros associados:**")
                st.write("- Jadarite (mineral de borossilicato encontrado na Sérvia)")
    
        st.divider()
    
        st.markdown("## Génese e Formação")
    
        st.warning(
            "Associadas à alteração hidrotermal ou meteórica de cinzas vulcânicas ricas em lítio."
        )
        
        st.write("- O lítio é mobilizado e posteriormente fixado nas estruturas das argilas durante a diagénese.")
        st.write("- Frequentemente encontradas em antigas caldeiras vulcânicas.")

        st.divider()
    
        st.markdown("## Exploração e Processamento")
    
        st.error(
            "A extração envolve mineração a céu aberto, mas a metalurgia é mais complexa e ainda está em fase de escalonamento."
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("**Características do Depósito:**")
            st.write("- Grandes volumes de minério disponíveis")
            st.write("- Teores intermédios (menores que pegmatitos, maiores que salmouras)")
    
        with col2:
            st.markdown("**Desafios:**")
            st.write("- Requer lixiviação ácida intensiva para libertar o lítio da argila")
            st.write("- Gestão de resíduos (tailings) e elevado consumo de reagentes")

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
