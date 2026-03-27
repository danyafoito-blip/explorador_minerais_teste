# ===============================
# BIBLIOTECAS EXTERNAS
# ===============================

import streamlit as st
import streamlit.components.v1 as components


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_metano(deposito):

    st.markdown("### 🔥 Características do Metano")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- Fórmula química: CH₄")
        st.write("- Gás incolor e inodoro")
        st.write("- Baixa densidade")
        st.write("- Alta inflamabilidade")
        st.write("- Principal componente do gás natural")

    with col2:

        st.info("**Importância Energética**")

        st.write("- Fonte energética global relevante")
        st.write("- Menor emissão de CO₂ que carvão e petróleo")
        st.write("- Utilizado em geração elétrica")
        st.write("- Base para produção de hidrogénio (SMR)")

    st.divider()

    if "Biogénico" in deposito:

        st.markdown("### 🧊 Hidratos de Metano")

        st.write("**Características principais:**")
        st.write("- Estruturas cristalinas (clatratos)")
        st.write("- Metano aprisionado em gelo")
        st.write("- Estáveis a alta pressão e baixa temperatura")
        st.write("- Encontrados em sedimentos marinhos e permafrost")

        st.write("**Ambientes típicos:**")
        st.write("- Margens continentais")
        st.write("- Taludes oceânicos")
        st.write("- Regiões árticas")

    elif "Termogénico" in deposito:

        st.markdown("### ⚙️ Recursos Não Convencionais de Metano")

        st.write("**Tipos principais:**")
        st.write("- Shale gas")
        st.write("- Coalbed methane (CBM)")
        st.write("- Tight gas")

        st.write("**Características principais:**")
        st.write("- Baixa permeabilidade")
        st.write("- Necessidade de fraturação hidráulica")
        st.write("- Produção tecnicamente exigente")

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_metano():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("Existem várias confusões frequentes no estudo do metano.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. Metano vs Gás Natural**")
        st.write("- Metano: composto específico (CH₄)")
        st.write("- Gás natural: mistura (metano dominante)")

        st.markdown("**2. Hidratos vs Gelo Comum**")
        st.write("- Hidratos: estrutura cristalina com gás")
        st.write("- Gelo: apenas H₂O")

        st.markdown("**3. Convencional vs Não Convencional**")
        st.write("- Convencional: fácil extração")
        st.write("- Não convencional: requer tecnologia avançada")

        st.markdown("**4. Metano Biogénico vs Termogénico**")
        st.write("- Biogénico: origem microbiana")
        st.write("- Termogénico: origem térmica profunda")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_metano(deposito):

    st.markdown("### 🧠 Quiz Interativo: Metano")
    st.write("Testa os teus conhecimentos 👇")

    # ---------------------- BIOGÉNICO ----------------------
    if "Biogénico" in deposito:

        st.markdown("#### Quiz: Metano Biogénico")

        if "corrigido_bio" not in st.session_state:
            st.session_state.corrigido_bio = False

        corretas = [
            "Atividade microbiana",
            "Ambientes rasos e anaeróbios",
            "Baixa temperatura",
            "CH₄",
            "Sedimentos marinhos e pântanos"
        ]

        q1 = st.radio("1️⃣ Origem do metano biogénico:",
                      ["Atividade microbiana", "Alta temperatura", "Processos magmáticos"],
                      key="bio_q1", index=None)

        if st.session_state.corrigido_bio:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        q2 = st.radio("2️⃣ Ambiente típico:",
                      ["Ambientes rasos e anaeróbios", "Ambientes profundos e quentes", "Crosta oceânica"],
                      key="bio_q2", index=None)

        if st.session_state.corrigido_bio:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        q3 = st.radio("3️⃣ Condições de formação:",
                      ["Alta temperatura", "Baixa temperatura", "Sem água"],
                      key="bio_q3", index=None)

        if st.session_state.corrigido_bio:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        q4 = st.radio("4️⃣ Principal gás produzido:",
                      ["CO₂", "CH₄", "H₂"],
                      key="bio_q4", index=None)

        if st.session_state.corrigido_bio:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        q5 = st.radio("5️⃣ Local comum de ocorrência:",
                      ["Sedimentos marinhos e pântanos", "Granitos profundos", "Basaltos"],
                      key="bio_q5", index=None)

        if st.session_state.corrigido_bio:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")

        if st.button("Corrigir Quiz Biogénico"):
            st.session_state.corrigido_bio = True

        if st.session_state.corrigido_bio:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    # ---------------------- TERMOGÉNICO ----------------------
    elif "Termogénico" in deposito:

        st.markdown("#### Quiz: Metano Termogénico")

        if "corrigido_termo" not in st.session_state:
            st.session_state.corrigido_termo = False

        corretas = [
            "Maturação térmica da matéria orgânica",
            "Alta temperatura e pressão",
            "Profundidade elevada",
            "CH₄",
            "Catagénese"
        ]

        q1 = st.radio("1️⃣ Origem do metano termogénico:",
                      ["Atividade microbiana", "Maturação térmica da matéria orgânica", "Processos superficiais"],
                      key="termo_q1", index=None)

        if st.session_state.corrigido_termo:
            if q1 == corretas[0]:
                st.success("Correto ✅")
            elif q1 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[0]}**")

        q2 = st.radio("2️⃣ Condições típicas:",
                      ["Baixa temperatura", "Alta temperatura e pressão", "Ambiente superficial"],
                      key="termo_q2", index=None)

        if st.session_state.corrigido_termo:
            if q2 == corretas[1]:
                st.success("Correto ✅")
            elif q2 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[1]}**")

        q3 = st.radio("3️⃣ Ambiente de formação:",
                      ["Superficial", "Profundidade elevada", "Atmosfera"],
                      key="termo_q3", index=None)

        if st.session_state.corrigido_termo:
            if q3 == corretas[2]:
                st.success("Correto ✅")
            elif q3 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[2]}**")

        q4 = st.radio("4️⃣ Principal gás produzido:",
                      ["CO₂", "CH₄", "H₂"],
                      key="termo_q4", index=None)

        if st.session_state.corrigido_termo:
            if q4 == corretas[3]:
                st.success("Correto ✅")
            elif q4 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[3]}**")

        q5 = st.radio("5️⃣ Fase geológica associada:",
                      ["Diagénese", "Catagénese", "Sedimentação"],
                      key="termo_q5", index=None)

        if st.session_state.corrigido_termo:
            if q5 == corretas[4]:
                st.success("Correto ✅")
            elif q5 is not None:
                st.error(f"Errado ❌ → Resposta correta: **{corretas[4]}**")

        if st.button("Corrigir Quiz Termogénico"):
            st.session_state.corrigido_termo = True

        if st.session_state.corrigido_termo:
            respostas = [q1, q2, q3, q4, q5]
            score = sum([r == c for r, c in zip(respostas, corretas)])
            st.markdown(f"### 🎯 Pontuação: {score}/5")

    else:
        st.info("Selecione um tipo de metano válido.")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_metano():

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado na prospeção de metano:")

    st.checkbox("Identificar bacias sedimentares")
    st.checkbox("Avaliar matéria orgânica")
    st.checkbox("Determinar maturação térmica")
    st.checkbox("Mapear estruturas geológicas")
    st.checkbox("Analisar dados sísmicos")
    st.checkbox("Medir emissões de gás")
    st.checkbox("Avaliar pressão e temperatura")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_metano():

    st.markdown("### 🌍 Mapa Global de Ocorrências de Metano")

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

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- Kvenvolden – Gas Hydrates: Geological Perspective")
    st.write("- USGS – Methane Hydrates Research")
    st.write("- IPCC Reports – Methane Emissions")
    st.write("- Sloan – Clathrate Hydrates of Natural Gases")
    st.write("- AAPG – Unconventional Gas Resources")

    st.caption("Fontes científicas relevantes para metano e hidratos.")