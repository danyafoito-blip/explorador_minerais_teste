# ===============================
# BIBLIOTECAS EXTERNAS
# ===============================

import streamlit as st
import streamlit.components.v1 as components


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_petroleo(deposito):

    st.markdown("### Características do Petróleo e Gás")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- Mistura complexa de hidrocarbonetos")
        st.write("- Densidade variável (API gravity)")
        st.write("- Viscosidade variável")
        st.write("- Presença de gás associado (CH₄ dominante)")
        st.write("- Composição controlada por maturação térmica")

    with col2:

        st.info("**Importância Energética**")

        st.write("- Principal fonte global de energia")
        st.write("- Produção de combustíveis (gasolina, diesel)")
        st.write("- Matéria-prima petroquímica")
        st.write("- Base da economia energética global")

    st.divider()

    if "Reservatório de óleo" in deposito:

        st.markdown("## Reservatório de Petróleo")
    
        st.success(
            "Um reservatório de petróleo é um reservatório em que a mistura de hidrocarbonetos "
            "se encontra predominantemente no estado líquido, nas condições de pressão e temperatura do reservatório."
        )
    
        st.divider()
    
        st.markdown("## Rocha-mãe")
    
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
                st.write("- Shales lacustres")
                st.write("- Margas calcárias")
    
        st.markdown("### Tipo de Querogénio")
    
        st.success(
            "Tipo I (Liptinito): origem algal (ambientes lacustres/lagunares), principal responsável pela geração de petróleo."
        )
    
        st.divider()
    
        st.markdown("## Geração (Maturação Térmica)")
    
        st.warning(
            "A maturação térmica ocorre com o soterramento (overburden), aumentando pressão e temperatura."
        )
    
        col1, col2 = st.columns(2)
    
        with col1:
            st.metric("Temperatura (janela de petróleo)", "100 – 150 ºC")
    
        with col2:
            st.metric("Refletância da vitrinite", "0.6 – 1.3 %")
    
        st.write("Fase principal: catagénese")
    
        st.divider()
    
        st.markdown("## Migração")
    
        st.info(
            "Processo de deslocação dos hidrocarbonetos desde a rocha-mãe até ao reservatório ou à superfície."
        )
    
        st.markdown("**Tipos de migração:**")
        st.write("- Primária → expulsão da rocha-mãe")
        st.write("- Secundária → movimento em rochas permeáveis")
        st.write("- Terciária → fuga para a superfície")
    
        st.divider()
    
        st.markdown("## Rocha Reservatório")
    
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
    
        st.markdown("## Rocha Selante")
    
        st.error(
            "Camada impermeável que impede a migração dos hidrocarbonetos, garantindo a sua acumulação."
        )
    
        st.write("**Principais tipos:**")
        st.write("- Folhelhos (shales)")
        st.write("- Evaporitos (sal e anidrita)")
    
        st.divider()
    
        st.markdown("## Armadilhas Geológicas")
    
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

    elif "Reservatórios de gás" in deposito:

        st.markdown("### Reservatórios de gás")
    
        st.success(
            "Um reservatório de gás é um reservatório em que a mistura de hidrocarbonetos "
            "se encontra predominantemente no estado gasoso, nas condições de pressão e temperatura do reservatório."
        )
    
        st.divider()
    
        st.markdown("## Rocha-mãe")
    
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
                st.write("- Folhelhos carbonosos")
                st.write("- Siltitos ricos em matéria vegetal")
    
        st.markdown("### Tipo de Querogénio")
    
        st.success(
            "Tipo III (Vitrinito): derivado de detritos de plantas terrestres superiores e lenhosas, principal responsável pela geração de gás."
        )
    
        st.divider()
    
        st.markdown("## Geração (Maturação Térmica)")
    
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
    
        st.markdown("## Migração")
    
        st.info(
            "Processo de deslocação dos hidrocarbonetos desde a rocha-mãe até ao reservatório ou à superfície."
        )
    
        st.markdown("**Tipos de migração:**")
        st.write("- Primária → expulsão da rocha-mãe")
        st.write("- Secundária → movimento em rochas permeáveis")
        st.write("- Terciária → fuga para a superfície")
    
        st.divider()
    
        st.markdown("## Rocha Reservatório")
    
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
    
        st.markdown("## Rocha Selante")
    
        st.error(
            "Camada impermeável que impede a migração dos hidrocarbonetos, garantindo a sua acumulação."
        )
    
        st.write("**Principais tipos:**")
        st.write("- Folhelhos (shales)")
        st.write("- Evaporitos (sal e anidrita)")
    
        st.divider()
    
        st.markdown("## Armadilhas Geológicas")
    
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

    elif "Reservatórios de petróleo e gás" in deposito:

        st.markdown("### Reservatórios de petróleo e gás")
    
        st.success(
            "Um reservatório de petróleo e gás contém hidrocarbonetos nas fases líquida e gasosa, "
            "em quantidades significativas, nas condições de pressão e temperatura do reservatório."
        )
        
        st.divider()
    
        st.markdown("## Rocha-mãe")
    
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
                st.write("- Folhelhos marinhos (black shales)")
                st.write("- Calcários betuminosos")
                st.write("- Margas")
    
        st.markdown("### Tipo de Querogénio")
    
        st.success(
            "Tipo II (Exinito): derivado de plâncton marinho e bactérias, associado à geração de petróleo e gás."
        )
    
        st.divider()
    
        st.markdown("## Geração (Maturação Térmica)")
    
        st.warning(
            "A maturação térmica ocorre com o soterramento (overburden), aumentando pressão e temperatura."
        )
        
        st.info(
            "A geração de petróleo e gás ocorre frequentemente quando a rocha-mãe atravessa diferentes estágios de maturação, de forma simultânea ou sucessiva."
        )
    
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Temperatura (janela petróleo + gás)", "100 – 300 ºC")
        
        with col2:
            st.metric("Refletância da vitrinite", "0.6 – 4.0 %")
        
        st.write("Fases principais: catagénese, catagénese tardia e metagénese")

        st.divider()
    
        st.markdown("## Migração")
    
        st.info(
            "Processo de deslocação dos hidrocarbonetos desde a rocha-mãe até ao reservatório ou à superfície."
        )
    
        st.markdown("**Tipos de migração:**")
        st.write("- Primária → expulsão da rocha-mãe")
        st.write("- Secundária → movimento em rochas permeáveis")
        st.write("- Terciária → fuga para a superfície")
    
        st.divider()
    
        st.markdown("## Rocha Reservatório")
    
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
    
        st.markdown("## Rocha Selante")
    
        st.error(
            "Camada impermeável que impede a migração dos hidrocarbonetos, garantindo a sua acumulação."
        )
    
        st.write("**Principais tipos:**")
        st.write("- Folhelhos (shales)")
        st.write("- Evaporitos (sal e anidrita)")
    
        st.divider()
    
        st.markdown("## Armadilhas Geológicas")
    
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

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("Conceitos errados são frequentes na geologia do petróleo.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. Petróleo vs Gás Natural**")
        st.write("- Petróleo: líquido")
        st.write("- Gás: fase gasosa (principalmente metano)")

        st.markdown("**2. Rocha reservatório vs Rocha-mãe**")
        st.write("- Rocha-mãe: onde se forma o hidrocarboneto")
        st.write("- Rocha reservatório: onde ele se acumula")

        st.markdown("**3. Porosidade vs Permeabilidade**")
        st.write("- Porosidade: espaço disponível")
        st.write("- Permeabilidade: capacidade de fluxo")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_petroleo(deposito):

    st.markdown("### 🧠 Quiz Interativo: Petróleo e Gás")
    st.write("Testa os teus conhecimentos 👇")

    if "Reservatório de petróleo" in deposito:

        st.markdown("#### Quiz: Reservatório de óleo")

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

        if st.button("Corrigir Quiz Petróleo"):
            st.session_state.corrigido_pet = True

        if st.session_state.corrigido_pet:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    elif "Reservatórios de gás" in deposito:

        st.markdown("#### Quiz: Reservatório de Gás")

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
                      ["Shales lacustres", "Carvões e folhelhos carbonosos", "Calcários marinhos"], key="gas_q4", index=None)

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

        if st.button("Corrigir Quiz Gás"):
            st.session_state.corrigido_gas = True

        if st.session_state.corrigido_gas:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    elif "Reservatórios misto (óleo + gás)" in deposito:

        st.markdown("#### Quiz: Petróleo e Gás")

        if "corrigido_mix" not in st.session_state:
            st.session_state.corrigido_mix = False

        corretas = ["Líquida e gasosa", "Tipo II", "100–300 ºC",
                    "Folhelhos marinhos", "Em múltiplos estágios"]

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
                      ["Granito", "Folhelhos marinhos", "Basalto"], key="mix_q4", index=None)

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

        if st.button("Corrigir Quiz Petróleo + Gás"):
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

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado na prospeção de petróleo e gás:")

    st.checkbox("Identificar rochas geradoras")
    st.checkbox("Avaliar maturação térmica")
    st.checkbox("Mapear estruturas (anticlinais, falhas)")
    st.checkbox("Avaliar porosidade e permeabilidade")
    st.checkbox("Identificar rocha selante")
    st.checkbox("Verificar presença de hidrocarbonetos")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_petroleo():

    st.markdown("### 🌍 Mapa Global de Ocorrências de Petróleo e Gás")

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

    st.markdown("### 📚 Referências e Bibliografia")

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
    
