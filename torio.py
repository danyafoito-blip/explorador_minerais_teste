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
# 3. QUIZ
# ===============================

def quiz_torio(deposito):
    st.header("📝 Quiz: Tório")
    st.markdown("Teste os seus conhecimentos sobre as características gerais e os depósitos específicos de tório.")

    # Converter a seleção para string (tal como nas características)
    if not deposito:
        deposito_str = ""
    elif isinstance(deposito, list):
        deposito_str = " ".join(deposito).lower()
    else:
        deposito_str = str(deposito).lower()

    # Dicionário com as perguntas GERAIS (Aparecem sempre)
    quiz_geral = [
        {
            "pergunta": "1. Qual é a abundância média do tório na crosta continental superior em comparação com o urânio?",
            "opcoes": [
                "A) O urânio é mais abundante que o tório.",
                "B) Ambos possuem a mesma abundância (2,7 ppm).",
                "C) O tório é cerca de 3 a 4 vezes mais abundante (10,5 ppm) que o urânio (2,7 ppm).",
                "D) O tório é 100 vezes mais abundante que o urânio."
            ],
            "correta": "C) O tório é cerca de 3 a 4 vezes mais abundante (10,5 ppm) que o urânio (2,7 ppm)."
        },
        {
            "pergunta": "2. Qual é o isótopo natural que constitui quase 100% do tório encontrado na natureza?",
            "opcoes": [
                "A) 235Th.",
                "B) 232Th.",
                "C) 233U.",
                "D) 230Th."
            ],
            "correta": "B) 232Th."
        },
        {
            "pergunta": "3. Como se comporta o tório durante o processo de cristalização de um magma (fase magmática)?",
            "opcoes": [
                "A) Entra facilmente nos minerais de silicato comuns.",
                "B) Desaparece devido à alta temperatura.",
                "C) Comporta-se como um elemento incompatível, concentrando-se nos fundidos residuais das fases tardias.",
                "D) Precipita imediatamente no início da fusão."
            ],
            "correta": "C) Comporta-se como um elemento incompatível, concentrando-se nos fundidos residuais das fases tardias."
        },
        {
            "pergunta": "4. No ciclo do combustível nuclear, o tório (232Th) é considerado um material 'fértil' porque, após absorver um neutrão, ele transmuta-se em:",
            "opcoes": [
                "A) 233U (um isótopo físsil).",
                "B) 238U.",
                "C) Plutónio-239.",
                "D) Chumbo estável."
            ],
            "correta": "A) 233U (um isótopo físsil)."
        },
        {
            "pergunta": "5. Qual é a principal característica geoquímica do tório em processos de superfície (meteorização)?",
            "opcoes": [
                "A) É altamente solúvel em água da chuva.",
                "B) É geoquimicamente inerte, permanecendo em minerais estáveis e formando depósitos de prazeres.",
                "C) Oxida-se rapidamente e evapora.",
                "D) Transforma-se em urânio solúvel."
            ],
            "correta": "B) É geoquimicamente inerte, permanecendo em minerais estáveis e formando depósitos de prazeres."
        }
    ]

    # Filtrar as perguntas dos DEPÓSITOS consoante a seleção do utilizador
    quiz_depositos_filtrado = []

    if "carbonatitos" in deposito_str or "alcalinos" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Carbonatitos e Complexos Alcalinos: O tório encontrado em carbonatitos, como no depósito de Bayan Obo (China), é geralmente extraído como:",
            "opcoes": [
                "A) O produto principal da mina.",
                "B) Subproduto da extração de Elementos de Terras Raras (REE) e nióbio.",
                "C) Um resíduo sem qualquer valor estratégico.",
                "D) Combustível líquido direto."
            ],
            "correta": "B) Subproduto da extração de Elementos de Terras Raras (REE) e nióbio."
        })
        
    if "placeres" in deposito_str or "paleoplaceres" in deposito_str or "sedimentares" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Placeres e Paleoplaceres: Qual é o mineral de fosfato mais comum que serve como a principal fonte de tório nestes depósitos de areias pesadas?",
            "opcoes": [
                "A) Uraninite.",
                "B) Bastnaesite.",
                "C) Monazite.",
                "D) Quartzo."
            ],
            "correta": "C) Monazite."
        })

    if "metamórficos" in deposito_str or "metamorficos" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Terrenos e Sistemas Metamórficos: O depósito de Tranomaro, em Madagáscar, é um exemplo de qual subtipo de depósito metamórfico/hidrotermal?",
            "opcoes": [
                "A) Depósito de roll-front.",
                "B) Skarn (formado pela interação de fluidos com rochas carbonatadas).",
                "C) Conglomerado de seixos de quartzo.",
                "D) Depósito de calcrete."
            ],
            "correta": "B) Skarn (formado pela interação de fluidos com rochas carbonatadas)."
        })

    if "granitos" in deposito_str or "pegmatitos" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Granitos Evoluídos e Pegmatitos: Por que razão o tório e o urânio são frequentemente enriquecidos em simultâneo nestes sistemas?",
            "opcoes": [
                "A) Porque ambos são solúveis em água fria.",
                "B) Devido ao seu comum grande raio iónico e carga elevada, que os impede de entrar em minerais comuns.",
                "C) Porque são os primeiros minerais a cristalizar no magma.",
                "D) Porque são atraídos pelo ferro no centro da intrusão."
            ],
            "correta": "B) Devido ao seu comum grande raio iónico e carga elevada, que os impede de entrar em minerais comuns."
        })

    if "alteração residual" in deposito_str or "alteracao" in deposito_str or "weathering" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Perfis de Alteração Residual: Como se forma a concentração de tório em depósitos como o de Mt. Weld (Austrália)?",
            "opcoes": [
                "A) Através de erupções vulcânicas subaquáticas.",
                "B) Por meteorização química intensa, onde minerais solúveis são removidos e o tório permanece concentrado no resíduo laterítico.",
                "C) Por precipitação em águas geladas.",
                "D) Por impacto de meteoritos ricos em metais pesados."
            ],
            "correta": "B) Por meteorização química intensa, onde minerais solúveis são removidos e o tório permanece concentrado no resíduo laterítico."
        })

    # Criação do formulário para o Quiz
    with st.form("quiz_torio_form"):
        respostas_utilizador_geral = []
        respostas_utilizador_depositos = []
        
        st.subheader("Parte 1: Tório em Geral")
        for i, q in enumerate(quiz_geral):
            resp = st.radio(q["pergunta"], q["opcoes"], key=f"tg_{i}", index=None)
            respostas_utilizador_geral.append(resp)
            st.write("---")
            
        # Só mostra a Parte 2 se houver perguntas específicas para o depósito escolhido
        if quiz_depositos_filtrado:
            st.subheader("Parte 2: Questões Específicas do Depósito")
            for i, q in enumerate(quiz_depositos_filtrado):
                resp = st.radio(q["pergunta"], q["opcoes"], key=f"td_{i}", index=None)
                respostas_utilizador_depositos.append(resp)
                st.write("---")
        else:
            st.info("💡 Seleciona um tipo de depósito específico no menu para desbloquear perguntas extra nesta secção!")

        # Botão de submissão
        submetido = st.form_submit_button("Verificar Respostas")

    # Lógica de validação (executada quando o botão é clicado)
    if submetido:
        pontuacao = 0
        total_perguntas = len(quiz_geral) + len(quiz_depositos_filtrado)
        
        st.divider()
        st.subheader("Resultados:")
        
        st.write("**Parte 1: Tório em Geral**")
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
# 4. CHECKLIST
# ===============================

def checklist_torio(deposito):
    st.header("✅ Checklist de Exploração: Tório")
    st.markdown("Utilize esta checklist para confirmar as principais características geológicas, mineralógicas e de campo durante a avaliação do recurso.")

    # Converter a seleção para string para garantir o funcionamento dos ifs
    if not deposito:
        deposito_str = ""
    elif isinstance(deposito, list):
        deposito_str = " ".join(deposito).lower()
    else:
        deposito_str = str(deposito).lower()

    # --- PARTE 1: GERAL ---
    st.subheader("Parte 1: Características Gerais do Tório")
    st.checkbox("**Radioatividade Natural:** O tório é um elemento radioativo natural de vida longa, cujas emissões gama podem ser detetadas com instrumentos portáteis, como cintilómetros ou contadores Geiger.")
    st.checkbox("**Afinidade com Oxigénio (Litófilo):** O tório ocorre quase exclusivamente na forma de óxidos ou sais oxigenados (fosfatos, silicatos, carbonatos), nunca formando sulfuretos ou selenetos.")
    st.checkbox("**Propriedades Físicas do Metal:** Se observado como metal puro (raro em estado natural), apresenta uma cor branco-prateada que se torna cinzenta sob exposição atmosférica, sendo relativamente macio e muito denso (11,72 g/cm³).")
    st.checkbox("**Incompatibilidade Magmática:** Procure evidências de enriquecimento em rochas ácidas, pegmatíticas e alcalinas, uma vez que o tório permanece nos fundidos residuais durante a evolução magmática.")
    st.checkbox("**Inércia em Superfície:** Devido à sua natureza quimicamente inerte, o tório é transportado mecanicamente dentro da rede cristalina de minerais resistentes à meteorização, como a monazite.")

    st.divider()

    # --- PARTE 2: ESPECÍFICA ---
    st.subheader("Parte 2: Critérios Específicos do Depósito")
    
    # Variável para controlar se mostramos a mensagem de "selecione um depósito"
    mostrou_especifico = False

    if "carbonatitos" in deposito_str or "alcalinos" in deposito_str:
        mostrou_especifico = True
        st.markdown("### Carbonatitos e Complexos Alcalinos")
        st.checkbox("**Matriz Carbonatada:** Mineralização hospedada em rochas ígneas ricas em minerais de carbonato (>50%), como calcite, dolomite e ankerite.")
        st.checkbox("**Associação com REE e Nb:** Presença frequente de minerais de Elementos de Terras Raras (bastnaesite, monazite) e nióbio (pirocloro), sendo o tório muitas vezes um subproduto destes depósitos.")
        st.checkbox("**Minerais Indicadores:** Presença de monazite, thorite, thorianite, allanite e bastnaesite dentro da massa rochosa.")
        st.checkbox("**Texturas Disseminadas ou em Veios:** O minério pode ocorrer como cristais disseminados (ex: monazite em dolomite) ou preenchendo net de filões e fraturas.")
        st.checkbox("**Metassomatismo:** Evidência de intensa alteração hidrotérmica nas rochas encaixantes, frequentemente apresentando substituição sódica e de flúor.")

    if "placeres" in deposito_str or "paleoplaceres" in deposito_str or "sedimentares" in deposito_str:
        mostrou_especifico = True
        st.markdown("### Placeres e Paleoplaceres (Depósitos Sedimentares de Superfície)")
        st.checkbox("**Areias Pesadas (Black Sands):** Concentrações mecânicas de minerais densos em ambientes de praia, rios ou dunas, frequentemente apresentando camadas escuras devido à presença de ilmenite e magnetite.")
        st.checkbox("**Presença de Monazite Detrítica:** A monazite é o principal mineral portador de tório nestes depósitos, ocorrendo como grãos amarelos a castanho-amarelados misturados com quartzo.")
        st.checkbox("**Resistência Química:** Os minerais de tório nestes depósitos devem exibir formas angulares a sub-angulares, indicando transporte a partir de fontes próximas e resistência à meteorização química.")
        st.checkbox("**Minerais Associados de Valor Industrial:** Coexistência com minerais como zircão, rutilo, ilmenite, cassiterite, granada e estaurolite.")
        st.checkbox("**Conglomerados Antigos (Paleoplaceres):** No caso de depósitos pré-câmbricos, o tório e o urânio ocorrem em conglomerados de seixos de quartzo ricos em pirite, onde a uraninite clástica pode conter vários pontos percentuais de tório.")

    if "metamórficos" in deposito_str or "metamorficos" in deposito_str:
        mostrou_especifico = True
        st.markdown("### Terrenos e Sistemas Metamórficos")
        st.checkbox("**Hospedeiros Metamórficos:** Ocorrência em gnaisses, xistos, migmatitos e quartzitos de alto grau, onde o tório se concentrou durante processos de metasomatismo ou recristalização.")
        st.checkbox("**Controlo em Planos de Foliação:** Minerais de tório frequentemente distribuídos ao longo de planos de xistosidade, fraturas ou juntas.")
        st.checkbox("**Texturas de Skarn:** Mineralização associada a minerais como diópsido, calcite, wollastonite e espinela, resultante da interação de fluidos graníticos com mármores.")
        st.checkbox("**Auréolas Radiogénicas:** Observação de halos de radiação em torno de minerais de tório (como thorianite) quando incluídos em minerais vizinhos.")
        st.checkbox("**Associações Complexas:** Presença de elementos como Mo, Bi, Zr, Sn e W associados ao tório em zonas de contacto metasomático.")

    if "granitos" in deposito_str or "pegmatitos" in deposito_str:
        mostrou_especifico = True
        st.markdown("### Granitos Evoluídos e Pegmatitos")
        st.checkbox("**Rochas Felsicas e Leucocráticas:** Enriquecimento em granitos peralcalinos, leuco-granitos e pegmatitos altamente fracionados.")
        st.checkbox("**Sincronismo U-Th:** Em sistemas de alta temperatura, o tório ocorre frequentemente associado ao urânio na uraninite (pechblenda), com teores de tório que podem atingir vários pontos percentuais.")
        st.checkbox("**Minerais Acessórios Radioativos:** Identificação de uranothorite, brannerite, allanite e xenotime dentro da matriz granítica ou pegmatítica.")
        st.checkbox("**Concentração em Magmas Residuais:** Mineralização frequentemente localizada em zonas tardias de cristalização, como vugues ou zonas de substituição dentro de corpos ígneos.")
        st.checkbox("**Variedade de Cores:** Minerais como a monazite nestes granitos podem apresentar cores variadas, de incolor a esverdeado ou acastanhado em secções finas.")

    if "alteração residual" in deposito_str or "alteracao" in deposito_str or "weathering" in deposito_str:
        mostrou_especifico = True
        st.markdown("### Perfis de Alteração Residual (Weathering Crusts)")
        st.checkbox("**Resíduos Lateríticos:** Concentrações de tório em solos e crostas de meteorização intensas, formadas pela remoção química de Ca e Mg da rocha original (frequentemente carbonatitos).")
        st.checkbox("**Minerais Secundários Porosos:** Presença de agregados porosos de monazite secundária e minerais do grupo da crandallite e goyazite.")
        st.checkbox("**Associação com Óxidos de Ferro:** O tório e as terras raras ficam retidos em massas de goethite e limonite que compõem a crosta de meteorização.")
        st.checkbox("**Adsorção em Argilas:** Uma parte significativa do tório pode estar adsorvida em minerais de argila (como caulinite ou ilite) formados durante a alteração das rochas primárias.")
        st.checkbox("**Texturas Biomórficas/Coloformes:** Em alguns depósitos supergénicos, o minério pode apresentar estruturas globulares coloformes ou tubos microscópicos indicativos de processos de baixa temperatura.")

    if not mostrou_especifico:
        st.info("💡 Seleciona um tipo de depósito específico no menu principal para visualizar os critérios de campo detalhados desta secção.")

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
