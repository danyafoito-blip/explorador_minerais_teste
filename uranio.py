import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_uranio(deposito):

    st.markdown("### ☢️ Características do Urânio")

    col1, col2 = st.columns(2)

    # Verificação de segurança
    if not deposito:
        st.warning("Por favor, seleciona um tipo de depósito para visualizar as características.")
        return

    if isinstance(deposito, list):
        deposito = ", ".join(deposito)
    
    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- Elementos radioativos (U, Th)")
        st.write("- Elevada densidade")
        st.write("- Radioatividade e Decaimento Natural")
        st.write("- Comportamento de Elemento Incompatível")
        st.write("- Sensibilidade Redox e Solubilidade Variável")

    with col2:

        st.info("**Importância Energética**")

        st.write("- Combustível para energia nuclear")
        st.write("- Geração de Eletricidade em Larga Escala")
        st.write("- Baixas emissões de CO₂")
        st.write("- Estabilidade de Custos e Competitividade")
        st.write("- Sustentabilidade de Longo Prazo")
    
    st.divider()

# 1. Arenitos
    if "Arenitos" in deposito:
        st.markdown("## Depósitos em Arenitos (Sandstone-hosted)")
        
        st.success(
            "Representam uma grande parte da produção mundial (ex: Cazaquistão, EUA). Ocorrem em rochas sedimentares clásticas de grão médio a grosseiro."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.warning(
            "Formam-se pela dinâmica de fluidos: águas subterrâneas oxidantes ricas em urânio atravessam aquíferos permeáveis."
        )
        st.write("- A precipitação ocorre quando o fluido encontra uma **barreira redutora** (matéria orgânica, pirite, gás sulfídrico).")
        st.write("- Morfologia clássica em forma de meia-lua ou crescente, conhecida como **'Roll-front'**.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Vantagens:**")
            st.write("- Maioritariamente extraídos por **ISR** (In-Situ Recovery).")
            st.write("- Baixo custo de capital (CAPEX) e impacto visual superficial mínimo.")
        with col2:
            st.markdown("**Desafios:**")
            st.write("- Exige hidrogeologia altamente controlada para evitar contaminação de aquíferos.")
            st.write("- Teores tipicamente baixos a moderados.")

    # 2. Discordâncias
    elif "Discordâncias" in deposito or "Unconformity" in deposito:
        st.markdown("## Depósitos Relacionados com Discordâncias (Unconformity-related)")
        
        st.success(
            "Famosos pelos depósitos da Bacia de Athabasca (Canadá) e Alligator Rivers (Austrália). São os depósitos com os **teores mais elevados do mundo**."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.info(
            "Ocorrem no contacto espacial entre bacias sedimentares proterozoicas e o soco metamórfico/ígneo mais antigo (a discordância)."
        )
        st.write("- Resultam da mistura de salmouras oxidantes da bacia com fluidos redutores provenientes do soco.")
        st.write("- Estão frequentemente associados a zonas de falha com litologias ricas em grafite (que atuam como condutores e redutores).")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.error(
            "Devido aos teores extremos (que podem ultrapassar os 20% de Urânio), exigem métodos de mineração altamente especializados."
        )
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Características:**")
            st.write("- Menor volume de minério necessário para grande produção.")
        with col2:
            st.markdown("**Desafios:**")
            st.write("- Risco de radiação extremo (exige ventilação massiva e equipamento telecomandado).")
            st.write("- Necessidade de congelar artificialmente as rochas envolventes para evitar inundações nas minas.")

    # 3. Intrusivos e Magmáticos
    elif "Intrusivos e Magmáticos" in deposito:
        st.markdown("## Depósitos Intrusivos e Magmáticos")
        
        st.success(
            "Depósitos associados à cristalização direta de magmas ou fluidos tardi-magmáticos. Exemplos incluem os alaskitos de Rössing (Namíbia)."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.warning(
            "Sendo o urânio um elemento altamente incompatível, não se integra nos minerais comuns durante a cristalização magmática inicial."
        )
        st.write("- Concentra-se nas fases finais da diferenciação magmática (magmas residuais).")
        st.write("- Ocorre em rochas como granitos muito evoluídos, pegmatitos, sienitos ou carbonatitos.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Características:**")
            st.write("- Operações de grande escala, geralmente a céu aberto.")
            st.write("- Minério muito homogéneo em grandes volumes.")
        with col2:
            st.markdown("**Desafios:**")
            st.write("- Teores muito baixos (frequentemente < 0.05% U).")
            st.write("- Requer o processamento de enormes quantidades de rocha.")

    # 4. Hidrotermal e Metassomática
    elif "Hidrotermal e Metassomática" in deposito:
        st.markdown("## Depósitos de Origem Hidrotermal e Metassomática")
        
        st.success(
            "Incluem sistemas clássicos de filões (veios) de quartzo-carbonato-uraninita e depósitos complexos como os skarns."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.info(
            "Formados pela circulação de fluidos quentes (hidrotermais) ao longo de fraturas, falhas ou zonas de cisalhamento na rocha hospedeira."
        )
        st.write("- A alteração metassomática altera quimicamente a rocha encaixante (ex: depósitos de alteração albitítica).")
        st.write("- Podem estar intimamente ligados a fluidos derivados de magmas ou águas de formação aquecidas profundamente.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- Historicamente muito importantes (ex: minas europeias no Maciço Ibérico e da Boémia).")
        st.write("- Mineração predominantemente subterrânea.")
        st.write("- Podem ser depósitos polimetálicos, onde o urânio é recuperado com outros metais (ex: Ag, Co, Ni).")

    # 5. Superficiais e Sedimentares Específicos
    elif "Superficiais e Sedimentares" in deposito:
        st.markdown("## Depósitos Superficiais e Sedimentares Específicos")
        
        st.success(
            "Depósitos formados perto da superfície terrestre em ambientes sedimentares recentes. Inclui depósitos em calcretos, fosforitos e xistos negros."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Depósitos em Calcreto:**")
            st.write("- Típicos de climas áridos (ex: Austrália Ocidental, Namíbia).")
            st.write("- Águas ricas em urânio e vanádio evaporam em paleocanais, precipitando carnotite.")
        with col2:
            st.markdown("**Fosforitos e Xistos Negros:**")
            st.write("- Ambientes marinhos redutores (anóxicos).")
            st.write("- O urânio adsorve na matéria orgânica ou substitui o cálcio na apatite.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.warning(
            "A viabilidade económica destes depósitos é muito sensível ao preço de mercado do urânio."
        )
        st.write("- Calcretos: Extração fácil, a céu aberto, mas com teores marginais.")
        st.write("- Fosforitos: O urânio é geralmente extraído como **subproduto** da indústria de fertilizantes fosfatados.")

    # 6. Brechas
    elif "Brechas" in deposito or "Breccia" in deposito:
        st.markdown("## Depósitos em Brechas (Breccia-pipe)")
        
        st.success(
            "Estruturas geológicas cilíndricas ou em forma de tubo preenchidas com fragmentos de rocha colapsada (brecha), famosas no planalto do Colorado (EUA)."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.info(
            "Resultam de colapsos cársicos: a dissolução de calcários profundos cria cavernas, e as rochas sedimentares sobrejacentes desabam para o seu interior."
        )
        st.write("- Estes 'tubos' verticais tornam-se condutas altamente permeáveis para a circulação de fluidos minerais.")
        st.write("- O urânio precipita ao encontrar barreiras redutoras nestes tubos.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Vantagens:**")
            st.write("- Apresentam frequentemente **teores muito elevados**.")
            st.write("- Ocupam uma área de superfície (pegada) extremamente pequena.")
        with col2:
            st.markdown("**Desafios:**")
            st.write("- Difíceis de encontrar na prospeção ('agulha num palheiro').")
            st.write("- Volumes totais de minério por cada tubo são relativamente pequenos.")

    else:
        st.info("Selecione um tipo de depósito válido para visualizar a informação.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

# ===============================
# 2. CONFUSÕES COMUNS E DISTINÇÕES
# ===============================

def mostrar_confusoes_uranio(deposito=""):

    st.markdown("### ⚠️ Pontos de Distinção e Confusão: Urânio e Tório")

    st.markdown("#### 🌍 5 Pontos Gerais de Distinção e Confusão")

    with st.expander("🔍 Ver pontos gerais", expanded=True):
        st.markdown("**1. Morfologia vs. Génese:** Depósitos situados no mesmo ambiente sedimentar (ex: paleocanais) e com formas semelhantes (ex: tabulares) podem ter mecanismos de formação completamente diferentes, o que pode induzir em erro durante a exploração.")
        st.markdown("**2. Temperatura e Salinidade dos Fluidos:** A principal forma de distinguir sistemas meteóricos de sistemas hidrotermais/diagenéticos é através da temperatura (fluidos meteóricos <50°C vs. brinas quentes 70-250°C) e da salinidade (baixa em águas meteóricas vs. alta em brinas diagenéticas).")
        st.markdown("**3. Origem do Redutor:** Existe confusão entre redutores intrínsecos (como matéria orgânica vegetal depositada com o sedimento) e extrínsecos (como hidrocarbonetos ou gases sulfídricos que migraram de outras zonas), sendo que ambos podem criar depósitos de aparência similar.")
        st.markdown("**4. Evolução Atmosférica:** A distinção temporal é vital; depósitos hidrotermais de urânio só se tornaram possíveis após a oxigenação da atmosfera (~2,4 Ga), permitindo o transporte de U6+ solúvel, enquanto antes disso o urânio era transportado mecanicamente como detrito.")
        st.markdown("**5. Metamorfismo:** Muitos depósitos classificados como \"metamórficos\" são, na verdade, depósitos em arenitos que sofreram metamorfismo posterior, mantendo muitas vezes a sua natureza redutora original.")

    st.divider()

    if deposito:
        st.markdown(f"#### 🔎 Distinções Específicas: {deposito}")

        if "unconformity" in deposito.lower():
            st.markdown("**1. Localização Estratigráfica:** Ocorrem especificamente na interface entre um soco metamórfico (geralmente do Arcaico ao Paleoproterozoico) e uma cobertura sedimentar proterozoica rica em arenitos vermelhos.")
            st.markdown("**2. Teores Excecionais:** Distinguem-se por possuírem os teores mais elevados do mundo (chegando a mais de 20% de U), muito superiores aos depósitos típicos em arenitos.")
            st.markdown("**3. Controladores Estruturais:** Estão quase sempre associados a falhas reativadas e a condutores grafíticos no soco, que funcionam como agentes redutores ou caminhos para fluidos.")

        elif "arenitos" in deposito.lower():
            st.markdown("**1. Dependência Biológica:** Estão maioritariamente restritos a rochas do Silúrico ou mais recentes, devido à necessidade de matéria orgânica proveniente de plantas terrestres vasculares para atuar como redutor.")
            st.markdown("**2. Morfologias Clássicas:** Dividem-se principalmente em tipos roll-front (em forma de crescente, cruzando a estratigrafia) e tabulares (paralelos à deposição), controlados pela permeabilidade do arenito.")
            st.markdown("**3. Fronteiras de Redox:** A mineralização ocorre tipicamente na transição entre uma zona oxidada (frequentemente avermelhada/amarelada) e uma zona reduzida (cinzenta/preta) dentro do aquífero.")

        elif "hidrotermais" in deposito.lower():
            st.markdown("**1. Origem dos Fluidos:** Ao contrário dos depósitos sedimentares puros, estes envolvem fluidos de origem magmática ou do manto, ricos em mineralizadores como CO2 e H2S.")
            st.markdown("**2. Associações Minerais Complexas:** Frequentemente contêm tório (Th) e elementos de terras raras (REE), que se enriquecem sincronamente em condições de alta temperatura, algo raro em depósitos sedimentares de baixa temperatura.")
            st.markdown("**3. Controlo Estrutural em Veios:** Apresentam-se geralmente como veios, preenchimentos de fraturas ou zonas de brecha, muitas vezes associados a complexos alcalinos ou carbonatitos.")

    else:
        st.info("Selecione um tipo de depósito na barra lateral para ver as distinções específicas.")



# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_uranio():

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

def checklist_uranio():

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

def mapa_uranio():

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

def referencias_uranio():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- IAEA – Uranium Resources and Production")
    st.write("- OECD NEA – Uranium Reports (Red Book)")
    st.write("- World Nuclear Association")
    st.write("- Dahlkamp – Uranium Deposits of the World")
    st.write("- USGS – Uranium and Thorium Resources")

    st.caption("Fontes científicas e institucionais sobre urânio e tório.")
