import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_uranio(deposito=""):

    st.markdown("### ☢️ Características do Urânio e Tório")

    st.markdown("#### 🌍 5 Características Gerais do Recurso")
    
    with st.expander("🔍 Ver características gerais", expanded=True):
        st.markdown("**1. Potencial Energético e Estratégico:** Tanto o urânio como o tório são elementos radioativos naturais fundamentais para a geração de energia nuclear. O tório é considerado um combustível promissor para o futuro devido à sua maior abundância, segurança intrínseca e menor produção de resíduos nucleares de vida longa.")
        st.markdown("**2. Abundância Crostal:** O tório é cerca de três vezes mais abundante na crosta terrestre do que o urânio. A abundância média na crosta continental superior é de aproximadamente 10,5 ppm para o tório e 2,7 ppm para o urânio.")
        st.markdown("**3. Comportamento Geoquímico e Solubilidade:** A formação de depósitos de urânio é controlada pela sua solubilidade: é altamente móvel em condições oxidantes (U6+) e precipita em condições redutoras (U4+). O tório, pelo contrário, é geoquimicamente inerte e muito pouco solúvel na maioria das águas naturais, não possuindo um estado oxidado móvel como o urânio.")
        st.markdown("**4. Isótopos Naturais:** O urânio natural consiste principalmente em 238U (99,3%) e 235U (0,7%), o único isótopo físsil em reatores convencionais. O tório natural é composto quase inteiramente pelo isótopo 232Th, que pode ser transmutado em 233U físsil.")
        st.markdown("**5. Tipos Genéticos de Depósitos:** Os recursos globais estão classificados em três grandes categorias de génese: ígneos (magmáticos), metamórficos e sedimentares (incluindo depósitos de prazeres e em arenitos).")

    st.divider()

    if deposito:
        st.markdown(f"#### 🔎 Características Específicas: {deposito}")

        if "unconformity" in deposito.lower():
            st.markdown("- **Localização Estratigráfica:** Situam-se especificamente na interface (discordância) entre um soco metamórfico (geralmente Arcaico a Paleoproterozoico) e uma bacia sedimentar proterozoica rica em arenitos vermelhos (redbeds).")
            st.markdown("- **Teores Excecionalmente Elevados:** Estes depósitos possuem os teores de urânio mais altos do mundo, com algumas zonas a atingirem mais de 20% de U, como se verifica nos depósitos de Cigar Lake e McArthur River no Canadá.")
            st.markdown("- **Associação com Grafite:** A mineralização está frequentemente associada a condutores grafíticos e zonas de cisalhamento no soco, que funcionam como agentes redutores cruciais para a precipitação do urânio.")
            st.markdown("- **Halos de Alteração Hidrotermal:** Caracterizam-se por halos de alteração extensos contendo minerais como ilite, clorite (sudoíte), caulinite e dravite, que servem como guias para a exploração.")
            st.markdown("- **Mineralogia e Forma:** Ocorrem tipicamente como lentes sub-horizontais, filões ou preenchimentos de brecha, dominados por uraninita (pechblenda) massiva a disseminada.")

        elif "arenitos" in deposito.lower():
            st.markdown("- **Hospedeiro e Permeabilidade:** São depósitos epigenéticos hospedados em arenitos de grão médio a grosseiro, caracterizados por alta porosidade e permeabilidade, o que permite a circulação de fluidos mineralizantes.")
            st.markdown("- **Mecanismo de Frente de Redox:** A mineralização concentra-se em \"frentes de oxirredução\", onde águas oxidantes que transportam urânio dissolvido encontram ambientes redutores, forçando a precipitação da uraninita ou coffinite.")
            st.markdown("- **Variedade Morfológica:** Dividem-se em subtipos principais baseados na forma: roll-front (em forma de crescente), tabulares (horizontais e paralelos à estratificação) e de canal basal (paleocanais).")
            st.markdown("- **Papel da Matéria Orgânica:** Dependem frequentemente da presença de agentes redutores intrínsecos como restos de plantas fossilizadas, matéria carbonosa ou pirite diagenética para fixar o urânio.")
            st.markdown("- **Idade e Ambiente:** A maioria destes depósitos é do Silúrico ou mais recente, refletindo a evolução das plantas terrestres como principal redutor, embora existam exemplos proterozoicos ligados à migração de hidrocarbonetos.")

        elif "hidrotermais" in deposito.lower():
            st.markdown("- **Natureza dos Fluidos:** Envolvem o movimento de fluidos quentes e frequentemente salinos (brinas diagenéticas ou fluidos magmáticos) com temperaturas entre 70°C e 250°C.")
            st.markdown("- **Controlo Estrutural em Veios:** A mineralização apresenta-se geralmente sob a forma de filões (veios), zonas de fratura ou preenchimento de brechas, frequentemente associados a falhas regionais ou zonas de cisalhamento.")
            st.markdown("- **Complexidade Mineralógica:** Frequentemente contêm associações complexas de urânio, tório e elementos de terras raras (REE), refletindo a mobilidade simultânea destes elementos a altas temperaturas.")
            st.markdown("- **Associação com Rochas Alcalinas:** Estão muitas vezes ligados a complexos ígneos alcalinos e carbonatitos, onde os fluidos hidrotermais concentram metais extraídos das rochas circundantes.")
            st.markdown("- **Presença de Mineralizadores:** Os fluidos mineralizantes são frequentemente ricos em componentes como CO2, flúor (F), cloro (Cl) e H2S, que auxiliam no transporte e posterior precipitação dos minerais de tório e urânio.")

    else:
        st.info("Selecione um tipo de depósito na barra lateral para visualizar as características específicas.")


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
