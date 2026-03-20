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

def quiz_sms(deposito=""):

    st.markdown("### 🧠 Quiz Interativo: SMS e Recursos Marinhos")
    st.write("Testa os teus conhecimentos sobre os recursos minerais do fundo do mar! 👇")

    # --- PARTE 1: QUESTÕES GERAIS ---
    st.markdown("#### 🌍 Questões Gerais")
    
    with st.expander("📝 Mostrar Questões Gerais", expanded=True):
        # Q1
        q1 = st.radio(
            "1️⃣ Quais são os principais metais base encontrados nos Sulfuretos Maciços do Fundo do Mar (SMS)?",
            ["Ouro e Prata", "Cobre, Zinco, Chumbo e Ferro", "Cobalto e Níquel", "Alumínio e Magnésio"],
            key="sms_geral_q1"
        )
        if st.button("Verificar Q1", key="btn_g1"):
            if q1 == "Cobre, Zinco, Chumbo e Ferro":
                st.success("Correto! ✅ Estes são os metais base dominantes, embora possam conter ouro e prata como subprodutos.")
            else:
                st.error("Incorreto. ❌ Tenta novamente!")

        st.divider()

        # Q2
        q2 = st.radio(
            "2️⃣ Qual é a taxa de crescimento típica das crostas de ferro-manganês de origem hidrogenética?",
            ["1-5 metros por ano", "1-5 centímetros por século", "1-5 milímetros por milhão de anos", "10-20 milímetros por década"],
            key="sms_geral_q2"
        )
        if st.button("Verificar Q2", key="btn_g2"):
            if q2 == "1-5 milímetros por milhão de anos":
                st.success("Correto! ✅ É um processo extremamente lento comparado com depósitos hidrotermais.")
            else:
                st.error("Incorreto. ❌ Lembra-te que a precipitação hidrogenética é um processo muito lento.")

        st.divider()

        # Q3
        q3 = st.radio(
            "3️⃣ Em que intervalo de profundidade se encontram geralmente as crostas mais ricas em cobalto e de maior interesse económico?",
            ["100 a 500 metros", "800 a 2500 metros", "4000 a 6000 metros", "Apenas abaixo dos 7000 metros"],
            key="sms_geral_q3"
        )
        if st.button("Verificar Q3", key="btn_g3"):
            if q3 == "800 a 2500 metros":
                st.success("Correto! ✅ Encontram-se tipicamente nos flancos de montes submarinos (seamounts) a estas profundidades.")
            else:
                st.error("Incorreto. ❌ Tenta novamente!")

        st.divider()

        # Q4
        q4 = st.radio(
            "4️⃣ Qual é o mineral de manganês predominante nas crostas hidrogenéticas?",
            ["Vernadite", "Todorokite", "Calcite", "Pirite"],
            key="sms_geral_q4"
        )
        if st.button("Verificar Q4", key="btn_g4"):
            if q4 == "Vernadite":
                st.success("Correto! ✅ A vernadite (δ-MnO2) é o mineral de manganês mais comum nestas crostas.")
            else:
                st.error("Incorreto. ❌ Tenta novamente!")

        st.divider()

        # Q5
        q5 = st.radio(
            "5️⃣ Que morfologia de superfície é característica de muitas crostas de ferro-manganês?",
            ["Cristais euédricos perfeitos", "Superfície lisa e vítrea", "Botrioidal (em forma de cacho de uvas)", "Estrutura fibrosa verticalizada"],
            key="sms_geral_q5"
        )
        if st.button("Verificar Q5", key="btn_g5"):
            if q5 == "Botrioidal (em forma de cacho de uvas)":
                st.success("Correto! ✅ Esta textura globular/botrioidal é muito típica na superfície destas crostas.")
            else:
                st.error("Incorreto. ❌ Pensa em formas circulares ou em cacho.")

    st.write("") # Espaçamento

    # --- PARTE 2: QUESTÕES ESPECÍFICAS ---
    if deposito:
        st.markdown(f"#### 🔎 Questões Específicas: {deposito}")

        if "Arcos" in deposito:
            # Arcos Q1
            q_arc1 = st.radio(
                "Ao contrário das dorsais, que tipo de rochas hospedeiras são típicas em arcos vulcânicos?",
                ["Basaltos e Peridotitos", "Rochas vulcânicas ácidas e evoluídas como dacitos e riolitos", "Calcários puros", "Arenitos"],
                key="sms_arc_q1"
            )
            if st.button("Verificar Resposta 1 (Arcos)", key="btn_a1"):
                if q_arc1 == "Rochas vulcânicas ácidas e evoluídas como dacitos e riolitos":
                    st.success("Correto! ✅ O vulcanismo de arco é geralmente mais silícico (ácido).")
                else:
                    st.error("Incorreto. ❌ Tenta novamente!")
            
            st.divider()
            
            # Arcos Q2
            q_arc2 = st.radio(
                "Qual destes elementos tóxicos pode ocorrer como metal nativo em campos hidrotermais de arco (ex: Calypso)?",
                ["Mercúrio (Hg)", "Ferro (Fe)", "Magnésio (Mg)", "Sódio (Na)"],
                key="sms_arc_q2"
            )
            if st.button("Verificar Resposta 2 (Arcos)", key="btn_a2"):
                if q_arc2 == "Mercúrio (Hg)":
                    st.success("Correto! ✅ Ambientes de arco apresentam frequentemente maior toxicidade por elementos como o Hg.")
                else:
                    st.error("Incorreto. ❌ Tenta novamente!")

        elif "Dorsais" in deposito:
            # Dorsais Q1
            q_dor1 = st.radio(
                "Qual é o principal tipo de rocha que constitui o substrato nas Dorsais Médio-Oceânicas?",
                ["Granito", "Basalto (MORB)", "Argila pelágica", "Calcário coralino"],
                key="sms_dor_q1"
            )
            if st.button("Verificar Resposta 1 (Dorsais)", key="btn_d1"):
                if q_dor1 == "Basalto (MORB)":
                    st.success("Correto! ✅ Os Mid-Ocean Ridge Basalts (MORB) são a rocha dominante.")
                else:
                    st.error("Incorreto. ❌ Pensa no magma que se forma nos centros de expansão oceânica.")
            
            st.divider()

            # Dorsais Q2
            q_dor2 = st.radio(
                "O que caracteriza a estrutura de depósitos extintos (eSMS) nas dorsais para os proteger da oxidação?",
                ["Uma camada de matéria orgânica", "Uma capa de jasper (sílica rica em ferro)", "Uma barreira de anidrite ativa", "Não possuem qualquer proteção"],
                key="sms_dor_q2"
            )
            if st.button("Verificar Resposta 2 (Dorsais)", key="btn_d2"):
                if q_dor2 == "Uma capa de jasper (sílica rica em ferro)":
                    st.success("Correto! ✅ Esta carapaça impermeável de sílica protege os sulfuretos da água do mar.")
                else:
                    st.error("Incorreto. ❌ Tenta novamente!")

        elif "retro-arco" in deposito.lower():
            # Retro-arco Q1
            q_ret1 = st.radio(
                "Como se comparam os teores combinados de Cu+Zn+Pb nas bacias de retro-arco em relação a outros ambientes tectónicos?",
                ["São sistematicamente os mais baixos", "São frequentemente os mais elevados (média de 16,1 wt.%)", "São idênticos aos das bacias oceânicas profundas", "Não contêm metais base"],
                key="sms_ret_q1"
            )
            if st.button("Verificar Resposta 1 (Retro-arco)", key="btn_r1"):
                if q_ret1 == "São frequentemente os mais elevados (média de 16,1 wt.%)":
                    st.success("Correto! ✅ As bacias de retro-arco apresentam uma elevada densidade e concentração metálica.")
                else:
                    st.error("Incorreto. ❌ Tenta novamente!")
            
            st.divider()

            # Retro-arco Q2
            q_ret2 = st.radio(
                "Em relação ao ouro (Au), os depósitos em bacias de retro-arco tendem a ter teores:",
                ["Superiores aos das cristas médio-oceânicas", "Inexistentes", "Muito inferiores aos das dorsais", "Apenas vestigiais sem interesse económico"],
                key="sms_ret_q2"
            )
            if st.button("Verificar Resposta 2 (Retro-arco)", key="btn_r2"):
                if q_ret2 == "Superiores aos das cristas médio-oceânicas":
                    st.success("Correto! ✅ Há frequentemente um enriquecimento notável em metais preciosos nestes ambientes.")
                else:
                    st.error("Incorreto. ❌ Tenta novamente!")

    else:
        st.info("Selecione um tipo de depósito na barra lateral para ver as questões específicas deste ambiente.")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_sms(deposito=""):

    st.markdown("### ✅ Checklist de Campo (Exploração Submarina)")

    st.write("Critérios de identificação de amostras e depósitos SMS:")

    st.markdown("#### 🌍 Checklist Geral de Identificação")
    
    with st.expander("🔍 Ver checklist geral", expanded=True):
        st.checkbox("**Morfologia Externa:** Verificar se a amostra apresenta estruturas tubulares (fragmentos de chaminés com condutos centrais), massas de sulfuretos maciços ou pavimentos de crostas botrioidais (em forma de cacho de uvas).", key="chk_geral_1")
        st.checkbox("**Mineralogia Primária de Sulfuretos:** Identificar a presença de pirite, calcopirite (amarelo-latão), esfalerite (brilho resinoso) ou galena (brilho metálico cinza).", key="chk_geral_2")
        st.checkbox("**Presença de Oxidação e Capas Protetoras:** Em depósitos extintos, procurar pela capa de jasper (sílica rica em ferro, cor laranja a vermelho-escuro) ou camadas de oxihidróxidos de ferro (FeOOH) que revestem o minério.", key="chk_geral_3")
        st.checkbox("**Crostas de Fe-Mn:** Identificar a alternância de lâminas escuras (pretas a castanhas) diretamente sobre o substrato rochoso, apresentando uma textura fosca ou localmente brilhante se houver influência diagenética.", key="chk_geral_4")
        st.checkbox("**Texturas de Maturação:** Diferenciar entre texturas coloformes (bandadas e zonadas, indicando cristalização imatura) e texturas maciças (recristalizadas e euédricas, indicando maturação térmica).", key="chk_geral_5")

    st.divider()

    if deposito:
        st.markdown(f"#### 🔎 Checklist Específica: {deposito}")

        if "Arcos" in deposito:
            st.checkbox("**Substrato e Rocha Hospedeira:** Presença de fragmentos de rochas vulcânicas evoluídas e ácidas, como dacito ou riolito, em vez de basaltos simples.", key="chk_arc_1")
            st.checkbox("**Mineralogia de Sulfossais:** Identificar visualmente sulfossais da série tennantite-tetraedrite e abundância de galena, que são mais comuns neste ambiente.", key="chk_arc_2")
            st.checkbox("**Enriquecimento em Voláteis:** Procurar indicadores de mercúrio (Hg), por vezes ocorrendo como mercúrio nativo ou sulfuretos reativos (ex: campo Calypso).", key="chk_arc_3")
            st.checkbox("**Gangue Abundante:** Presença significativa de minerais de gangue como barite (muitas vezes em texturas vuggy) e anidrite.", key="chk_arc_4")
            st.checkbox("**Morfologia de Substituição:** Amostras que indicam infiltração e substituição de sedimentos ou rochas pré-existentes, resultando em minérios de aspeto 'sujo' ou brechificado com matriz sedimentar.", key="chk_arc_5")

        elif "Dorsais" in deposito:
            st.checkbox("**Host Rock Máfico/Ultramáfico:** Amostras associadas a basaltos (MORB), gabros ou peridotitos serpentinizados (frequentemente com clorite verde).", key="chk_dor_1")
            st.checkbox("**Estrutura de Chaminé 'Black Smoker':** Fragmentos com condutos de fluidos intactos revestidos por calcopirite ou marcasite.", key="chk_dor_2")
            st.checkbox("**Capa de Jasper Distintiva:** Presença de uma camada impermeável de sílica-ferro (3-6m no depósito original) com cores variando entre o mosqueado vermelho e cinza.", key="chk_dor_3")
            st.checkbox("**Zonamento Térmico Simples:** Observar a separação clara entre zonas ricas em cobre (calcopirite) no núcleo e zinco (esfalerite) na periferia das chaminés.", key="chk_dor_4")
            st.checkbox("**Pirite Maciça e Brechas:** Massas densas de pirite brechificada que formam a base dos montículos, muitas vezes com baixo teor visual de gangue.", key="chk_dor_5")

        elif "retro-arco" in deposito.lower():
            st.checkbox("**Elevada Densidade Metálica:** Amostras com os teores combinados mais elevados de Cu+Zn+Pb, apresentando-se extremamente pesadas e compactas.", key="chk_ret_1")
            st.checkbox("**Mineralogia Bimodal:** Assembleias complexas e mistas de pirite-esfalerite e calcopirite-esfalerite na mesma amostra.", key="chk_ret_2")
            st.checkbox("**Presença de Ouro e Prata:** Embora microscópicos, estes depósitos tendem a exibir teores de metais preciosos superiores aos de crista médio-oceânica.", key="chk_ret_3")
            st.checkbox("**Chaminés Ramificadas:** Morfologia de chaminés mais finas e ramificadas (ex: 20 cm de diâmetro), indicando regimes de fluxo distintos (ex: 'Satanic Mills').", key="chk_ret_4")
            st.checkbox("**Influência Magmática:** Presença de minerais e texturas associados a fluidos magmáticos exsolvidos, resultando numa geoquímica rica em metais 'epitermais' como As e Sb.", key="chk_ret_5")
    else:
        st.info("Selecione um tipo de depósito na barra lateral para ver a checklist específica.")


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
