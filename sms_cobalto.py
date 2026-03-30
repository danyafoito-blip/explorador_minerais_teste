import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_sms(deposito):

    st.markdown("### 🌊⚙️ Sulfuretos Maciços Submarinos (SMS) e Crostas de Cobalto")

    col1, col2 = st.columns(2)

    with col1:

        st.success("**Propriedades Geológicas e Geoquímicas**")

        st.write("- Depósitos hidrotermais submarinos")
        st.write("- Ricos em Cu, Zn, Pb, Au, Ag")
        st.write("- Associados a fluidos quentes")
        st.write("- Precipitação rápida de sulfuretos")
        st.write("- Elevada heterogeneidade")

    with col2:

        st.info("**Importância Económica**")

        st.write("- Fonte de metais críticos")
        st.write("- Cobalto essencial para baterias")
        st.write("- Potencial elevado no fundo oceânico")
        st.write("- Interesse crescente em mineração profunda")

    st.divider()

    if "Dorsais" in deposito:

        st.markdown("### 🌋 Dorsais Médio-Oceânicas")

        st.write("**Características principais:**")
        st.write("- Associadas a expansão do fundo oceânico")
        st.write("- Sistemas hidrotermais ativos (black smokers)")
        st.write("- Formação rápida de sulfuretos")
        st.write("- Alta temperatura")

    elif "Arcos" in deposito:

        st.markdown("### 🌊 Arcos Vulcânicos Submarinos")

        st.write("**Características principais:**")
        st.write("- Associados a zonas de subducção")
        st.write("- Magmatismo intenso")
        st.write("- Maior diversidade metálica")
        st.write("- Ambientes complexos")

    elif "retro-arco" in deposito.lower():

        st.markdown("### 🌊 Bacias de Retro-Arco")

        st.write("**Características principais:**")
        st.write("- Extensão tectónica atrás de arcos vulcânicos")
        st.write("- Sistemas hidrotermais ativos")
        st.write("- Depósitos economicamente relevantes")
        st.write("- Variabilidade geológica")

    else:
        st.info("Selecione um tipo de depósito válido.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_sms():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("Os depósitos SMS e crostas de cobalto são frequentemente confundidos.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. SMS vs Nódulos Polimetálicos**")
        st.write("- SMS: associados a hidrotermalismo")
        st.write("- Nódulos: crescimento lento em planícies abissais")

        st.markdown("**2. SMS vs Crostas de Cobalto**")
        st.write("- SMS: sulfuretos maciços")
        st.write("- Crostas: enriquecimento em superfícies rochosas")

        st.markdown("**3. Ativo vs Inativo**")
        st.write("- Ativo: associado a fluidos quentes")
        st.write("- Inativo: sistemas fossilizados")

        st.markdown("**4. Mineração Simples?**")
        st.write("- Ambientes profundos implicam desafios técnicos e ambientais")


def quiz_sms():
    """Função que guarda e corre o quiz dos Sulfuretos (SMS)"""
    
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
            st.balloons()
            st.success(f"🎉 Brilhante! Acertou {pontuacao} em 4 questões!")
        elif q1 and q2 and q3 and q4:
            st.info(f"Acertou {pontuacao} em 4. Reveja as opções incorretas e tente novamente!")
        else:
            st.warning("⚠️ Responda a todas as perguntas para ver o seu resultado final.")



def mostrar_referencias_sms():
    """Função que guarda e formata as referências bibliográficas dos SMS"""
    st.markdown("### Fontes e Bibliografia - SMS")
    
    st.markdown("""
    Abaixo encontram-se as principais referências científicas e académicas consultadas para a elaboração do perfil dos Sulfuretos Maciços do Fundo Oceânico:
    
    * **Hannington, M. D., de Ronde, C. E. J., & Petersen, S. (2005).** *Sea-floor tectonics and submarine hydrothermal systems.* Economic Geology 100th Anniversary Volume, 111-141.
    * **Pirajno, F. (2009).** *Hydrothermal Processes and Mineral Systems.* Springer.
    * **Robb, L. (2005).** *Introduction to Ore-Forming Processes.* Blackwell Publishing.
    """)
    
    st.divider()
    st.caption("Organizado por: Grupo Quartzo (SB, GM, CP, DA)")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_sms():

    st.markdown("### ✅ Checklist de Campo (Exploração Submarina)")

    st.write("Utilizado na exploração de depósitos SMS:")

    st.checkbox("Identificar atividade hidrotermal")
    st.checkbox("Mapear estruturas tectónicas")
    st.checkbox("Analisar plumas hidrotermais")
    st.checkbox("Amostragem de sulfuretos")
    st.checkbox("Caracterização geoquímica")
    st.checkbox("Avaliação ambiental")
    st.checkbox("Utilização de ROVs/AUVs")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_sms():

    st.markdown("### 🌍 Mapa Global de Depósitos SMS e Cobalto")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="sms_map"
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Base de dados carregada com sucesso")
        st.dataframe(df.head())

        mapa = folium.Map(
            location=[0, 0],
            zoom_start=2
        )

        Fullscreen().add_to(mapa)

        for _, row in df.iterrows():

            if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):

                popup = f"""
                <b>Local:</b> {row.get('Field Name','N/A')}<br>
                <b>Região:</b> {row.get('Region','N/A')}<br>
                <b>Tipo:</b> {row.get('Type','N/A')}
                """

                folium.CircleMarker(
                    [row["Latitude"], row["Longitude"]],
                    radius=5,
                    color="black",
                    fill=True,
                    fill_opacity=0.8,
                    popup=popup
                ).add_to(mapa)

        st_folium(mapa, use_container_width=True, height=600)

    else:
        st.info("Carregue um ficheiro CSV para visualizar os dados.")


