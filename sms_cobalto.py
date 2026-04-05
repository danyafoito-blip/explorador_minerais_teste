import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_sms(deposito):

    st.markdown("### 🌊⚙️ Características dos Depósitos Oceânicos")

    # Verificação de segurança
    if not deposito:
        st.warning("Por favor, seleciona um tipo de depósito para visualizar as características.")
        return

    # Converter lista de seleções para string para facilitar verificação
    if isinstance(deposito, list):
        deposito_str = " ".join(deposito)
    else:
        deposito_str = deposito

    # 1. Sulfuretos Maciços (SMS)
    if "Sulfuretos" in deposito_str or "SMS" in deposito_str or "Arcos" in deposito_str or "Dorsais" in deposito_str:
        st.markdown("## 1. Sulfuretos Maciços do Fundo do Mar (SMS) / Arcos e Retro-arcos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**5 Propriedades Físicas e Geoquímicas**")
            st.write("- **Composição de Metais Base:** Apresentam altos teores de ferro, zinco, cobre e chumbo.")
            st.write("- **Riqueza em Metais Preciosos:** Contêm concentrações comercialmente exploráveis de ouro e prata.")
            st.write("- **Zonamento Térmico:** A mineralogia é influenciada pela temperatura; fluidos >300°C enriquecem em cobre, temperaturas mais baixas favorecem zinco.")
            st.write("- **Estrutura Tridimensional:** Compostos por chaminés ('black smokers'), montículos de talude e zona de stockwork.")
            st.write("- **Assinatura de Voláteis (Arcos):** Enriquecimento em elementos magmatófilos tóxicos como arsénio, mercúrio e antimónio.")

        with col2:
            st.info("**5 Pontos da Importância Energética**")
            st.write("- **Cobre para Eletrificação:** Fornecem cobre essencial para a construção de infraestruturas de redes elétricas.")
            st.write("- **Zinco para Armazenamento:** Fundamental para a produção de baterias e proteção de estruturas de energia renovável.")
            st.write("- **Transição de Baixo Carbono:** Fornecem matérias-primas críticas necessárias para uma economia de baixo carbono.")
            st.write("- **Alternativa a Minas Terrestres:** Teores frequentemente superiores aos de depósitos terrestres em declínio de qualidade.")
            st.write("- **Segurança de Abastecimento:** Reduzem a dependência externa de metais estratégicos para os setores tecnológico e energético.")

    # 2. Crostas de Ferro-Manganês
    elif "Crostas" in deposito_str or "Ferro-Manganês" in deposito_str or "Cobalto" in deposito_str:
        st.markdown("## 2. Crostas de Ferro-Manganês (Ricas em Cobalto)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**5 Propriedades Físicas e Geoquímicas**")
            st.write("- **Mineralogia Principal:** Compostas por oxihidróxidos de ferro e óxidos de manganês (vernadite e birnessite).")
            st.write("- **Enriquecimento em Cobalto:** Principal fonte oceânica de cobalto, com teores que podem atingir os 2%.")
            st.write("- **Crescimento Lento:** Taxa de crescimento extremamente lenta (1 a 5 milímetros por milhão de anos).")
            st.write("- **Alta Área Superficial:** Superfície específica média enorme (325 m²/cm³), potenciando a adsorção de metais.")
            st.write("- **Conteúdo de Metais Raros:** Concentram telúrio, platina, molibdénio e elementos de terras raras (REY).")

        with col2:
            st.info("**5 Pontos da Importância Energética**")
            st.write("- **Cobalto para Mobilidade Elétrica:** Essencial para o fabrico de baterias de iões de lítio para veículos elétricos.")
            st.write("- **Telúrio para Energia Solar:** Constituem a maior reserva global de telúrio, usado em células solares de película fina.")
            st.write("- **Terras Raras (REY) para Aerogeradores:** Contêm neodímio e térbio, cruciais para ímanes em turbinas eólicas.")
            st.write("- **Platina para Células de Combustível:** Fonte de platina, catalisador em tecnologias de hidrogénio.")
            st.write("- **Autonomia Estratégica:** Fornecem Minerais Críticos (CRM) fundamentais para a independência energética.")

    # 3. Nódulos Polimetálicos
    elif "Nódulos" in deposito_str:
        st.markdown("## 3. Nódulos Polimetálicos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**5 Propriedades Físicas e Geoquímicas**")
            st.write("- **Acreção Concêntrica:** Deposição concêntrica de óxidos em torno de um núcleo (ex: dente de tubarão ou rocha).")
            st.write("- **Génese Mista:** Crescimento hidrogenético (água do mar) e diagenético (água dos poros dos sedimentos).")
            st.write("- **Mineralogia de Manganês:** Compostos essencialmente por vernadite, todorokite e birnessite.")
            st.write("- **Riqueza em Níquel e Cobre:** Apresentam teores de níquel e cobre superiores aos das crostas.")
            st.write("- **Localização Abissal:** Ocorrem de forma vasta nas planícies abissais oceânicas.")

        with col2:
            st.info("**5 Pontos da Importância Energética**")
            st.write("- **Níquel para Baterias:** O elevado teor de níquel é vital para baterias de alta densidade energética.")
            st.write("- **Manganês para Armazenamento:** Utilizado em ligas metálicas e em novas tecnologias de armazenamento.")
            st.write("- **Suplemento de Recursos Terrestres:** Alternativa massiva para suprir a procura global de metais base.")
            st.write("- **Diversificação de Fontes:** Aumentam a resiliência do mercado contra interrupções no fornecimento terrestre.")
            st.write("- **Economia de Escala:** Potencial de exploração em larga escala pode reduzir custos nas energias renováveis.")

    # 4. Fosforitos
    elif "Fosforitos" in deposito_str:
        st.markdown("## 4. Fosforitos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**5 Propriedades Físicas e Geoquímicas**")
            st.write("- **Mineralogia de Fosfato:** Compostos predominantemente por fluorapatite carbonatada (CFA).")
            st.write("- **Composição Química:** Ricos em fósforo (P₂O₅) e cálcio (CaO).")
            st.write("- **Associação com Crostas:** Servem frequentemente de substrato rochoso para as crostas de cobalto.")
            st.write("- **Hospedeiros de REY:** Atuam como depósitos secundários importantes para elementos de terras raras e ítrio.")
            st.write("- **Origem Oceanográfica:** Ligada a correntes de fundo intensas e períodos de elevada produtividade biológica.")

        with col2:
            st.info("**5 Pontos da Importância Energética**")
            st.write("- **Ítrio para Eficiência Energética:** Fonte de ítrio, usado em tecnologias de iluminação eficiente e LEDs.")
            st.write("- **Terras Raras para Tecnologia:** O seu conteúdo em REY apoia a produção de componentes eletrónicos avançados.")
            st.write("- **Valorização de Recursos:** A presença aumenta significativamente o valor económico total dos montes submarinos.")
            st.write("- **Independência Tecnológica:** Contribuem para a segurança de abastecimento de metais críticos.")
            st.write("- **Fósforo Industrial:** Potencial para aplicações químicas e industriais ligadas a infraestruturas energéticas.")

    # 5. Lamas REY
    elif "Lamas" in deposito_str or "Sedimentos" in deposito_str:
        st.markdown("## 5. Lamas REY")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**5 Propriedades Físicas e Geoquímicas**")
            st.write("- **Origem Hidrotermal:** Deposição de partículas ricas em metais de plumas hidrotermais.")
            st.write("- **Preservação Metálica:** Retêm Cu, Zn e sulfuretos por soterramento rápido e ausência de fluxo residual.")
            st.write("- **Estratigrafia Fina:** Apresentam frequentemente sequências de grão fino de depósitos turbidíticos.")
            st.write("- **Concentração de Terras Raras:** Enriquecidas em terras raras leves (LREE) e ítrio.")
            st.write("- **Extensão Territorial:** Dispersam-se por áreas de vários quilómetros quadrados em torno dos depósitos centrais.")

        with col2:
            st.info("**5 Pontos da Importância Energética**")
            st.write("- **Fonte de LREE:** Fornecem terras raras leves essenciais para ímanes de alta tecnologia e motores elétricos.")
            st.write("- **Metais Base Dispersos:** Contêm misturas de cobre e zinco que representam um recurso volumétrico.")
            st.write("- **Volume de Recurso:** A vasta dispersão sugere um potencial de extração massivo por quilómetro quadrado.")
            st.write("- **Diversificação Estratégica:** Via alternativa para obter metais críticos fora dos depósitos maciços tradicionais.")
            st.write("- **Autonomia em CRM:** Apoiam diretamente as metas de autonomia estratégica em matérias-primas críticas.")

    else:
        st.info("Selecione um tipo de depósito válido para visualizar a informação detalhada.")

# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_sms(deposito):

    st.markdown("### ⚠️ Confusões Comuns e Mitos")

    # Verificação de segurança
    if not deposito:
        st.warning("Por favor, seleciona um tipo de depósito para visualizar as confusões e mitos.")
        return

    # Converter lista de seleções para string para facilitar verificação
    if isinstance(deposito, list):
        deposito_str = " ".join(deposito)
    else:
        deposito_str = deposito

    st.markdown("#### 🔍 Os 5 Mitos e Confusões")

    # 1. Sulfuretos Maciços (SMS)
    if "Sulfuretos" in deposito_str or "SMS" in deposito_str or "Arcos" in deposito_str or "Dorsais" in deposito_str:
        st.markdown("### 🌋 1. Sulfuretos Maciços do Fundo do Mar (SMS)")
        
        st.markdown("**1. Mito da Abundância Visível**")
        st.write("- Existe a ideia de que o recurso se limita ao montículo visível no fundo do mar.")
        st.write("- **A Realidade:** Os depósitos estendem-se até 200 metros abaixo do leito marinho, contendo até cinco vezes mais minério do que o previsto apenas pela topografia de superfície.")

        st.markdown("**2. Confusão sobre a Rocha Hospedeira**")
        st.write("- Frequentemente acredita-se que a composição do substrato (máfico vs. ultramáfico) dita a geoquímica do depósito.")
        st.write("- **A Realidade:** Análises sugerem que a temperatura de deposição e a taxa de espalhamento da crista são fatores muito mais determinantes para a variabilidade metálica.")

        st.markdown("**3. Confusão Ativos vs. Extintos**")
        st.write("- Pensa-se que apenas fontes ativas têm interesse económico.")
        st.write("- **A Realidade:** Os depósitos extintos (eSMS) são muito mais abundantes e acessíveis, embora muitas vezes estejam escondidos sob sedimentos pelágicos.")

        st.markdown("**4. Mito do Rácio Co/Ni**")
        st.write("- Este rácio é usado para distinguir sistemas máficos de ultramáficos, mas os dados mostram que tem pouco poder discriminatório.")
        st.write("- **A Realidade:** Elementos como o estanho (Sn) são indicadores muito mais fiáveis de influência ultramáfica.")

        st.markdown("**5. Mito da Presença de Anidrite**")
        st.write("- Embora a anidrite domine o interior dos depósitos ativos, ela está ausente em depósitos extintos.")
        st.write("- **A Realidade:** A anidrite dissolve-se quando as temperaturas caem abaixo de 140°C, o que pode inclusive causar o colapso estrutural do depósito.")

    # 2. Crostas de Ferro-Manganês
    elif "Crostas" in deposito_str or "Ferro-Manganês" in deposito_str or "Cobalto" in deposito_str:
        st.markdown("### ⛰️ 2. Crostas de Ferro-Manganês (Ricas em Cobalto)")
        
        st.markdown("**1. Confusão Genética**")
        st.write("- É comum confundir crostas puramente hidrogenéticas com hidrotermais.")
        st.write("- **A Realidade:** Apenas as hidrogenéticas (precipitadas da água do mar) contêm metais raros suficientes para interesse económico; as hidrotermais são ricas em ferro, mas pobres em metais críticos.")

        st.markdown("**2. Mito da Taxa de Formação**")
        st.write("- Devido à sua espessura (até 26 cm), pode-se pensar que se formam rapidamente.")
        st.write("- **A Realidade:** O seu crescimento é de apenas 1 a 5 milímetros por milhão de anos, sendo um dos processos geológicos mais lentos da Terra.")

        st.markdown("**3. Confusão sobre a Camada Diagenética**")
        st.write("- Lâminas brilhantes dentro das crostas são por vezes vistas como meras variações estéticas.")
        st.write("- **A Realidade:** Indicam diagénese subóxica, sendo camadas enriquecidas em níquel e cobre, mas pobres em cobalto.")

        st.markdown("**4. Mito da Facilidade de Extração**")
        st.write("- Existe o mito de que são tão fáceis de colher como os nódulos.")
        st.write("- **A Realidade:** A sua forte adesão ao substrato rochoso e a variabilidade de espessura tornam a sua exploração tecnicamente muito mais desafiante.")

        st.markdown("**5. Confusão sobre o Valor do Substrato**")
        st.write("- O substrato rochoso das crostas é muitas vezes considerado estéril ou sem valor.")
        st.write("- **A Realidade:** Quando o substrato é composto por fosforitos, o valor económico global do recurso aumenta drasticamente devido ao conteúdo extra de fósforo e ítrio.")

    # 3. Nódulos Polimetálicos
    elif "Nódulos" in deposito_str:
        st.markdown("### 🌑 3. Nódulos Polimetálicos")
        
        st.markdown("**1. Mito da Fonte Única**")
        st.write("- Pensa-se frequentemente que os metais dos nódulos vêm apenas da precipitação direta da água do mar.")
        st.write("- **A Realidade:** Têm uma génese mista, recebendo um aporte significativo de metais a partir da água dos poros dos sedimentos (diagénese).")

        st.markdown("**2. Confusão com as Crostas**")
        st.write("- São frequentemente confundidos com as crostas de cobalto.")
        st.write("- **A Realidade:** Os nódulos são sistematicamente mais ricos em níquel e cobre e ocorrem soltos em planícies abissais, não encrustados em montes submarinos.")

        st.markdown("**3. Mito da Renovabilidade**")
        st.write("- Devido ao seu crescimento contínuo contatando com a água, há quem os veja como renováveis.")
        st.write("- **A Realidade:** À escala humana, são recursos absolutamente não-renováveis, dado que levam milhões de anos a atingir tamanhos exploráveis.")

        st.markdown("**4. Confusão no Processamento**")
        st.write("- Acredita-se que métodos de lixiviação simples funcionam igualmente para todos os nódulos.")
        st.write("- **A Realidade:** Minerais específicos presentes nos nódulos, como a todorokite, podem ser bastante resistentes a certos processos hidrometalúrgicos padronizados.")

        st.markdown("**5. Mito da Distribuição Aleatória**")
        st.write("- Pensa-se que os nódulos estão espalhados por todo o lado nas planícies abissais.")
        st.write("- **A Realidade:** A sua presença depende criticamente de correntes de fundo ativas que mantenham os núcleos de nucleação livres de sedimentação excessiva que os enterraria.")

    # 4. Fosforitos
    elif "Fosforitos" in deposito_str:
        st.markdown("### 🦴 4. Fosforitos")
        
        st.markdown("**1. Confusão Rocha vs. Minério**")
        st.write("- São muitas vezes vistos apenas como a 'rocha de base' das crostas de cobalto.")
        st.write("- **A Realidade:** Na verdade, são um recurso potencial riquíssimo em terras raras (REY) e fósforo, com um tremendo valor económico próprio.")

        st.markdown("**2. Mito da Composição Simples**")
        st.write("- Pensa-se que os fosforitos marinhos são apenas fosfatos de cálcio básicos.")
        st.write("- **A Realidade:** A sua estrutura mineral complexa (CFA - fluorapatite carbonatada) permite a incorporação de uma vasta gama de metais críticos.")

        st.markdown("**3. Confusão Visual**")
        st.write("- Em campo ou em amostras de museu, são facilmente confundidos com um calcário comum.")
        st.write("- **A Realidade:** A sua assinatura química revela teores de P₂O₅ e terras raras (REY) ordens de grandeza superiores ao calcário.")

        st.markdown("**4. Mito da Formação Aleatória**")
        st.write("- Existe a ideia de que podem aparecer em qualquer monte submarino.")
        st.write("- **A Realidade:** A sua génese está estritamente ligada a eventos oceanográficos muito específicos, como períodos de elevada produtividade biológica e correntes de afloramento (*upwelling*).")

        st.markdown("**5. Confusão na Lixiviação**")
        st.write("- Existe a ideia de que os metais valiosos estão nos óxidos secundários associados ao fosforito.")
        st.write("- **A Realidade:** As terras raras estão intrinsecamente concentradas e substituídas dentro dos próprios minerais de fosfato.")

    # 5. Lamas REY (Sedimentos Metalíferos)
    elif "Lamas" in deposito_str or "Sedimentos" in deposito_str:
        st.markdown("### 🌫️ 5. Lamas REY")
        
        st.markdown("**1. Mito do Material de Desperdício**")
        st.write("- São frequentemente ignorados como mera 'lama' sem valor localizada em redor dos campos hidrotermais SMS.")
        st.write("- **A Realidade:** Estes sedimentos podem estender-se por quilómetros quadrados e representar um recurso volumétrico massivo de metais como cobre e zinco.")

        st.markdown("**2. Confusão de Origem**")
        st.write("- São repetidamente confundidos com os sedimentos pelágicos normais do fundo do mar.")
        st.write("- **A Realidade:** Derivam fundamentalmente da deposição de 'cinzas' ricas em metais provenientes das plumas hidrotermais e da erosão dos montículos de sulfuretos.")

        st.markdown("**3. Mito da Toxicidade Uniforme**")
        st.write("- Pensa-se que, por serem sedimentos finos ricos em metais, são sempre letalmente tóxicos para toda a vida.")
        st.write("- **A Realidade:** A toxicidade varia; as comunidades adaptadas de fontes ativas conseguem tolerá-los, mas a fauna pelágica e de fundo comum é que é altamente vulnerável.")

        st.markdown("**4. Confusão sobre a Preservação**")
        st.write("- Acredita-se que os metais particulados nestas lamas se oxidam e dissolvem rapidamente na água fria do fundo.")
        st.write("- **A Realidade:** O soterramento rápido e a baixa permeabilidade da lama podem preservar grãos de sulfuretos perfeitamente intactos durante muito tempo.")

        st.markdown("**5. Mito da Concentração de Terras Raras**")
        st.write("- Assume-se que os elementos de terras raras (REY) estão distribuídos uniformemente por toda a lama.")
        st.write("- **A Realidade:** As terras raras leves (LREE) concentram-se preferencialmente e de forma muito específica nas fases minerais de ferro e manganês destes sedimentos.")

    else:
        st.info("Selecione um tipo de depósito válido para visualizar as informações.")



# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_sms(*args):
    st.header("🧠 Quiz: Depósitos de Fundo Oceânico")
    st.markdown("Testa os teus conhecimentos gerais sobre todos os recursos minerais abordados nesta secção.")

    # Dicionário com todas as 10 perguntas gerais
    quiz_data = [
        {
            "pergunta": "1. Sulfuretos Maciços (SMS): Qual é o processo geológico fundamental que leva à formação dos depósitos de SMS?",
            "opcoes": [
                "A) Erosão de montanhas continentais.",
                "B) Circulação hidrotermal de água do mar aquecida por magma.",
                "C) Acumulação de esqueletos de baleias no abismo.",
                "D) Precipitação de sal devido à evaporação solar."
            ],
            "correta": "B) Circulação hidrotermal de água do mar aquecida por magma."
        },
        {
            "pergunta": "2. Sulfuretos Maciços (SMS): Quais são os metais preciosos frequentemente encontrados com teores económicos nestes depósitos?",
            "opcoes": [
                "A) Platina e Irídio.",
                "B) Ouro e Prata.",
                "C) Alumínio e Magnésio.",
                "D) Urânio e Tório."
            ],
            "correta": "B) Ouro e Prata."
        },
        {
            "pergunta": "3. Nódulos Polimetálicos: Em que ambiente marinho se localizam predominantemente os nódulos polimetálicos?",
            "opcoes": [
                "A) No topo de vulcões ativos.",
                "B) Nas praias de ilhas oceânicas.",
                "C) Nas planícies abissais oceânicas.",
                "D) Nos recifes de coral pouco profundos."
            ],
            "correta": "C) Nas planícies abissais oceânicas."
        },
        {
            "pergunta": "4. Nódulos Polimetálicos: Qual é a estrutura interna característica de um nódulo polimetálico?",
            "opcoes": [
                "A) Estrutura oca como um balão.",
                "B) Acreção concêntrica de óxidos em torno de um núcleo.",
                "C) Uma única massa de cristal de quartzo.",
                "D) Camadas de carvão fóssil."
            ],
            "correta": "B) Acreção concêntrica de óxidos em torno de um núcleo."
        },
        {
            "pergunta": "5. Crostas de Ferro-Manganês: Qual é a taxa de crescimento típica das crostas hidrogenéticas que se formam nos montes submarinos?",
            "opcoes": [
                "A) 1 metro por cada mil anos.",
                "B) 1 a 5 milímetros por cada milhão de anos.",
                "C) 10 centímetros por década.",
                "D) Elas crescem instantaneamente após tempestades."
            ],
            "correta": "B) 1 a 5 milímetros por cada milhão de anos."
        },
        {
            "pergunta": "6. Crostas de Ferro-Manganês: Qual é o metal estratégico que dá o nome comum a estas crostas devido à sua elevada concentração?",
            "opcoes": [
                "A) Níquel.",
                "B) Cobre.",
                "C) Cobalto.",
                "D) Ferro."
            ],
            "correta": "C) Cobalto."
        },
        {
            "pergunta": "7. Fosforitos: Qual é o mineral principal que constitui a base dos fosforitos marinhos?",
            "opcoes": [
                "A) Pirite.",
                "B) Fluorapatite carbonatada (CFA).",
                "C) Calcite pura.",
                "D) Feldspato."
            ],
            "correta": "B) Fluorapatite carbonatada (CFA)."
        },
        {
            "pergunta": "8. Fosforitos: Qual é a relação comum entre os fosforitos e as crostas de cobalto?",
            "opcoes": [
                "A) Estão sempre em oceanos diferentes.",
                "B) Os fosforitos servem frequentemente de substrato geológico para as crostas.",
                "C) As crostas transformam-se em fosforitos quando aquecem.",
                "D) Os fosforitos impedem o crescimento de qualquer outro mineral."
            ],
            "correta": "B) Os fosforitos servem frequentemente de substrato geológico para as crostas."
        },
        {
            "pergunta": "9. Lamas REY: Qual é a origem das partículas ricas em metais que compõem estas lamas?",
            "opcoes": [
                "A) Areias sopradas pelo vento do deserto.",
                "B) Deposição de partículas das plumas de fontes hidrotermais.",
                "C) Restos de plâncton que brilha no escuro.",
                "D) Cinzas de fogos florestais costeiros."
            ],
            "correta": "B) Deposição de partículas das plumas de fontes hidrotermais."
        },
        {
            "pergunta": "10. Lamas REY: Estas lamas são consideradas um recurso estratégico principalmente devido ao seu teor em:",
            "opcoes": [
                "A) Sal de cozinha.",
                "B) Diamantes industriais.",
                "C) Elementos de Terras Raras (REY).",
                "D) Ferro e Alumínio apenas."
            ],
            "correta": "C) Elementos de Terras Raras (REY)."
        }
    ]

    # Criação do formulário para o Quiz
    with st.form("quiz_sms_form"):
        respostas_utilizador = []
        
        for i, q in enumerate(quiz_data):
            # Usar 'qsms_' como chave única para os radio buttons
            resp = st.radio(f"**{q['pergunta']}**", q["opcoes"], key=f"qsms_{i}", index=None)
            respostas_utilizador.append(resp)
            st.write("---")
            
        # Botão de submissão do formulário
        submetido = st.form_submit_button("Verificar Respostas")

    # Lógica de validação das respostas ao submeter
    if submetido:
        pontuacao = 0
        total_perguntas = len(quiz_data)
        
        st.divider()
        st.subheader("Resultados:")
        
        for i, q in enumerate(quiz_data):
            if respostas_utilizador[i] == q["correta"]:
                pontuacao += 1
            elif respostas_utilizador[i] is None:
                st.warning(f"⚠️ Pergunta {i+1} não respondida.")
            else:
                st.error(f"❌ Pergunta {i+1}: Incorreta. A resposta certa era: **{q['correta']}**")
            
        st.success(f"Pontuação Final: {pontuacao} / {total_perguntas}")
        
        if pontuacao == total_perguntas:
            st.balloons()
            st.success("Perfeito! Acertaste em todas as perguntas do Fundo Oceânico! 🎉🌊")
        elif pontuacao >= 7:
            st.info("Muito bom resultado! Dominas bem os conceitos dos depósitos oceânicos. 👍")
        else:
            st.info("Podes sempre rever a informação nas secções acima e tentar novamente. 💪")

def referencias_sms():
    """Função que guarda e formata as referências bibliográficas dos SMS"""
    st.markdown("### Fontes e Bibliografia - SMS")
    
    st.markdown("""
    Abaixo encontram-se as principais referências científicas e académicas consultadas para a elaboração do perfil dos Sulfuretos Maciços do Fundo Oceânico:
    
    * **Hannington, M. D., de Ronde, C. E. J., & Petersen, S. (2005).** *Sea-floor tectonics and submarine hydrothermal systems.* Economic Geology 100th Anniversary Volume, 111-141.
    * **Pirajno, F. (2009).** *Hydrothermal Processes and Mineral Systems.* Springer.
    * **Robb, L. (2005).** *Introduction to Ore-Forming Processes.* Blackwell Publishing.
    """)
    
    st.divider()
    st.caption("Organizado por: Grupo Quartzo (SB, GM, CP, DA)")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_sms():

    st.markdown("### ✅ Checklist de Campo (Exploração Submarina)")

    st.write("Utilizado na exploração de depósitos SMS:")

    st.checkbox("Identificar atividade hidrotermal")
    st.checkbox("Mapear estruturas tectónicas")
    st.checkbox("Analisar plumas hidrotermais")
    st.checkbox("Amostragem de sulfuretos")
    st.checkbox("Caracterização geoquímica")
    st.checkbox("Avaliação ambiental")
    st.checkbox("Utilização de ROVs/AUVs")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_sms():

    st.markdown("### 🌍 Mapa Global de Depósitos SMS e Cobalto")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="sms_map"
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Base de dados carregada com sucesso")
        st.dataframe(df.head())

        mapa = folium.Map(
            location=[0, 0],
            zoom_start=2
        )

        Fullscreen().add_to(mapa)

        for _, row in df.iterrows():

            if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):

                popup = f"""
                <b>Local:</b> {row.get('Field Name','N/A')}<br>
                <b>Região:</b> {row.get('Region','N/A')}<br>
                <b>Tipo:</b> {row.get('Type','N/A')}
                """

                folium.CircleMarker(
                    [row["Latitude"], row["Longitude"]],
                    radius=5,
                    color="black",
                    fill=True,
                    fill_opacity=0.8,
                    popup=popup
                ).add_to(mapa)

        st_folium(mapa, use_container_width=True, height=600)

    else:
        st.info("Carregue um ficheiro CSV para visualizar os dados.")


