import streamlit as st
import google.generativeai as genai
import os

# --- Configuração da API Key do Gemini ---
try:
    GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
except FileNotFoundError:
    # ATENÇÃO: Para o GitHub, esta linha deve ser GOOGLE_API_KEY = ""
    # e a chave real deve estar nos Secrets do Streamlit Cloud.
    GOOGLE_API_KEY = "" 

if GOOGLE_API_KEY == "SUA_CHAVE_API_AQUI_PARA_TESTE_LOCAL" or not GOOGLE_API_KEY: 
    st.error("Chave de API do Gemini não configurada. Verifique o código ou os Secrets do Streamlit Cloud.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# --- Definições das Funções ---
def gerar_plano_estudos_com_gemini(meta_nota, dias_semana, horas_dia_str, materias_dificuldade, materias_facilidade):
    prompt = f"""
    Crie um cronograma de estudos preliminar para o ENEM para um aluno com as seguintes características:
    - Meta de nota: {meta_nota}
    - Dias disponíveis por semana para estudo: {dias_semana}
    - Média de horas de estudo por dia: {horas_dia_str}
    - Matérias com MAIS dificuldade: {', '.join(materias_dificuldade) if materias_dificuldade else 'Nenhuma específica'}
    - Matérias com MAIS facilidade ou bom conhecimento: {', '.join(materias_facilidade) if materias_facilidade else 'Nenhuma específica'}

    O cronograma deve ser realista, distribuindo as matérias ao longo da semana.
    Sugira um plano para a primeira semana de estudos, detalhando quais matérias e tópicos gerais focar em cada dia disponível.
    
    IMPORTANTE PARA FORMATAÇÃO:
    Qualquer texto introdutório geral ao plano deve vir ANTES do primeiro dia.
    Para cada dia da semana do plano, comece a seção do dia com um título de cabeçalho markdown de nível 3, seguido do nome do dia. Por exemplo:
    ### Segunda-feira
    [Conteúdo da Segunda-feira aqui]

    ### Terça-feira
    [Conteúdo da Terça-feira aqui]

    E assim por diante para os outros dias planejados.
    Apresente o conteúdo de cada dia em formato de tópicos (markdown) para fácil leitura.
    Lembre o aluno da importância de pausas e revisões (pode ser na introdução ou no final do plano).
    Para a Sexta-feira, após o conteúdo de estudo planejado, inclua a seguinte seção de observações importantes:
    ### 📝 Observações Importantes para sua Sexta-feira e Fim de Semana:
    - Este é um plano inicial, adaptável às suas necessidades.
    - Utilize materiais didáticos adequados ao nível do ENEM.
    - Resolva muitas questões de provas anteriores para simular a prova e identificar seus pontos fracos.
    - Procure por videoaulas e materiais complementares online para auxiliar nos assuntos que apresentar maior dificuldade.
    - A revisão semanal é crucial para consolidar o conhecimento adquirido.
    - Não se esqueça de incluir pausas regulares durante seus estudos para evitar o esgotamento mental. Um descanso adequado é tão importante quanto o estudo em si.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"Erro ao gerar o plano com a IA: {e}")
        return None

def gerar_plano_adaptado_com_gemini(metas_originais, plano_anterior_texto, feedback_aluno_texto):
    prompt_adaptacao = f"""
Você é um mentor de estudos para o ENEM chamado Cronos.
As metas originais do aluno são:
- Meta de nota: {metas_originais['meta_nota']}
- Dias disponíveis por semana para estudo: {metas_originais['dias_semana']}
- Média de horas de estudo por dia: {metas_originais['horas_dia_str']}
- Matérias com MAIS dificuldade: {', '.join(metas_originais['materias_dificuldade']) if metas_originais['materias_dificuldade'] else 'Nenhuma específica'}
- Matérias com MAIS facilidade ou bom conhecimento: {', '.join(metas_originais['materias_facilidade']) if metas_originais['materias_facilidade'] else 'Nenhuma específica'}

O plano de estudos que estava em vigor (semana anterior) é:
\"\"\"
{plano_anterior_texto}
\"\"\"

O feedback do aluno sobre este plano e seu progresso foi:
\"\"\"
{feedback_aluno_texto}
\"\"\"

Com base em TODAS essas informações (metas originais, plano anterior e o feedback do aluno), gere um NOVO plano de estudos OTIMIZADO e ADAPTADO para a PRÓXIMA semana.
O novo plano deve:
1. Ser realista e motivador.
2. Considerar o progresso real informado pelo aluno.
3. Dar atenção especial aos tópicos onde o aluno AINDA demonstra dificuldade ou onde ficou para trás, conforme o feedback.
4. Se necessário, reagendar conteúdos importantes que não foram cobertos. Priorize os tópicos essenciais.
5. Manter o foco nas metas originais do aluno.
6. Se o aluno estiver progredindo bem, sugira avanços ou desafios moderados.

Apresente o novo plano em formato de tópicos (markdown) para fácil leitura. 
Para cada dia da semana do plano, comece a seção do dia com um título de cabeçalho markdown de nível 3, seguido do nome do dia. Por exemplo:
### Segunda-feira
[Conteúdo da Segunda-feira aqui]
No início do plano, inclua uma breve análise do progresso do aluno (baseada no feedback) e explique as principais mudanças ou focos para a nova semana em relação ao plano anterior, se relevante.
Finalize com uma mensagem de encorajamento.
Para a Sexta-feira, após o conteúdo de estudo planejado, inclua a seguinte seção de observações importantes:
### 📝 Observações Importantes para sua Sexta-feira e Fim de Semana:
- Este é um plano inicial, adaptável às suas necessidades.
- Utilize materiais didáticos adequados ao nível do ENEM.
- Resolva muitas questões de provas anteriores para simular a prova e identificar seus pontos fracos.
- Procure por videoaulas e materiais complementares online para auxiliar nos assuntos que apresentar maior dificuldade.
- A revisão semanal é crucial para consolidar o conhecimento adquirido.
- Não se esqueça de incluir pausas regulares durante seus estudos para evitar o esgotamento mental. Um descanso adequado é tão importante quanto o estudo em si.
"""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt_adaptacao)
        return response.text
    except Exception as e:
        st.error(f"Erro ao gerar o plano ADAPTADO com a IA: {e}")
        return None

def callback_atualizar_feedback():
    if "widget_feedback_key" in st.session_state:
        st.session_state.feedback_do_aluno = st.session_state.widget_feedback_key

def exibir_plano_formatado(texto_do_plano, titulo_da_secao_principal):
    if texto_do_plano and texto_do_plano.strip():
        st.subheader(titulo_da_secao_principal)
        secoes_plano = texto_do_plano.strip().split("\n### ")
        introducao_do_plano = ""
        dias_do_plano_formatados = []

        if secoes_plano:
            if not texto_do_plano.strip().startswith("### ") and len(secoes_plano) > 0 and secoes_plano[0].strip():
                introducao_do_plano = secoes_plano[0]
                dias_do_plano_formatados = secoes_plano[1:]
            else:
                dias_do_plano_formatados = secoes_plano
            
            if introducao_do_plano:
                st.markdown(introducao_do_plano)
                st.divider()

            for i, bloco_dia_texto in enumerate(dias_do_plano_formatados):
                bloco_dia_limpo = bloco_dia_texto.strip()
                if not bloco_dia_limpo:
                    continue
                
                partes_do_dia = bloco_dia_limpo.split('\n', 1)
                titulo_dia = partes_do_dia[0].strip().replace("### ", "")
                
                conteudo_do_dia = partes_do_dia[1].strip() if len(partes_do_dia) > 1 else ""
                
                texto_markdown_para_dia = f"### {titulo_dia}\n{conteudo_do_dia}"
                
                expandir_este = (i == 0) 
                with st.expander(label=f"🗓️ {titulo_dia}", expanded=expandir_este):
                    st.markdown(texto_markdown_para_dia)
    elif texto_do_plano is not None: 
        st.warning("O plano recebido da IA está vazio ou não pôde ser formatado.")

# --- Inicialização do st.session_state ---
if 'plano_atual' not in st.session_state:
    st.session_state.plano_atual = None
if 'feedback_do_aluno' not in st.session_state:
    st.session_state.feedback_do_aluno = ""

# --- Interface Principal ---
st.title("Cronos - Seu Assistente Pessoal de Estudos para o ENEM")
st.image("https://i.imgur.com/4X9v1gM.png", width=300) 
st.write("""
Bem-vindo(a) ao seu assistente pessoal de estudos para o ENEM!
Vamos configurar seu plano de estudos personalizado.
""")

# --- Coleta de Informações do Aluno ---
st.header("Conte-me sobre Você e Seus Objetivos:")
meta_nota = st.number_input("Qual sua meta de nota para o ENEM? (Ex: 750)", min_value=300, max_value=1000, value=700, step=10)

st.subheader("Tempo Disponível para Estudo:")
dias_semana = st.slider("Quantos dias por semana você pode estudar?", min_value=1, max_value=7, value=5)
horas_dia_input = st.time_input("Em média, quantas horas por dia?", value=None)

st.subheader("Suas Matérias:")
todas_materias_enem = [
    "Linguagens, Códigos e suas Tecnologias", "Matemática e suas Tecnologias",
    "Ciências Humanas e suas Tecnologias (História, Geografia, Filosofia, Sociologia)",
    "Ciências da Natureza e suas Tecnologias (Química, Física, Biologia)", "Redação"
]
materias_dificuldade = st.multiselect("Quais matérias você sente MAIS dificuldade?", options=todas_materias_enem, key="ms_dificuldade")
materias_facilidade = st.multiselect("Quais matérias você sente MAIS facilidade ou já tem um bom conhecimento?", options=todas_materias_enem, key="ms_facilidade")

# --- Lógica do Botão para Gerar o Plano de Estudos Inicial ---
if st.button("Gerar Plano de Estudos com IA 🧠", key="botao_gerar_inicial"):
    if horas_dia_input:
        horas_dia_str = horas_dia_input.strftime('%H:%M')
        with st.spinner("O Cronos IA está montando seu plano inicial... Por favor, aguarde! 🧙‍♂️"):
            plano_gerado = gerar_plano_estudos_com_gemini( 
                meta_nota, dias_semana, horas_dia_str,
                materias_dificuldade, materias_facilidade
            )

        if plano_gerado:
            exibir_plano_formatado(plano_gerado, "🌟 Seu Plano de Estudos Personalizado (1ª Semana): 🌟")
            
            st.session_state.plano_atual = plano_gerado
            st.session_state.feedback_do_aluno = "" 
            # A tentativa de limpar st.session_state.widget_feedback_key = "" foi removida daqui
            st.success("Plano inicial gerado com sucesso!")
        else:
            st.error("Não foi possível gerar o plano inicial. Verifique as configurações e tente novamente.")
            st.session_state.plano_atual = None
    else:
        st.warning("Por favor, informe quantas horas por dia você pode estudar antes de gerar o plano.")

# --- Seção para Feedback e Adaptação do Plano ---
# As linhas de DEBUG foram removidas para a versão final.
# Elas podem ser adicionadas novamente se necessário para futuras investigações.

if st.session_state.get('plano_atual'): 
    st.divider() 
    st.subheader("📝 Como foi seu progresso com o plano acima?") 
    
    st.text_area(
        "Descreva o que você conseguiu estudar, onde teve dificuldades, ou se algo mudou no seu tempo disponível. Quanto mais detalhes, melhor a IA poderá te ajudar a adaptar!",
        value=st.session_state.feedback_do_aluno,
        height=150,
        key="widget_feedback_key",
        on_change=callback_atualizar_feedback
    )

    if st.button("Gerar Plano Adaptado para Próxima Semana 🚀", key="botao_adaptar"):
        if not st.session_state.get('feedback_do_aluno', '').strip():
            st.warning("Por favor, descreva seu progresso antes de gerar um plano adaptado.")
        else:
            metas_atuais = {
                'meta_nota': meta_nota, 
                'dias_semana': dias_semana,
                'horas_dia_str': horas_dia_input.strftime('%H:%M') if horas_dia_input else "Não informado",
                'materias_dificuldade': materias_dificuldade, 
                'materias_facilidade': materias_facilidade
            }
            plano_para_adaptar = st.session_state.plano_atual
            feedback_do_aluno_para_adaptar = st.session_state.feedback_do_aluno
            
            with st.spinner("O Cronos IA está ADAPTANDO seu plano... Isso pode levar um momento! 🧠✨"):
                novo_plano_adaptado = gerar_plano_adaptado_com_gemini(
                    metas_atuais, plano_para_adaptar, feedback_do_aluno_para_adaptar
                )

            if novo_plano_adaptado:
                exibir_plano_formatado(novo_plano_adaptado, "✨ Seu Novo Plano de Estudos ADAPTADO: ✨")
                
                st.session_state.plano_atual = novo_plano_adaptado
                st.session_state.feedback_do_aluno = "" 
                # A linha st.session_state.widget_feedback_key = "" foi REMOVIDA daqui.
                st.success("Seu plano foi adaptado com sucesso!")
                st.balloons()
            else:
                st.error("Não foi possível adaptar o plano. Tente novamente.")

# --- Informações na Barra Lateral ---
st.sidebar.info("Cronos ENEM - Protótipo v0.3")
