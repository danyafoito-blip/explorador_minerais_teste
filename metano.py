# ===============================
# BIBLIOTECAS EXTERNAS
# ===============================

import streamlit as st
import streamlit.components.v1 as components

# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_metano(deposito):

    st.markdown("### Hidrato de metano")
    
    st.markdown(
    """
    Os **hidratos de metano** (ou clatratos de metano) são **sólidos cristalinos não estequiométricos** 
    em que moléculas de água formam uma estrutura em **gaiola (clatrato)** que aprisiona 
    moléculas de **metano (CH₄)**.
    """
    )
    
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        
        st.success("**Propriedades físicas**")
        
        st.write("- Sólido semelhante ao gelo")
        st.write("- Estrutura cristalina em gaiola (clatrato)")
        st.write("- Densidade inferior à água (~0,91 g/cm³)")
        st.write("- Mais resistente que o gelo comum")
        st.write("- Elevada densidade energética (liberta muito gás)")
        st.write("- Estável apenas a **alta pressão e baixa temperatura**")

    with col2:

        st.info("**Propriedades químicas**")
                
        st.write("- Metano aprisionado fisicamente (sem ligação química)")
        st.write("- Estrutura não estequiométrica (nem todas as cavidades ocupadas)")
        st.write("- Formação liberta calor (processo exotérmico)")
        st.write("- Dissociação absorve calor")
        st.write("- Sensível à salinidade (sais dificultam formação)")
        st.write("- Inibido por álcool e poros muito pequenos")

    st.divider()

    if "Biogénico" in deposito:
        
        st.markdown("### Hidratos de metano biogénico")    
        
        st.write("""
        Os **hidratos de metano biogénicos** são clatratos (sólidos cristalinos não estequiométricos) 
        formados por uma rede de água que aprisiona **metano produzido por microrganismos**, 
        resultante da **biodegradação da matéria orgânica** em ambientes sedimentares.
        """)
    
        st.divider()
        
        st.markdown("### Metanogénese")

        st.write("""
        A **produção de metano biogénico** ocorre em ambientes **anóxicos (sem oxigénio)**, 
        quando a matéria orgânica é degradada por microrganismos ao longo do soterramento.
        """)
        
        st.markdown("#### Sequência diagenética")
        
        st.markdown("""
        - **Zona aeróbica** → degradação com oxigénio  
        - **Zona de redução de sulfato** → consumo de sulfato (inibe metano)  
        - **Zona metanogénica** → inicia-se a produção de CH₄  
        """)
        
        st.info("🧪 A metanogénese começa apenas após o esgotamento do sulfato.")
        
        st.markdown("#### Vias de produção de metano biogénico")
        
        col1, col2 = st.columns(2)

        with col1:
            st.success("Redução de CO₂")
            st.write("""
            - Dominante em ambientes marinhos  
            - Usa H₂ gerado por fermentação  
            """)
            
            st.code(
                """
        CO₂ + 4H₂ → CH₄ + 2H₂O
        (Dióxido de carbono + Hidrogénio → Metano + Água)
                """
            )
        
        with col2:
            st.success("Fermentação de acetato")
            st.write("""
            - Mais comum em água doce  
            - Deriva da degradação orgânica  
            """)
            
            st.code(
                """
        CH₃COOH → CH₄ + CO₂
        (Ácido acético → Metano + Dióxido de carbono)
                """
            )
        
        st.markdown("#### Fatores de controlo")
        
        st.markdown("""
        - **Matéria orgânica lábil** (biodegradável)  
        - **Temperatura** (< 50 °C)  
        - **Tempo geológico** (processo lento)  
        """)
        
        st.warning("""
        ⚠️ Parte da matéria orgânica pode originar metano **termogénico** em maior profundidade.
        """)        
        
        st.divider()
        
        st.markdown("### Rocha-mãe")
        
        st.write("""
        A **rocha-mãe** é o nível sedimentar rico em matéria orgânica responsável pela 
        **geração de metano biogénico**.
        """)
        
        st.markdown("#### Características principais")
        
        st.markdown("""
        - Sedimentos finos: **lamas, argilas e siltes**  
        - Elevado **Carbono Orgânico Total (COT)**  
        - Ambiente deposicional geralmente **marinho**  
        """)
        
        st.markdown("#### Matéria orgânica")
        
        st.write("""
        Nem toda a matéria orgânica contribui para a formação de metano:
        """)
        
        st.markdown("""
        - **Fração lábil** → biodegradável → gera metano biogénico  
        - **Fração refratária** → resistente → pode originar metano termogénico em profundidade  
        """)
        
        st.info("""
        A eficiência da rocha-mãe depende da quantidade e qualidade da matéria orgânica disponível.
        """)
        
        st.divider()
        
        st.markdown("### Migração")
        
        st.write("""
        A **migração do metano** corresponde ao transporte do gás desde a sua zona de geração 
        até à **GHSZ (Gas Hydrate Stability Zone)**, onde pode formar hidratos.
        """)
        
        st.markdown("#### Etapas da migração")
        
        st.markdown("""
        - **Migração primária** → libertação do metano da rocha-mãe  
        - **Migração secundária** → deslocação através dos sedimentos até zonas de acumulação  
        """)
        
        st.markdown("#### Mecanismos de transporte")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("Advecção")
            st.write("""
            - Controlada por **gradientes de pressão** e flutuabilidade  
            - Transporte rápido e eficiente  
            - Ocorre em fraturas, falhas e sedimentos permeáveis  
            """)
        
        with col2:
            st.info("Difusão")
            st.write("""
            - Controlada por **gradientes de concentração**  
            - Processo lento  
            - Dominante em meios pouco permeáveis  
            """)
        
        st.markdown("#### Forma de transporte")
        
        st.markdown("""
        - Metano pode migrar como:
          - Gás livre (bolhas)  
          - Dissolvido na água intersticial  
        """)
        
        st.warning("""
        ⚠️ A migração eficiente é essencial para concentrar metano suficiente 
        para formar hidratos.
        """)        
        
        st.divider()
        
        st.markdown("### Condições físico-químicas de estabilidade")
        
        st.write("""
        Os hidratos são estáveis na **GHSZ**:
        
        - Alta pressão + baixa temperatura  
        - Oceanos: > 300–600 m profundidade  
        - Permafrost: 100–200 m profundidade
        
        **Controlos principais:**
        - Pressão e temperatura  
        - Disponibilidade de metano e água  
        - Salinidade (inibe formação)
        """)        
        
        st.divider()
        
        st.markdown("### Formação dos hidratos")

        st.write("""
        A **formação de hidratos de metano** ocorre quando a concentração de metano na água 
        excede a sua **solubilidade local** dentro da **GHSZ**.
        """)
        
        st.markdown("#### Processo")
        
        st.markdown("""
        1. Aumento da concentração de metano na água intersticial  
        2. Excede a solubilidade local  
        3. O metano incorpora-se na rede de moléculas de água  
        4. Formação de estrutura cristalina (hidrato)  
        """)
        
        st.info("""
        A cristalização pode ser rápida após atingir o equilíbrio termodinâmico.
        """)
        
        st.markdown("#### Ocorrência nos sedimentos")
        
        st.markdown("""
        - **Sedimentos arenosos** → hidratos preenchem os espaços porosos  
        - **Matrizes argilosas** → hidratos formam-se em fraturas  
        """)
        
        st.markdown("#### Condição favorável")
        
        st.markdown("""
        - Baixas pressões capilares em sedimentos arenosos favorecem a acumulação de hidratos  
        """)
        
        st.divider()
        
        st.markdown("### Ambientes geológicos favoráveis")
                       
        st.write("""
        Principais locais de ocorrência:
        
        - Margens continentais e bacias profundas  
        - Zonas com migração ativa (cold seeps)  
        - Regiões de permafrost
        
        Estes ambientes favorecem a **acumulação e estabilidade** dos hidratos.
        """)

    elif "Termogénico" in deposito:
    
        st.markdown("### Hidratos de metano termogénico")

        st.write("""
        Os **hidratos de metano termogénicos** são clatratos (sólidos cristalinos não estequiométricos) 
        formados por uma rede de água que aprisiona **metano gerado por processos térmicos em profundidade**.
        """)
        
        st.divider()
    
        st.markdown("### Metanogénese")
        
        st.write("""
        O **metano termogénico** resulta da transformação da matéria orgânica em profundidade, 
        sob **elevadas pressões e temperaturas**.
        """)
        
        st.markdown("#### Processo")
        
        st.markdown("""
        - Ocorre durante a **catagénese e metagénese**  
        - Resulta da **quebra térmica do querogénio**  
        - Desenvolve-se geralmente a profundidades > 1 km  
        """)
        
        st.markdown("#### Condições")
        
        st.markdown("""
        - Intervalo típico: **80 °C – 150 °C**  
        - Pico de geração de metano: ~ **150 °C**  
        """)
        
        st.info("""
        O metano forma-se a partir de matéria orgânica que resistiu à biodegradação inicial.
        """)
        
        st.divider()
    
        st.markdown("### Rocha-mãe")
        
        st.write("""
        A **rocha-mãe** corresponde a formações profundas ricas em matéria orgânica, 
        com capacidade para gerar hidrocarbonetos.
        """)
        
        st.markdown("#### Características")
        
        st.markdown("""
        - Profundidade típica: **> 1 km até ~5 km**  
        - Litologias: **argilitos, margas e rochas carbonatadas**  
        - Elevado **Carbono Orgânico Total (COT)**  
        """)
        
        st.markdown("#### Matéria orgânica")
        
        st.markdown("""
        - **Fração refratária** → resistente à biodegradação  
        - Conversão térmica do **querogénio (Tipos I, II ou III)** em metano  
        """)
        
        st.divider()
    
        st.markdown("### Migração")
    
        st.write("""
        A **migração do metano** corresponde ao transporte do gás desde a sua zona de geração 
        até à **GHSZ (Gas Hydrate Stability Zone)**, onde pode formar hidratos.
        """)
    
        st.markdown("#### Etapas da migração")
    
        st.markdown("""
        - **Migração primária** → libertação do metano da rocha-mãe  
        - **Migração secundária** → deslocação através dos sedimentos até zonas de acumulação  
        """)
    
        st.markdown("#### Mecanismos de transporte")
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.success("Advecção")
            st.write("""
            - Controlada por **gradientes de pressão** e flutuabilidade  
            - Transporte rápido e eficiente  
            - Ocorre em fraturas, falhas e sedimentos permeáveis  
            """)
    
        with col2:
            st.info("Difusão")
            st.write("""
            - Controlada por **gradientes de concentração**  
            - Processo lento  
            - Dominante em meios pouco permeáveis  
            """)
    
        st.markdown("#### Forma de transporte")
    
        st.markdown("""
        - Metano pode migrar como:
          - Gás livre (bolhas)  
          - Dissolvido na água intersticial  
        """)
    
        st.warning("""
        ⚠️ A migração eficiente é essencial para concentrar metano suficiente 
        para formar hidratos.
        """)
    
        st.divider()
    
        st.markdown("### Condições físico-químicas de estabilidade")
    
        st.write("""
        Os hidratos são estáveis na **GHSZ**:
        
        - Alta pressão + baixa temperatura  
        - Oceanos: > 300–600 m profundidade  
        - Permafrost: 100–200 m profundidade
        
        **Controlos principais:**
        - Pressão e temperatura  
        - Disponibilidade de metano e água  
        - Salinidade (inibe formação)
        """)
    
        st.divider()
    
        st.markdown("### Formação dos hidratos")
    
        st.write("""
        A **formação de hidratos de metano** ocorre quando a concentração de metano na água 
        excede a sua **solubilidade local** dentro da **GHSZ**.
        """)
    
        st.markdown("#### Processo")
    
        st.markdown("""
        1. Aumento da concentração de metano na água intersticial  
        2. Excede a solubilidade local  
        3. O metano incorpora-se na rede de moléculas de água  
        4. Formação de estrutura cristalina (hidrato)  
        """)
    
        st.info("""
        A cristalização pode ser rápida após atingir o equilíbrio termodinâmico.
        """)
    
        st.markdown("#### Ocorrência nos sedimentos")
    
        st.markdown("""
        - **Sedimentos arenosos** → hidratos preenchem os espaços porosos  
        - **Matrizes argilosas** → hidratos formam-se em fraturas  
        """)
    
        st.markdown("#### Condição favorável")
    
        st.markdown("""
        - Baixas pressões capilares em sedimentos arenosos favorecem a acumulação de hidratos  
        """)
    
        st.divider()
    
        st.markdown("### Ambientes geológicos favoráveis")
    
        st.write("""
        Principais locais de ocorrência:
        
        - Margens continentais e bacias profundas  
        - Zonas com migração ativa (cold seeps)  
        - Regiões de permafrost
        
        Estes ambientes favorecem a **acumulação e estabilidade** dos hidratos.
        """)

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_metano():

    st.markdown("### Confusões comuns")

    st.markdown("**1. Metano biogénico vs Metano termogénico**")

    st.write("""
- **Metano biogénico**:
  - Origem microbiana (metanogénese)
  - Baixas temperaturas (< 50 ºC)
  - Sedimentos superficiais
  - Matéria orgânica lábil

- **Metano termogénico**:
  - Origem térmica (catagénese/metagénese)
  - Altas temperaturas (80–150 ºC ou mais)
  - Grandes profundidades (> 1 km)
  - Matéria orgânica refratária (querogénio)
    """)

    st.info("💡 A diferença está na origem do metano.")

    st.divider()

    st.markdown("**2. Hidratos biogénicos vs Hidratos termogénicos**")

    st.write("""
- **Hidratos biogénicos**:
  - Formados a partir de metano produzido localmente
  - Associados a sedimentos pouco profundos
  - Migração curta ou inexistente

- **Hidratos termogénicos**:
  - Formados a partir de metano gerado em profundidade
  - Requerem migração até à GHSZ
  - Podem estar associados a sistemas petrolíferos
    """)
    
    st.info("💡 Os hidratos são estruturalmente iguais, o que muda é apenas a origem do metano.")

    st.divider()

    st.markdown("**3. Local de formação vs Local de acumulação**")

    st.write("""
- **Metano biogénico**:
  - Formação e acumulação ocorrem praticamente no mesmo local

- **Metano termogénico**:
  - Formação em profundidade
  - Acumulação na GHSZ após migração
    """)

    st.info("💡 No termogénico, geração e acumulação estão separadas.")

    st.divider()

    st.markdown("**4. Migração do metano**")

    st.write("""
- **Metano biogénico**:
  - Migração limitada
  - Difusão dominante

- **Metano termogénico**:
  - Migração longa distância
  - Advecção dominante (falhas, fraturas)
    """)

    st.info("💡 A migração é muito mais importante nos sistemas termogénicos.")

    st.divider()

    st.markdown("**5. Relação com sistemas petrolíferos**")

    st.write("""
- **Metano biogénico**:
  - Sistema mais simples
  - Controlado por processos microbiológicos

- **Metano termogénico**:
  - Parte de um sistema petrolífero completo
  - Inclui rocha-mãe, migração e acumulação
    """)

    st.info("💡 Hidratos termogénicos podem estar ligados a reservatórios de petróleo e gás.")

# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_metano(deposito):

    st.markdown("### Quiz interativo")
    st.caption("Testa os teus conhecimentos")

    if "Biogénico" in deposito:

        if "corrigido_bio" not in st.session_state:
            st.session_state.corrigido_bio = False

        corretas = [
            "Microbiana (metanogénese)",
            "< 50 ºC",
            "Zona metanogénica",
            "Difusão",
            "Matéria orgânica lábil"
        ]

        q1 = st.radio("1️⃣ Origem do metano biogénico:",
                      ["Térmica", "Microbiana (metanogénese)", "Magmática"],
                      key="bio_q1", index=None)

        if st.session_state.corrigido_bio:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        q2 = st.radio("2️⃣ Intervalo típico de temperatura:",
                      ["< 50 ºC", "80–150 ºC", "> 200 ºC"],
                      key="bio_q2", index=None)

        if st.session_state.corrigido_bio:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        q3 = st.radio("3️⃣ Zona onde se inicia a produção de metano:",
                      ["Zona aeróbica", "Zona de redução de sulfato", "Zona metanogénica"],
                      key="bio_q3", index=None)

        if st.session_state.corrigido_bio:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        q4 = st.radio("4️⃣ Principal mecanismo de migração:",
                      ["Advecção", "Difusão", "Convecção"],
                      key="bio_q4", index=None)

        if st.session_state.corrigido_bio:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        q5 = st.radio("5️⃣ Tipo de matéria orgânica dominante:",
                      ["Refratária", "Matéria orgânica lábil", "Querogénio maduro"],
                      key="bio_q5", index=None)

        if st.session_state.corrigido_bio:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")

        if st.button("Concluir"):
            st.session_state.corrigido_bio = True

        if st.session_state.corrigido_bio:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    elif "Termogénico" in deposito:

        if "corrigido_termo" not in st.session_state:
            st.session_state.corrigido_termo = False

        corretas = [
            "Térmica (catagénese/metagénese)",
            "80–150 ºC",
            "> 1 km",
            "Advecção",
            "Querogénio"
        ]

        q1 = st.radio("1️⃣ Origem do metano termogénico:",
                      ["Microbiana", "Térmica (catagénese/metagénese)", "Atmosférica"],
                      key="termo_q1", index=None)

        if st.session_state.corrigido_termo:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        q2 = st.radio("2️⃣ Intervalo típico de temperatura:",
                      ["< 50 ºC", "80–150 ºC", "0–20 ºC"],
                      key="termo_q2", index=None)

        if st.session_state.corrigido_termo:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        q3 = st.radio("3️⃣ Profundidade típica de formação:",
                      ["< 100 m", "200–500 m", "> 1 km"],
                      key="termo_q3", index=None)

        if st.session_state.corrigido_termo:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        q4 = st.radio("4️⃣ Principal mecanismo de migração:",
                      ["Difusão", "Advecção", "Osmose"],
                      key="termo_q4", index=None)

        if st.session_state.corrigido_termo:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        q5 = st.radio("5️⃣ Principal fonte de metano:",
                      ["Matéria orgânica lábil", "Querogénio", "Plâncton vivo"],
                      key="termo_q5", index=None)

        if st.session_state.corrigido_termo:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")

        if st.button("Concluir"):
            st.session_state.corrigido_termo = True

        if st.session_state.corrigido_termo:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    else:
        st.info("Selecione um tipo de depósito válido.")

# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_metano():

    st.markdown("### Checklist de campo")

    st.write("Avaliação integrada de um sistema de hidratos de metano:")

    st.markdown("**1. Fonte de metano**")

    st.checkbox("Identificar sedimentos ricos em matéria orgânica")
    st.checkbox("Avaliar Carbono Orgânico Total (COT)")
    st.checkbox("Determinar origem do metano (biogénica, termogénica ou mista)")
    st.checkbox("Confirmar presença de matéria orgânica lábil ou querogénio")
    st.checkbox("Avaliar potencial de geração de metano")

    st.divider()

    st.markdown("**2. Geração de metano**")

    st.checkbox("Confirmar metanogénese (ambientes anóxicos)")
    st.checkbox("Identificar zona metanogénica (abaixo da zona de sulfato)")
    st.checkbox("Confirmar maturação térmica (catagénese/metagénese)")
    st.checkbox("Verificar intervalo térmico adequado (<50 ºC ou >80 ºC)")
    st.checkbox("Avaliar profundidade de geração")

    st.divider()

    st.markdown("**3. Migração do metano**")

    st.checkbox("Avaliar extensão da migração (curta ou longa distância)")
    st.checkbox("Avaliar difusão (meios pouco permeáveis)")
    st.checkbox("Avaliar advecção (falhas e fraturas)")
    st.checkbox("Mapear vias de migração (estruturas geológicas)")
    st.checkbox("Confirmar transporte até à GHSZ")

    st.divider()

    st.markdown("**4. Condições de estabilidade (GHSZ)**")

    st.checkbox("Confirmar presença da GHSZ (Gas Hydrate Stability Zone)")
    st.checkbox("Verificar alta pressão e baixa temperatura")
    st.checkbox("Avaliar profundidade da coluna de água ou permafrost")
    st.checkbox("Confirmar disponibilidade de água")
    st.checkbox("Avaliar impacto da salinidade")

    st.divider()

    st.markdown("**5. Formação de hidratos**")

    st.checkbox("Confirmar supersaturação de metano na água intersticial")
    st.checkbox("Verificar incorporação do metano na estrutura cristalina")
    st.checkbox("Avaliar equilíbrio termodinâmico")
    st.checkbox("Identificar zonas de cristalização ativa")
    st.checkbox("Confirmar condições favoráveis à nucleação")

    st.divider()

    st.markdown("**6. Acumulação**")

    st.checkbox("Identificar hidratos em sedimentos arenosos (poros)")
    st.checkbox("Identificar hidratos em sedimentos argilosos (fraturas)")
    st.checkbox("Avaliar saturação de hidratos")
    st.checkbox("Confirmar concentração suficiente de metano")
    st.checkbox("Avaliar estabilidade do depósito")

    st.divider()

    st.markdown("**7. Indicadores complementares**")

    st.checkbox("Presença de cold seeps ou exsudações de gás")
    st.checkbox("Anomalias sísmicas (BSR - Bottom Simulating Reflector)")
    st.checkbox("Deteção de metano (CH₄) em sedimentos ou água")
    st.checkbox("Evidência de fluxos de fluido")
    st.checkbox("Dados geofísicos e geoquímicos consistentes")

    st.success("💡 Sistema viável: fonte de metano + geração + migração + GHSZ + acumulação.")
    
# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_metano():

    st.markdown("### 🌍 Mapa global de ocorrências de metano")

    with open("hydrates_methane_clathrates_occurrences.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    html_with_fullscreen = f"""
    <button onclick="openFullscreen()" style="
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 9999;
        padding: 8px 12px;
        background-color: #1f77b4;
        color: white;
        border: none;
        border-radius: 6px;
        cursor: pointer;">
        ⛶ Fullscreen
    </button>

    <script>
    function openFullscreen() {{
        var elem = document.documentElement;
        if (elem.requestFullscreen) {{
            elem.requestFullscreen();
        }} else if (elem.webkitRequestFullscreen) {{
            elem.webkitRequestFullscreen();
        }} else if (elem.msRequestFullscreen) {{
            elem.msRequestFullscreen();
        }}
    }}
    </script>

    {html_content}
    """

    components.html(html_with_fullscreen, height=700, scrolling=True)

# ===============================
# 6. REFERÊNCIAS
# ===============================

def referencias_metano():

    st.markdown("### 📚 Referências bibliográficas")

    st.write(
    "- You, K., Flemings, P. B., Malinverno, A., Collett, T. S., "
    "& Darnell, K. (2019). Mechanisms of methane hydrate formation "
    "in geological systems. Reviews of Geophysics, 57, 1146–1196."
    )
    
    st.write(
    "- Boswell, R., & Collett, T. S. (2011). Current perspectives "
    "on gas hydrate resources. Energy & Environmental Science, 4, "
    "1206–1215."
    )
    
    st.write(
    "- Chen, W., Bai, C., Xu, H., & Xu, X. (2025). Sedimentary "
    "processes controlling gas hydrate accumulation in the Shenhu "
    "area. Frontiers in Marine Science, 12, 1637686."
    )
    
    st.write(
    "- Ferreira, D. de B. (2007). Os hidratos de metano: Fonte "
    "energética do futuro ou fonte de risco ambiental? Finisterra, "
    "42(83), 79–90."
    )
    
    st.write(
    "- Souza, M. B. B., Oliveira, M. B., Castro, J. A., Silva, A. J., "
    "& Rossi, L. F. S. (2012). Análise termodinâmica da formação de "
    "hidratos de gás metano. Rev. Eng. e Tecnologia, 4(1), 1–10."
    )
    
    st.write(
    "- Ferreira Filho, I. R., da Silveira, K. C., & Silva Neto, A. J. "
    "(2021). Tecnologia de hidrato de gás: modelagem computacional. "
    "Vetor, 31(1), 23–42."
    )
    
    st.write(
    "- Wang, X., Yuan, Y., Du, Z., Guo, G., Liu, B., & Yang, J. "
    "(2024). Mineral effects on methane hydrate formation. "
    "Geoenergy Science and Engineering, 243, 213379."
    )
    
    st.write(
    "- Daigle, H., & Dugan, B. (2010). Origin and evolution of "
    "fracture-hosted methane hydrate deposits. JGR Solid Earth, "
    "115, B11103."
    )
    
    st.write(
    "- Spigolon, A. L. D., Pena dos Reis, R. P. B., Pimentel, N. L., "
    "& Matos, V. G. A. E. (2011). Geoquímica orgânica de rochas "
    "geradoras de petróleo. Bol. Geociências Petrobras, 19, 131–162."
    )
    
    st.write(
    "- Menezes, D. E. S. et al. (2016). Estudo experimental da "
    "formação e dissociação de hidratos de metano. COBEQ 2016."
    )
    
    st.caption("Referências utilizadas.")
    