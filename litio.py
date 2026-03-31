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
        st.write("- Metal mais leve da Tabela Periódica")
        st.write("- Elevado potencial eletroquímico")
        st.write("- Altamente reativo e inflamável")
        st.write("- Excelente condutividade elétrica")

    with col2:
        st.info("**Importância Energética**")
        st.write("- Elemento central na transição energética")
        st.write("- Crucial para o fabrico de baterias de iões de lítio")
        st.write("- Utilizado em ligas metálicas leves)")
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



import streamlit as st

def quiz_litio(deposito=None):
    # Verificação de segurança para evitar TypeError se o argumento for None ou vazio
    if not deposito:
        st.warning("Por favor, seleciona um tipo de depósito para carregar o quiz.")
        return

    # Se for uma lista (caso uses st.multiselect no futuro), junta tudo numa string
    if isinstance(deposito, list):
        deposito = ", ".join(deposito)

    st.markdown(f"### 🧠 Quiz Interativo: Lítio ({deposito})")
    st.info("Testa os teus conhecimentos sobre as características geológicas e a exploração do Lítio!")

    # ==========================================
    # BASE DE DADOS DE PERGUNTAS
    # ==========================================
    
    questoes_gerais = [
        {
            "pergunta": "1. Qual é a abundância relativa do lítio na crosta terrestre?",
            "opcoes": [
                "A) É o elemento mais abundante.",
                "B) É o 25.º elemento mais abundante, com cerca de 25 ppm.",
                "C) É o 50.º elemento mais abundante.",
                "D) Existe apenas em vestígios indetetáveis."
            ],
            "resposta_correta": "B) É o 25.º elemento mais abundante, com cerca de 25 ppm."
        },
        {
            "pergunta": "2. Por que razão o lítio é armazenado em óleo mineral ou vácuo?",
            "opcoes": [
                "A) Para evitar que derreta a baixas temperaturas.",
                "B) Porque é altamente reativo e inflama-se em contacto com o ar ou água.",
                "C) Para manter a sua cor prateada original.",
                "D) Porque é um material radioativo perigoso."
            ],
            "resposta_correta": "B) Porque é altamente reativo e inflama-se em contacto com o ar ou água."
        },
        {
            "pergunta": "3. Qual destas indústrias consome a maior percentagem de lítio globalmente (cerca de 80%)?",
            "opcoes": [
                "A) Cerâmica e Vidro.",
                "B) Lubrificantes industriais.",
                "C) Baterias.",
                "D) Indústria Nuclear."
            ],
            "resposta_correta": "C) Baterias."
        },
        {
            "pergunta": "4. Em que estado físico o lítio é extraído das salmouras continentais?",
            "opcoes": [
                "A) Sólido (cristais de metal puro).",
                "B) Gasoso (vapores vulcânicos).",
                "C) Líquido (dissolvido em águas hipersalinas).",
                "D) Plasma."
            ],
            "resposta_correta": "C) Líquido (dissolvido em águas hipersalinas)."
        },
        {
            "pergunta": "5. Qual é o peso atómico do lítio, o metal mais leve da tabela periódica?",
            "opcoes": [
                "A) 1,008 g/mol.",
                "B) 6,941 g/mol.",
                "C) 12,011 g/mol.",
                "D) 22,989 g/mol."
            ],
            "resposta_correta": "B) 6,941 g/mol."
        }
    ]

    questoes_pegmatitos = [
        {
            "pergunta": "6. Qual é o mineral de minério de lítio mais importante encontrado em pegmatitos?",
            "opcoes": [
                "A) Quartzo.",
                "B) Espodumena.",
                "C) Halite.",
                "D) Pirite."
            ],
            "resposta_correta": "B) Espodumena."
        },
        {
            "pergunta": "7. A que distância máxima de um plutão granítico progenitor se encontram geralmente os pegmatitos LCT?",
            "opcoes": [
                "A) A mais de 100 km.",
                "B) Geralmente a menos de 10 km.",
                "C) Exclusivamente dentro do núcleo do granito.",
                "D) Não têm relação com granitos."
            ],
            "resposta_correta": "B) Geralmente a menos de 10 km."
        },
        {
            "pergunta": "8. No processamento de espodumena, a que temperatura deve ocorrer a ustulação (calcinação) para tornar o mineral solúvel?",
            "opcoes": [
                "A) 100 °C.",
                "B) 500 °C.",
                "C) Cerca de 1050 °C a 1100 °C.",
                "D) 3000 °C."
            ],
            "resposta_correta": "C) Cerca de 1050 °C a 1100 °C."
        },
        {
            "pergunta": "9. Qual é a característica estrutural comum em pegmatitos de lítio?",
            "opcoes": [
                "A) Homogeneidade total sem variações.",
                "B) Zonamento mineralógico (zonas de borda, parede, intermédia e núcleo).",
                "C) Estrutura gasosa borbulhante.",
                "D) Formação exclusiva em profundidades oceânicas."
            ],
            "resposta_correta": "B) Zonamento mineralógico (zonas de borda, parede, intermédia e núcleo)."
        },
        {
            "pergunta": "10. Os pegmatitos LCT (Lítio-Césio-Tântalo) estão associados a que contexto tectónico?",
            "opcoes": [
                "A) Cinturões orogénicos (colisão de placas).",
                "B) Fossas abissais estáveis.",
                "C) Planícies abissais sem atividade.",
                "D) Dorsais meso-oceânicas apenas."
            ],
            "resposta_correta": "A) Cinturões orogénicos (colisão de placas)."
        }
    ]

    questoes_salmouras = [
        {
            "pergunta": "6. Onde se localizam as maiores bacias de salmoura de lítio do mundo?",
            "opcoes": [
                "A) No 'Triângulo do Lítio' (Argentina, Bolívia e Chile).",
                "B) No centro da Europa.",
                "C) Na floresta amazónica.",
                "D) No fundo do Oceano Atlântico."
            ],
            "resposta_correta": "A) No 'Triângulo do Lítio' (Argentina, Bolívia e Chile)."
        },
        {
            "pergunta": "7. Qual é o método tradicional e mais económico para concentrar o lítio das salmouras?",
            "opcoes": [
                "A) Mineração subterrânea com explosivos.",
                "B) Evaporação solar em tanques extensos.",
                "C) Filtragem magnética direta.",
                "D) Destilação por fervura industrial."
            ],
            "resposta_correta": "B) Evaporação solar em tanques extensos."
        },
        {
            "pergunta": "8. Qual o principal entrave químico na extração de lítio de salmouras?",
            "opcoes": [
                "A) A falta de sal comum (NaCl).",
                "B) A presença de impurezas como Magnésio (Mg), devido à sua semelhança química.",
                "C) A água ser demasiado doce.",
                "D) O lítio evaporar-se com o sol."
            ],
            "resposta_correta": "B) A presença de impurezas como Magnésio (Mg), devido à sua semelhança química."
        },
        {
            "pergunta": "9. Qual é a idade geológica da maioria dos depósitos de salmoura economicamente viáveis?",
            "opcoes": [
                "A) Arqueico (4 mil milhões de anos).",
                "B) Jurássico.",
                "C) Quaternário (de 2,6 milhões de anos até ao presente).",
                "D) Cretáceo."
            ],
            "resposta_correta": "C) Quaternário (de 2,6 milhões de anos até ao presente)."
        },
        {
            "pergunta": "10. Qual é a concentração típica de lítio em salmouras ricas?",
            "opcoes": [
                "A) 1 a 5 ppm.",
                "B) 200 a 1400 ppm.",
                "C) 50% de lítio puro.",
                "D) 100.000 mg/L."
            ],
            "resposta_correta": "B) 200 a 1400 ppm."
        }
    ]

    questoes_argilas = [
        {
            "pergunta": "6. Em que mineral do grupo das esmectites se encontra tipicamente o lítio nestes depósitos?",
            "opcoes": [
                "A) Caulinite.",
                "B) Hectorite.",
                "C) Talco.",
                "D) Quartzo."
            ],
            "resposta_correta": "B) Hectorite."
        },
        {
            "pergunta": "7. Qual é o ambiente de formação destes depósitos sedimentares de argila?",
            "opcoes": [
                "A) Desertos de areia seca.",
                "B) Lagos em caldeiras vulcânicas alterados hidrotermalmente.",
                "C) Recifes de coral.",
                "D) Picos de montanhas nevadas."
            ],
            "resposta_correta": "B) Lagos em caldeiras vulcânicas alterados hidrotermalmente."
        },
        {
            "pergunta": "8. Onde se localiza a maior reserva mundial de argila com lítio?",
            "opcoes": [
                "A) Salar de Uyuni.",
                "B) Caldeira de McDermitt (EUA).",
                "C) Minas Gerais (Brasil).",
                "D) Vale do Tejo (Portugal)."
            ],
            "resposta_correta": "B) Caldeira de McDermitt (EUA)."
        },
        {
            "pergunta": "9. Qual é a vantagem económica da mineração de argilas de lítio?",
            "opcoes": [
                "A) São depósitos muito duros que protegem o lítio.",
                "B) São 'macios', permitindo extração a céu aberto sem necessidade de explosivos.",
                "C) O lítio separa-se apenas com água fria.",
                "D) Estão localizados em grandes profundidades oceânicas."
            ],
            "resposta_correta": "B) São 'macios', permitindo extração a céu aberto sem necessidade de explosivos."
        },
        {
            "pergunta": "10. Qual o processo químico necessário para libertar o lítio da estrutura da argila?",
            "opcoes": [
                "A) Lavagem simples com sabão.",
                "B) Lixiviação ácida ou ustulação com calcário.",
                "C) Exposição prolongada ao vento.",
                "D) Congelamento extremo."
            ],
            "resposta_correta": "B) Lixiviação ácida ou ustulação com calcário."
        }
    ]

    # ==========================================
    # LÓGICA DE SELEÇÃO DE PERGUNTAS
    # ==========================================
    
    # As questões gerais entram sempre
    questoes_atuais = questoes_gerais.copy()

    # Adiciona as questões específicas dependendo da seleção do utilizador
    if "Pegmatitos" in deposito:
        questoes_atuais.extend(questoes_pegmatitos)
    elif "Salmouras" in deposito:
        questoes_atuais.extend(questoes_salmouras)
    elif "Argilas" in deposito:
        questoes_atuais.extend(questoes_argilas)

    # ==========================================
    # INTERFACE DO QUIZ (FORMULÁRIO)
    # ==========================================
    
    with st.form(key="quiz_litio_form"):
        respostas_utilizador = []
        
        for i, q in enumerate(questoes_atuais):
            st.markdown(f"**{q['pergunta']}**")
            resposta = st.radio(
                "Selecione a opção:", 
                q["opcoes"], 
                key=f"questao_litio_{i}", 
                label_visibility="collapsed"
            )
            respostas_utilizador.append(resposta)
            st.write("---")

        submit = st.form_submit_button("Submeter Respostas")

    # ==========================================
    # AVALIAÇÃO E RESULTADOS
    # ==========================================
    
    if submit:
        score = 0
        for i, q in enumerate(questoes_atuais):
            if respostas_utilizador[i] == q["resposta_correta"]:
                score += 1

        st.markdown(f"### 🎯 O teu resultado: **{score} / {len(questoes_atuais)}**")
        
        if score == len(questoes_atuais):
            st.balloons()
            st.success("Brilhante! Acertaste em tudo. És um verdadeiro especialista em Lítio!")
        elif score >= len(questoes_atuais) / 2:
            st.info("Bom trabalho! Mas ainda podes afinar alguns conceitos.")
        else:
            st.warning("Bom esforço! Vale a pena reveres as características na secção acima e tentar de novo.")

        st.divider()
        st.markdown("### Correção:")

        for i, q in enumerate(questoes_atuais):
            if respostas_utilizador[i] == q["resposta_correta"]:
                st.success(f"✔️ **Questão correta!** {q['resposta_correta']}")
            else:
                st.error(f"❌ **Questão incorreta.** Respondeste: *{respostas_utilizador[i]}* | A resposta certa era: **{q['resposta_correta']}**")


def checklist_litio(deposito=None):
    # Verificação de segurança
    if not deposito:
        st.warning("Por favor, seleciona um tipo de depósito para carregar a checklist.")
        return

    if isinstance(deposito, list):
        deposito = ", ".join(deposito)

    st.markdown("### ✅ Checklist de Observação: Lítio")
    st.info("Utiliza esta checklist para identificares as principais características do lítio e dos seus depósitos, quer em amostras de mão, quer no contexto geológico.")

    # ===============================
    # CHECKLIST GERAL (Sempre visível)
    # ===============================
    st.markdown("#### 🔍 Checklist Geral do Recurso")
    
    st.checkbox("**Leveza Extrema:** Identifique se a descrição menciona ser o metal mais leve da tabela periódica (densidade de 0,534 g/cm³).", key="chk_geral_1")
    st.checkbox("**Modo de Conservação:** Em exposições de metal puro, verifique se está submerso em óleo mineral, querosene ou vácuo, devido à sua alta reatividade com o ar.", key="chk_geral_2")
    st.checkbox("**Cor e Brilho:** O metal puro deve apresentar um brilho prateado (embora oxide rapidamente para cinza se exposto).", key="chk_geral_3")
    st.checkbox("**Abundância Curiosa:** Procure notas que indiquem que, apesar da fama, é apenas o 25.º elemento mais abundante na crosta (~25-35 ppm).", key="chk_geral_4")
    st.checkbox("**Foco Tecnológico:** Procure associações com a 'Transição Energética' ou amostras de baterias de iões de lítio ao lado do minério.", key="chk_geral_5")

    st.divider()

    # ===============================
    # CHECKLISTS ESPECÍFICAS
    # ===============================
    
    if "Pegmatitos" in deposito:
        st.markdown("#### 🪨 Pegmatitos (Rocha Dura - LCT)")
        
        st.checkbox("**Cristais Gigantes:** Verifique se a amostra apresenta uma textura muito grosseira, típica de pegmatitos, com cristais que podem atingir dimensões métricas.", key="chk_peg_1")
        st.checkbox("**Espodumena:** Procure cristais prismáticos de cor branco-creme, esverdeada ou rosada; é o principal mineral de minério.", key="chk_peg_2")
        st.checkbox("**Micas Coloridas:** Identifique a lepidolite, uma mica de cor violeta ou lilás característica destes depósitos.", key="chk_peg_3")
        st.checkbox("**Zonamento Mineralógico:** Em diagramas, observe se o depósito está organizado em zonas (borda, parede, intermédia e núcleo).", key="chk_peg_4")
        st.checkbox("**Associação Granítica:** Confirme se o depósito está associado a granitos peraluminosos (ricos em alumínio).", key="chk_peg_5")

    elif "Salmouras" in deposito:
        st.markdown("#### 💧 Salmouras Continentais (Salares)")
        
        st.checkbox("**Minerais Evaporíticos:** Procure amostras de halite (sal comum), gesso ou silvite, que formam as crostas superficiais dos salares.", key="chk_sal_1")
        st.checkbox("**Contexto Geográfico:** Verifique se o mapa indica bacias em climas áridos ou bacias endorreicas (fechadas), como o 'Triângulo do Lítio'.", key="chk_sal_2")
        st.checkbox("**Amostra Líquida:** Se houver frascos, a salmoura rica em lítio é geralmente um líquido transparente ou amarelado com altíssima salinidade.", key="chk_sal_3")
        st.checkbox("**Subprodutos:** Identifique a presença de potássio (potassa), magnésio ou boro, frequentemente extraídos em conjunto.", key="chk_sal_4")
        st.checkbox("**Cenário Tectónico:** Observe se o depósito está associado a atividade geotérmica ou vulcânica recente (Cenozoica).", key="chk_sal_5")

    elif "Argilas" in deposito:
        st.markdown("#### 🏜️ Argilas Ricas em Lítio (Sedimentares)")
        
        st.checkbox("**Hectorite:** Identifique este mineral do grupo das esmectites; é uma argila rica em magnésio e lítio.", key="chk_arg_1")
        st.checkbox("**Origem Vulcânica:** Verifique se a rocha hospedeira é um tufo vulcânico ou cinza alterada.", key="chk_arg_2")
        st.checkbox("**Ambiente de Lagoa:** O contexto geológico deve mencionar lagos em caldeiras vulcânicas.", key="chk_arg_3")
        st.checkbox("**Aspeto Estratificado:** As amostras costumam ser estratiformes (em camadas) e visualmente semelhantes a barros comuns.", key="chk_arg_4")
        st.checkbox("**Consistência:** Notas sobre a extração referem frequentemente que são depósitos 'macios', que não exigem explosivos para a mineração.", key="chk_arg_5")

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
