import streamlit as st
import pandas as pd
import folium
from folium.plugins import Fullscreen
from streamlit_folium import st_folium


# ===============================
# 1. CARACTERÍSTICAS
# ===============================

def mostrar_caracteristicas_ortoclase(deposito):

    st.markdown("### 🪨 Características da Ortoclase")

    col1, col2 = st.columns(2)

    # Verificação de segurança
    if not deposito:
        st.warning("Por favor, seleciona um tipo de depósito para visualizar as características.")
        return

    if isinstance(deposito, list):
        deposito = ", ".join(deposito)
    
    with col1:

        st.success("**Propriedades Físicas e Geoquímicas**")

        st.write("- **Composição Química:** Silicato de alumínio e potássio (KAlSi₃O₈), podendo conter pequenas quantidades de sódio.")
        st.write("- **Estrutura Cristalina:** Pertence aos tectossilicatos, com tetraedros formando uma rede complexa.")
        st.write("- **Hábito e Simetria:** Monoclínica, exibindo frequentemente microtextura tipo 'tweed'.")
        st.write("- **Clivagem e Dureza:** Duas direções de clivagem perfeitas a 90º; dureza de 6 a 6,5 (Mohs).")
        st.write("- **Comportamento Térmico:** Baixo ponto de fusão, atuando como agente fundente essencial.")

    with col2:

        st.info("**Importância Energética**")

        st.write("- **Minerais Radioativos:** Em pegmatitos, pode hospedar uraninite e thorianite (combustível nuclear).")
        st.write("- **Lítio e Baterias:** Ocorre associada a pegmatitos LCT (fontes primárias de lítio).")
        st.write("- **Isolamento Térmico/Elétrico:** Fabrico de porcelanas e isoladores para redes de energia.")
        st.write("- **Geocronologia (K/Ar):** Datação potássio-árgon para mapear histórias térmicas de bacias.")
        st.write("- **Eficiência Industrial:** Reduz a temperatura de fusão de vidro/cerâmica, poupando energia.")
    
    st.divider()

    # 1. Pegmatitos Graníticos
    if "Pegmatitos" in deposito or "Pegmatito" in deposito:
        st.markdown("## 1. Pegmatitos Graníticos")
        
        st.success(
            "Corpos ígneos caracterizados por cristais de dimensões anómalas, fontes vitais de feldspatos de elevada pureza."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.warning(
            "Formam-se na fase final da cristalização de magmas graníticos."
        )
        st.write("- A concentração de voláteis nestes estágios permite o crescimento de cristais gigantes de ortoclase.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- **Método:** Extração em pedreiras (frequentemente a céu aberto).")
        st.write("- **Processamento:** Inclui britagem e separação magnética para remover minerais de ferro, como a biotite.")

    # 2. Granitoides Félsicos
    elif "Granitoides" in deposito or "Granitos" in deposito or "Félsicos" in deposito:
        st.markdown("## 2. Granitoides Félsicos")
        
        st.success(
            "Rochas ígneas plutónicas onde os feldspatos potássicos dominam a composição mineralógica."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.info(
            "Resultam da solidificação de intrusões magmáticas leucocráticas."
        )
        st.write("- Muitas vezes sofrem processos de feldspatização secundária (metassomatismo), que enriquece a rocha encaixante em potássio.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- **Método:** Exploração mecanizada em larga escala.")
        st.write("- **Processamento:** A matéria-prima é submetida a moagem fina e classificação granulométrica específica para uso cerâmico.")

    # 3. Depósitos Metamórficos
    elif "Metamórficos" in deposito or "Metamorfismo" in deposito:
        st.markdown("## 3. Depósitos Metamórficos")
        
        st.success(
            "Associações rochosas formadas a grandes profundidades sob regimes de pressão e temperatura elevados, como os ortognaisses."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.warning(
            "A ortoclase forma-se muitas vezes pela decomposição de micas (como a biotite e a muscovite)."
        )
        st.write("- Ocorrem de forma pronunciada em condições de alta temperatura (fácies granulito).")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- **Método:** Mineração direta de rochas consolidadas (ex: ortognaisses).")
        st.write("- **Processamento:** Envolve separação magnética a seco de alta intensidade para garantir a máxima pureza química do feldspato.")

    # 4. Acumulações Sedimentares
    elif "Sedimentares" in deposito or "Areias" in deposito or "residuais" in deposito.lower() or "Acumulações" in deposito:
        st.markdown("## 4. Acumulações Sedimentares")
        
        st.success(
            "Concentrações detríticas conhecidas comercialmente como 'areias feldspáticas', muito procuradas pela indústria vidreira."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.info(
            "Resultam da erosão agressiva de granitos seguida de transporte fluvial."
        )
        st.write("- Os grãos de ortoclase acumulam-se em paleocanais, depósitos de praia ou terraços como areias ricas em feldspato.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- **Método:** Muitas vezes extraídas em meio aquático (em lagos ou leitos de rios) através de dragas de sucção.")
        st.write("- **Processamento:** Foca-se predominantemente em operações de lavagem vigorosa e triagem por densidade.")

    # 5. Veios Hidrotermais
    elif "Hidrotermais" in deposito or "Veios" in deposito:
        st.markdown("## 5. Veios Hidrotermais")
        
        st.success(
            "Ocorrências que frequentemente albergam a variedade cristalina translúcida conhecida como 'adulária'."
        )
        st.divider()
        
        st.markdown("## Génese e Formação")
        st.warning(
            "A variedade adulária forma-se por precipitação de fluidos hidrotermais."
        )
        st.write("- Estes fluidos circulam em fendas e cavidades nas rochas a temperaturas relativamente baixas, onde o mineral precipita livremente.")
        
        st.divider()
        st.markdown("## Exploração e Processamento")
        st.write("- **Método:** Exploração geralmente mais localizada e de escala reduzida (frequentemente manual ou semi-mecanizada).")
        st.write("- **Processamento:** É bastante simplificado, maioritariamente focado na limpeza de impurezas superficiais e moagem seletiva.")

    else:
        st.info("Selecione um tipo de depósito válido para visualizar a informação.")
# ===============================
# 2. CONFUSÕES COMUNS
# ===============================

def mostrar_confusoes_ortoclase():

    st.markdown("### ⚠️ Confusões Comuns")

    st.warning("A ortoclase é frequentemente confundida com outros feldspatos.")

    with st.expander("🔍 Ver detalhes"):

        st.markdown("**1. Ortoclase vs Plagioclase**")
        st.write("- Ortoclase: feldspato potássico")
        st.write("- Plagioclase: feldspato sódio-cálcico")

        st.markdown("**2. Ortoclase vs Quartzo**")
        st.write("- Ortoclase: clivagem presente")
        st.write("- Quartzo: fratura concoidal")

        st.markdown("**3. Feldspatos ≠ Minerais Raros**")
        st.write("- São os minerais mais abundantes da crosta")

        st.markdown("**4. Alteração para Argilas**")
        st.write("- Feldspatos alteram-se facilmente (caulinização)")


# ===============================
# 3. QUIZ INTERATIVO
# ===============================

def quiz_ortoclase():

    st.markdown("### 🧠 Quiz Interativo: Ortoclase")

    st.write("Testa os teus conhecimentos 👇")

    pergunta1 = st.radio(
        "1️⃣ A ortoclase pertence a que grupo mineral?",
        [
            "Óxidos",
            "Feldspatos",
            "Carbonatos",
            "Sulfuretos"
        ],
        key="ort_q1"
    )

    if st.button("Responder Pergunta 1"):

        if pergunta1 == "Feldspatos":
            st.success("Correto! ✅")
        else:
            st.error("Incorreto ❌")

    st.divider()

    pergunta2 = st.radio(
        "2️⃣ Qual elemento caracteriza a ortoclase?",
        [
            "Ferro",
            "Potássio",
            "Magnésio",
            "Cálcio"
        ],
        key="ort_q2"
    )

    if st.button("Responder Pergunta 2"):

        if pergunta2 == "Potássio":
            st.success("Exato! ✅")
        else:
            st.error("Resposta incorreta ❌")


# ===============================
# 4. CHECKLIST DE CAMPO
# ===============================

def checklist_ortoclase():

    st.markdown("### ✅ Checklist de Campo")

    st.write("Utilizado na identificação de ortoclase:")

    st.checkbox("Observar clivagem em 2 direções")
    st.checkbox("Testar dureza (~6 Mohs)")
    st.checkbox("Identificar cor típica (rosa/branco)")
    st.checkbox("Associar a granitos/pegmatitos")
    st.checkbox("Distinguir de quartzo")
    st.checkbox("Verificar alteração para argilas")
    st.checkbox("Recolher amostras")


# ===============================
# 5. MAPA GLOBAL
# ===============================

def mapa_ortoclase():

    st.markdown("### 🌍 Mapa Global de Depósitos de Ortoclase")

    uploaded_file = st.file_uploader(
        "Carregar CSV com Latitude e Longitude",
        type=["csv"],
        key="ortoclase_map"
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Base de dados carregada com sucesso")
        st.dataframe(df.head())

        mapa = folium.Map(
            location=[20, 0],
            zoom_start=2
        )

        Fullscreen().add_to(mapa)

        for _, row in df.iterrows():

            if pd.notna(row["Latitude"]) and pd.notna(row["Longitude"]):

                popup = f"""
                <b>Local:</b> {row.get('Field Name','N/A')}<br>
                <b>País:</b> {row.get('Country','N/A')}<br>
                <b>Tipo:</b> {row.get('Type','N/A')}
                """

                folium.CircleMarker(
                    [row["Latitude"], row["Longitude"]],
                    radius=5,
                    color="pink",
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

def referencias_ortoclase():

    st.markdown("### 📚 Referências e Bibliografia")

    st.write("- Deer, Howie & Zussman – Rock-Forming Minerals")
    st.write("- Klein & Dutrow – Manual of Mineral Science")
    st.write("- USGS – Feldspar Data")
    st.write("- British Geological Survey – Industrial Minerals")
    st.write("- IMA – Mineral Database")

    st.caption("Fontes científicas sobre feldspatos e ortoclase.")
