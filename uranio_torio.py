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

def quiz_uranio(deposito=""):

    st.markdown("### 🧠 Quiz Interativo: Urânio e Tório")
    st.write("Testa os teus conhecimentos sobre a geologia e exploração destes combustíveis nucleares! 👇")

    # --- PARTE 1: QUESTÕES GERAIS ---
    st.markdown("#### 🌍 Questões Gerais")
    
    with st.expander("📝 Mostrar Questões Gerais", expanded=True):
        # Q1 (Tua Q1)
        q1 = st.radio(
            "1️⃣ Em termos de abundância na crosta continental superior, qual é a relação aproximada entre o tório e o urânio?",
            [
                "A) O urânio é o dobro do tório.", 
                "B) O tório é cerca de 3 a 4 vezes mais abundante que o urânio.", 
                "C) Ambos possuem a mesma abundância (2,7 ppm).", 
                "D) O tório é 100 vezes mais abundante."
            ],
            key="ura_geral_q1"
        )
        if st.button("Verificar Q1", key="btn_ug1"):
            if q1.startswith("B)"):
                st.success("Correto! ✅ O tório (aprox. 10,5 ppm) é cerca de 3 a 4 vezes mais abundante que o urânio (aprox. 2,7 ppm).")
            else:
                st.error("Incorreto. ❌ Lembra-te que o tório é significativamente mais comum.")

        st.divider()

        # Q2 (Tua Q2)
        q2 = st.radio(
            "2️⃣ O urânio é geoquimicamente móvel e solúvel em águas naturais quando se encontra em qual estado de oxidação?",
            [
                "A) Estado tetravalente (U4+).", 
                "B) Estado hexavalente (U6+) sob condições oxidantes.", 
                "C) Estado metálico.", 
                "D) O urânio nunca é solúvel em água."
            ],
            key="ura_geral_q2"
        )
        if st.button("Verificar Q2", key="btn_ug2"):
            if q2.startswith("B)"):
                st.success("Correto! ✅ É a oxidação para U6+ que permite ao urânio dissolver-se e viajar nos fluidos.")
            else:
                st.error("Incorreto. ❌ Pensa nas condições necessárias para formar iões solúveis (uranilo).")

        st.divider()

        # Q3 (Tua Q5)
        q3 = st.radio(
            "3️⃣ Qual é o mineral de fosfato que constitui a principal fonte de tório em depósitos sedimentares do tipo 'prazeres' (placers)?",
            [
                "A) Uraninita.", 
                "B) Monazite.", 
                "C) Quartzo.", 
                "D) Pirite."
            ],
            key="ura_geral_q3"
        )
        if st.button("Verificar Q3", key="btn_ug3"):
            if q3.startswith("B)"):
                st.success("Correto! ✅ A monazite é um fosfato de terras raras e tório muito resistente, acumulando-se em areias de praia e rios.")
            else:
                st.error("Incorreto. ❌ Tenta novamente!")

    st.write("") # Espaçamento

    # --- PARTE 2: QUESTÕES ESPECÍFICAS ---
    if deposito:
        st.markdown(f"#### 🔎 Questões Específicas: {deposito}")

        if "unconformity" in deposito.lower():
            # Unconformity Q1 (Tua Q4)
            q_unc1 = st.radio(
                "Os depósitos de urânio do tipo 'Unconformity' (Discordância), como os da Bacia de Athabasca no Canadá, são mundialmente conhecidos por:",
                [
                    "A) Terem os teores mais elevados do mundo, por vezes excedendo 20% de U.", 
                    "B) Ocorrerem apenas em rochas vulcânicas jovens.", 
                    "C) Serem pobres em minério mas fáceis de extrair.", 
                    "D) Não necessitarem de agentes redutores para a precipitação."
                ],
                key="ura_unc_q1"
            )
            if st.button("Verificar Resposta 1", key="btn_uu1"):
                if q_unc1.startswith("A)"):
                    st.success("Correto! ✅ São depósitos de classe mundial devido aos seus teores excecionalmente altos.")
                else:
                    st.error("Incorreto. ❌ Tenta novamente!")
            
            st.divider()

            # Unconformity Q2 (Tua Q6)
            q_unc2 = st.radio(
                "Nos depósitos de discordância, a precipitação do urânio ocorre geralmente quando fluidos oxidantes encontram uma barreira redutora. No soco metamórfico, um alvo comum é:",
                [
                    "A) Ouro nativo.", 
                    "B) Condutores grafíticos (metapelitos com grafite).", 
                    "C) Camadas de sal-gema.", 
                    "D) Granitos pobres em ferro."
                ],
                key="ura_unc_q2"
            )
            if st.button("Verificar Resposta 2", key="btn_uu2"):
                if q_unc2.startswith("B)"):
                    st.success("Correto! ✅ O grafite atua como um excelente agente redutor, forçando a precipitação do urânio.")
                else:
                    st.error("Incorreto. ❌ Pensa num material rico em carbono.")

        elif "arenitos" in deposito.lower():
            # Arenitos Q1 (Tua Q3)
            q_are1 = st.radio(
                "Qual é a morfologia característica de um depósito de urânio em arenito do tipo 'roll-front' quando observado em corte transversal?",
                [
                    "A) Uma esfera perfeita.", 
                    "B) Uma forma de crescente ou meia-lua que corta a estratigrafia.", 
                    "C) Um cilindro vertical estreito.", 
                    "D) Uma camada tabular perfeitamente paralela ao leito."
                ],
                key="ura_are_q1"
            )
            if st.button("Verificar Resposta", key="btn_ua1"):
                if q_are1.startswith("B)"):
                    st.success("Correto! ✅ A frente de oxirredução avança pelo aquífero criando esta típica forma em crescente ('roll-front').")
                else:
                    st.error("Incorreto. ❌ Tenta novamente!")

        elif "hidrotermais" in deposito.lower():
            # Hidrotermais Q1 (Adaptada da tua Q6 que menciona hidrotermais)
            q_hid1 = st.radio(
                "Nos depósitos hidrotermais, a precipitação do urânio ocorre geralmente quando fluidos encontram uma barreira redutora. Qual destes pode ser um alvo estrutural/redutor?",
                [
                    "A) Ouro nativo.", 
                    "B) Condutores grafíticos ou zonas de cisalhamento com fluidos redutores.", 
                    "C) Camadas de sal-gema puros.", 
                    "D) Granitos estéreis."
                ],
                key="ura_hid_q1"
            )
            if st.button("Verificar Resposta", key="btn_uh1"):
                if q_hid1.startswith("B)"):
                    st.success("Correto! ✅ A interação com grafite ou mistura com fluidos redutores (ex: com H2S) em falhas provoca a precipitação.")
                else:
                    st.error("Incorreto. ❌ Tenta novamente!")

    else:
        st.info("Selecione um tipo de depósito na barra lateral para ver as questões específicas deste ambiente.")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_uranio(deposito=""):

    st.markdown("### ✅ Checklist de Campo e Identificação (Urânio e Tório)")
    st.write("Critérios práticos para identificação de amostras e depósitos no campo ou laboratório:")

    # --- CHECKLIST GERAL ---
    st.markdown("#### 🌍 Checklist Geral do Recurso")
    
    with st.expander("🔍 Ver checklist geral", expanded=True):
        st.checkbox("**Radioatividade Detetável:** Presença de emissões gama que podem ser identificadas com contadores Geiger ou cintilómetros no campo ou museu.", key="chk_ura_geral_1")
        st.checkbox("**Densidade Elevada:** Minerais primários de urânio, como a uraninite, são extremamente densos e pesados (densidade ~9-10 g/cm³), destacando-se de rochas comuns.", key="chk_ura_geral_2")
        st.checkbox("**Cores Vibrantes de Minerais Secundários:** Presença de minerais de oxidação de cores intensas, como o amarelo néon (carnotite/autunite) ou verde maçã (torbernite), frequentemente associados a zonas de alteração superficial.", key="chk_ura_geral_3")
        st.checkbox("**Abundância Relativa e Brilho:** O tório é 3 a 4 vezes mais abundante que o urânio e ocorre frequentemente em minerais com brilho resinoso ou ceroso, como a monazite (amarelo-mel a castanho) e a thorite (vermelho a preto).", key="chk_ura_geral_4")
        st.checkbox("**Controlo Redox:** Evidência de mudanças de estado de oxidação, onde o urânio precipita em ambientes reduzidos (escuros/cinzentos) após ser transportado em soluções oxidadas.", key="chk_ura_geral_5")

    st.divider()

    # --- CHECKLIST ESPECÍFICA ---
    if deposito:
        st.markdown(f"#### 🔎 Checklist Específica: {deposito}")

        if "unconformity" in deposito.lower():
            st.checkbox("**Interface Geológica Marcante:** Observação do contacto (discordância) entre um soco metamórfico altamente deformado (gneisses/xistos) e uma bacia de cobertura de arenitos proterozoicos horizontais.", key="chk_ura_unc_1")
            st.checkbox("**Presença de Grafite:** Alvos de minério frequentemente associados a metapelitos grafíticos (condutores eletrónicos) no soco metamórfico.", key="chk_ura_unc_2")
            st.checkbox("**Teores Excecionalmente Elevados:** Amostras de museu podem exibir minério maciço de uraninite (pechblenda botrioidal ou fuliginosa) com teores que excedem 20%, por vezes até 50% de U.", key="chk_ura_unc_3")
            st.checkbox("**Alteração Argilosa e Hematítica:** Presença de halos de alteração extensos compostos por ilite, sudoíte (clorite de magnésio) e dravite (turmalina rica em boro) que rodeiam o minério.", key="chk_ura_unc_4")
            st.checkbox("**Texturas de Substituição e Brecha:** Minério que preenche fraturas ou substitui a matriz do arenito logo acima ou abaixo da discordância.", key="chk_ura_unc_5")

        elif "arenitos" in deposito.lower():
            st.checkbox("**Morfologias Roll-Front ou Tabulares:** Corpos de minério em forma de crescente (roll-front) que cortam a estratigrafia ou camadas planas (tabular) paralelas à deposição.", key="chk_ura_are_1")
            st.checkbox("**Zonamento de Cores Redox:** Transição visível entre arenitos oxidados (vermelhos/amarelos por hematite/limonite) e arenitos reduzidos (cinzentos por pirite e matéria orgânica).", key="chk_ura_are_2")
            st.checkbox("**Redutores Orgânicos Visíveis:** Presença de restos de plantas carbonizadas, madeira fossilizada, troncos silicificados ou impregnações de betume/hidrocarbonetos que serviram para precipitar o urânio.", key="chk_ura_are_3")
            st.checkbox("**Permeabilidade da Rocha Hospedeira:** Ocorrência em arenitos de grão médio a grosseiro, frequentemente com cimento de calcite ou sílica, evidenciando o antigo fluxo de águas subterrâneas.", key="chk_ura_are_4")
            st.checkbox("**Associações de Minerais de Baixa Temperatura:** Disseminações finas de coffinite e uraninite na matriz arenosa, muitas vezes invisíveis a olho nu sem radiação.", key="chk_ura_are_5")

        elif "hidrotermais" in deposito.lower():
            st.checkbox("**Preenchimento de Fraturas (Veios):** Mineralização que ocorre em filões, zonas de cisalhamento ou brechas tectónicas, cruzando as estruturas da rocha encaixante.", key="chk_ura_hid_1")
            st.checkbox("**Associação com Rochas Alcalinas:** Hospedados em complexos ígneos alcalinos ou carbonatitos (rochas ricas em carbonatos como dolomite e calcite de origem ígnea).", key="chk_ura_hid_2")
            st.checkbox("**Complexidade Mineralógica REE-Th:** Presença simultânea de minerais de Terras Raras (como bastnaesite) e tório (como monazite e thorite), típica de sistemas de alta temperatura.", key="chk_ura_hid_3")
            st.checkbox("**Minerais Indicadores (Mineralizadores):** Presença comum de fluorite (roxo/verde), barite e carbonatos que atuaram como agentes de transporte nos fluidos hidrotermais.", key="chk_ura_hid_4")
            st.checkbox("**Halos de Alteração Potássica/Sódica:** Evidência de metasomatismo nas rochas encaixantes, com formação de novos feldspatos (albitização) ou micas.", key="chk_ura_hid_5")

    else:
        st.info("Selecione um tipo de depósito na barra lateral para ver a checklist específica.")


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
