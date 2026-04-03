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

# ===============================
# 2. CONFUSÕES E MITOS
# ===============================

def mostrar_confusoes_uranio():
    st.header("❌ Mitos e Confusões Comuns: Urânio")
    st.markdown("O urânio é um dos elementos mais estigmatizados devido à sua associação com armas nucleares e acidentes. Vamos desmistificar algumas das ideias mais comuns.")

    col1, col2 = st.columns(2)

    with col1:
        st.error("**Mito 1: O urânio natural brilha a verde no escuro**")
        st.success(
            "**Realidade:** O minério de urânio natural não brilha no escuro. "
            "A ideia da radiação verde fluorescente vem da cultura pop (como os Simpsons) e dos mostradores de relógios antigos (que usavam rádio e fósforo, não urânio). "
            "Alguns minerais secundários de urânio podem emitir fluorescência sob luz ultravioleta (UV), mas nunca emitem luz própria no escuro."
        )

        st.error("**Mito 2: O urânio natural é perigoso só de estar perto**")
        st.success(
            "**Realidade:** O urânio natural é composto maioritariamente por U-238 (99,27%), que tem uma meia-vida de 4,5 mil milhões de anos. "
            "Isto significa que decai muito lentamente. A sua principal emissão são partículas alfa, que não penetram a pele humana ou mesmo uma folha de papel. "
            "O verdadeiro perigo está na inalação ou ingestão do pó do minério, que é tóxico como um metal pesado (semelhante ao chumbo)."
        )

    with col2:
        st.error("**Mito 3: O minério de urânio pode explodir espontaneamente**")
        st.success(
            "**Realidade:** É fisicamente impossível que um depósito de urânio natural ou o minério bruto sofra uma explosão nuclear. "
            "Para que ocorra uma reação em cadeia descontrolada ou explosiva, o isótopo físsil (U-235) precisa de ser artificialmente enriquecido de 0,7% para mais de 90%. "
            "Em reatores comerciais para eletricidade, enriquece-se apenas até cerca de 3 a 5%, o que também impossibilita uma explosão nuclear."
        )

        st.error("**Mito 4: Uma vez extraído, o terreno fica radioativo para sempre**")
        st.success(
            "**Realidade:** As minas de urânio modernas seguem rigorosos protocolos de remediação. "
            "Quando a mina fecha, os estéreis são contidos, selados e a área é coberta e revegetada. "
            "Com as práticas atuais, a radioatividade à superfície na área remediada regressa a níveis seguros, equivalentes à radiação de fundo natural."
        )


# ===============================
# 3. Quiz
# ===============================

def quiz_uranio():
    st.header("Quiz: Urânio")
    st.markdown("Teste os seus conhecimentos sobre as características gerais e os depósitos específicos de urânio.")

    # Dicionários com as perguntas, opções e respostas corretas
    quiz_geral = [
        {
            "pergunta": "1. Qual é a principal característica geoquímica que controla a formação da maioria dos depósitos de urânio?",
            "opcoes": [
                "A) A sua afinidade extrema com o oxigénio em qualquer estado.",
                "B) A alta solubilidade no estado hexavalente (U6+) e a baixa solubilidade no estado tetravalente (U4+).",
                "C) A sua capacidade de se fundir com o ferro no núcleo da Terra.",
                "D) O facto de ser um elemento quimicamente inerte."
            ],
            "correta": "B) A alta solubilidade no estado hexavalente (U6+) e a baixa solubilidade no estado tetravalente (U4+)."
        },
        {
            "pergunta": "2. Qual é a abundância média de urânio na crosta continental superior?",
            "opcoes": ["A) 10,5 ppm.", "B) 2,7 ppm.", "C) 100 ppm.", "D) 0,7 ppm."],
            "correta": "B) 2,7 ppm."
        },
        {
            "pergunta": "3. Qual o isótopo de urânio que é físsil e utilizado diretamente em reatores de fissão convencionais?",
            "opcoes": [
                "A) 238U.",
                "B) 235U (que representa cerca de 0,7% do urânio natural).",
                "C) 232Th.",
                "D) 233U."
            ],
            "correta": "B) 235U (que representa cerca de 0,7% do urânio natural)."
        },
        {
            "pergunta": "4. A relação de produção de energia entre quantidades iguais de urânio natural e carvão é de aproximadamente:",
            "opcoes": ["A) 10 para 1.", "B) 100 para 1.", "C) 10.000 para 1.", "D) 1.000.000 para 1."],
            "correta": "C) 10.000 para 1."
        },
        {
            "pergunta": "5. Por que razão o urânio é considerado uma fonte de energia limpa no contexto das metas 'dual carbon'?",
            "opcoes": [
                "A) Porque é renovável como a energia solar.",
                "B) Porque é neutro em termos de efeito de estufa, não emitindo CO2 durante a geração.",
                "C) Porque não produz qualquer tipo de resíduo.",
                "D) Porque é encontrado em todas as rochas da superfície."
            ],
            "correta": "B) Porque é neutro em termos de efeito de estufa, não emitindo CO2 durante a geração."
        }
    ]

    quiz_depositos = [
        {
            "pergunta": "1. Depósitos em Arenitos: Qual é a forma característica de um depósito tipo 'roll-front' em corte transversal?",
            "opcoes": [
                "A) Um cilindro vertical perfeito.",
                "B) Uma forma de crescente ou meia-lua que corta a estratigrafia.",
                "C) Uma esfera isolada no centro do aquífero.",
                "D) Uma camada perfeitamente plana e horizontal."
            ],
            "correta": "B) Uma forma de crescente ou meia-lua que corta a estratigrafia."
        },
        {
            "pergunta": "2. Depósitos tipo Unconformity: Onde se localizam tipicamente os depósitos de urânio com os teores mais elevados do mundo?",
            "opcoes": [
                "A) No centro de vulcões ativos.",
                "B) Na interface entre um soco metamórfico e uma cobertura de arenitos proterozoicos.",
                "C) Em desertos arenosos modernos.",
                "D) No fundo dos oceanos."
            ],
            "correta": "B) Na interface entre um soco metamórfico e uma cobertura de arenitos proterozoicos."
        },
        {
            "pergunta": "3. Depósitos Intrusivos e Magmáticos: Como se comporta o urânio durante a cristalização de um magma?",
            "opcoes": [
                "A) Entra precocemente nos minerais de silicato comuns.",
                "B) É um elemento incompatível que se concentra nos magmas residuais tardios (ex: granitos e pegmatitos).",
                "C) Desaparece por evaporação térmica.",
                "D) Transforma-se imediatamente em chumbo."
            ],
            "correta": "B) É um elemento incompatível que se concentra nos magmas residuais tardios (ex: granitos e pegmatitos)."
        },
        {
            "pergunta": "4. Depósitos de Origem Hidrotermal e Metassomática: Qual é o intervalo de temperatura típico dos fluidos (brinas) que formam estes depósitos?",
            "opcoes": ["A) Entre 0°C e 20°C.", "B) Entre 70°C e 250°C.", "C) Acima de 1000°C.", "D) Exclusivamente a 500°C."],
            "correta": "B) Entre 70°C e 250°C."
        },
        {
            "pergunta": "5. Depósitos Superficiais e Sedimentares Específicos: O que causa a precipitação de urânio (como a carnotite) em depósitos de calcrete em ambientes áridos?",
            "opcoes": [
                "A) O arrefecimento súbito das águas termais.",
                "B) A evapotranspiração, que aumenta a concentração de urânio nas águas próximas da superfície.",
                "C) O impacto de meteoritos.",
                "D) A atividade vulcânica submarina."
            ],
            "correta": "B) A evapotranspiração, que aumenta a concentração de urânio nas águas próximas da superfície."
        }
    ]

    # Criação do formulário para o Quiz
    with st.form("quiz_uranio_form"):
        respostas_utilizador_geral = []
        respostas_utilizador_depositos = []
        
        st.subheader("Parte 1: Urânio em Geral")
        for i, q in enumerate(quiz_geral):
            resp = st.radio(q["pergunta"], q["opcoes"], key=f"ug_{i}", index=None)
            respostas_utilizador_geral.append(resp)
            st.write("---")
            
        st.subheader("Parte 2: Tipos de Depósitos Específicos")
        for i, q in enumerate(quiz_depositos):
            resp = st.radio(q["pergunta"], q["opcoes"], key=f"ud_{i}", index=None)
            respostas_utilizador_depositos.append(resp)
            st.write("---")

        # Botão de submissão
        submetido = st.form_submit_button("Verificar Respostas")

    # Lógica de validação fora do formulário
    if submetido:
        pontuacao_geral = 0
        pontuacao_depositos = 0
        
        st.divider()
        st.subheader("Resultados:")
        
        # Validação da Parte 1
        st.write("**Parte 1: Urânio em Geral**")
        for i, q in enumerate(quiz_geral):
            if respostas_utilizador_geral[i] == q["correta"]:
                pontuacao_geral += 1
            elif respostas_utilizador_geral[i] is None:
                st.warning(f"Pergunta {i+1} não respondida.")
            else:
                st.error(f"Pergunta {i+1}: Incorreta. A resposta certa era: {q['correta']}")
                
        st.success(f"Pontuação Geral: {pontuacao_geral} / {len(quiz_geral)}")
        
        # Validação da Parte 2
        st.write("**Parte 2: Tipos de Depósitos Específicos**")
        for i, q in enumerate(quiz_depositos):
            if respostas_utilizador_depositos[i] == q["correta"]:
                pontuacao_depositos += 1
            elif respostas_utilizador_depositos[i] is None:
                st.warning(f"Pergunta {i+1} não respondida.")
            else:
                st.error(f"Pergunta {i+1}: Incorreta. A resposta certa era: {q['correta']}")
                
        st.success(f"Pontuação Depósitos: {pontuacao_depositos} / {len(quiz_depositos)}")
        
        # Mensagem final consoante o resultado total
        pontuacao_total = pontuacao_geral + pontuacao_depositos
        if pontuacao_total == 10:
            st.balloons()
            st.success("Perfeito! Acertaste em tudo!")
        elif pontuacao_total >= 7:
            st.info("Muito bom resultado!")
        else:
            st.info("Podes sempre tentar novamente para melhorar a pontuação.")




# ===============================
# 3. QUIZ
# ===============================

def quiz_uranio(deposito):
    st.header("Quiz: Urânio")
    st.markdown("Teste os seus conhecimentos sobre as características gerais e os depósitos específicos de urânio.")

    # Converter a seleção para string (caso seja uma lista do multiselect)
    if not deposito:
        deposito_str = ""
    elif isinstance(deposito, list):
        deposito_str = " ".join(deposito).lower()
    else:
        deposito_str = deposito.lower()

    # Dicionário com as perguntas GERAIS (Aparecem sempre)
    quiz_geral = [
        {
            "pergunta": "1. Qual é a principal característica geoquímica que controla a formação da maioria dos depósitos de urânio?",
            "opcoes": [
                "A) A sua afinidade extrema com o oxigénio em qualquer estado.",
                "B) A alta solubilidade no estado hexavalente (U6+) e a baixa solubilidade no estado tetravalente (U4+).",
                "C) A sua capacidade de se fundir com o ferro no núcleo da Terra.",
                "D) O facto de ser um elemento quimicamente inerte."
            ],
            "correta": "B) A alta solubilidade no estado hexavalente (U6+) e a baixa solubilidade no estado tetravalente (U4+)."
        },
        {
            "pergunta": "2. Qual é a abundância média de urânio na crosta continental superior?",
            "opcoes": ["A) 10,5 ppm.", "B) 2,7 ppm.", "C) 100 ppm.", "D) 0,7 ppm."],
            "correta": "B) 2,7 ppm."
        },
        {
            "pergunta": "3. Qual o isótopo de urânio que é físsil e utilizado diretamente em reatores de fissão convencionais?",
            "opcoes": [
                "A) 238U.",
                "B) 235U (que representa cerca de 0,7% do urânio natural).",
                "C) 232Th.",
                "D) 233U."
            ],
            "correta": "B) 235U (que representa cerca de 0,7% do urânio natural)."
        },
        {
            "pergunta": "4. A relação de produção de energia entre quantidades iguais de urânio natural e carvão é de aproximadamente:",
            "opcoes": ["A) 10 para 1.", "B) 100 para 1.", "C) 10.000 para 1.", "D) 1.000.000 para 1."],
            "correta": "C) 10.000 para 1."
        },
        {
            "pergunta": "5. Por que razão o urânio é considerado uma fonte de energia limpa no contexto das metas 'dual carbon'?",
            "opcoes": [
                "A) Porque é renovável como a energia solar.",
                "B) Porque é neutro em termos de efeito de estufa, não emitindo CO2 durante a geração.",
                "C) Porque não produz qualquer tipo de resíduo.",
                "D) Porque é encontrado em todas as rochas da superfície."
            ],
            "correta": "B) Porque é neutro em termos de efeito de estufa, não emitindo CO2 durante a geração."
        }
    ]

    # Filtrar as perguntas dos DEPÓSITOS consoante a seleção
    quiz_depositos_filtrado = []

    if "arenito" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Depósitos em Arenitos: Qual é a forma característica de um depósito tipo 'roll-front' em corte transversal?",
            "opcoes": [
                "A) Um cilindro vertical perfeito.",
                "B) Uma forma de crescente ou meia-lua que corta a estratigrafia.",
                "C) Uma esfera isolada no centro do aquífero.",
                "D) Uma camada perfeitamente plana e horizontal."
            ],
            "correta": "B) Uma forma de crescente ou meia-lua que corta a estratigrafia."
        })
        
    if "unconformity" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Depósitos tipo Unconformity: Onde se localizam tipicamente os depósitos de urânio com os teores mais elevados do mundo?",
            "opcoes": [
                "A) No centro de vulcões ativos.",
                "B) Na interface entre um soco metamórfico e uma cobertura de arenitos proterozoicos.",
                "C) Em desertos arenosos modernos.",
                "D) No fundo dos oceanos."
            ],
            "correta": "B) Na interface entre um soco metamórfico e uma cobertura de arenitos proterozoicos."
        })

    if "hidrotermai" in deposito_str or "hidrotermal" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Depósitos de Origem Hidrotermal e Metassomática: Qual é o intervalo de temperatura típico dos fluidos (brinas) que formam estes depósitos?",
            "opcoes": ["A) Entre 0°C e 20°C.", "B) Entre 70°C e 250°C.", "C) Acima de 1000°C.", "D) Exclusivamente a 500°C."],
            "correta": "B) Entre 70°C e 250°C."
        })

    # (Mantive estas preparadas caso no futuro adiciones estas opções no menu principal do testestream2)
    if "intrusivo" in deposito_str or "magmático" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Depósitos Intrusivos e Magmáticos: Como se comporta o urânio durante a cristalização de um magma?",
            "opcoes": ["A) Entra precocemente nos minerais de silicato comuns.", "B) É um elemento incompatível que se concentra nos magmas residuais tardios (ex: granitos e pegmatitos).", "C) Desaparece por evaporação térmica.", "D) Transforma-se imediatamente em chumbo."],
            "correta": "B) É um elemento incompatível que se concentra nos magmas residuais tardios (ex: granitos e pegmatitos)."
        })

    if "superficia" in deposito_str or "sedimentar" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Depósitos Superficiais e Sedimentares Específicos: O que causa a precipitação de urânio (como a carnotite) em depósitos de calcrete em ambientes áridos?",
            "opcoes": ["A) O arrefecimento súbito das águas termais.", "B) A evapotranspiração, que aumenta a concentração de urânio nas águas próximas da superfície.", "C) O impacto de meteoritos.", "D) A atividade vulcânica submarina."],
            "correta": "B) A evapotranspiração, que aumenta a concentração de urânio nas águas próximas da superfície."
        })

    # Criação do formulário para o Quiz
    with st.form("quiz_uranio_form"):
        respostas_utilizador_geral = []
        respostas_utilizador_depositos = []
        
        st.subheader("Parte 1: Urânio em Geral")
        for i, q in enumerate(quiz_geral):
            resp = st.radio(q["pergunta"], q["opcoes"], key=f"ug_{i}", index=None)
            respostas_utilizador_geral.append(resp)
            st.write("---")
            
        # Só mostra a Parte 2 se houver perguntas específicas para o depósito escolhido
        if quiz_depositos_filtrado:
            st.subheader(f"Parte 2: Questões Específicas ({deposito})")
            for i, q in enumerate(quiz_depositos_filtrado):
                resp = st.radio(q["pergunta"], q["opcoes"], key=f"ud_{i}", index=None)
                respostas_utilizador_depositos.append(resp)
                st.write("---")
        else:
            st.info("💡 Seleciona um tipo de depósito específico no menu superior para desbloquear perguntas extra nesta secção!")

        # Botão de submissão
        submetido = st.form_submit_button("Verificar Respostas")

    # Lógica de validação fora do formulário
    if submetido:
        pontuacao = 0
        total_perguntas = len(quiz_geral) + len(quiz_depositos_filtrado)
        
        st.divider()
        st.subheader("Resultados:")
        
        st.write("**Parte 1: Urânio em Geral**")
        for i, q in enumerate(quiz_geral):
            if respostas_utilizador_geral[i] == q["correta"]:
                pontuacao += 1
            elif respostas_utilizador_geral[i] is None:
                st.warning(f"Pergunta Geral {i+1} não respondida.")
            else:
                st.error(f"Pergunta Geral {i+1}: Incorreta. A resposta certa era: {q['correta']}")
                
        if quiz_depositos_filtrado:
            st.write("**Parte 2: Depósitos Específicos**")
            for i, q in enumerate(quiz_depositos_filtrado):
                if respostas_utilizador_depositos[i] == q["correta"]:
                    pontuacao += 1
                elif respostas_utilizador_depositos[i] is None:
                    st.warning(f"Pergunta Específica {i+1} não respondida.")
                else:
                    st.error(f"Pergunta Específica {i+1}: Incorreta. A resposta certa era: {q['correta']}")
            
        st.success(f"Pontuação Final: {pontuacao} / {total_perguntas}")
        
        if pontuacao == total_perguntas and total_perguntas > 0:
            st.balloons()
            st.success("Perfeito! Acertaste em tudo!")
        elif pontuacao >= (total_perguntas * 0.7):
            st.info("Muito bom resultado!")
        else:
            st.info("Podes sempre tentar novamente para melhorar a pontuação.")

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
