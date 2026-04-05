# ===============================
# BIBLIOTECAS EXTERNAS
# ===============================

import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium

# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_quartzo(deposito):

    st.markdown("### Quartzo")
    
    st.markdown(
    """
    O **quartzo** é o polimorfo mais importante da sílica (**SiO₂**) 
    e um dos minerais mais abundantes e puros da crosta terrestre.  
    
    Ocorre principalmente em duas formas:
    - **Quartzo-α** → sistema trigonal, estável à superfície  
    - **Quartzo-β** → sistema hexagonal, estável acima de ~573°C  

    A transformação entre estas formas é **reversível**.
    """
    )
    
    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades físicas**")

        st.write("- Sólido cristalino, geralmente transparente a translúcido")
        st.write("- Rede tridimensional de tetraedros [SiO₄]⁴⁻")
        st.write("- Sistema trigonal (quartzo-α) e hexagonal (quartzo-β)")
        st.write("- Densidade de cerca de 2,65 g/cm³ (α) e 2,51 g/cm³ (β)")
        st.write("- Mineral uniaxial com propriedades ópticas características")
        st.write("- Dureza 7 na escala de Mohs")
        st.write("- Pode apresentar luminescência (azul ou vermelha)")
        st.write("- Grande variedade de cores (ametista, citrino, fumado, rosa)")

    with col2:

        st.info("**Propriedades químicas**")

        st.write("- Dióxido de silício (SiO₂) com elevada pureza")
        st.write("- Impurezas extremamente baixas, geralmente inferiores a 1 ppm")
        st.write("- Presença frequente de alumínio na estrutura")
        st.write("- Elementos traço como ferro, titânio, germânio, gálio, boro e fósforo")
        st.write("- Substituições iónicas na rede cristalina")
        st.write("- Iões leves podem ocupar posições intersticiais (H⁺, Li⁺, Na⁺, K⁺)")
        st.write("- Defeitos estruturais responsáveis por cor e propriedades ópticas")
        st.write("- Elevada estabilidade química e resistência a agentes externos")

    st.divider()

    if "Veios hidrotermais" in deposito:
        
        st.markdown("### Veios hidrotermais")
        
        st.write(
        """
        Os **veios hidrotermais de quartzo** resultam do preenchimento de fraturas 
        por soluções aquosas quentes ricas em sílica. Estes sistemas variam 
        desde ambientes rasos e frios até condições profundas e de alta temperatura.
        
        **Classificação:**
        
        **Epitermais**
        - **Temperatura:** 100–300 °C
        - **Profundidade:** < 2 km
        
        **Mesotermais**
        - **Temperatura:** 200–400 °C
        - **Profundidade:** 6–12 km
        
        **Hipotermais**
        - **Temperatura:** > 475 °C
        - **Profundidade:** > 12 km
        """
        )
        
        st.divider()
        
        st.markdown("### Geração dos fluidos hidrotermais")
        
        st.write(
        """
        Os **fluidos hidrotermais** podem ter origem:
        
        - **Magmática** (libertação de voláteis)
        - **Metamórfica** (desidratação de rochas)
        - **Meteórica** (infiltração de água superficial)
        - **Intersticial** (água retida em sedimentos)
        
        A circulação é controlada por **gradientes térmicos** e estruturas como 
        **falhas** e **zonas de cisalhamento**.
        """
        )
        
        st.divider()
        
        st.markdown("### Processos de formação do quartzo")
        
        st.write(
        """
        O **quartzo** precipita a partir de soluções supersaturadas em sílica.
        
        **Fatores principais:**
        
        - **Diminuição da temperatura**
        - **Ebulição dos fluidos** (separação de fases)
        - **Mistura de fluidos quentes e frios**
        - **Variações de pH**
        
        Estes processos reduzem a **solubilidade da sílica** e promovem a deposição.
        """
        )
        
        st.divider()
        
        st.markdown("### Transporte de sílica")
        
        st.write(
        """
        A **sílica** é transportada como complexos aquosos (**SiO₂(aq)**).
        
        - A solubilidade **aumenta com a temperatura**
        - **Diminui com arrefecimento e descompressão**
        
        A ascensão do fluido provoca **precipitação** e formação de veios.
        """
        )
        
        st.divider()
        
        st.markdown("### Condições físico-químicas")
        
        st.write(
        """
        - **Temperatura:** 150°C a 700°C
        - **Pressão:** <1 a 5 kbar
        - **Salinidade:** variável (baixa a hipersalina)
        
        O sistema alterna entre:
        
        - **Regime litostático** (profundo)
        - **Regime hidrostático** (fraturação)
        
        Este ciclo promove **deposição repetida de quartzo**.
        """
        )
        
        st.divider()
        
        st.markdown("### Estruturas e texturas")
        
        st.write(
        """
        O quartzo pode ocorrer como:
        
        - **Veios:** preenchimento de fraturas
        - **Stockworks:** redes de microveios
        - **Brechas:** fragmentos cimentados por quartzo
        
        **Texturas típicas:**
        
        - **Bandada** (crustiforme/coloforme)
        - **Drusas** (cristais em cavidades)
        - **Maciça** (sem zonamento)
        """
        )
        
        st.divider()
        
        st.markdown("### Ambientes geológicos")
        
        st.write(
        """
        Associados a contextos tectónicos convergentes:
        
        - **Arcos magmáticos**
        - **Cinturões orogénicos**
        
        A deformação tectónica facilita a **circulação de fluidos** e criação de espaço.
        """
        )
        
        st.divider()
        
        st.markdown("### Condições que favorecem a formação")
        
        st.write(
        """
        - **Fraturação da rocha encaixante** (hidrofraturação)
        - **Fluxo contínuo de fluidos**
        - **Gradientes térmicos acentuados**
        
        Estas condições permitem **acumulação significativa de quartzo**.
        """
        )
        
    elif "Depósitos sedimentares" in deposito:

        st.markdown("### Depósitos sedimentares")

        st.write(
        """
        Os depósitos sedimentares ricos em quartzo correspondem a acumulações onde o 
        **quartzo é o mineral dominante**, ocorrendo sobretudo em rochas clásticas 
        como **arenitos e metagrauvaques**.

        Distinção fundamental:
        - **Quartzo detrítico** → proveniente da erosão de rochas pré-existentes  
        - **Quartzo autigénico** → precipitado in situ durante a diagénese  
        """
        )

        st.divider()

        st.markdown("### Origem do quartzo")

        st.write(
        """
        A origem está associada à **meteorização de rochas silicáticas**.

        O quartzo destaca-se por:
        - Elevada **resistência química**
        - Elevada **resistência mecânica**
        
        Resiste ao transporte enquanto outros minerais (ex: feldspatos) são destruídos.
        """
        )

        st.divider()

        st.markdown("### Processos sedimentares")

        st.write(
        """
        O quartzo é transportado por diferentes sistemas:

        - **Fluvial**
        - **Eólico**
        - **Marinho**

        Controlos principais:
        - Energia do meio → seleção granulométrica  
        - Transporte prolongado → aumento da maturidade sedimentar  

        Resultados:
        - Grãos mais **arredondados**
        - Remoção de minerais instáveis  
        - Preservação de estruturas como:
          - Estratificação cruzada
          - Estratificação gradacional
        """
        )

        st.divider()

        st.markdown("### Ciclo do quartzo")

        st.write(
        """
        O quartzo participa num **ciclo sedimentar contínuo**:

        Erosão → Transporte → Deposição → Litificação → Reexposição

        Importância:
        - Preserva **assinaturas químicas**
        - Mantém **defeitos estruturais**
        
        ➜ Permite determinar a **proveniência das rochas-mãe**
        """
        )

        st.divider()

        st.markdown("### Diagénese")

        st.write(
        """
        Durante o soterramento ocorrem:

        - **Compactação**
        - **Cimentação**

        Formação de quartzo autigénico:
        - Sobrecrescimentos (overgrowths)
        - Crescimento contínuo sobre grãos detríticos

        Impacto:
        - Redução da **porosidade**
        - Alteração da **permeabilidade**
        """
        )

        st.divider()

        st.markdown("### Condições físico-químicas")

        st.write(
        """
        Controladas por:
        - Temperatura
        - Pressão
        - Química dos fluidos intersticiais

        Quartzo de baixa temperatura (<250°C):
        - Maior densidade de defeitos estruturais

        Influência química:
        - pH e salinidade controlam incorporação de:
          - Alumínio (Al)
          - Hidrogénio (H)
        """
        )

        st.divider()

        st.markdown("### Ambientes geológicos")

        st.write(
        """
        Principais ambientes de deposição:

        - Sistemas fluviais e deltas  
        - Praias e plataformas marinhas  
        - Ambientes desérticos  

        Características:
        - Alta energia → seleção e limpeza dos grãos  
        - Formação de:
          - Arenitos quartzosos
          - Quartzitos (em metamorfismo)
        """
        )

        st.divider()

        st.markdown("### Condições que favorecem a formação")

        st.write(
        """
        Para acumulação significativa de quartzo:

        **Meteorização intensa**
        - Climas quentes e húmidos

        **Elevada maturidade sedimentar**
        - Ciclos repetidos de erosão e deposição

        **Ambientes tectonicamente estáveis**
        - Margens passivas
        - Bacias intracratónicas

        ➜ Favorecem depósitos **puros e bem selecionados**
        """
        )

    elif "Depósitos magmáticos" in deposito:

        st.markdown("### Depósitos magmáticos")

        st.write(
        """
        Os depósitos magmáticos de quartzo formam-se quando a **sílica (SiO₂)** 
        se torna um componente dominante durante a cristalização de um magma.

        Relação fundamental:
        - Rochas **félsicas** → ricas em sílica → quartzo abundante  
        - Rochas **máficas** → pobres em sílica → quartzo raro ou ausente  
        """
        )

        st.divider()

        st.markdown("### Geração do quartzo magmático")

        st.write(
        """
        O quartzo forma-se a partir de **magmas saturados em sílica**.

        Processo chave:
        - **Diferenciação magmática**
        - **Fracionamento cristalino**

        ➜ Minerais pobres em sílica cristalizam primeiro  
        ➜ O magma residual torna-se progressivamente mais rico em SiO₂  

        Resultado:
        - Formação de quartzo em estágios tardios
        - Desenvolvimento extremo em **pegmatitos graníticos**
        """
        )

        st.divider()

        st.markdown("### Processos de cristalização")

        st.write(
        """
        Na **Série de Bowen**, o quartzo é um dos últimos minerais a cristalizar.

        Formação:
        - A partir de líquidos residuais ricos em sílica
        - Após cristalização de feldspatos e minerais ferromagnesianos

        Transformação estrutural:
        - Quartzo-β (alta temperatura)
        - Quartzo-α (<573°C)

        Modos de ocorrência:
        - Fenocristais (em rochas vulcânicas)
        - Grãos intersticiais (em rochas plutónicas)
        """
        )

        st.divider()

        st.markdown("### Transporte e evolução do magma")

        st.write(
        """
        O magma ascende através de:
        - Diques
        - Intrusões magmáticas

        Dinâmica:
        - Velocidade de ascensão pode atingir ~0,015 m/s
        - Associada a regimes de hidrofraturação

        Processos evolutivos:
        - Mistura de magmas
        - Assimilação crustal

        ➜ Produzem assinaturas químicas e zonamento nos cristais de quartzo
        """
        )

        st.divider()

        st.markdown("### Condições físico-químicas")

        st.write(
        """
        Temperatura:
        - Formação típica ~750°C (ex: riólitos)

        Pressão e voláteis:
        - Controlam incorporação de elementos como Ti

        Química do magma:
        - Evolução de **metaluminoso → peraluminoso**
        - Aumenta incorporação de Al na estrutura do quartzo

        ➜ A composição do magma controla diretamente as impurezas no quartzo
        """
        )

        st.divider()

        st.markdown("### Texturas e estruturas")

        st.write(
        """
        Dependem da taxa de arrefecimento:

        Arrefecimento lento:
        - Textura **fanerítica** (granitos)
        - Cristais visíveis

        Arrefecimento rápido:
        - Textura **afanítica/porfirítica** (riólitos)
        - Fenocristais em matriz fina

        Estágio final:
        - **Pegmatitos**
        - Cristais gigantes de quartzo
        - Baixa densidade de defeitos estruturais
        """
        )

        st.divider()

        st.markdown("### Ambientes geológicos")

        st.write(
        """
        Distribuição predominante na **crosta continental**:

        - Arcos magmáticos (continentais e insulares)
        - Intrusões plutónicas de grande escala
        - Sistemas vulcânicos félsicos

        ➜ Associados a tectónica convergente e atividade magmática intensa
        """
        )

        st.divider()

        st.markdown("### Condições que favorecem a formação")

        st.write(
        """
        Para formar depósitos significativos:

        **Magmas evoluídos**
        - Elevado enriquecimento em sílica

        **Arrefecimento lento**
        - Permite crescimento de cristais bem desenvolvidos

        **Alta viscosidade**
        - Característica de magmas félsicos
        - Influencia retenção de voláteis

        ➜ Favorece cristalização tardia e formação de quartzo de elevada pureza
        """
        )
        
    elif "Depósitos metamórficos" in deposito:

        st.markdown("### Depósitos metamórficos")

        st.write(
        """
        Os depósitos metamórficos de quartzo resultam da **transformação de rochas pré-existentes**
        sob condições de **alta pressão e temperatura**, no estado sólido.

        Tipos principais:
        - **Quartzo relicto** → preserva características da rocha original  
        - **Quartzo recristalizado** → novos grãos mais estáveis  
        """
        )

        st.divider()

        st.markdown("### Origem do quartzo metamórfico")

        st.write(
        """
        Origina-se a partir de:
        - Arenitos
        - Metagrauvaques
        - Sequências vulcano-sedimentares

        Processo dominante:
        - **Recristalização da sílica**

        ➜ Eliminação de defeitos estruturais  
        ➜ Formação de uma mineralogia mais pura e estável  
        """
        )

        st.divider()

        st.markdown("### Processos metamórficos")

        st.write(
        """
        O quartzo responde a diferentes tipos de metamorfismo:

        **Metamorfismo regional**
        - Associado a cinturões orogénicos

        **Metamorfismo de contacto**
        - Próximo de intrusões magmáticas

        Processos principais:
        - Crescimento de grão
        - Migração de limites de grão
        - Redução da energia de superfície

        Transformação estrutural:
        - Transição quartzo-α ↔ quartzo-β (~573°C)
        - Formação de maclas e defeitos
        """
        )

        st.divider()

        st.markdown("### Mobilização da sílica")

        st.write(
        """
        A sílica é mobilizada por **fluidos metamórficos**:

        Origem dos fluidos:
        - Reações de desidratação (devolatilização)

        ➜ Transporte de sílica em profundidade

        Resultado:
        - Formação de veios metamórficos
        - Preenchimento de:
          - Zonas de cisalhamento
          - Fraturas dilatantes

        Orientação:
        - Paralela ou transversal à foliação da rocha encaixante
        """
        )

        st.divider()

        st.markdown("### Condições físico-químicas")

        st.write(
        """
        Temperatura:
        - 180°C a 700°C

        Pressão:
        - 1 a 5 kbar

        Intervalo metamórfico:
        - Fácies xisto verde → granulito

        Papel dos fluidos:
        - Facilitam migração iónica
        - Controlam recristalização

        Característica distintiva:
        - Baixo teor de OH (<5 ppm)
        """
        )

        st.divider()

        st.markdown("### Texturas e estruturas")

        st.write(
        """
        Principais formas:

        **Quartzitos**
        - Rochas compactas
        - Recristalização total de arenitos

        **Bandamento metamórfico**
        - Alternância de minerais claros e escuros
        - Acumulação de quartzo em bandas

        Texturas:
        - Deformadas
        - Cisalhadas
        - Laminadas
        """
        )

        st.divider()

        st.markdown("### Ambientes geológicos")

        st.write(
        """
        Ocorrem principalmente em:

        **Cinturões orogénicos**
        - Ambientes colisionais e acrecionários

        **Zonas de subducção**
        - Importantes para geração de fluidos

        ➜ Forte deformação crustal  
        ➜ Circulação de fluidos em larga escala  
        """
        )

        st.divider()

        st.markdown("### Condições que favorecem a formação")

        st.write(
        """
        Para formação de depósitos significativos:

        **Altas pressões e temperaturas**
        - Promovem recristalização eficiente

        **Presença de fluidos**
        - Essenciais para transporte de sílica

        **Tempo geológico prolongado**
        - Ciclos orogénicos longos

        ➜ Permite acumulação, purificação e reorganização do quartzo
        """
        )

    else:
        st.info("Selecione um tipo de depósito válido.")

# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_quartzo():

    st.markdown("### Confusões comuns")

    st.markdown("**1. Quartzo vs Feldspato**")

    st.write("""
    - **Quartzo**:
      - Dureza maior (Mohs 7)
      - Fratura concoidal
      - Sem clivagem
    
    - **Feldspato**:
      - Dureza menor (Mohs 6)
      - Apresenta clivagem
      - Aspeto mais opaco
        """)

    st.info("💡 Teste rápido: feldspato parte em planos, enquanto o quartzo quebra irregularmente.")

    st.divider()

    st.markdown("**2. Quartzo vs Vidro**")

    st.write("""
    - **Quartzo**:
      - Estrutura cristalina
      - Pode formar cristais bem definidos
      - Propriedades ópticas organizadas
    
    - **Vidro**:
      - Estrutura amorfa
      - Sem cristais
      - Origem artificial ou vulcânica
        """)

    st.info("💡 Ambos têm fratura concoidal, mas só o quartzo é cristalino.")

    st.divider()

    st.markdown("**3. Quartzo vs Calcite**")

    st.write("""
    - **Quartzo**:
      - Duro (Mohs 7)
      - Não reage com ácido
      - Fratura concoidal
    
    - **Calcite**:
      - Mais macia (Mohs 3)
      - Reage com ácido (efervescência)
      - Clivagem bem definida
        """)

    st.info("💡 Teste rápido: ácido → efervescência = calcite.")

    st.divider()

    st.markdown("**4. Areia ≠ apenas quartzo**")

    st.write("""
    - Areia pode conter:
      - Feldspatos
      - Fragmentos de rocha
      - Outros minerais
    
    - O quartzo domina apenas em sedimentos muito maduros
        """)

    st.info("💡 Nem toda areia é quartzosa — depende da maturidade sedimentar.")

    st.divider()

    st.markdown("**5. Cor do quartzo**")

    st.write("""
    - Diferentes cores não significam minerais diferentes:
      - Ametista (roxo)
      - Citrino (amarelo)
      - Quartzo fumado
      - Quartzo rosa
    
    - A cor resulta de:
      - Impurezas
      - Defeitos estruturais
        """)

    st.info("Apesar da cor variar, quimicamente é sempre SiO₂.")

    st.divider()

    st.markdown("**6. Origem do quartzo**")

    st.write("""
    O quartzo pode formar-se em vários contextos:
    
    - **Magmático** → cristalização em granitos e pegmatitos  
    - **Hidrotermal** → veios em fraturas  
    - **Sedimentar** → grãos detríticos  
    - **Metamórfico** → quartzitos e recristalização  
    
    O mesmo mineral pode ter origens completamente diferentes
        """)

    st.info("💡 Identificar o contexto geológico é essencial, não só o mineral.")

    st.divider()

    st.markdown("**7. Pureza do quartzo**")

    st.write("""
    - Nem todo quartzo é puro:
      - Pode conter Al, Fe, Ti, etc.
      - Pode apresentar inclusões
    
    - Apenas quartzo muito puro é usado em aplicações tecnológicas
        """)

    st.info("💡 Aparência limpa não garante pureza química.")

    st.divider()

    st.markdown("**8. Veios de quartzo ≠ depósito económico**")

    st.write("""
    - Veios de quartzo são comuns
    - Nem todos contêm metais ou interesse económico
    
    - Formação depende de:
      - Circulação de fluidos
      - Temperatura
      - Estrutura geológica
        """)

    st.info("💡 A presença de quartzo não implica automaticamente mineralização valiosa.")

# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_quartzo(deposito):

    st.markdown("### Quiz interativo")
    st.caption("Testa os teus conhecimentos")

    if "Veios hidrotermais" in deposito:

        if "corrigido_veios" not in st.session_state:
            st.session_state.corrigido_veios = False
    
        corretas = ["100–300 °C", "Magmática", "Diminuição da temperatura", "Veios", "Arcos magmáticos"]
    
        q1 = st.radio("1️⃣ Intervalo típico de temperatura dos sistemas epitermais:",
                      ["50–100 °C", "100–300 °C", "400–700 °C"], key="pet_q1", index=None)
    
        if st.session_state.corrigido_veios:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")
    
        q2 = st.radio("2️⃣ Origem possível dos fluidos hidrotermais:",
                      ["Magmática", "Atmosférica", "Biológica"], key="pet_q2", index=None)
    
        if st.session_state.corrigido_veios:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")
    
        q3 = st.radio("3️⃣ Principal fator que promove a precipitação do quartzo:",
                      ["Aumento da pressão", "Diminuição da temperatura", "Aumento da salinidade"], key="pet_q3", index=None)
    
        if st.session_state.corrigido_veios:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")
    
        q4 = st.radio("4️⃣ Forma típica de ocorrência do quartzo hidrotermal:",
                      ["Camadas sedimentares", "Veios", "Nódulos"], key="pet_q4", index=None)
    
        if st.session_state.corrigido_veios:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")
    
        q5 = st.radio("5️⃣ Ambiente geológico comum dos veios hidrotermais:",
                      ["Planícies aluviais", "Arcos magmáticos", "Plataformas continentais estáveis"], key="pet_q5", index=None)
    
        if st.session_state.corrigido_veios:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")
    
        if st.button("Concluir"):
            st.session_state.corrigido_veios = True
    
        if st.session_state.corrigido_veios:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    elif "Depósitos sedimentares" in deposito:

        if "corrigido_sedimentares" not in st.session_state:
            st.session_state.corrigido_sedimentares = False
    
        corretas = ["Quartzo detrítico", "Elevada resistência química e mecânica", "Fluvial, eólico e marinho",
                    "Sobrecrescimentos", "Ambientes tectonicamente estáveis"]
    
        q1 = st.radio("1️⃣ Tipo de quartzo proveniente da erosão de rochas pré-existentes:",
                      ["Quartzo autigénico", "Quartzo detrítico", "Quartzo metamórfico"], key="gas_q1", index=None)
    
        if st.session_state.corrigido_sedimentares:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")
    
        q2 = st.radio("2️⃣ Propriedade que permite ao quartzo resistir ao transporte sedimentar:",
                      ["Baixa densidade", "Elevada resistência química e mecânica", "Alta solubilidade"], key="gas_q2", index=None)
    
        if st.session_state.corrigido_sedimentares:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")
    
        q3 = st.radio("3️⃣ Principais sistemas de transporte sedimentar do quartzo:",
                      ["Glaciar apenas", "Fluvial, eólico e marinho", "Apenas marinho"], key="gas_q3", index=None)
    
        if st.session_state.corrigido_sedimentares:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")
    
        q4 = st.radio("4️⃣ Estrutura típica do quartzo autigénico durante a diagénese:",
                      ["Fragmentação", "Sobrecrescimentos", "Fusão parcial"], key="gas_q4", index=None)
    
        if st.session_state.corrigido_sedimentares:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")
    
        q5 = st.radio("5️⃣ Ambiente que favorece depósitos sedimentares ricos em quartzo:",
                      ["Ambientes tectonicamente instáveis", "Ambientes tectonicamente estáveis", "Zonas vulcânicas ativas"], key="gas_q5", index=None)
    
        if st.session_state.corrigido_sedimentares:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")
    
        if st.button("Concluir"):
            st.session_state.corrigido_sedimentares = True
    
        if st.session_state.corrigido_sedimentares:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    elif "Depósitos magmáticos" in deposito:

        if "corrigido_magmatico" not in st.session_state:
            st.session_state.corrigido_magmatico = False
        
        corretas = ["Rochas félsicas", "Diferenciação magmática", "Último a cristalizar",
                    "Pegmatitos", "Arrefecimento lento"]
        
        q1 = st.radio("1️⃣ Tipo de rocha mais rica em quartzo:",
                      ["Rochas máficas", "Rochas félsicas", "Rochas ultramáficas"], key="mix_q1", index=None)
        
        if st.session_state.corrigido_magmatico:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")
        
        q2 = st.radio("2️⃣ Processo responsável pelo enriquecimento em sílica no magma:",
                      ["Compactação", "Diferenciação magmática", "Erosão"], key="mix_q2", index=None)
        
        if st.session_state.corrigido_magmatico:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")
        
        q3 = st.radio("3️⃣ Posição do quartzo na série de Bowen:",
                      ["Primeiro a cristalizar", "Intermédio", "Último a cristalizar"], key="mix_q3", index=None)
        
        if st.session_state.corrigido_magmatico:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")
        
        q4 = st.radio("4️⃣ Ambiente onde se formam cristais gigantes de quartzo:",
                      ["Basaltos", "Pegmatitos", "Calcários"], key="mix_q4", index=None)
        
        if st.session_state.corrigido_magmatico:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")
        
        q5 = st.radio("5️⃣ Condição que favorece o crescimento de cristais bem desenvolvidos:",
                      ["Arrefecimento rápido", "Arrefecimento lento", "Baixa viscosidade"], key="mix_q5", index=None)
        
        if st.session_state.corrigido_magmatico:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")
        
        if st.button("Concluir"):
            st.session_state.corrigido_magmatico = True
        
        if st.session_state.corrigido_magmatico:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")
            
    elif "Depósitos metamórficos" in deposito:

        if "corrigido_metamorfico" not in st.session_state:
            st.session_state.corrigido_metamorfico = False
    
        corretas = ["Recristalização", "Metamorfismo regional", "Fluidos metamórficos",
                    "Quartzitos", "Altas pressões e temperaturas"]
    
        q1 = st.radio("1️⃣ Processo principal de formação do quartzo metamórfico:",
                      ["Fusão parcial", "Recristalização", "Sedimentação"], key="mix_q1", index=None)
    
        if st.session_state.corrigido_metamorfico:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")
    
        q2 = st.radio("2️⃣ Tipo de metamorfismo associado a cinturões orogénicos:",
                      ["Metamorfismo de contacto", "Metamorfismo regional", "Metamorfismo hidrotermal"], key="mix_q2", index=None)
    
        if st.session_state.corrigido_metamorfico:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")
    
        q3 = st.radio("3️⃣ Principal agente de mobilização da sílica:",
                      ["Magmas", "Fluidos metamórficos", "Atmosfera"], key="mix_q3", index=None)
    
        if st.session_state.corrigido_metamorfico:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")
    
        q4 = st.radio("4️⃣ Rocha resultante da recristalização total de arenitos:",
                      ["Granito", "Quartzitos", "Basalto"], key="mix_q4", index=None)
    
        if st.session_state.corrigido_metamorfico:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")
    
        q5 = st.radio("5️⃣ Condição essencial para a formação de depósitos metamórficos:",
                      ["Baixa temperatura", "Altas pressões e temperaturas", "Ambiente superficial"], key="mix_q5", index=None)
    
        if st.session_state.corrigido_metamorfico:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")
    
        if st.button("Concluir"):
            st.session_state.corrigido_metamorfico = True
    
        if st.session_state.corrigido_metamorfico:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    else:
        st.info("Selecione um tipo de depósito válido.")

# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_quartzo():

    st.markdown("### Checklist de Campo")

    st.write("Avaliação sistemática para identificação e interpretação geológica:")

    st.markdown("**1. Identificação do mineral**")

    st.checkbox("Dureza elevada (risca vidro – Mohs 7)")
    st.checkbox("Fratura concoidal (sem clivagem)")
    st.checkbox("Transparente a translúcido")
    st.checkbox("Aspeto vítreo (brilho)")
    st.checkbox("Cristais ou massa granular")

    st.divider()

    st.markdown("**2. Cor e pureza**")

    st.checkbox("Cor (incolor, roxo, amarelo, fumado, rosa)")
    st.checkbox("Homogéneo ou zonado")
    st.checkbox("Presença de inclusões")
    st.checkbox("Quartzo aparentemente puro ou com impurezas")

    st.divider()

    st.markdown("**3. Contexto no terreno**")

    st.checkbox("Ocorre em veio (preenchimento de fratura)")
    st.checkbox("Associado a falhas ou zonas de cisalhamento")
    st.checkbox("Inserido em rocha sedimentar, magmática ou metamórfica")
    st.checkbox("Associado a outros minerais")

    st.divider()

    st.markdown("**4. Texturas diagnósticas**")

    st.checkbox("Veio simples ou múltiplos veios (stockwork)")
    st.checkbox("Textura maciça")
    st.checkbox("Cristais bem formados (drusas)")
    st.checkbox("Bandamento visível")

    st.divider()

    st.markdown("**5. Interpretação geológica**")

    st.checkbox("Indícios de origem hidrotermal (veios, fraturas)")
    st.checkbox("Indícios de origem magmática (em granito/pegmatito)")
    st.checkbox("Indícios de origem sedimentar (grãos em arenito)")
    st.checkbox("Indícios de recristalização metamórfica (quartzito, bandamento)")

    st.divider()

    st.markdown("**6. Indícios de formação**")

    st.checkbox("Evidência de arrefecimento (precipitação)")
    st.checkbox("Presença de fraturação (circulação de fluidos)")
    st.checkbox("Possível variação de temperatura/pH (texturas)")

    st.divider()

    st.markdown("**7. Registo**")

    st.checkbox("Localização do afloramento registada")
    st.checkbox("Fotografias tiradas")
    st.checkbox("Amostra recolhida")
    st.checkbox("Contexto geológico descrito")

    st.success("💡 Foco: identificar → contextualizar → interpretar.")

# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_quartzo():
    st.markdown("### 🌍 Mapa global de depósitos de quartzo")

    uploaded_file = st.file_uploader(
        "Upload CSV with Latitude and Longitude",
        type=["csv"],
        key="monazite_map"
    )

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)


        df.columns = df.columns.str.strip().str.lower()

        st.success("Database successfully loaded")
        st.dataframe(df.head())


        lat_col = next((col for col in df.columns if "lat" in col), None)
        lon_col = next((col for col in df.columns if "lon" in col), None)

        if lat_col is None or lon_col is None:
            st.error("Latitude/Longitude columns not found.")
            return


        color_map = {
            "pegmatite": "purple",
            "high purity quartz": "gold",
            "sedimentary": "blue",
            "hydrothermal vein": "red",
            "metamorphic": "green",
            "quartzite": "orange"
        }


        mapa = folium.Map(location=[20, 0], zoom_start=2)
        Fullscreen().add_to(mapa)


        for _, row in df.iterrows():
            if pd.notna(row[lat_col]) and pd.notna(row[lon_col]):

                deposit_type = str(row.get("deposit_type", "unknown")).lower()
                color = color_map.get(deposit_type, "gray")

                popup = f"""
                <b>Country:</b> {row.get('country', 'N/A')}<br>
                <b>Region:</b> {row.get('region', 'N/A')}<br>
                <b>Type:</b> {row.get('deposit_type', 'N/A')}<br>
                <b>Host Rock:</b> {row.get('host_rock', 'N/A')}<br>
                """

                folium.CircleMarker(
                    [row[lat_col], row[lon_col]],
                    radius=6,
                    color=color,
                    fill=True,
                    fill_opacity=0.8,
                    popup=folium.Popup(popup, max_width=350)
                ).add_to(mapa)

        legend_html = """
        <div style="
            position: fixed;
            bottom: 40px;
            left: 40px;
            width: 260px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(6px);
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            z-index: 9999;
            font-family: Arial, sans-serif;
            padding: 15px;
        ">
        
        <div style="
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 10px;
            color: #333;
        ">
            Deposit Type
        </div>
        
        <div style="font-size: 14px; line-height: 1.6; color: #444;">
        
        <div><span style="color:purple;">●</span> Pegmatite</div>
        <div><span style="color:gold;">●</span> High Purity Quartz</div>
        <div><span style="color:blue;">●</span> Sedimentary</div>
        <div><span style="color:red;">●</span> Hydrothermal Vein</div>
        <div><span style="color:green;">●</span> Metamorphic</div>
        <div><span style="color:orange;">●</span> Quartzite</div>
        <div><span style="color:gray;">●</span> Others</div>
        
        </div>
        </div>
        """

        mapa.get_root().html.add_child(folium.Element(legend_html))

        st_folium(mapa, use_container_width=True, height=600)

    else:
        st.info("Upload a CSV file to visualize the data.")

# ===============================
# 6. REFERÊNCIAS
# ===============================

def referencias_quartzo():

    st.markdown("### 📚 Referências bibliográficas")
    
    st.write(
    "- Götze, J., Pan, Y., & Müller, A. (2021). Mineralogy and mineral "
    "chemistry of quartz: A review. Mineralogical Magazine, 85, 639–664."
    )
    
    st.write(
    "- Mercer, C. N., Reed, M. H., & Mercer, C. M. (2015). Time scales "
    "of porphyry Cu deposit formation: Insights from titanium diffusion "
    "in quartz. Economic Geology, 110(3), 587–602."
    )
    
    st.write(
    "- Pirajno, F. (2009). Hydrothermal processes and mineral systems. Springer."
    )
    
    st.write(
    "- Groves, D. I., Goldfarb, R. J., Gebre-Mariam, M., Hagemann, S. G., "
    "& Robert, F. (1998). Orogenic gold deposits: A proposed classification "
    "in the context of their crustal distribution and relationship to other "
    "gold deposit types. Ore Geology Reviews, 13, 7–27."
    )
    
    st.write(
    "- Öhlander, B., & Markkula, H. (1994). Alteration associated with the "
    "gold-bearing quartz veins at Middagsberget, northern Sweden. "
    "Mineralium Deposita, 29, 120–127."
    )
    
    st.write(
    "- Abdel-Rahman, A. M., El-Desoky, H. M., Shebl, A., El-Awny, H., Amer, "
    "Y. Z., & Csámer, Á. (2023). The geochemistry, origin, and hydrothermal "
    "alteration mapping associated with the gold-bearing quartz veins at "
    "Hamash district, South Eastern Desert, Egypt. Scientific Reports, 13, 15058."
    )
    
    st.write(
    "- Hasria, Idrus, A., & Warmada, I. W. (2022). The quartz veins, "
    "hydrothermal alteration and ore mineralization of orogenic gold deposit "
    "at Mendoke Mountains, Southeast Sulawesi, Indonesia. Iraqi Geological "
    "Journal, 55(2C), 1–13."
    )
    
    st.write(
    "- Ferenc, Š., Števko, M., Mikuš, T., Milovská, S., Kopáčik, R., & "
    "Hoppanová, E. (2021). Primary minerals and age of the hydrothermal quartz "
    "veins containing U–Mo–(Pb, Bi, Te) mineralization in the Majerská Valley "
    "near Cučma (Slovak Republic). Minerals, 11(6), 629."
    )
    
    st.caption("Referências utilizadas.")