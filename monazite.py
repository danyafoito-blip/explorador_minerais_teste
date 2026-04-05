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

def mostrar_caracteristicas_monazite(deposito):

    st.markdown("### Monazite")
    
    st.markdown("""
    A monazite é um mineral de fosfato de terras raras leves (LREE) e 
    constitui um dos principais minérios destes elementos.  
    Ocorre como mineral acessório em rochas ígneas 
    (granitos e pegmatitos), metamórficas e em depósitos 
    sedimentares do tipo plácer (placer).
    """)
    
    st.divider ()

    col1, col2 = st.columns(2)
    
    with col1:
    
        st.success("**Propriedades físicas**")
        
        st.write("- Sólido cristalino")
        st.write("- Cor variável (amarelo, castanho, avermelhado, cinzento ou incolor)")
        st.write("- Alta densidade")
        st.write("- Dureza média (5 – 5,5 na escala de Mohs)")
        st.write("- Muito resistente ao desgaste")
        st.write("- Pode ter estrutura zonada")
    
    with col2:
    
        st.info("**Propriedades químicas**")
        
        st.write("- Composto por fosfato de terras raras")
        st.write("- Fórmula geral (REE)PO₄")
        st.write("- Pode conter tório e urânio")
        st.write("- Naturalmente radioativo")
        st.write("- Muito estável quimicamente")
        st.write("- Pode sofrer substituições na estrutura")

    st.divider()

    if "Depósitos sedimentares" in deposito:

        st.markdown("### Depósitos sedimentares")
        
        st.markdown(
         """
         Depósitos sedimentares de monazite correspondem a **acumulações detríticas**
         deste mineral em sedimentos não consolidados, geralmente designados por
         **pláceres (placers)**.
        
         Ocorrem principalmente em **areias fluviais e litorais**, onde processos físicos
         promovem a concentração seletiva de minerais pesados.
         """
         )
        
        st.divider()
        
        st.markdown("### Origem da monazite sedimentar")
               
        st.markdown(
        """
        A monazite tem origem em **rochas ígneas e metamórficas**, sendo libertada
        através da **meteorização**.
    
        **Rochas fonte típicas:**
        - Granitos e pegmatitos  
        - Gnaisses e xistos 
    
        Devido à sua:
        - **Elevada resistência química**
        - **Elevada densidade**
        
        A monazite **resiste ao transporte sedimentar**.
        """)
        
        st.divider()
        
        st.markdown("### Processos de concentração sedimentar")
        
        st.markdown(
          """
          Após a libertação, a monazite é transportada por **rios** até zonas de deposição.
        
          A concentração ocorre por **seleção hidráulica**:
        
          - Minerais leves (quartzo, feldspato) → removidos  
          - Minerais pesados (monazite) → concentrados  
        
          Este processo forma **camadas ricas em minerais pesados**.
          """
          )
        
        st.divider()
        
        st.markdown("### Ambientes deposicionais")
        
        st.write("""
        - Sistemas fluviais (depósitos aluvionares)  
        - Praias e zonas costeiras  
        - Dunas litorais  
        - Plataformas continentais rasas  
            """)

        st.divider()
        
        st.markdown("### Ciclo sedimentar e retrabalhamento")
        
        st.markdown(
        """
        A monazite pode passar por **vários ciclos sedimentares**:
        
        1. Erosão da rocha fonte  
        2. Transporte fluvial  
        3. Deposição  
        4. Retrabalhamento (ondas/correntes)  
        
        Cada ciclo aumenta a concentração de minerais pesados.
        """
        )
                
        st.divider()
        
        st.markdown("### Condições físico-químicas")
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Estabilidade", "Muito elevada")
            st.write("Resiste à meteorização física e química")
        
        with col2:
            st.metric("pH", "Ácido")
            st.write("Favorece dissolução e mobilização")
        
        with col3:
            st.metric("Salinidade", "Elevada")
            st.write("Aumenta solubilidade em ambientes costeiros")
        
        st.divider()
        
        st.markdown("### Mecanismos de acumulação")
        
        st.markdown(
        """
        A acumulação é **controlada por processos físicos**:
    
        - Energia das correntes fluviais  
        - Ação das ondas  
        - Separação por densidade  
    
        Formam-se **lentes ou camadas ricas em minerais pesados**.
        """
        )
    
        st.write("""
        **Minerais associados:**
        - Ilmenite  
        - Zircão  
        - Rutilo  
        - Magnetite  
        - Granada  
        """)
            
        st.divider()
        
        st.markdown("### Ambientes geológicos típicos")
        
        st.write("""
        - Margens continentais passivas  
        - Bacias costeiras  
        - Sistemas deltaicos  
        - Zonas de foz de grandes rios  
            """)
                
        st.divider()
        
        st.markdown("### Fatores que favorecem a acumulação")
        
        st.markdown(
        """
        **1. Rochas fonte ricas em REE**  
        - Fornecem monazite ao sistema sedimentar  
        
        **2. Meteorização intensa**  
        - Liberta os grãos minerais  
        
        **3. Energia hidrodinâmica adequada**  
        - Remove minerais leves e concentra os pesados  
        
        **4. Retrabalhamento sedimentar**  
        - Aumenta o grau de enriquecimento  
        
        **5. Estabilidade tectónica (margens passivas)**  
        - Permite acumulação prolongada  
        """
        )
            
    elif "Depósitos magmáticos" in deposito:

        st.markdown("### Depósitos magmáticos")
        
        
        st.markdown(
        """
        Um depósito magmático de monazite refere-se à ocorrência e acumulação
        deste mineral como uma fase acessória formada diretamente durante a
        cristalização de um magma.
    
        Estes depósitos resultam de processos petrogenéticos em fundidos
        silicatados ou carbonatados.
        """
        )
        
        st.divider()
        
        st.markdown("### Origem magmática da monazite")
        
        st.markdown(
         """
         A monazite cristaliza-se a partir de magmas que atingem saturação em:
         - Terras raras (REE)
         - Fósforo
        
         Estes magmas derivam frequentemente de:
         - Fusões parciais de pequena escala  
         - Magmas parentais enriquecidos  
        
         A monazite concentra elementos incompatíveis como:
         - REE  
         - Tório (Th)  
         - Urânio (U)  
        
         Estes elementos são enriquecidos no líquido residual durante a diferenciação magmática.
        
         Em sistemas complexos, pode registar idades de cristalização do evento magmático.
         """
         )
        
        st.divider()
        
        st.markdown("### Processos de cristalização")
        
        st.markdown(
          """
          A acumulação de REE ocorre por cristalização fracionada prolongada:
        
          - Minerais principais capturam elementos maiores  
          - REE permanecem no líquido residual  
        
          A precipitação da monazite depende de:
          - Atividade de fósforo  
          - Concentração de REE  
        
          Em carbonatitos:
          - Monazite primária é rara  
          - Forma-se quando a apatite deixa de dominar  
        
          A monazite é uma fase:
          - Tardia  
          - Associada a líquidos magmáticos evoluídos  
          - Frequente em bordaduras de plutões  
          """
          )

        st.divider()
        
        st.markdown("### Geoquímica e partição de elementos")
        
        st.markdown(
         """
         A monazite magmática é dominada por:
         - Ce  
         - La  
         - Nd  
        
         Apresenta fracionamento de La para Lu.
        
         Substituições estruturais importantes:
         - Huttonite: Th⁴⁺ + Si⁴⁺ ↔ REE³⁺ + P⁵⁺  
         - Cheralite: Th⁴⁺ + Ca²⁺ ↔ 2REE³⁺  
        
         Associa-se a minerais como:
         - Apatite  
         - Zircão  
         - Xenotime  
         - Allanite  
        
         Em carbonatitos:
         - Associação com apatite  
         - Pode substituí-la em fases tardias  
         """)
        
        st.divider()
        
        st.markdown("### Ambientes magmáticos")
        
        st.write("""
        - Granitos peraluminosos (tipo S)  
        - Pegmatitos graníticos  
        - Dikes associados  
        - Sienitos nefelínicos  
        - Carbonatitos  
            """)
        
        st.divider()
        
        st.markdown("### Condições físico-químicas")
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Temperatura (carbonatitos)", "< 750 °C")
            st.write("Cristalização magmática")
    
        with col2:
            st.metric("Temperatura de fecho", "> 900 °C")
            st.write("Sistema U-Th-Pb")
    
        with col3:
            st.metric("Voláteis", "F, H₂O, CO₂")
            st.write("Controlam transporte de REE")
    
        st.warning("Voláteis influenciam fortemente a mobilidade dos elementos")
        
        st.divider()
        
        st.markdown("### Mecanismos de concentração")
        
        st.markdown(
        """
        A concentração de monazite ocorre por:
        
        - Diferenciação de magmas evoluídos  
        - Enriquecimento em líquidos residuais  
        
        Pode acumular-se em:
        - Bolsas de líquido residual  
        - Cavidades preenchidas por fluidos tardios  
        """)
        
        st.divider()
        
        st.markdown("### Evolução magmática")
        
        st.markdown(
          """
          Nos estágios iniciais:
          - Apatite pode dominar o balanço de REE  
        
          Nos estágios finais:
          - Monazite precipita após esgotamento de Ca  
          - Aumento da atividade de fósforo  
        
          Fluidos pós-magmáticos podem causar:
          - Recristalização  
          - Zoneamento patchy  
          - Formação de coroas de allanite e apatite  
          """)
        
        st.divider()
        
        st.markdown("### Ambientes geológicos típicos")
        
        st.write("""
        - Cinturões orogénicos  
        - Províncias alcalinas  
        - Zonas de rift intracontinental  
        - Margens continentais  
            """)

        st.divider()
        
        st.markdown("### Fatores que favorecem a acumulação")
        
        st.markdown(
          """
          **1. Magmas saturados em fósforo**  
          - Estabilizam a monazite  
        
          **2. Alto grau de diferenciação**  
          - Concentra REE no líquido residual  
        
          **3. Baixa cristalização de competidores**  
          - Preserva REE para formação tardia  
        
          **4. Presença de tório (Th)**  
          - Estabiliza a estrutura mineral  
          """
          )

    elif "Depósitos metamórficos" in deposito:
    
        st.markdown("### Depósitos metamórficos")
        
        st.markdown(
        """
        Um depósito metamórfico de monazite refere-se à ocorrência e crescimento
        deste mineral como uma fase acessória em rochas que sofreram **transformações
        físico-químicas devido a variações de pressão e temperatura**.
    
        Estes depósitos formam-se ou recristalizam-se **in situ**, a partir dos
        **componentes químicos da própria rocha** ou da **interação com fluidos metamórficos**.
        """
        )
    
        st.divider()
        
        st.markdown("### Origem metamórfica da monazite")
        
        st.markdown(
        """
        A monazite metamórfica pode formar-se através da:
        
        - **Recristalização de grãos detríticos ou ígneos**  
        - **Metamorfismo regional ou eventos sin-colisionais**  
        
        Em metamorfismo de muito baixo grau, pode formar-se **monazite autigénica**
        por recristalização de **precursores como géis ou agregados criptocristalinos**
        durante a **diagénese ou soterramento**.
        
        A formação pode resultar de:
        - **Remobilização de REE de camadas vulcanogénicas**  
        - **Decomposição de feldspato e formação de ilite (60–120 °C)**  
        - **Libertação de fósforo de fontes biogénicas**  
        - **Desestabilização de apatite em matrizes pobres em Ca**  
        """
        )
        
        st.divider()
        
        st.markdown("### Processos metamórficos")
        
        st.markdown(
         """
         A paragénese da monazite é controlada pela sua relação com:
        
         - **Alanite**  
         - **Apatite**  
        
         A monazite pode reagir para formar **alanite e apatite, ou vice-versa**,
         dependendo do **grau metamórfico e da disponibilidade de Ca**.
        
         Rochas ricas em Ca expandem o **campo de estabilidade da alanite**,
         restringindo a monazite a **condições de fácies granulito**.
        
         O **tamanho do grão aumenta com o grau metamórfico**,
         raramente excedendo **250 µm**.
         """
         )
    
        st.divider()
        
        st.markdown("### Geoquímica e mobilidade dos REE")
        
        st.markdown(
           """
           A geoquímica da monazite é influenciada pelo **fracionamento de**:
        
           - **Ítrio (Y)**  
           - **REE pesados (HREE) com a granada**  
        
           Monazites que crescem **simultaneamente ou após a granada**
           tendem a ser **pobres em Y**.
        
           A solubilidade da monazite em fluidos metamórficos aumenta com:
           - **Acidez**  
           - **Salinidade**  
        
           permitindo a **remobilização local de REE**.
           """
           )
        
        st.divider()
        
        st.markdown("### Ambientes metamórficos")
        
        st.markdown(
         """
         A monazite ocorre tipicamente em:
        
         - **Cinturões metamórficos regionais**  
         - **Fácies anfibolito alto a granulito**  
        
         Também ocorre em:
         - **Gnaisses de ultra-alta pressão (UHP)**  
         - **Rochas de contacto de baixa pressão (ex: hornfels granatíferos)**  
         """
         )
        
        st.divider()
        
        st.markdown("### Condições físico-químicas")
    
        col1, col2, col3 = st.columns(3)
        
        with col1:
             st.metric("Temperatura (baixo grau)", "210–275 °C")
             st.write("**Crescimento em metapelitos**")
        
        with col2:
             st.metric("Fluidos", "Aquosos ou alcalinos")
             st.write("**Controlam alteração e recristalização**")
        
        with col3:
             st.metric("Ambiente", "Redutor")
             st.write("**Favorece monazite rica em Nd e Sm**")
        
        st.warning("**Fluidos são um motor fundamental dos processos metamórficos**")
        
        st.divider()
        
        st.markdown("### Crescimento e evolução da monazite")
        
        st.markdown(
           """
           A monazite apresenta **zonamento composicional complexo**:
        
           - **Concêntrico**  
           - **Oscilatório**  
           - **Patchy**  
        
           Reflete variações no **conteúdo de tório (Th)**.
        
           Microestruturas típicas:
        
           - **Coronas de alanite-apatite → retrometamorfismo**  
           - **Estruturas satélites → reaquecimento após retrogressão**  
           - **Agregados poligonais → formação inicial em alto grau**  
           """
           )
        
        st.divider()
        
        st.markdown("### Interação com fluidos")
                
        st.markdown(
        """
        A alteração mediada por fluidos pode gerar:
        
        - **Zonas de borda ricas ou pobres em Th**  
        - **Contactos côncavos agudos**  
        
        Pode ocorrer **redefinição total ou parcial do sistema U-Th-Pb**.
        
        A decomposição da monazite pode originar:
        
        - **Alanite**  
        - **Rhabdophane**  
        - **Minerais do grupo da crandallite**  
        """
        )
        
        st.divider()
        
        st.markdown("### Ambientes geológicos típicos")
        
        st.write("""
        - **Cinturões orogénicos antigos**  
        - **Terrenos granulíticos**  
            """)
        
        st.divider()
        
        st.markdown("### Fatores que favorecem a formação")
        
        st.markdown(
        """
        **1. Composição do protólito**  
        - **Rochas sedimentares ricas em REE e alumínio**  
    
        **2. Grau metamórfico**  
        - **Condições de médio a alto grau**  
    
        **3. Presença de fluidos ativos**  
        - **Facilita nucleação e transporte de elementos**  
    
        **4. Tempo geológico**  
        - **Permite desenvolvimento de grãos complexos**  
        """
        )

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_monazite():

    st.markdown("### Confusões comuns")

    st.markdown("**1. Monazite vs Zircão**")

    st.write("""
    - **Monazite**:
      - Fosfato de terras raras (REE)PO₄
      - Pode conter Th e U (radioativa)
      - Dureza 5–5,5 (escala de Mohs)
      - Geralmente em grãos arredondados ou zonados
    
    - **Zircão**:
      - Silicato (ZrSiO₄)
      - Também pode conter U, mas menos REE
      - Dureza maior (~7,5 na escala de Mohs)
      - Cristais bem formados (prismáticos)
    """)

    st.info("💡 Ambos são usados em geocronologia, mas têm composições diferentes.")

    st.divider()

    st.markdown("**2. Monazite vs Allanite**")

    st.write("""
    - **Monazite**:
      - Rica em LREE (Ce, La, Nd)
      - Fosfato
      - Mais comum em condições de baixo Ca
    
    - **Allanite**:
      - Silicato (grupo da epidoto)
      - Contém REE + Ca + Fe
      - Estável em rochas ricas em cálcio
    """)

    st.info("💡 O teor de Ca da rocha ajuda a distinguir qual dos dois é estável.")

    st.divider()

    st.markdown("**3. Monazite vs Apatite**")

    st.write("""
    - **Monazite**:
      - Fosfato de REE
      - Fase tardia em muitos sistemas
      - Pode ser radioativa
    
    - **Apatite**:
      - Fosfato de Ca (Ca₅(PO₄)₃)
      - Muito comum em rochas ígneas
      - Não é rica em REE
    """)

    st.info("💡 Ambos são fosfatos, mas a apatite é rica em cálcio e não em terras raras.")

    st.divider()

    st.markdown("**4. Monazite vs Minerais pesados em pláceres (placers)**")

    st.write("""
    Em depósitos sedimentares, a monazite pode ser confundida com:

    - Ilmenite  
    - Rutilo  
    - Zircão  
    - Magnetite  

    Diferenças:
    - Monazite → rica em REE e radioativa  
    - Outros minerais → óxidos ou silicatos sem REE significativas
    """)

    st.info("💡 Só separar por densidade não basta, é preciso fazer uma análise mineralógica.")

    st.divider()

    st.markdown("**5. Cor da monazite**")

    st.write("""
    - A monazite pode apresentar várias cores:
      - Amarelo
      - Castanho
      - Avermelhado
      - Cinzento

    - A cor não define composição exata
    """)

    st.info("💡 A composição química (REE, Th) é mais importante que a cor.")

    st.divider()

    st.markdown("**6. Monazite ≠ sempre depósito económico**")

    st.write("""
    - A monazite pode estar presente em pequenas quantidades
    - Nem todos os depósitos são economicamente viáveis

    Depende de:
    - Concentração de REE
    - Facilidade de extração
    - Presença de tório (radioatividade)
    """)

    st.info("💡 A presença do mineral não garante exploração económica.")

    st.divider()

    st.markdown("**7. Radioatividade da monazite**")

    st.write("""
    - Nem toda monazite tem o mesmo nível de radioatividade
    - Depende do teor de:
      - Tório (Th)
      - Urânio (U)
    """)

    st.info("💡 É necessário medir a radioatividade")

    st.divider()

    st.markdown("**8. Origem da monazite**")

    st.write("""
    A monazite pode formar-se em vários contextos:

    - **Magmático** → cristalização em granitos e pegmatitos  
    - **Metamórfico** → recristalização e crescimento in situ  
    - **Sedimentar** → concentração em pláceres (placers)  

    O mesmo mineral pode ter origens completamente diferentes.
    """)

    st.info("💡 O contexto geológico é essencial para interpretar a monazite.")

# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_monazite(deposito):

    st.markdown("### Quiz interativo")
    st.caption("Testa os teus conhecimentos")

    if "Depósitos sedimentares" in deposito:

        if "corrigido_pet" not in st.session_state:
            st.session_state.corrigido_pet = False

        corretas = ["Elevada densidade", "Seleção hidráulica", "Pláceres (placers)", "Areias fluviais e litorais", "Ilmenite"]

        q1 = st.radio("1️⃣ Propriedade que favorece a concentração da monazite:",
                      ["Baixa densidade", "Elevada densidade", "Alta solubilidade"], key="pet_q1", index=None)

        if st.session_state.corrigido_pet:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        q2 = st.radio("2️⃣ Processo principal de concentração sedimentar:",
                      ["Cristalização magmática", "Seleção hidráulica", "Metamorfismo"], key="pet_q2", index=None)

        if st.session_state.corrigido_pet:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        q3 = st.radio("3️⃣ Tipo de depósito típico:",
                      ["Veios hidrotermais", "Pláceres (placers)", "Intrusões magmáticas"], key="pet_q3", index=None)

        if st.session_state.corrigido_pet:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        q4 = st.radio("4️⃣ Ambiente deposicional comum:",
                      ["Câmaras magmáticas", "Areias fluviais e litorais", "Manto terrestre"], key="pet_q4", index=None)

        if st.session_state.corrigido_pet:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        q5 = st.radio("5️⃣ Mineral frequentemente associado:",
                      ["Quartzo", "Ilmenite", "Calcite"], key="pet_q5", index=None)

        if st.session_state.corrigido_pet:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")

        if st.button("Concluir"):
            st.session_state.corrigido_pet = True

        if st.session_state.corrigido_pet:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    elif "Depósitos magmáticos" in deposito:

        if "corrigido_gas" not in st.session_state:
            st.session_state.corrigido_gas = False

        corretas = ["Cristalização magmática", "Elementos incompatíveis", "Fósforo e REE",
                    "Fase tardia", "Granitos e pegmatitos"]

        q1 = st.radio("1️⃣ Processo de formação da monazite:",
                      ["Sedimentação", "Cristalização magmática", "Alteração química"], key="gas_q1", index=None)

        if st.session_state.corrigido_gas:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        q2 = st.radio("2️⃣ Comportamento dos REE no magma:",
                      ["Compatíveis", "Elementos incompatíveis", "Voláteis"], key="gas_q2", index=None)

        if st.session_state.corrigido_gas:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        q3 = st.radio("3️⃣ O que controla a precipitação da monazite:",
                      ["Silício", "Fósforo e REE", "Oxigénio"], key="gas_q3", index=None)

        if st.session_state.corrigido_gas:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        q4 = st.radio("4️⃣ Tipo de fase da monazite:",
                      ["Inicial", "Fase tardia", "Intermédia"], key="gas_q4", index=None)

        if st.session_state.corrigido_gas:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        q5 = st.radio("5️⃣ Ambiente típico:",
                      ["Pláceres", "Granitos e pegmatitos", "Bacias sedimentares"], key="gas_q5", index=None)

        if st.session_state.corrigido_gas:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")

        if st.button("Concluir"):
            st.session_state.corrigido_gas = True

        if st.session_state.corrigido_gas:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    elif "Depósitos metamórficos" in deposito:

        if "corrigido_mix" not in st.session_state:
            st.session_state.corrigido_mix = False

        corretas = ["Recristalização", "Fluidos metamórficos", "Alanite",
                    "Granada", "Zonamento composicional"]

        q1 = st.radio("1️⃣ Processo principal de formação:",
                      ["Sedimentação", "Recristalização", "Cristalização magmática"], key="mix_q1", index=None)

        if st.session_state.corrigido_mix:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        q2 = st.radio("2️⃣ O que controla a mobilidade dos REE:",
                      ["Pressão", "Fluidos metamórficos", "Temperatura apenas"], key="mix_q2", index=None)

        if st.session_state.corrigido_mix:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        q3 = st.radio("3️⃣ Mineral associado:",
                      ["Olivina", "Alanite", "Halite"], key="mix_q3", index=None)

        if st.session_state.corrigido_mix:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        q4 = st.radio("4️⃣ Mineral que influencia o Y:",
                      ["Quartzo", "Granada", "Calcite"], key="mix_q4", index=None)

        if st.session_state.corrigido_mix:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        q5 = st.radio("5️⃣ Característica típica:",
                      ["Alta porosidade", "Zonamento composicional", "Sem estrutura"], key="mix_q5", index=None)

        if st.session_state.corrigido_mix:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")

        if st.button("Concluir"):
            st.session_state.corrigido_mix = True

        if st.session_state.corrigido_mix:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    else:
        st.info("Selecione um tipo de depósito válido.")

# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_monazite():

    st.markdown("### Checklist de Campo")

    st.write("Avaliação sistemática para identificação e prospeção de monazite:")

    st.markdown("**1. Identificação do mineral**")

    st.checkbox("Cor típica (amarelo, castanho, avermelhado)")
    st.checkbox("Alta densidade (mineral pesado)")
    st.checkbox("Dureza média (5–5,5 na escala de Mohs)")
    st.checkbox("Grãos pequenos, arredondados ou prismáticos")
    st.checkbox("Aspeto maciço ou zonado")

    st.divider()

    st.markdown("**2. Propriedades diagnósticas**")

    st.checkbox("Presença possível de radioatividade (Th/U)")
    st.checkbox("Associação a minerais de terras raras (REE)")
    st.checkbox("Identificação com lupa ou microscópio")

    st.divider()

    st.markdown("**3. Contexto no terreno**")

    st.checkbox("Presente em areias fluviais ou costeiras")
    st.checkbox("Associado a depósitos de plácer (placer)")
    st.checkbox("Proximidade de rochas fonte (granitos, pegmatitos, gnaisses)")
    st.checkbox("Acumulação em zonas de baixa energia")
    st.checkbox("Concentração em camadas ou lentes sedimentares")

    st.divider()

    st.markdown("**4. Minerais associados**")

    st.checkbox("Ilmenite")
    st.checkbox("Zircão")
    st.checkbox("Rutilo")
    st.checkbox("Magnetite")
    st.checkbox("Granada")

    st.divider()

    st.markdown("**5. Indícios de concentração**")

    st.checkbox("Separação por densidade evidente")
    st.checkbox("Remoção de minerais leves (quartzo/feldspato)")
    st.checkbox("Enriquecimento em minerais pesados")
    st.checkbox("Camadas escuras ricas em minerais densos")
    st.checkbox("Retrabalhamento sedimentar (ondas/correntes)")

    st.divider()

    st.markdown("**6. Interpretação geológica**")

    st.checkbox("Origem sedimentar (plácer)")
    st.checkbox("Possível origem magmática (granitos/pegmatitos)")
    st.checkbox("Possível origem metamórfica")
    st.checkbox("Identificação da rocha fonte")

    st.divider()

    st.markdown("**7. Avaliação económica e segurança**")

    st.checkbox("Estimativa da concentração de REE")
    st.checkbox("Verificação de radioatividade")
    st.checkbox("Acessibilidade do local")
    st.checkbox("Impacto ambiental potencial")

    st.divider()

    st.markdown("**8. Registo de campo**")

    st.checkbox("Localização GPS registada")
    st.checkbox("Fotografias do afloramento")
    st.checkbox("Amostras recolhidas")

# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_monazite():

    st.markdown("### 🌍 Mapa global de depósitos de monazite")

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
            "carbonatite": "orange",
            "metamorphic": "green",
            "heavy mineral sands": "blue",
            "hydrothermal": "red"
        }

        mapa = folium.Map(location=[20, 0], zoom_start=2)
        Fullscreen().add_to(mapa)

        for _, row in df.iterrows():
            if pd.notna(row[lat_col]) and pd.notna(row[lon_col]):

                deposit_type = str(row.get("deposit_type", "")).strip().lower()
                color = color_map.get(deposit_type, "gray")

                popup = f"""
                <b>Deposit:</b> {row.get('deposit_name', 'N/A')}<br>
                <b>Country:</b> {row.get('country', 'N/A')}<br>
                <b>Region:</b> {row.get('region', 'N/A')}<br>
                <b>Type:</b> {row.get('deposit_type', 'N/A')}<br>
                <b>REE:</b> {row.get('ree_content', 'N/A')}<br>
                <b>Th:</b> {row.get('thorium_content', 'N/A')}<br>
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
        
        <div><span style="color:orange;">●</span> Carbonatite</div>
        <div><span style="color:green;">●</span> Metamorphic</div>
        <div><span style="color:blue;">●</span> Heavy Mineral Sands</div>
        <div><span style="color:red;">●</span> Hydrothermal</div>
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

def referencias_monazite():

    st.markdown("### 📚 Referências bibliográficas")

    st.write(
    "- Oliveira, E. K., & Chaves, A. O. (2016). Processos geológicos "
    "registados em monazites de pláceres marinhos de Buena (Rio de Janeiro, Brasil). "
    "Comunicações Geológicas, 103(1), 45–49."
    )
    
    st.write(
    "- Clavier, N., Podor, R., & Dacheux, N. (2011). Crystal chemistry "
    "of the monazite structure. Journal of the European Ceramic Society, "
    "31(6), 941–976."
    )
    
    st.write(
    "- García de Madinabeitia, S., Beranoaguirre, A., Martínez, P., "
    "Castroviejo, R., Ortega, E., Bastida, F., Hellebrand, E. W. G., "
    "Burkhalter, E., & Gil Ibarguchi, J. I. (2026). Authigenic grey "
    "monazite from Ordovician metasediments of the Iberian Massif: "
    "The Matamulas placer. Mineralium Deposita."
    )
    
    st.write(
    "- Schulz, B. (2021). Monazite microstructures and their "
    "interpretation in petrochronology. Frontiers in Earth Science, 9, 668566."
    )
    
    st.write(
    "- Dostal, J. (2025). Deposits of rare earth elements in Canada. "
    "FACETS, 10, 1–18."
    )
    
    st.write(
    "- Mohanty, A. K., Sengupta, D., Das, S. K., Saha, S. K., & Van, K. V. "
    "(2004). Natural radioactivity and radiation exposure in the high "
    "background area at Chhatrapur beach placer deposit of Orissa, India. "
    "Journal of Environmental Radioactivity, 75(1), 15–33."
    )
    
    st.write(
    "- Al-Ani, T., Molnár, F., Lintinen, P., & Leinonen, S. (2018). "
    "Geology and mineralogy of rare earth elements deposits and occurrences "
    "in Finland. Minerals, 8(8), 356."
    )
    
    st.write(
    "- Chen, W., Huang, H., Bai, T., & Jiang, S. (2017). Geochemistry "
    "of monazite within carbonatite related REE deposits. Resources, 6(4), 51."
    )
    
    st.write(
    "- Staatz, M. H., Armbrustmacher, T. J., Olson, J. C., Brownfield, I. K., "
    "Brock, M. R., Lemons, J. F., Jr., Coppa, L. V., & Clingan, B. V. (1979). "
    "Principal thorium resources in the United States (Geological Survey "
    "Circular 805). U.S. Geological Survey."
    )
    
    st.write(
    "- Smith, M. P., Moore, K., Kavecsánszki, D., Finch, A. A., Kynicky, J., "
    "& Wall, F. (2016). From mantle to critical zone: A review of large "
    "and giant sized deposits of the rare earth elements. Geoscience "
    "Frontiers, 7(3), 315–334."
    )
    
    st.write(
    "- Goodenough, K. M., Schilling, J., Jonsson, E., Kalvig, P., Charles, N., "
    "Tuduri, J., Deady, E. A., Sadeghi, M., Schiellerup, H., Müller, A., "
    "Bertrand, G., Arvanitidis, N., Eliopoulos, D. G., Shaw, R. A., "
    "Thrane, K., & Keulen, N. (2016). Europe’s rare earth element resource "
    "potential: An overview of REE metallogenetic provinces and their "
    "geodynamic setting. Ore Geology Reviews, 72, 838–856."
    )
    
    st.caption("Referências utilizadas.")