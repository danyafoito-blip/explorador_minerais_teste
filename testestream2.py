
import streamlit as st

# --- 1. Configurações da Página (Tem de ser a primeira linha!) ---
st.set_page_config(
    page_title="Explorador de Recursos Energéticos", 
    layout="wide", # Usa o ecrã todo
    page_icon="💎" # Ícone no separador do navegador
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

tipos_deposito = [
    "Depósitos de Origem Magmática",
    "Depósitos Hidrotermais",
    "Depósitos Sedimentares",
    "Depósitos Metamórficos"
]

# --- 3. BARRA LATERAL (Sidebar) ---
with st.sidebar:
    # Agora a imagem é carregada diretamente da pasta do GitHub
    try:
        # Usa apenas o nome do ficheiro que subiste para o GitHub
        nome_imagem = "ChatGPT Image 2_03_2026, 13_53_00.png" 
        st.image(nome_imagem)
    except Exception:
        st.write("*(Logótipo não carregado)*")
    st.markdown("### ⚙️ Painel de Controlo")
    st.divider()
    
    recurso_selecionado = st.selectbox("Selecione a Matéria-Prima:", materias_primas)
    deposito_selecionado = st.selectbox("Selecione o Tipo de Depósito:", tipos_deposito)
    
    st.divider()
    st.info("💡 **Dica:** Utilize os separadores no ecrã principal para navegar pela informação do mineral selecionado.")

# --- 4. ECRÃ PRINCIPAL ---
st.markdown(f"## 🔎 Análise: {recurso_selecionado}")
st.markdown(f"**Contexto Geológico:** {deposito_selecionado}")
st.write("") # Pequeno espaço

# Criar os separadores (Tabs)
tab_caract, tab_confusoes, tab_quiz, tab_check = st.tabs([
    "📊 Características", 
    "⚠️ Confusões Comuns", 
    "🧠 Quiz Interativo", 
    "✅ Checklist de Campo"
])

# --- CONTEÚDO DOS SEPARADORES ---

# Separador 1: Características
with tab_caract:
    st.markdown("### Propriedades Principais")
    # Usar colunas dentro do separador para organizar a informação
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

# Separador 2: Confusões
with tab_confusoes:
    st.markdown("### Minerais Semelhantes (Falsos Amigos)")
    st.warning("É comum confundir este recurso com outras amostras no trabalho de campo. Veja as diferenças abaixo:")
    
    # O expander cria uma "gaveta" que o utilizador pode abrir e fechar
    with st.expander("Mineral Parecido 1 vs Mineral Parecido 2"):
        st.write("A principal diferença para distinguir estes dois a olho nu é o traço deixado na placa de porcelana e a reação a ácidos fracos.")

# Separador 3: Quiz
with tab_quiz:
    st.markdown("### Teste os seus conhecimentos")
    pergunta = st.radio(
        f"Qual é a principal característica de identificação de {recurso_selecionado.split(' ')[0]}?",
        ["Opção A", "Opção B", "Opção C", "Opção D"],
        index=None # Não seleciona nenhuma por defeito
    )
    
    if st.button("Submeter Resposta"):
        if pergunta == "Opção B":
            st.success("Correto! Muito bem.")
        elif pergunta != None:
            st.error("Incorreto. Tente novamente!")
        else:
            st.warning("Selecione uma opção primeiro.")

# Separador 4: Checklist
with tab_check:
    st.markdown("### Checklist de Identificação em Campo")
    st.checkbox("Verificar a cor e o traço")
    st.checkbox("Testar a dureza com canivete/vidro")
    st.checkbox("Observar o tipo de fratura/clivagem")
    st.checkbox("Testar reação com ácido clorídrico (HCl)")


