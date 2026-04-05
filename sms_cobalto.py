import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_sms(deposito):

    st.markdown("### 🌊⚙️ Características dos Depósitos Oceânicos")

    # Verificação de segurança
    if not deposito:
        st.warning("Por favor, seleciona um tipo de depósito para visualizar as características.")
        return

    # Converter lista de seleções para string para facilitar verificação
    if isinstance(deposito, list):
        deposito_str = " ".join(deposito)
    else:
        deposito_str = deposito

    # 1. Sulfuretos Maciços (SMS)
    if "Sulfuretos" in deposito_str or "SMS" in deposito_str or "Arcos" in deposito_str or "Dorsais" in deposito_str:
        st.markdown("## 1. Sulfuretos Maciços do Fundo do Mar (SMS) / Arcos e Retro-arcos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**5 Propriedades Físicas e Geoquímicas**")
            st.write("- **Composição de Metais Base:** Apresentam altos teores de ferro, zinco, cobre e chumbo.")
            st.write("- **Riqueza em Metais Preciosos:** Contêm concentrações comercialmente exploráveis de ouro e prata.")
            st.write("- **Zonamento Térmico:** A mineralogia é influenciada pela temperatura; fluidos >300°C enriquecem em cobre, temperaturas mais baixas favorecem zinco.")
            st.write("- **Estrutura Tridimensional:** Compostos por chaminés ('black smokers'), montículos de talude e zona de stockwork.")
            st.write("- **Assinatura de Voláteis (Arcos):** Enriquecimento em elementos magmatófilos tóxicos como arsénio, mercúrio e antimónio.")

        with col2:
            st.info("**5 Pontos da Importância Energética**")
            st.write("- **Cobre para Eletrificação:** Fornecem cobre essencial para a construção de infraestruturas de redes elétricas.")
            st.write("- **Zinco para Armazenamento:** Fundamental para a produção de baterias e proteção de estruturas de energia renovável.")
            st.write("- **Transição de Baixo Carbono:** Fornecem matérias-primas críticas necessárias para uma economia de baixo carbono.")
            st.write("- **Alternativa a Minas Terrestres:** Teores frequentemente superiores aos de depósitos terrestres em declínio de qualidade.")
            st.write("- **Segurança de Abastecimento:** Reduzem a dependência externa de metais estratégicos para os setores tecnológico e energético.")

    # 2. Crostas de Ferro-Manganês
    elif "Crostas" in deposito_str or "Ferro-Manganês" in deposito_str or "Cobalto" in deposito_str:
        st.markdown("## 2. Crostas de Ferro-Manganês (Ricas em Cobalto)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**5 Propriedades Físicas e Geoquímicas**")
            st.write("- **Mineralogia Principal:** Compostas por oxihidróxidos de ferro e óxidos de manganês (vernadite e birnessite).")
            st.write("- **Enriquecimento em Cobalto:** Principal fonte oceânica de cobalto, com teores que podem atingir os 2%.")
            st.write("- **Crescimento Lento:** Taxa de crescimento extremamente lenta (1 a 5 milímetros por milhão de anos).")
            st.write("- **Alta Área Superficial:** Superfície específica média enorme (325 m²/cm³), potenciando a adsorção de metais.")
            st.write("- **Conteúdo de Metais Raros:** Concentram telúrio, platina, molibdénio e elementos de terras raras (REY).")

        with col2:
            st.info("**5 Pontos da Importância Energética**")
            st.write("- **Cobalto para Mobilidade Elétrica:** Essencial para o fabrico de baterias de iões de lítio para veículos elétricos.")
            st.write("- **Telúrio para Energia Solar:** Constituem a maior reserva global de telúrio, usado em células solares de película fina.")
            st.write("- **Terras Raras (REY) para Aerogeradores:** Contêm neodímio e térbio, cruciais para ímanes em turbinas eólicas.")
            st.write("- **Platina para Células de Combustível:** Fonte de platina, catalisador em tecnologias de hidrogénio.")
            st.write("- **Autonomia Estratégica:** Fornecem Minerais Críticos (CRM) fundamentais para a independência energética.")

    # 3. Nódulos Polimetálicos
    elif "Nódulos" in deposito_str:
        st.markdown("## 3. Nódulos Polimetálicos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**5 Propriedades Físicas e Geoquímicas**")
            st.write("- **Acreção Concêntrica:** Deposição concêntrica de óxidos em torno de um núcleo (ex: dente de tubarão ou rocha).")
            st.write("- **Génese Mista:** Crescimento hidrogenético (água do mar) e diagenético (água dos poros dos sedimentos).")
            st.write("- **Mineralogia de Manganês:** Compostos essencialmente por vernadite, todorokite e birnessite.")
            st.write("- **Riqueza em Níquel e Cobre:** Apresentam teores de níquel e cobre superiores aos das crostas.")
            st.write("- **Localização Abissal:** Ocorrem de forma vasta nas planícies abissais oceânicas.")

        with col2:
            st.info("**5 Pontos da Importância Energética**")
            st.write("- **Níquel para Baterias:** O elevado teor de níquel é vital para baterias de alta densidade energética.")
            st.write("- **Manganês para Armazenamento:** Utilizado em ligas metálicas e em novas tecnologias de armazenamento.")
            st.write("- **Suplemento de Recursos Terrestres:** Alternativa massiva para suprir a procura global de metais base.")
            st.write("- **Diversificação de Fontes:** Aumentam a resiliência do mercado contra interrupções no fornecimento terrestre.")
            st.write("- **Economia de Escala:** Potencial de exploração em larga escala pode reduzir custos nas energias renováveis.")

    # 4. Fosforitos
    elif "Fosforitos" in deposito_str:
        st.markdown("## 4. Fosforitos")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**5 Propriedades Físicas e Geoquímicas**")
            st.write("- **Mineralogia de Fosfato:** Compostos predominantemente por fluorapatite carbonatada (CFA).")
            st.write("- **Composição Química:** Ricos em fósforo (P₂O₅) e cálcio (CaO).")
            st.write("- **Associação com Crostas:** Servem frequentemente de substrato rochoso para as crostas de cobalto.")
            st.write("- **Hospedeiros de REY:** Atuam como depósitos secundários importantes para elementos de terras raras e ítrio.")
            st.write("- **Origem Oceanográfica:** Ligada a correntes de fundo intensas e períodos de elevada produtividade biológica.")

        with col2:
            st.info("**5 Pontos da Importância Energética**")
            st.write("- **Ítrio para Eficiência Energética:** Fonte de ítrio, usado em tecnologias de iluminação eficiente e LEDs.")
            st.write("- **Terras Raras para Tecnologia:** O seu conteúdo em REY apoia a produção de componentes eletrónicos avançados.")
            st.write("- **Valorização de Recursos:** A presença aumenta significativamente o valor económico total dos montes submarinos.")
            st.write("- **Independência Tecnológica:** Contribuem para a segurança de abastecimento de metais críticos.")
            st.write("- **Fósforo Industrial:** Potencial para aplicações químicas e industriais ligadas a infraestruturas energéticas.")

    # 5. Lamas REY
    elif "Lamas" in deposito_str or "Sedimentos" in deposito_str:
        st.markdown("## 5. Lamas REY")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("**5 Propriedades Físicas e Geoquímicas**")
            st.write("- **Origem Hidrotermal:** Deposição de partículas ricas em metais de plumas hidrotermais.")
            st.write("- **Preservação Metálica:** Retêm Cu, Zn e sulfuretos por soterramento rápido e ausência de fluxo residual.")
            st.write("- **Estratigrafia Fina:** Apresentam frequentemente sequências de grão fino de depósitos turbidíticos.")
            st.write("- **Concentração de Terras Raras:** Enriquecidas em terras raras leves (LREE) e ítrio.")
            st.write("- **Extensão Territorial:** Dispersam-se por áreas de vários quilómetros quadrados em torno dos depósitos centrais.")

        with col2:
            st.info("**5 Pontos da Importância Energética**")
            st.write("- **Fonte de LREE:** Fornecem terras raras leves essenciais para ímanes de alta tecnologia e motores elétricos.")
            st.write("- **Metais Base Dispersos:** Contêm misturas de cobre e zinco que representam um recurso volumétrico.")
            st.write("- **Volume de Recurso:** A vasta dispersão sugere um potencial de extração massivo por quilómetro quadrado.")
            st.write("- **Diversificação Estratégica:** Via alternativa para obter metais críticos fora dos depósitos maciços tradicionais.")
            st.write("- **Autonomia em CRM:** Apoiam diretamente as metas de autonomia estratégica em matérias-primas críticas.")

    else:
        st.info("Selecione um tipo de depósito válido para visualizar a informação detalhada.")

# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_sms(deposito):

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



def referencias_sms():
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


