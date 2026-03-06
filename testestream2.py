
import streamlit as st

# --- 1. Configurações da Página ---
st.set_page_config(
    page_title="Explorador de Recursos Energéticos", 
    layout="wide", 
    page_icon="💎" 
)

# --- 2. Base de Dados ---
materias_primas = [
    "Hidrogénio (Geração natural e armazenamento)",
    "Petróleo e Gás (Sistemas convencionais)",
    "Metano (Hidratos e recursos não convencionais)",
    "Lítio (Rocha dura versus salmouras)",
    "Urânio e Tório (Combustíveis nucleares)",
    "Sulfuretos maciços do fundo oceânico (SMS)",
    "Quartzo",
    "Monazite",
    "Ortoclase"
]

# --- 3. BARRA LATERAL (Sidebar) ---
with st.sidebar:
    try:
        # Imagem do topo
        nome_imagem = "ChatGPT Image 2_03_2026, 13_53_00.png"
        st.image(nome_imagem)
    except Exception:
        st.write("*(Espaço para o Logótipo)*")
    
    st.markdown("### ⚙️ Painel de Controlo")
    st.divider()
    
    # Agora apenas selecionamos a matéria-prima
    recurso_selecionado = st.selectbox("Selecione a Matéria-Prima:", materias_primas)
    
    st.divider()
    st.info("💡 **Dica:** Utilize os separadores no ecrã principal para navegar pela informação.")

# --- 4. ECRÃ PRINCIPAL ---
st.markdown(f"## 🔎 Análise: {recurso_selecionado}")
st.write("") # Pequeno espaço

# --- SEPARADORES (Tabs) ---
tab_caract, tab_confusoes, tab_quiz, tab_check, tab_ref = st.tabs([
    "📊 Características", 
    "⚠️ Confusões Comuns", 
    "🧠 Quiz Interativo", 
    "✅ Checklist de Campo",
    "📚 Referências"
])

# --- CONTEÚDO DOS SEPARADORES ---

with tab_caract:
    st.markdown("### Propriedades Principais")
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Propriedades Físicas**")
        st.write("- Dureza (Escala de Mohs): *A definir*")
        st.write("- Brilho: *A definir*")
        st.write("- Clivagem / Fratura: *A definir*")
    with col2:
        st.info("**Aplicações Industriais**")
        st.write("- Uso 1")
        st.write("- Uso 2")
        st.write("- Uso 3")

with tab_confusoes:
    st.markdown("### Minerais Semelhantes (Falsos Amigos)")
    st.warning("Diferenças cruciais para identificação em campo:")
    with st.expander("Ver detalhes de comparação"):
        st.write("Conteúdo comparativo entre minerais semelhantes.")

with tab_quiz:
    st.markdown("### Teste os seus conhecimentos")
    pergunta = st.radio(
        f"Qual é a principal característica de identificação de {recurso_selecionado.split(' ')[0]}?",
        ["Opção A", "Opção B", "Opção C", "Opção D"],
        index=None
    )
    if st.button("Submeter Resposta"):
        if pergunta == "Opção B":
            st.success("Correto!")
        elif pergunta is not None:
            st.error("Incorreto.")
        else:
            st.warning("Selecione uma opção.")

with tab_check:
    st.markdown("### Checklist de Identificação em Campo")
    st.checkbox("Verificar a cor e o traço")
    st.checkbox("Testar a dureza com canivete/vidro")
    st.checkbox("Observar o tipo de fratura/clivagem")
    st.checkbox("Testar reação com HCl")

with tab_ref:
    st.markdown("### Fontes e Bibliografia")
    st.markdown("""
    Abaixo encontram-se as fontes consultadas para a elaboração deste guia:
    
    * **Livros:** * *Manual de Mineralogia*, Dana & Hurlbut.
        * *Introduction to Ore-Forming Processes*, Laurence Robb.
    * **Web:**
        * [Mindat.org](https://www.mindat.org) - Base de dados mineralógica.
        * [Webmineral](http://webmineral.com) - Mineralogy Database.
    * **Artigos Científicos:**
        * Referências específicas sobre exploração de *{recurso_selecionado}*.
    """)
    
    st.divider()
    st.caption("Organizado por: Grupo Quartzo (SB, GM, CP, DA)")

