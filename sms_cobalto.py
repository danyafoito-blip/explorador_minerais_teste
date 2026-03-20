import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_sms(deposito=""):

    st.markdown("### 🌊⚙️ Sulfuretos Maciços Submarinos (SMS) e Crostas de Cobalto")

    st.markdown("#### 🌍 5 Características Gerais do Recurso")
    
    with st.expander("🔍 Ver características gerais", expanded=True):
        st.markdown("**1. Geração Hidrotermal:** Estes depósitos formam-se através da circulação hidrotermal, onde a água do mar penetra na crosta, é aquecida por energia geotérmica, dissolve metais das rochas circundantes e os precipita como sulfuretos ao ser expelida.")
        st.markdown("**2. Composição Metálica:** São ricos em metais base (Cobre, Zinco, Ferro e Chumbo) e contêm concentrações exploráveis de metais preciosos como Ouro e Prata.")
        st.markdown("**3. Estrutura Tridimensional:** O recurso consiste em montículos de sulfuretos na superfície, chaminés (como os \"black smokers\") e uma zona de alimentação subsuperficial conhecida como stockwork.")
        st.markdown("**4. Potencial Económico:** Estima-se que os depósitos ativos contenham centenas de milhões de toneladas de material, com teores de metal comparáveis ou superiores aos depósitos terrestres.")
        st.markdown("**5. Ecossistemas Associados:** Suportam comunidades biológicas únicas baseadas na quimiossíntese em locais ativos, enquanto locais inativos servem de substrato duro para fauna séssil de águas profundas.")

    st.divider()

    # Mostra apenas as 5 características específicas dependendo do depósito selecionado
    if deposito:
        st.markdown(f"#### 🔎 Características Específicas: {deposito}")

        if "Arcos" in deposito:
            st.markdown("- **Rocha Hospedeira Evoluída:** Diferente das dorsais, estes depósitos estão associados a composições vulcânicas mais ácidas e evoluídas, como andesito, dacito e riolito.")
            st.markdown("- **Aporte de Voláteis Magmáticos:** Apresentam enriquecimento em elementos magmatófilos (As, Sb, Bi, Te) derivados da desgaseificação de câmaras magmáticas.")
            st.markdown("- **Elevado Teor de Mercúrio:** Podem conter concentrações muito altas de mercúrio (Hg), ocorrendo por vezes como mercúrio nativo (ex: campo Calypso).")
            st.markdown("- **Depósitos de Substituição:** Frequentemente formam-se por substituição e infiltração no subsolo marinho, o que pode resultar em corpos de minério enterrados sem as chaminés clássicas expostas.")
            st.markdown("- **Toxicidade Potencial:** Possuem o maior risco de toxicidade ambiental devido à associação de metais como As, Sb, Pb e Hg em minerais reativos como sulfossais e galena.")

        elif "Dorsais" in deposito:
            st.markdown("- **Substrato Máfico/Ultramáfico:** São predominantemente alojados em basaltos e gabros, ou peridotitos serpentinizados em zonas de falhas de destacamento.")
            st.markdown("- **Assinatura de Metais Primários:** Demonstram concentrações elevadas de Cu, Fe, Co, Se, Ni e Mo, refletindo a lixiviação direta da crosta oceânica máfica.")
            st.markdown("- **Morfologia de Montículo:** Sistemas maduros (como o campo TAG) formam grandes montículos circulares por acumulação e retrabalhamento de taludes de chaminés ao longo de milénios.")
            st.markdown("- **Capa de Jasper Protetora:** Em depósitos extintos, o corpo principal de sulfureto é frequentemente protegido da oxidação por uma camada de jasper (sílica rica em ferro) de 3 a 6 metros de espessura.")
            st.markdown("- **Controlo da Taxa de Expansão:** A taxa de espalhamento da crista influencia a profundidade da célula hidrotermal e a rácio rocha/água, afetando diretamente os teores de Au, Ag e Ni.")

        elif "retro-arco" in deposito.lower():
            st.markdown("- **Teores Metálicos Combinados Elevados:** Apresentam frequentemente os teores mais altos de Cu + Zn + Pb (média de 16,1 wt.%) entre todos os ambientes tectónicos.")
            st.markdown("- **Enriquecimento em Ouro:** Tendem a possuir teores de ouro (Au) sistematicamente superiores aos encontrados nas cristas médio-oceânicas puras.")
            st.markdown("- **Dualidade Geodinâmica:** Combinam características de centros de expansão (semelhantes às dorsais) com a influência geoquímica de zonas de subducção.")
            st.markdown("- **Zonamento Mineralógico:** Possuem assembleias complexas de pirite-esfalerite e calcopirite-esfalerite, muitas vezes acompanhadas por barite.")
            st.markdown("- **Densidade de Ocorrência:** A frequência de depósitos ativos nestas bacias é comparável à das dorsais de espalhamento lento, ocorrendo aproximadamente a cada 174 km.")
    else:
        st.info("Selecione um tipo de depósito na barra lateral para ver as características específicas.")


# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_sms(deposito=""):

    st.markdown("### ⚠️ Confusões e Distinções Comuns")

    st.warning("A distinção entre os vários tipos de sulfuretos maciços e crostas exige atenção a detalhes geoquímicos, texturais e tectónicos.")

    st.markdown("#### 🌍 7 Pontos Gerais de Distinção e Confusão")
    
    with st.expander("🔍 Ver detalhes gerais", expanded=True):
        st.markdown("**1. Origem Genética (Rácio Mn/Fe):** A confusão entre crostas hidrogenéticas, diagenéticas e hidrotermais resolve-se pelo rácio Mn/Fe. Crostas hidrogenéticas têm rácios próximos de 1; depósitos hidrotermais mostram uma separação extrema (predomínio de Fe ou Mn); e diagenéticos são enriquecidos em Mn, Ni e Cu em relação ao Fe.")
        st.markdown("**2. Estado de Atividade:** Sistemas ativos possuem fluidos a altas temperaturas (>350°C) e mineralogia de anidrite. Sistemas extintos (eSMS) perdem a anidrite por dissolução, sofrem colapso interno e são frequentemente protegidos por uma capa de jasper (sílica-ferro) de 3 a 6 metros.")
        st.markdown("**3. Maturação Textural:** As texturas coloformes (zonadas e imaturas) retêm concentrações mais elevadas de elementos traço tóxicos (As, Pb, Ag, Sb) que são perdidos durante a recristalização para texturas maciças (maduras e euédricas).")
        st.markdown("**4. Assinatura Geoquímica por Substrato:** Embora o rácio Co/Ni tenha sido usado para distinguir substratos máficos de ultramáficos, ele tem pouco poder discriminatório. O estanho (Sn) e um rácio Au/Ag cinco vezes superior são marcadores mais fiáveis de influência ultramáfica.")
        st.markdown("**5. Mapeamento Acústico (ABI):** A intensidade de retrodispersão acústica pode confundir crostas puras com misturas de sedimentos. Áreas de crosta dominante (C) e mistas (M) exibem ABI elevado, enquanto áreas de sedimento (S) têm ABI baixo.")
        st.markdown("**6. Taxas de Espalhamento (Spreading Rate):** Cristas de espalhamento lento ou ultralento favorecem rácios rocha/água mais elevados e percursos de fluidos mais profundos, influenciando o enriquecimento em metais preciosos (Au, Ag) face a cristas rápidas.")
        st.markdown("**7. Zonamento Térmico:** Chaminés de alta temperatura são ricas em cobre (calcopirite), enquanto fluidos de temperatura mais baixa (<300°C) favorecem o enriquecimento em zinco e chumbo (esfalerite e galena).")

    st.divider()

    if deposito:
        st.markdown(f"#### 🔎 Distinções Específicas: {deposito}")

        if "Arcos" in deposito:
            st.markdown("- **Rocha Hospedeira Evoluída:** Associados a composições vulcânicas mais ácidas/evoluidas, como andesito, dacito e riolito.")
            st.markdown("- **Enriquecimento em Voláteis:** Presença distinta de elementos magmatófilos (As, Sb, Bi, Te) derivados da desgaseificação de câmaras magmáticas profundas.")
            st.markdown("- **Toxicidade Elevada:** Potencial de toxicidade superior devido à abundância de mercúrio (Hg) nativo e sulfuretos de mercúrio (ex: campo Calypso).")
            st.markdown("- **Mineralogia Específica:** Ocorrência de sulfossais (série tennantite-tetraedrite) e galena, raramente vistos em cristas médio-oceânicas puras.")
            st.markdown("- **Depósitos de Substituição:** Podem formar depósitos enterrados por substituição e infiltração no subsolo marinho (ex: Palinuro), em vez de chaminés clássicas expostas.")

        elif "Dorsais" in deposito:
            st.markdown("- **Substrato Máfico/Ultramáfico:** Dominadas por basalto e gabro, ou peridotitos serpentinizados em zonas de falhas de destacamento.")
            st.markdown("- **Assinatura Metálica Primária:** Ricas em Cu, Fe, Co, Se e Mo, com baixa concentração de elementos \"epitermais\" como As e Sb.")
            st.markdown("- **Morfologia de Montículo:** Depósitos maduros como o TAG formam grandes montículos por acumulação e retrabalhamento de taludes de chaminés ao longo de milhares de anos.")
            st.markdown("- **Exclusividade do Cobalto:** O Co está associado quase exclusivamente a locais de alta temperatura (~400°C) nestas dorsais.")
            st.markdown("- **Sequência de Jasper:** Em depósitos extintos, a preservação do minério é garantida por uma carapaça de sílica impermeável que impede a oxidação pela água do mar.")

        elif "retro-arco" in deposito.lower():
            st.markdown("- **Elevado Teor Metálico:** Demonstram frequentemente os teores combinados de Cu + Zn + Pb mais elevados (média de 16,1 wt%) entre todos os ambientes tectónicos.")
            st.markdown("- **Riqueza em Ouro:** Tendem a apresentar teores de ouro (Au) sistematicamente superiores aos sistemas de crista médio-oceânica.")
            st.markdown("- **Dualidade Geológica:** Combinam características de dorsais (centros de expansão) com a influência de subducção, resultando em misturas de assinaturas geoquímicas máficas e félsicas.")
            st.markdown("- **Densidade de Depósitos:** A frequência de ocorrência de depósitos ativos é comparável à das dorsais de espalhamento lento (aprox. cada 174 km).")
            st.markdown("- **Zonamento Complexo:** Devido à natureza bimodal do vulcanismo, apresentam um zonamento mineralógico complexo entre assembleias de pirite-esfalerite e calcopirite-esfalerite.")
    else:
        st.info("Selecione um tipo de depósito na barra lateral para ver as confusões específicas.")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_sms():

    st.markdown("### 🧠 Quiz Interativo: SMS e Cobalto")

    st.write("Testa os teus conhecimentos 👇")

    pergunta1 = st.radio(
        "1️⃣ Onde se formam os SMS?",
        [
            "Desertos",
            "Sistemas hidrotermais submarinos",
            "Atmosfera",
            "Glaciares"
        ],
        key="sms_q1"
    )

    if st.button("Responder Pergunta 1"):

        if pergunta1 == "Sistemas hidrotermais submarinos":
            st.success("Correto! ✅")
        else:
            st.error("Incorreto ❌")

    st.divider()

    pergunta2 = st.radio(
        "2️⃣ O cobalto é crítico para:",
        [
            "Produção de cimento",
            "Baterias",
            "Areia industrial",
            "Vidro comum"
        ],
        key="sms_q2"
    )

    if st.button("Responder Pergunta 2"):

        if pergunta2 == "Baterias":
            st.success("Exato! ✅")
        else:
            st.error("Resposta incorreta ❌")


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


# ===============================
# 6. REFERÊNCIAS
# ===============================

def referencias_sms():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- Hannington et al. – Seafloor Massive Sulfides")
    st.write("- ISA (International Seabed Authority)")
    st.write("- USGS – Marine Mineral Resources")
    st.write("- Hein et al. – Cobalt-Rich Crusts")
    st.write("- Nature Reviews – Deep-Sea Mining")

    st.caption("Fontes científicas sobre mineração submarina e SMS.")
