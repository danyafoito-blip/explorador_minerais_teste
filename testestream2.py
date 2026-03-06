
import streamlit as st
import pandas as pd
import plotly.express as px # --- NOVA BIBLIOTECA PARA MAPAS AVANÇADOS ---

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
        nome_imagem = "ChatGPT Image 2_03_2026, 13_53_00.png"
        st.image(nome_imagem)
    except Exception:
        st.write("*(Espaço para o Logótipo)*")
    
    st.markdown("### ⚙️ Painel de Controlo")
    st.divider()
    
    recurso_selecionado = st.selectbox("Selecione a Matéria-Prima:", materias_primas)
    
    st.divider()
    st.info("💡 **Dica:** Utilize os separadores no ecrã principal para navegar pela informação.")

# --- 4. ECRÃ PRINCIPAL ---
st.markdown(f"## 🔎 Análise: {recurso_selecionado}")
st.write("") 

# --- SEPARADORES (Tabs) ---
tab_caract, tab_confusoes, tab_quiz, tab_check, tab_mapa, tab_ref = st.tabs([
    "📊 Características", 
    "⚠️ Confusões Comuns", 
    "🧠 Quiz Interativo", 
    "✅ Checklist de Campo",
    "🗺️ Mapa Global",
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

# --- NOVO MAPA COM PLOTLY ---
with tab_mapa:
    st.markdown("### Principais Reservas e Produtores Globais")
    
    if recurso_selecionado == "Quartzo":
        st.write("Países com maiores extrações/reservas de Quartzo de alta pureza destacados a vermelho.")
        
        # Tabela com os códigos ISO-3 dos países para o Plotly os reconhecer
        dados_quartzo = pd.DataFrame({
            "País": ["Brasil", "Estados Unidos", "China", "Rússia", "Madagáscar"],
            "Código_ISO": ["BRA", "USA", "CHN", "RUS", "MDG"],
            "Status": ["Produtor", "Produtor", "Produtor", "Produtor", "Produtor"]
        })
        
        # Criar o mapa coroplético
        figura_mapa = px.choropleth(
            dados_quartzo,
            locations="Código_ISO",
            color="Status", # Pinta baseado nesta coluna
            hover_name="País", # Mostra o nome ao passar o rato
            color_discrete_map={"Produtor": "#FF4B4B"}, # Define o vermelho vivo do Streamlit
            projection="natural earth" # Mapa ligeiramente curvo (mais bonito que o plano)
        )
        
        # Pequenos ajustes visuais (esconder a legenda e tirar margens desnecessárias)
        figura_mapa.update_layout(
            showlegend=False, 
            margin={"r":0,"t":0,"l":0,"b":0},
            geo=dict(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="lightgrey")
        )
        
        # Dizer ao Streamlit para mostrar o gráfico interativo
        st.plotly_chart(figura_mapa, use_container_width=True)
        
    else:
        st.info(f"📍 Os dados geográficos para **{recurso_selecionado}** ainda estão a ser compilados. Por favor, selecione **Quartzo** na barra lateral para ver um exemplo do mapa.")

with tab_ref:
    st.markdown("### Fontes e Bibliografia")
    st.markdown("""
    Abaixo encontram-se as fontes consultadas para a elaboração deste guia:
    * **Web:**
        * [Mindat.org](https://www.mindat.org) - Base de dados mineralógica.
    """)
    st.divider()
    st.caption("Organizado por: Grupo Quartzo (SB, GM, CP, DA)")
