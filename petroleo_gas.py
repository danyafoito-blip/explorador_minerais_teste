# ===============================
# BIBLIOTECAS EXTERNAS
# ===============================

import streamlit as st
import streamlit.components.v1 as components


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_petroleo(deposito):

    st.markdown("### Petróleo e gás")
    
    st.markdown(
        """
        O **petróleo e o gás natural** são misturas complexas de **hidrocarbonetos** 
        e compostos orgânicos associados, gerados a partir da matéria orgânica 
        ao longo de processos geológicos e acumulados em sistemas petrolíferos.  
        """
    )
      
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
    
        st.success("**Propriedades físicas**")
    
        st.write("- Estado líquido (óleo), podendo ocorrer como gás ou sólido (betume)")
        st.write("- Densidade geralmente menor que a da água")
        st.write("- Grau API define óleo leve ou pesado")
        st.write("- Viscosidade variável controla o fluxo")
        st.write("- Dependência de pressão e temperatura (P–T)")
    
    with col2:
    
        st.info("**Propriedades químicas**")
    
        st.write("- Mistura complexa de compostos orgânicos")
        st.write("- Predominância de carbono e hidrogénio")
        st.write("- Presença de enxofre, oxigénio e azoto")
        st.write("- Diferentes tipos de hidrocarbonetos com estruturas variadas")
        st.write("- Componentes pesados influenciam as propriedades do óleo")

    st.divider()

    if "Reservatório de óleo" in deposito:

        st.markdown("### Reservatório de óleo")
    
        st.success(
            "Um reservatório de óleo é um reservatório em que a mistura de hidrocarbonetos "
            "se encontra predominantemente no estado líquido, nas condições de pressão e temperatura do reservatório."
        )
    
        st.divider()
    
        st.markdown("### Rocha-mãe")
    
        with st.container():
            st.info(
                "Rocha sedimentar de grão fino rica em matéria orgânica que, com soterramento e aquecimento, "
                "gera e expulsa hidrocarbonetos."
            )
    
            col1, col2 = st.columns(2)
    
            with col1:
                st.markdown("**Requisitos:**")
                st.write("- Rica em querogénio")
                st.write("- Elevado Carbono Orgânico Total (COT > 2%)")
    
            with col2:
                st.markdown("**Tipos comuns:**")
                st.write("- Argilitos lacustres (lacustrine shale)")
                st.write("- Margas calcárias")
    
        st.markdown("#### Tipo de querogénio")
    
        st.success(
            "Tipo I (liptinito): origem algal (ambientes lacustres/lagunares), principal responsável pela geração de óleo."
        )
    
        st.divider()
    
        st.markdown("### Maturação térmica")
    
        st.warning(
            "A maturação térmica ocorre com o soterramento (overburden), aumentando pressão e temperatura."
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.metric("Temperatura (janela de óleo)", "100 – 150 ºC")
    
        with col2:
            st.metric("Refletância da vitrinite", "0.6 – 1.3 %")
    
        st.write("Fase principal: catagénese")
    
        st.divider()
    
        st.markdown("### Migração")
    
        st.info(
            "Processo de deslocação dos hidrocarbonetos desde a rocha-mãe até ao reservatório ou à superfície."
        )
    
        st.markdown("**Tipos de migração:**")
        st.write("- Primária → expulsão da rocha-mãe")
        st.write("- Secundária → movimento em rochas permeáveis")
        st.write("- Terciária → fuga para a superfície")
    
        st.divider()
    
        st.markdown("### Rocha reservatório")
    
        st.success(
            "Formação geológica com porosidade e permeabilidade suficientes para armazenar e permitir o fluxo de hidrocarbonetos."
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("**Função:**")
            st.write("- Armazenamento de fluidos")
            st.write("- Permitir fluxo")
    
        with col2:
            st.markdown("**Tipos principais:**")
            st.write("- Arenitos")
            st.write("- Calcários e dolomitos")
    
        st.divider()
    
        st.markdown("### Rocha selante")
    
        st.error(
            "Camada impermeável que impede a migração dos hidrocarbonetos, garantindo a sua acumulação."
        )
    
        st.write("**Principais tipos:**")
        st.write("- Argilitos (shales)")
        st.write("- Evaporitos (sal e anidrita)")
    
        st.divider()
    
        st.markdown("### Armadilhas")
    
        st.info(
            "Configurações que permitem a acumulação significativa de hidrocarbonetos."
        )
    
        st.write("Uma armadilha eficaz requer:")
        st.write("- Rocha reservatório")
        st.write("- Rocha selante")
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("**Estruturais**")
            st.write("- Anticlinais")
            st.write("- Falhas")
            st.write("- Diapíricas")
    
        with col2:
            st.markdown("**Estratigráficas**")
            st.write("- Pinch-outs")
            st.write("- Mudanças de fácies")
            st.write("- Desconformidades")
            st.write("- Diagenéticas")

    elif "Reservatório de gás" in deposito:

        st.markdown("### Reservatório de gás")
    
        st.success(
            "Um reservatório de gás é um reservatório em que a mistura de hidrocarbonetos "
            "se encontra predominantemente no estado gasoso, nas condições de pressão e temperatura do reservatório."
        )
    
        st.divider()
    
        st.markdown("### Rocha-mãe")
    
        with st.container():
            st.info(
                "Rocha sedimentar de grão fino rica em matéria orgânica que, com soterramento e aquecimento, "
                "gera e expulsa hidrocarbonetos."
            )
    
            col1, col2 = st.columns(2)
    
            with col1:
                st.markdown("**Requisitos:**")
                st.write("- Rica em querogénio")
                st.write("- Elevado Carbono Orgânico Total (COT > 2%)")
    
            with col2:
                st.markdown("**Tipos comuns:**")
                st.write("- Carvões (lignito, hulha)")
                st.write("- Argilitos carbonosos (carbonaceous shale)")
                st.write("- Siltitos ricos em matéria vegetal")
    
        st.markdown("#### Tipo de querogénio")
    
        st.success(
            "Tipo III (vitrinito): derivado de detritos de plantas terrestres superiores e lenhosas, principal responsável pela geração de gás."
        )
    
        st.divider()
    
        st.markdown("### Maturação térmica")
    
        st.warning(
            "A maturação térmica ocorre com o soterramento (overburden), aumentando pressão e temperatura."
        )
    
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Temperatura (janela de gás)", "150 – 300 ºC")
        
        with col2:
            st.metric("Refletância da vitrinite", "1,3 – 4,0 %")
        
        st.write("Fases principais: catagénese tardia e metagénese")
    
        st.divider()
    
        st.markdown("### Migração")
    
        st.info(
            "Processo de deslocação dos hidrocarbonetos desde a rocha-mãe até ao reservatório ou à superfície."
        )
    
        st.markdown("**Tipos de migração:**")
        st.write("- Primária → expulsão da rocha-mãe")
        st.write("- Secundária → movimento em rochas permeáveis")
        st.write("- Terciária → fuga para a superfície")
    
        st.divider()
    
        st.markdown("### Rocha reservatório")
    
        st.success(
            "Formação geológica com porosidade e permeabilidade suficientes para armazenar e permitir o fluxo de hidrocarbonetos."
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("**Função:**")
            st.write("- Armazenamento de fluidos")
            st.write("- Permitir fluxo")
    
        with col2:
            st.markdown("**Tipos principais:**")
            st.write("- Arenitos")
            st.write("- Calcários e dolomitos")
    
        st.divider()
    
        st.markdown("### Rocha selante")
    
        st.error(
            "Camada impermeável que impede a migração dos hidrocarbonetos, garantindo a sua acumulação."
        )
    
        st.write("**Principais tipos:**")
        st.write("- Argilitos (shales)")
        st.write("- Evaporitos (sal e anidrita)")
    
        st.divider()
    
        st.markdown("### Armadilhas")
    
        st.info(
            "Configurações que permitem a acumulação significativa de hidrocarbonetos."
        )
    
        st.write("Uma armadilha eficaz requer:")
        st.write("- Rocha reservatório")
        st.write("- Rocha selante")
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("**Estruturais**")
            st.write("- Anticlinais")
            st.write("- Falhas")
            st.write("- Diapíricas")
    
        with col2:
            st.markdown("**Estratigráficas**")
            st.write("- Pinch-outs")
            st.write("- Mudanças de fácies")
            st.write("- Desconformidades")
            st.write("- Diagenéticas")

    elif "Reservatório misto (óleo + gás)" in deposito:

        st.markdown("### Reservatório misto")
    
        st.success(
            "Um reservatório misto contém hidrocarbonetos nas fases líquida e gasosa, "
            "em quantidades significativas, nas condições de pressão e temperatura do reservatório."
        )
        
        st.divider()
    
        st.markdown("### Rocha-mãe")
    
        with st.container():
            st.info(
                "Rocha sedimentar de grão fino rica em matéria orgânica que, com soterramento e aquecimento, "
                "gera e expulsa hidrocarbonetos."
            )
    
            col1, col2 = st.columns(2)
    
            with col1:
                st.markdown("**Requisitos:**")
                st.write("- Rica em querogénio")
                st.write("- Elevado Carbono Orgânico Total (COT > 2%)")
    
            with col2:
                st.markdown("**Tipos comuns:**")
                st.write("- Argilitos negros (black shales)")
                st.write("- Calcários betuminosos")
                st.write("- Margas")
    
        st.markdown("#### Tipo de querogénio")
    
        st.success(
            "Tipo II (exinito): derivado de plâncton marinho e bactérias, associado à geração de petróleo e gás."
        )
    
        st.divider()
    
        st.markdown("### Maturação térmica")
    
        st.warning(
            "A maturação térmica ocorre com o soterramento (overburden), aumentando pressão e temperatura."
        )
        
        st.info(
            "A geração de óleo e gás ocorre frequentemente quando a rocha-mãe atravessa diferentes estágios de maturação, de forma simultânea ou sucessiva."
        )
    
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Temperatura (janela óleo + gás)", "100 – 300 ºC")
        
        with col2:
            st.metric("Refletância da vitrinite", "0.6 – 4.0 %")
        
        st.write("Fases principais: catagénese, catagénese tardia e metagénese")

        st.divider()
    
        st.markdown("### Migração")
    
        st.info(
            "Processo de deslocação dos hidrocarbonetos desde a rocha-mãe até ao reservatório ou à superfície."
        )
    
        st.markdown("**Tipos de migração:**")
        st.write("- Primária → expulsão da rocha-mãe")
        st.write("- Secundária → movimento em rochas permeáveis")
        st.write("- Terciária → fuga para a superfície")
    
        st.divider()
    
        st.markdown("### Rocha reservatório")
    
        st.success(
            "Formação geológica com porosidade e permeabilidade suficientes para armazenar e permitir o fluxo de hidrocarbonetos."
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("**Função:**")
            st.write("- Armazenamento de fluidos")
            st.write("- Permitir fluxo")
    
        with col2:
            st.markdown("**Tipos principais:**")
            st.write("- Arenitos")
            st.write("- Calcários e dolomitos")
    
        st.divider()
    
        st.markdown("### Rocha selante")
    
        st.error(
            "Camada impermeável que impede a migração dos hidrocarbonetos, garantindo a sua acumulação."
        )
    
        st.write("**Principais tipos:**")
        st.write("- Argilitos (shales)")
        st.write("- Evaporitos (sal e anidrita)")
    
        st.divider()
    
        st.markdown("### Armadilhas")
    
        st.info(
            "Configurações que permitem a acumulação significativa de hidrocarbonetos."
        )
    
        st.write("Uma armadilha eficaz requer:")
        st.write("- Rocha reservatório")
        st.write("- Rocha selante")
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("**Estruturais**")
            st.write("- Anticlinais")
            st.write("- Falhas")
            st.write("- Diapíricas")
    
        with col2:
            st.markdown("**Estratigráficas**")
            st.write("- Pinch-outs")
            st.write("- Mudanças de fácies")
            st.write("- Desconformidades")
            st.write("- Diagenéticas")

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_petroleo():

    st.markdown("### Confusões comuns")

    st.markdown("**1. Reservatório de óleo vs Reservatório de gás vs Reservatório misto**")

    st.write("""
- **Reservatório de óleo**:
  - Hidrocarbonetos predominantemente no **estado líquido**
  - Associado a querogénio Tipo I ou II
  - Forma-se em temperaturas moderadas (janela de óleo)

- **Reservatório de gás**:
  - Hidrocarbonetos no **estado gasoso**
  - Associado a querogénio Tipo III ou maturação avançada
  - Forma-se a temperaturas mais elevadas

- **Reservatório misto**:
  - Presença simultânea de fases líquida e gasosa
  - Resulta de diferentes estágios de maturação térmica
    """)

    st.info("💡 O estado dos hidrocarbonetos depende das condições de pressão, temperatura e maturação.")

    st.divider()

    st.markdown("**2. Rocha-mãe vs Rocha reservatório**")

    st.write("""
- **Rocha-mãe**:
  - Local onde os hidrocarbonetos são **gerados**
  - Rica em matéria orgânica (querogénio)

- **Rocha reservatório**:
  - Local onde os hidrocarbonetos são **armazenados**
  - Possui porosidade e permeabilidade
    """)

    st.info("💡 Gerar e armazenar são processos distintos no sistema petrolífero.")

    st.divider()

    st.markdown("**3. Porosidade vs Permeabilidade**")

    st.write("""
- **Porosidade**:
  - Quantidade de espaço vazio na rocha
  - Controla a capacidade de armazenamento

- **Permeabilidade**:
  - Capacidade de os fluidos circularem
  - Controla a produção
    """)

    st.info("💡 Uma rocha pode ter porosidade alta e baixa permeabilidade.")

    st.divider()

    st.markdown("**4. Tipo de querogénio**")

    st.write("""
- **Tipo I**:
  - Origem algal (ambiente lacustre)
  - Gera principalmente **óleo**

- **Tipo II**:
  - Origem marinha (plâncton)
  - Gera **óleo e gás**

- **Tipo III**:
  - Origem terrestre (plantas)
  - Gera principalmente **gás**
    """)

    st.info("💡 O tipo de matéria orgânica controla o tipo de hidrocarboneto gerado.")

    st.divider()

    st.markdown("**5. Maturação térmica vs Geração**")

    st.write("""
- **Maturação térmica**:
  - Processo de aumento de temperatura e pressão com o soterramento

- **Geração de hidrocarbonetos**:
  - Resultado da transformação do querogénio em óleo e/ou gás
    """)

    st.info("💡 A maturação controla quando e quanto hidrocarboneto é gerado.")

    st.divider()

    st.markdown("**6. Migração vs Acumulação**")

    st.write("""
- **Migração**:
  - Movimento dos hidrocarbonetos desde a rocha-mãe

- **Acumulação**:
  - Concentração dos hidrocarbonetos numa armadilha
    """)

    st.info("💡 Sem armadilha eficaz, os hidrocarbonetos perdem-se para a superfície.")

    st.divider()

    st.markdown("**7. Rocha selante vs Reservatório**")

    st.write("""
- **Rocha selante**:
  - Impermeável
  - Impede a fuga dos hidrocarbonetos

- **Rocha reservatório**:
  - Permeável
  - Permite armazenar e produzir fluidos
    """)

    st.info("💡 O contraste entre permeabilidade é essencial para o sistema funcionar.")

    st.divider()

    st.markdown("**8. Janela de óleo vs Janela de gás**")

    st.write("""
- **Janela de óleo**:
  - ~100 – 150 ºC
  - Geração predominante de óleo

- **Janela de gás**:
  - ~150 – 300 ºC
  - Geração predominante de gás
    """)

    st.info("💡 Temperaturas mais elevadas favorecem a formação de gás.")

# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_petroleo(deposito):

    st.markdown("### Quiz interativo")
    st.caption("Testa os teus conhecimentos")

    if "Reservatório de óleo" in deposito:

        if "corrigido_pet" not in st.session_state:
            st.session_state.corrigido_pet = False

        corretas = ["Líquido", "Tipo I", "100–150 ºC", "Arenito", "Selar hidrocarbonetos"]

        q1 = st.radio("1️⃣ Estado predominante dos hidrocarbonetos:",
                      ["Gasoso", "Líquido", "Sólido"], key="pet_q1", index=None)

        if st.session_state.corrigido_pet:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        q2 = st.radio("2️⃣ Tipo de querogénio típico:",
                      ["Tipo I", "Tipo II", "Tipo III"], key="pet_q2", index=None)

        if st.session_state.corrigido_pet:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        q3 = st.radio("3️⃣ Janela de geração de petróleo:",
                      ["50–80 ºC", "100–150 ºC", "200–300 ºC"], key="pet_q3", index=None)

        if st.session_state.corrigido_pet:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        q4 = st.radio("4️⃣ Rocha reservatório comum:",
                      ["Granito", "Arenito", "Basalto"], key="pet_q4", index=None)

        if st.session_state.corrigido_pet:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        q5 = st.radio("5️⃣ Função da rocha selante:",
                      ["Gerar petróleo", "Permitir fluxo", "Selar hidrocarbonetos"], key="pet_q5", index=None)

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

    elif "Reservatório de gás" in deposito:

        if "corrigido_gas" not in st.session_state:
            st.session_state.corrigido_gas = False

        corretas = ["Gasoso", "Tipo III", "150–300 ºC",
                    "Carvões e folhelhos carbonosos",
                    "Catagénese tardia e metagénese"]

        q1 = st.radio("1️⃣ Estado predominante dos hidrocarbonetos:",
                      ["Líquido", "Gasoso", "Sólido"], key="gas_q1", index=None)

        if st.session_state.corrigido_gas:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        q2 = st.radio("2️⃣ Tipo de querogénio típico:",
                      ["Tipo I", "Tipo II", "Tipo III"], key="gas_q2", index=None)

        if st.session_state.corrigido_gas:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        q3 = st.radio("3️⃣ Janela de gás:",
                      ["100–150 ºC", "150–300 ºC", "50–80 ºC"], key="gas_q3", index=None)

        if st.session_state.corrigido_gas:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        q4 = st.radio("4️⃣ Tipo de rocha-mãe mais associado ao gás:",
                      ["Argilitos lacustres", "Carvões e folhelhos carbonosos", "Calcários marinhos"], key="gas_q4", index=None)

        if st.session_state.corrigido_gas:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        q5 = st.radio("5️⃣ Fase principal de geração:",
                      ["Diagénese", "Catagénese tardia e metagénese", "Compactação"], key="gas_q5", index=None)

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

    elif "Reservatório misto (óleo + gás)" in deposito:

        if "corrigido_mix" not in st.session_state:
            st.session_state.corrigido_mix = False

        corretas = ["Líquida e gasosa", "Tipo II", "100–300 ºC",
                    "Argilitos negros", "Em múltiplos estágios"]

        q1 = st.radio("1️⃣ Fases presentes:",
                      ["Apenas líquida", "Apenas gasosa", "Líquida e gasosa"], key="mix_q1", index=None)

        if st.session_state.corrigido_mix:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        q2 = st.radio("2️⃣ Tipo de querogénio associado:",
                      ["Tipo I", "Tipo II", "Tipo III"], key="mix_q2", index=None)

        if st.session_state.corrigido_mix:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        q3 = st.radio("3️⃣ Intervalo térmico típico:",
                      ["100–150 ºC", "150–200 ºC", "100–300 ºC"], key="mix_q3", index=None)

        if st.session_state.corrigido_mix:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        q4 = st.radio("4️⃣ Tipo de rocha-mãe comum:",
                      ["Granito", "Argilitos negros", "Basalto"], key="mix_q4", index=None)

        if st.session_state.corrigido_mix:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        q5 = st.radio("5️⃣ Geração ocorre:",
                      ["Num único estágio", "Em múltiplos estágios", "Sem maturação"], key="mix_q5", index=None)

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

def checklist_petroleo():

    st.markdown("### Checklist de campo")

    st.write("Avaliação integrada de um sistema petrolífero:")

    st.markdown("**1. Rocha-mãe**")

    st.checkbox("Identificar rochas ricas em matéria orgânica (shales, margas, carvões)")
    st.checkbox("Avaliar Carbono Orgânico Total (COT > 2%)")
    st.checkbox("Determinar tipo de querogénio (Tipo I, II ou III)")
    st.checkbox("Inferir ambiente deposicional (lacustre, marinho ou continental)")
    st.checkbox("Avaliar potencial gerador de óleo e/ou gás")

    st.divider()

    st.markdown("**2. Maturação térmica**")

    st.checkbox("Avaliar temperatura (100–300 ºC)")
    st.checkbox("Medir refletância da vitrinite (0.6–4.0%)")
    st.checkbox("Identificar fase: diagénese, catagénese ou metagénese")
    st.checkbox("Confirmar geração de óleo, gás ou ambos")
    st.checkbox("Avaliar evolução térmica do sistema")

    st.divider()

    st.markdown("**3. Migração**")

    st.checkbox("Mapear falhas, fraturas e vias de migração")
    st.checkbox("Distinguir migração primária e secundária")
    st.checkbox("Avaliar permeabilidade das formações")
    st.checkbox("Identificar evidências de migração (óleo ou gás)")
    st.checkbox("Reconhecer possíveis perdas (migração terciária)")

    st.divider()

    st.markdown("**4. Rocha reservatório**")

    st.checkbox("Identificar rochas porosas (arenitos, calcários, dolomitos)")
    st.checkbox("Avaliar porosidade")
    st.checkbox("Avaliar permeabilidade")
    st.checkbox("Confirmar presença de hidrocarbonetos (óleo e/ou gás)")
    st.checkbox("Analisar distribuição de fases (gás no topo, óleo abaixo)")

    st.divider()

    st.markdown("**5. Rocha selante**")

    st.checkbox("Identificar rochas impermeáveis (shales, evaporitos)")
    st.checkbox("Verificar continuidade lateral do selante")
    st.checkbox("Avaliar integridade (ausência de fraturas abertas)")
    st.checkbox("Confirmar capacidade de retenção de hidrocarbonetos")
    st.checkbox("Avaliar risco de fuga (especialmente gás)")

    st.divider()

    st.markdown("**6. Armadilha**")

    st.checkbox("Identificar armadilhas estruturais (anticlinais, falhas, domos de sal)")
    st.checkbox("Identificar armadilhas estratigráficas (pinch-outs, discordâncias)")
    st.checkbox("Confirmar geometria favorável à acumulação")
    st.checkbox("Verificar relação reservatório–selante")
    st.checkbox("Avaliar segregação de fases (óleo e gás)")

    st.divider()

    st.markdown("**7. Indicadores complementares**")

    st.checkbox("Presença de exsudações (óleo ou gás)")
    st.checkbox("Anomalias geoquímicas no solo")
    st.checkbox("Dados sísmicos favoráveis")
    st.checkbox("Presença de gases associados (CH₄, etc.)")

    st.success("💡 Um sistema viável requer: geração + migração + reservatório + selante + armadilha.")

# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_petroleo():

    st.markdown("### 🌍 Mapa global de ocorrências de petróleo e gás")

    with open("occurrences_oil_gas.html", "r", encoding="utf-8") as f:
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

def referencias_petroleo():

    st.markdown("### 📚 Referências bibliográficas")

    st.write(
    "- Magoon, L. B., & Dow, W. G. (1994). The petroleum system: "
    "From source to trap. American Association of Petroleum Geologists."
    )
    
    st.write(
    "- Gluyas, J., & Swarbrick, R. (2004). Petroleum geoscience. "
    "Blackwell Publishing."
    )
    
    st.write(
    "- Gomes, J. S., & Alves, F. B. (2014). O universo da indústria petrolífera: "
    "Da pesquisa à refinação (3ª ed.). Fundação Calouste Gulbenkian."
    )
    
    st.caption("Referências utilizadas.")
    