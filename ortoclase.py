import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_ortoclase(deposito):

    st.markdown("### ⛰️ Características da Ortoclase")

    col1, col2 = st.columns(2)

    # Verificação de segurança
    if not deposito:
        st.warning("Por favor, seleciona um tipo de depósito para visualizar as características.")
        return

    if isinstance(deposito, list):
        deposito = ", ".join(deposito)
    
    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- **Composição Química:** Silicato de alumínio e potássio (KAlSi₃O₈), podendo conter pequenas quantidades de sódio.")
        st.write("- **Estrutura Cristalina:** Pertence aos tectossilicatos, com tetraedros formando uma rede complexa.")
        st.write("- **Hábito e Simetria:** Monoclínica, exibindo frequentemente microtextura tipo 'tweed'.")
        st.write("- **Clivagem e Dureza:** Duas direções de clivagem perfeitas a 90º; dureza de 6 a 6,5 (Mohs).")
        st.write("- **Comportamento Térmico:** Baixo ponto de fusão, atuando como agente fundente essencial.")

    with col2:

        st.info("**Importância Energética**")

        st.write("- **Minerais Radioativos:** Em pegmatitos, pode hospedar uraninite e thorianite (combustível nuclear).")
        st.write("- **Lítio e Baterias:** Ocorre associada a pegmatitos LCT (fontes primárias de lítio).")
        st.write("- **Isolamento Térmico/Elétrico:** Fabrico de porcelanas e isoladores para redes de energia.")
        st.write("- **Geocronologia (K/Ar):** Datação potássio-árgon para mapear histórias térmicas de bacias.")
        st.write("- **Eficiência Industrial:** Reduz a temperatura de fusão de vidro/cerâmica, poupando energia.")
    
    st.divider()

    # 1. Pegmatitos Graníticos
    if "Pegmatitos" in deposito or "Pegmatito" in deposito:
        st.markdown("## 1. Pegmatitos Graníticos")
        
        st.success(
            "Corpos ígneos caracterizados por cristais de dimensões anómalas, fontes vitais de feldspatos de elevada pureza."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.warning(
            "Formam-se na fase final da cristalização de magmas graníticos."
        )
        st.write("- A concentração de voláteis nestes estágios permite o crescimento de cristais gigantes de ortoclase.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- **Método:** Extração em pedreiras (frequentemente a céu aberto).")
        st.write("- **Processamento:** Inclui britagem e separação magnética para remover minerais de ferro, como a biotite.")

    # 2. Granitoides Félsicos
    elif "Granitoides" in deposito or "Granitos" in deposito or "Félsicos" in deposito:
        st.markdown("## 2. Granitoides Félsicos")
        
        st.success(
            "Rochas ígneas plutónicas onde os feldspatos potássicos dominam a composição mineralógica."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.info(
            "Resultam da solidificação de intrusões magmáticas leucocráticas."
        )
        st.write("- Muitas vezes sofrem processos de feldspatização secundária (metassomatismo), que enriquece a rocha encaixante em potássio.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- **Método:** Exploração mecanizada em larga escala.")
        st.write("- **Processamento:** A matéria-prima é submetida a moagem fina e classificação granulométrica específica para uso cerâmico.")

    # 3. Depósitos Metamórficos
    elif "Metamórficos" in deposito or "Metamorfismo" in deposito:
        st.markdown("## 3. Depósitos Metamórficos")
        
        st.success(
            "Associações rochosas formadas a grandes profundidades sob regimes de pressão e temperatura elevados, como os ortognaisses."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.warning(
            "A ortoclase forma-se muitas vezes pela decomposição de micas (como a biotite e a muscovite)."
        )
        st.write("- Ocorrem de forma pronunciada em condições de alta temperatura (fácies granulito).")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- **Método:** Mineração direta de rochas consolidadas (ex: ortognaisses).")
        st.write("- **Processamento:** Envolve separação magnética a seco de alta intensidade para garantir a máxima pureza química do feldspato.")

    # 4. Acumulações Sedimentares
    elif "Sedimentares" in deposito or "Areias" in deposito or "residuais" in deposito.lower() or "Acumulações" in deposito:
        st.markdown("## 4. Acumulações Sedimentares")
        
        st.success(
            "Concentrações detríticas conhecidas comercialmente como 'areias feldspáticas', muito procuradas pela indústria vidreira."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.info(
            "Resultam da erosão agressiva de granitos seguida de transporte fluvial."
        )
        st.write("- Os grãos de ortoclase acumulam-se em paleocanais, depósitos de praia ou terraços como areias ricas em feldspato.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- **Método:** Muitas vezes extraídas em meio aquático (em lagos ou leitos de rios) através de dragas de sucção.")
        st.write("- **Processamento:** Foca-se predominantemente em operações de lavagem vigorosa e triagem por densidade.")

    # 5. Veios Hidrotermais
    elif "Hidrotermais" in deposito or "Veios" in deposito:
        st.markdown("## 5. Veios Hidrotermais")
        
        st.success(
            "Ocorrências que frequentemente albergam a variedade cristalina translúcida conhecida como 'adulária'."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.warning(
            "A variedade adulária forma-se por precipitação de fluidos hidrotermais."
        )
        st.write("- Estes fluidos circulam em fendas e cavidades nas rochas a temperaturas relativamente baixas, onde o mineral precipita livremente.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- **Método:** Exploração geralmente mais localizada e de escala reduzida (frequentemente manual ou semi-mecanizada).")
        st.write("- **Processamento:** É bastante simplificado, maioritariamente focado na limpeza de impurezas superficiais e moagem seletiva.")

    else:
        st.info("Selecione um tipo de depósito válido para visualizar a informação.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_ortoclase():

    st.markdown("### ⚠️ Confusões Comuns e Mitos")

    st.warning("Existem várias ideias erradas e ambiguidades comuns na identificação e estudo da ortoclase.")

    st.markdown("#### 🔍 Os 5 Mitos e Confusões")

    st.markdown("**1. Confusão entre Ortoclase e Quartzo**")
    st.write("- Em rochas vulcânicas ou pegmatitos, a ortoclase pode ser facilmente confundida com o quartzo por se apresentar límpida e ter uma clivagem pouco visível a olho nu.")
    st.write("- **Distinção:** A identificação segura exige a observação da natureza biaxial ou a presença de microporos sob o microscópio petrográfico.")

    st.markdown("**2. O Mito do Arrefecimento como Único Controlo**")
    st.write("- É falso assumir que a taxa de arrefecimento magmático é o único fator a ditar a transição da ortoclase para microclina.")
    st.write("- **A Realidade:** A presença de fluidos e a deformação mecânica são fundamentais no processo; sem a influência destes, a ortoclase pode persistir intacta mesmo em rochas antigas do Arcaico.")

    st.markdown("**3. A Ambiguidade do Nome \"Ortoclase\"**")
    st.write("- Na literatura geológica, o termo é frequentemente utilizado de forma ambígua.")
    st.write("- Pode referir-se ao **componente químico teórico** (KAlSi₃O₈) presente em soluções sólidas.")
    st.write("- Em alternativa, pode designar o **mineral monoclínico específico** que exibe uma microtextura interna complexa em xadrez (tipo \"tweed\").")

    st.markdown("**4. O Mito da Estabilidade a Baixa Temperatura**")
    st.write("- A ortoclase é, na verdade, **metaestável** a temperaturas abaixo dos 480°C – 500°C.")
    st.write("- Nestas condições, a fase mineralógica perfeitamente estável deveria ser a microclina. No entanto, a ortoclase consegue \"sobreviver\" porque a sua própria estrutura cristalina bloqueia a reorganização atómica que seria necessária para a transição.")

    st.markdown("**5. Interpretação Errada da Extinção Ondulante**")
    st.write("- Na observação microscópica, a extinção ondulante na ortoclase é quase sempre interpretada de imediato (e erradamente) como prova exclusiva de que a rocha sofreu forte deformação mecânica.")
    st.write("- Contudo, este fenómeno ótico pode ser simplesmente o resultado de **misturas sub-óticas (à nanoescala)** de domínios estruturais de ortoclase e microclina a coexistirem dentro do mesmo cristal.")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_ortoclase(deposito):
    st.header("🧠 Quiz: Ortoclase")
    st.markdown("Testa os teus conhecimentos sobre as características gerais e os depósitos específicos de ortoclase.")

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
            "pergunta": "1. Qual é a fórmula química teórica que define a ortoclase?",
            "opcoes": [
                "A) NaAlSi₃O₈",
                "B) KAlSi₃O₈",
                "C) CaAl₂Si₂O₈",
                "D) Mg₂SiO₄"
            ],
            "correta": "B) KAlSi₃O₈"
        },
        {
            "pergunta": "2. A ortoclase pertence a que grupo estrutural de silicatos (caracterizado por uma rede 3D de tetraedros)?",
            "opcoes": [
                "A) Filossilicatos (micas)",
                "B) Tectossilicatos (feldspatos)",
                "C) Inossilicatos (piroxenas)",
                "D) Nesossilicatos (olivinas)"
            ],
            "correta": "B) Tectossilicatos (feldspatos)"
        },
        {
            "pergunta": "3. Qual é o sistema cristalino característico da ortoclase, que a distingue da microclina?",
            "opcoes": [
                "A) Monoclínico",
                "B) Triclínico",
                "C) Cúbico",
                "D) Hexagonal"
            ],
            "correta": "A) Monoclínico"
        },
        {
            "pergunta": "4. Na indústria do vidro, qual é a principal função dos componentes alcalinos da ortoclase?",
            "opcoes": [
                "A) Atuar como pigmento para dar cor verde",
                "B) Aumentar a dureza final do vidro para o tornar inquebrável",
                "C) Reduzir a temperatura de fusão do quartzo (agente fundente)",
                "D) Substituir completamente a sílica na mistura"
            ],
            "correta": "C) Reduzir a temperatura de fusão do quartzo (agente fundente)"
        },
        {
            "pergunta": "5. Qual é o valor aproximado da dureza da ortoclase na escala de Mohs?",
            "opcoes": [
                "A) 3",
                "B) 6",
                "C) 8",
                "D) 10"
            ],
            "correta": "B) 6"
        }
    ]

    # Filtrar as perguntas dos DEPÓSITOS consoante a seleção
    quiz_depositos_filtrado = []

    if "pegmatito" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Pegmatitos Graníticos: Nos pegmatitos graníticos, qual é a característica textural que facilita a extração industrial de ortoclase?",
            "opcoes": [
                "A) O grão extremamente fino e homogéneo",
                "B) A presença de cristais gigantes e zonas mineralógicas distintas",
                "C) A rocha ser composta apenas por minerais escuros e pesados",
                "D) A ortoclase estar sempre misturada com argilas moles"
            ],
            "correta": "B) A presença de cristais gigantes e zonas mineralógicas distintas"
        })
        
    if "granit" in deposito_str or "félsico" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Granitoides Félsicos: Com o avanço tecnológico, que tipo de rochas magmáticas de grão mais fino passaram a ser exploradas como alternativa aos pegmatitos?",
            "opcoes": [
                "A) Granitos leucocráticos e aplitos",
                "B) Basaltos ricos em ferro",
                "C) Rochas vulcânicas ultramáficas",
                "D) Calcários cristalinos"
            ],
            "correta": "A) Granitos leucocráticos e aplitos"
        })

    if "metamórfic" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Depósitos Metamórficos: Em rochas metamórficas de alto grau (como gnaisses e granulitos), a ortoclase é frequentemente produzida através da instabilidade e decomposição de que grupo de minerais?",
            "opcoes": [
                "A) Carbonatos, como a calcite",
                "B) Micas, como a biotite e a muscovite",
                "C) Sulfuretos, como a pirite",
                "D) Zeólitos, como a natrolite"
            ],
            "correta": "B) Micas, como a biotite e a muscovite"
        })

    if "sedimentar" in deposito_str or "acumulações" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Acumulações Sedimentares: Em acumulações sedimentares, em que tipo de ambiente geológico se costuma concentrar o feldspato potássico economicamente viável?",
            "opcoes": [
                "A) No fundo de fossas oceânicas",
                "B) Em paleocanais de rios e terraços aluvionares",
                "C) Em dunas de deserto compostas por areia pura de sílica",
                "D) Em depósitos de carvão profundo"
            ],
            "correta": "B) Em paleocanais de rios e terraços aluvionares"
        })

    if "hidrotermai" in deposito_str or "hidrotermal" in deposito_str or "veio" in deposito_str:
        quiz_depositos_filtrado.append({
            "pergunta": "Veios Hidrotermais: Que variedade específica de ortoclase é característica de veios hidrotermais de baixa temperatura e apresenta um hábito de cristal próprio ({110})?",
            "opcoes": [
                "A) Sanidina",
                "B) Adulária",
                "C) Anortite",
                "D) Microclina"
            ],
            "correta": "B) Adulária"
        })

    # Criação do formulário para o Quiz
    with st.form("quiz_ortoclase_form"):
        respostas_utilizador_geral = []
        respostas_utilizador_depositos = []
        
        st.subheader("Parte 1: A Ortoclase em Geral")
        for i, q in enumerate(quiz_geral):
            # Usar 'oq_g_' como chave para garantir que é única (Ortoclase Quiz Geral)
            resp = st.radio(q["pergunta"], q["opcoes"], key=f"oq_g_{i}", index=None)
            respostas_utilizador_geral.append(resp)
            st.write("---")
            
        # Só mostra a Parte 2 se houver perguntas específicas para o depósito escolhido
        if quiz_depositos_filtrado:
            st.subheader(f"Parte 2: Questões Específicas ({deposito})")
            for i, q in enumerate(quiz_depositos_filtrado):
                # Usar 'oq_d_' como chave para garantir que é única (Ortoclase Quiz Depósitos)
                resp = st.radio(q["pergunta"], q["opcoes"], key=f"oq_d_{i}", index=None)
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
        
        st.write("**Parte 1: A Ortoclase em Geral**")
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
            st.success("Perfeito! Acertaste em tudo! 🎉")
        elif pontuacao >= (total_perguntas * 0.7):
            st.info("Muito bom resultado! 👍")
        else:
            st.info("Podes sempre rever a informação nas secções acima e tentar novamente. 💪")
# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_ortoclase():

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado na identificação de ortoclase:")

    st.checkbox("Observar clivagem em 2 direções")
    st.checkbox("Testar dureza (~6 Mohs)")
    st.checkbox("Identificar cor típica (rosa/branco)")
    st.checkbox("Associar a granitos/pegmatitos")
    st.checkbox("Distinguir de quartzo")
    st.checkbox("Verificar alteração para argilas")
    st.checkbox("Recolher amostras")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_ortoclase():

    st.markdown("### 🌍 Mapa Global de Depósitos de Ortoclase")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="ortoclase_map"
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
                <b>Local:</b> {row.get('Field Name','N/A')}<br>
                <b>País:</b> {row.get('Country','N/A')}<br>
                <b>Tipo:</b> {row.get('Type','N/A')}
                """

                folium.CircleMarker(
                    [row["Latitude"], row["Longitude"]],
                    radius=5,
                    color="pink",
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

def referencias_ortoclase():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- Deer, Howie & Zussman – Rock-Forming Minerals")
    st.write("- Klein & Dutrow – Manual of Mineral Science")
    st.write("- USGS – Feldspar Data")
    st.write("- British Geological Survey – Industrial Minerals")
    st.write("- IMA – Mineral Database")

    st.caption("Fontes científicas sobre feldspatos e ortoclase.")
