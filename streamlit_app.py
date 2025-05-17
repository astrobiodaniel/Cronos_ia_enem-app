import streamlit as st
import google.generativeai as genai
import os

# --- Configuração da API Key do Gemini ---
try:
    GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]
except (FileNotFoundError, KeyError):
    GOOGLE_API_KEY = "" # Sua Chave API

# Verificação da Chave API
api_key_valida = bool(GOOGLE_API_KEY and GOOGLE_API_KEY != "SUA_CHAVE_API_AQUI_PARA_TESTE_LOCAL")
if os.getenv("STREAMLIT_SERVER_RUNNING_ON_CLOUD") == "true" and GOOGLE_API_KEY == "AIzaSyACnFnEq6EGOhSrBtxOR2LiOC7RbeKoo1o":
    st.warning("Atenção: Usando chave API de fallback na nuvem. Verifique a configuração dos Secrets.")

if not api_key_valida:
    st.error("Chave de API do Gemini não configurada corretamente. Verifique o código ou os Secrets do Streamlit Cloud.")
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
        st.session_state.erro_na_geracao_inicial = f"Erro ao gerar o plano com a IA: {e}"
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
        st.session_state.erro_na_geracao_adaptado = f"Erro ao gerar o plano ADAPTADO com a IA: {e}"
        return None

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
if 'semanas_foco_concluidas' not in st.session_state:
    st.session_state.semanas_foco_concluidas = 0

VALOR_PADRAO_RADIO_CONCLUIU = "Sim, na maior parte!"
VALOR_PADRAO_MULTI_DIFICULDADE = []
VALOR_PADRAO_TEXT_OUTROS = ""

if 'radio_concluiu_tarefas' not in st.session_state:
    st.session_state.radio_concluiu_tarefas = VALOR_PADRAO_RADIO_CONCLUIU
if 'multi_materias_dificuldade' not in st.session_state:
    st.session_state.multi_materias_dificuldade = VALOR_PADRAO_MULTI_DIFICULDADE
if 'text_outros_comentarios' not in st.session_state:
    st.session_state.text_outros_comentarios = VALOR_PADRAO_TEXT_OUTROS

if 'status_geracao' not in st.session_state:
    st.session_state.status_geracao = None
if 'plano_para_exibir' not in st.session_state:
    st.session_state.plano_para_exibir = None
if 'erro_na_geracao_inicial' not in st.session_state:
    st.session_state.erro_na_geracao_inicial = None
if 'erro_na_geracao_adaptado' not in st.session_state:
    st.session_state.erro_na_geracao_adaptado = None
if 'resetar_feedback_agora' not in st.session_state:
    st.session_state.resetar_feedback_agora = False

# --- Lógica para resetar o feedback se o sinalizador estiver ativo ---
if st.session_state.resetar_feedback_agora:
    st.session_state.radio_concluiu_tarefas = VALOR_PADRAO_RADIO_CONCLUIU
    st.session_state.multi_materias_dificuldade = VALOR_PADRAO_MULTI_DIFICULDADE
    st.session_state.text_outros_comentarios = VALOR_PADRAO_TEXT_OUTROS
    st.session_state.resetar_feedback_agora = False

# --- Funções de Ação ---
def acao_gerar_plano_inicial(meta, dias, horas_str, dificuldades, facilidades):
    st.session_state.status_geracao = None
    st.session_state.plano_para_exibir = None
    st.session_state.erro_na_geracao_inicial = None

    plano_gerado = gerar_plano_estudos_com_gemini(meta, dias, horas_str, dificuldades, facilidades)
    if plano_gerado:
        st.session_state.plano_atual = plano_gerado
        st.session_state.plano_para_exibir = plano_gerado
        st.session_state.status_geracao = "inicial_sucesso"
        st.session_state.resetar_feedback_agora = True
    else:
        st.session_state.plano_atual = None
        st.session_state.status_geracao = "inicial_erro"

def acao_gerar_plano_adaptado(metas_cb, plano_anterior_cb, feedback_cb):
    st.session_state.status_geracao = None
    st.session_state.plano_para_exibir = None
    st.session_state.erro_na_geracao_adaptado = None

    novo_plano = gerar_plano_adaptado_com_gemini(metas_cb, plano_anterior_cb, feedback_cb)
    if novo_plano:
        st.session_state.plano_atual = novo_plano
        st.session_state.plano_para_exibir = novo_plano
        st.session_state.semanas_foco_concluidas += 1
        st.session_state.resetar_feedback_agora = True
        st.session_state.status_geracao = "adaptado_sucesso"
    else:
        st.session_state.status_geracao = "adaptado_erro"

# --- Interface Principal ---
st.set_page_config(page_title="Cronos ENEM", layout="wide")

st.image("https://i.imgur.com/Lm4TFfy.png", width=300) # Sua logomarca

st.title("Cronos - Seu Assistente Pessoal de Estudos para o ENEM")
st.write("""
Bem-vindo(a) ao seu assistente pessoal de estudos para o ENEM!
Vamos configurar seu plano de estudos personalizado.
""")

# --- Coleta de Informações do Aluno (usando st.form) ---
with st.form(key="form_infos_aluno"):
    st.header("Conte-me sobre Você e Seus Objetivos:")
    meta_nota_input = st.number_input("Qual sua meta de nota para o ENEM? (Ex: 750)", min_value=300, max_value=1000, value=700, step=10)
    dias_semana_input = st.slider("Quantos dias por semana você pode estudar?", min_value=1, max_value=7, value=5)
    horas_dia_widget = st.time_input("Em média, quantas horas por dia?", value=None)
    
    st.subheader("Suas Matérias:")
    todas_materias_enem = [
        "Linguagens, Códigos e suas Tecnologias", "Matemática e suas Tecnologias",
        "Ciências Humanas e suas Tecnologias (História, Geografia, Filosofia, Sociologia)",
        "Ciências da Natureza e suas Tecnologias (Química, Física, Biologia)", "Redação"
    ]
    materias_dificuldade_input = st.multiselect("Quais matérias você sente MAIS dificuldade (em geral)?", options=todas_materias_enem, key="ms_dificuldade_geral_key")
    materias_facilidade_input = st.multiselect("Quais matérias você sente MAIS facilidade ou já tem um bom conhecimento (em geral)?", options=todas_materias_enem, key="ms_facilidade_geral_key")
    
    submitted_form_infos = st.form_submit_button("Gerar Plano de Estudos com IA 🧠")

if submitted_form_infos:
    if horas_dia_widget:
        horas_dia_str_local = horas_dia_widget.strftime('%H:%M')
        acao_gerar_plano_inicial(
            meta_nota_input, dias_semana_input, horas_dia_str_local,
            materias_dificuldade_input, materias_facilidade_input
        )
        st.rerun() # SUBSTITUÍDO experimental_rerun por rerun
    else:
        st.warning("Por favor, informe quantas horas por dia você pode estudar antes de gerar o plano.")

# --- Exibir mensagens e planos após processamento ---
if st.session_state.status_geracao == "inicial_sucesso":
    exibir_plano_formatado(st.session_state.plano_para_exibir, "🌟 Seu Plano de Estudos Personalizado (1ª Semana): 🌟")
    st.success("Plano inicial gerado com sucesso!")
    st.session_state.status_geracao = None
elif st.session_state.status_geracao == "inicial_erro":
    erro_msg = st.session_state.get('erro_na_geracao_inicial', "Não foi possível gerar o plano inicial.")
    st.error(erro_msg)
    st.session_state.status_geracao = None
elif st.session_state.status_geracao == "adaptado_sucesso":
    if st.session_state.plano_para_exibir:
        exibir_plano_formatado(st.session_state.plano_para_exibir, "✨ Seu Novo Plano de Estudos ADAPTADO: ✨")
    st.success(f"Seu plano foi adaptado com sucesso! Mais uma semana de foco registrada! 🎉 ({st.session_state.semanas_foco_concluidas} total)")
    st.balloons()
    st.session_state.status_geracao = None
elif st.session_state.status_geracao == "adaptado_erro":
    erro_msg = st.session_state.get('erro_na_geracao_adaptado', "Não foi possível adaptar o plano.")
    st.error(erro_msg)
    st.session_state.status_geracao = None

# --- Seção para Feedback e Adaptação do Plano ---
if st.session_state.get('plano_atual'):
    st.divider()
    with st.form(key="form_feedback"):
        st.subheader("📝 Como foi seu progresso com o plano acima?")
        opcoes_concluiu = ["Sim, na maior parte!", "Consegui parcialmente", "Tive bastante dificuldade em seguir", "Não consegui seguir"]
        
        try:
            default_index_radio = opcoes_concluiu.index(st.session_state.radio_concluiu_tarefas)
        except ValueError:
            default_index_radio = 0 

        st.radio(
            "Você conseguiu seguir o plano de estudos desta semana?",
            options=opcoes_concluiu,
            index=default_index_radio,
            key="radio_concluiu_tarefas"
        )

        st.multiselect(
            "Em quais matérias você sentiu MAIS dificuldade esta semana? (Selecione quantas precisar)",
            options=todas_materias_enem,
            default=st.session_state.multi_materias_dificuldade,
            key="multi_materias_dificuldade"
        )

        st.text_area(
            "Algum outro comentário, observação ou algo que mudou no seu tempo e queira compartilhar? (Opcional)",
            value=st.session_state.text_outros_comentarios,
            height=100,
            key="text_outros_comentarios"
        )
        
        submitted_form_feedback = st.form_submit_button("Gerar Plano Adaptado para Próxima Semana 🚀")

    if submitted_form_feedback:
        feedback_formatado_para_ia = f"""
        Relatório de progresso da semana:
        - Conseguiu seguir o plano de estudos desta semana? {st.session_state.radio_concluiu_tarefas}
        - Matérias onde sentiu mais dificuldade esta semana: {', '.join(st.session_state.multi_materias_dificuldade) if st.session_state.multi_materias_dificuldade else 'Nenhuma específica relatada'}
        - Outros comentários do aluno: {st.session_state.text_outros_comentarios if st.session_state.text_outros_comentarios.strip() else 'Nenhum'}
        """
        metas_atuais_cb = {
            'meta_nota': meta_nota_input,
            'dias_semana': dias_semana_input,
            'horas_dia_str': horas_dia_widget.strftime('%H:%M') if horas_dia_widget else "Não informado",
            'materias_dificuldade': materias_dificuldade_input,
            'materias_facilidade': materias_facilidade_input
        }
        plano_anterior_cb = st.session_state.plano_atual
        
        acao_gerar_plano_adaptado(metas_atuais_cb, plano_anterior_cb, feedback_formatado_para_ia)
        st.rerun() # SUBSTITUÍDO experimental_rerun por rerun

# --- Barra Lateral com Conquistas e Informações ---
st.sidebar.title("🏆 Meu Mural de Conquistas 🏆")
estrelas = "✨" * st.session_state.semanas_foco_concluidas
if st.session_state.semanas_foco_concluidas > 0:
    st.sidebar.write(f"Semanas de Foco Concluídas: {st.session_state.semanas_foco_concluidas}")
    st.sidebar.markdown(f"<p style='font-size: 24px; text-align: center;'>{estrelas}</p>", unsafe_allow_html=True)
else:
    st.sidebar.write("Complete sua primeira semana adaptada para começar a colecionar estrelas! ⭐")
st.sidebar.divider()
versao_app = "v0.8" # Nova versão com correção do rerun
st.sidebar.info(f"Cronos ENEM - Protótipo {versao_app}")