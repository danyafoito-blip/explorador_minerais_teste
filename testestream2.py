
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

# --- SEPARADOR 3: QUIZ ---
with tab_quiz:
    st.markdown("### Teste os seus conhecimentos")
    
    # Verifica se a matéria-prima selecionada são os Sulfuretos (SMS)
    if recurso_selecionado == "Sulfuretos maciços do fundo oceânico (SMS)":
        
        st.write("Responda às seguintes questões sobre a formação e exploração de depósitos SMS:")
        
        q1 = st.radio(
            "**1. Qual é o principal mecanismo que faz com que os metais precipitem e formem as chaminés de SMS no fundo do mar?**",
            [
                "A) O arrefecimento lento do magma em profundidade.",
                "B) O choque térmico e químico entre o fluido hidrotermal a ~350°C e a água do mar a ~2°C.",
                "C) A compactação dos sedimentos marinhos devido ao peso da coluna de água.",
                "D) A oxidação das rochas basálticas pela luz solar."
            ],
            index=None
        )

        q2 = st.radio(
            "**2. Se fores avaliar a viabilidade de uma exploração mineira de um depósito análogo em terra (VMS), que diferença física fundamental esperas encontrar em relação a um SMS fresco do fundo do mar?**",
            [
                "A) O depósito em terra será muito mais poroso e leve.",
                "B) O depósito em terra não terá sulfuretos, apenas óxidos.",
                "C) O depósito em terra será muito mais denso, compacto e menos friável devido à compressão tectónica.",
                "D) Não haverá diferença, a rocha mantém-se intacta para sempre."
            ],
            index=None
        )

        q3 = st.radio(
            "**3. Quais são os dois metais base mais rentáveis e abundantes extraídos deste tipo de sulfuretos (tanto SMS como VMS)?**",
            [
                "A) Alumínio e Níquel.",
                "B) Ferro e Manganês.",
                "C) Cobre e Zinco.",
                "D) Lítio e Cobalto."
            ],
            index=None
        )

        q4 = st.radio(
            "**4. O que acontece à rocha por baixo do depósito maciço (a chamada zona de stockwork ou condutas) devido à passagem contínua dos fluidos quentes?**",
            [
                "A) Fica mais dura e resistente que o basalto original.",
                "B) Sofre alteração hidrotermal, tornando-se uma zona fraturada e frequentemente argilizada, com implicações na estabilidade mecânica.",
                "C) Transforma-se em calcário puro.",
                "D) Derrete completamente, formando um lago de lava subterrâneo."
            ],
            index=None
        )

        st.write("") # Espaço em branco
        
        if st.button("Submeter Respostas"):
            # Variável para contar a pontuação
            pontuacao = 0
            
            # Verificação da Q1
            if q1 and q1.startswith("B)"):
                st.success("1. Correto!")
                pontuacao += 1
            elif q1:
                st.error("1. Incorreto. A resposta certa era a B.")
                
            # Verificação da Q2
            if q2 and q2.startswith("C)"):
                st.success("2. Correto!")
                pontuacao += 1
            elif q2:
                st.error("2. Incorreto. A resposta certa era a C.")
                
            # Verificação da Q3
            if q3 and q3.startswith("C)"):
                st.success("3. Correto!")
                pontuacao += 1
            elif q3:
                st.error("3. Incorreto. A resposta certa era a C.")
                
            # Verificação da Q4
            if q4 and q4.startswith("B)"):
                st.success("4. Correto!")
                pontuacao += 1
            elif q4:
                st.error("4. Incorreto. A resposta certa era a B.")
                
            # Resultado Final
            st.divider()
            if pontuacao == 4:
                st.balloons() # Lança balões no ecrã!
                st.success(f"🎉 Brilhante! Acertou {pontuacao} em 4 questões!")
            elif q1 and q2 and q3 and q4:
                st.info(f"Acertou {pontuacao} em 4. Reveja as opções incorretas e tente novamente!")
            else:
                st.warning("⚠️ Responda a todas as perguntas para ver o seu resultado final.")
                
    else:
        # Mensagem que aparece se não for selecionado os Sulfuretos
        st.info(f"🧠 O quiz específico para **{recurso_selecionado}** ainda está em desenvolvimento. Selecione **Sulfuretos maciços do fundo oceânico (SMS)** na barra lateral para testar um quiz completo.")

with tab_check:
    st.markdown("### Checklist de Identificação em Campo")
    st.checkbox("Verificar a cor e o traço")
    st.checkbox("Testar a dureza com canivete/vidro")
    st.checkbox("Observar o tipo de fratura/clivagem")
    st.checkbox("Testar reação com HCl")

# --- NOVO MAPA COM PLOTLY (GLOBO 3D) ---
with tab_mapa:
    st.markdown("### Principais Reservas e Produtores Globais")
    
    if recurso_selecionado == "Quartzo":
        st.write("🌍 **Dica:** Clique e arraste o globo para o rodar. Os principais 5 produtores de Quartzo estão destacados a vermelho.")
        
        # Tabela com os códigos ISO-3 dos países
        dados_quartzo = pd.DataFrame({
            "País": ["Brasil", "Estados Unidos", "China", "Rússia", "Madagáscar"],
            "Código_ISO": ["BRA", "USA", "CHN", "RUS", "MDG"],
            "Status": ["Produtor", "Produtor", "Produtor", "Produtor", "Produtor"]
        })
        
        # Criar o mapa coroplético em 3D
        figura_mapa = px.choropleth(
            dados_quartzo,
            locations="Código_ISO",
            color="Status", 
            hover_name="País", 
            color_discrete_map={"Produtor": "#FF4B4B"}, 
            projection="orthographic"  
        )
        
        # Ajustes visuais para tornar o globo mais realista
        figura_mapa.update_layout(
            showlegend=False, 
            margin={"r":0,"t":0,"l":0,"b":0},
            geo=dict(
                showcoastlines=True, 
                coastlinecolor="Black", 
                showland=True, 
                landcolor="lightgrey",
                showocean=True,         # Ativa os oceanos
                oceancolor="#7990db",   # Azul muito suave para a água ("Alice Blue")
                showframe=False         # Remove a moldura quadrada à volta do globo
            )
        )
        
        # Mostrar o mapa no Streamlit
        st.plotly_chart(figura_mapa, use_container_width=True)
        
    else:
        st.info(f"📍 Pedimos desculpa, como estamos ainda em fase de teste, os dados geográficos para **{recurso_selecionado}** ainda estão a ser compilados. Por favor, selecione **Quartzo** na barra lateral para ver um exemplo do globo.")

with tab_ref:
    st.markdown("### Fontes e Bibliografia")
    st.markdown("""
    Abaixo encontram-se as fontes consultadas para a elaboração deste guia:
    * **Web:**
        * [Mindat.org](https://www.mindat.org) - Base de dados mineralógica.
    """)
    st.divider()
    st.caption("Organizado por: Grupo Quartzo (SB, GM, CP, DA)")





