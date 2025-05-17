**Nome do Projeto:** 

Cronos ENEM

**Descrição:** 

Um assistente de estudos inteligente e adaptativo para candidatos do ENEM, utilizando a API Gemini do Google para criar e ajustar planos de estudo personalizados.

**Problema:** 

Muitos estudantes enfrentam dificuldades significativas com planejamento, gestão eficaz do tempo e acesso a ferramentas de estudo personalizadas para o ENEM. Este desafio é ainda maior para aqueles com menos condições financeiras, que muitas vezes não podem arcar com cursinhos ou plataformas pagas.

**Como Funciona:**

O usuário insere suas metas (nota desejada no ENEM), o tempo que tem disponível para estudo e as matérias em que sente maior dificuldade.
O sistema inteligente (utilizando a tecnologia Gemini do Google) cria um cronograma de estudos personalizado para a primeira semana. Este cronograma é organizado por dias e apresentado em seções expansíveis para facilitar a visualização.
Ao final de cada semana, o aluno fornece feedback sobre seu progresso e dificuldades através de uma caixa de texto.
O sistema inteligente utiliza esse feedback, juntamente com o plano da semana anterior, para gerar um novo plano de estudos adaptado e otimizado para a próxima semana, também exibido de forma organizada.
Este ciclo de feedback e adaptação contínua permite que o plano de estudos evolua com o aluno, acompanhando seu desenvolvimento e necessidades.

**Tecnologias Utilizadas:**

  * Python
  * Streamlit (para a interface web interativa)
  * API Google Gemini (para a inteligência artificial e geração de texto)

**Como Rodar Localmente:**

1.  Clone o repositório: `git clone https://github.com/astrobiodaniel/Cronos_ia_enem-app.git`
2.  Navegue até a pasta do projeto: `cd Cronos_ia_enem-app`
3.  Crie e ative um ambiente virtual (recomendado Python 3.8+):
      * Bash (macOS/Linux):
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
      * Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```
4.  Instale as dependências: `pip install -r requirements.txt`
5.  Configure sua chave de API do Gemini:
      * Crie um arquivo `.streamlit/secrets.toml` na raiz do projeto com o seguinte conteúdo:
        ```toml
        GEMINI_API_KEY = "SUA_CHAVE_API_REAL_AQUI"
        ```
      * Ou, para um teste rápido local, altere a linha `GOOGLE_API_KEY = ""` no arquivo `streamlit_app.py` para `GOOGLE_API_KEY = "SUA_CHAVE_API_REAL_AQUI"`. 
6.  Rode o aplicativo: `streamlit run streamlit_app.py`

**Diferencial e Impacto:**

O Cronos ENEM busca democratizar o acesso a um planejamento de estudos de alta qualidade e adaptativo. Ao utilizar inteligência artificial de ponta de forma gratuita, o projeto oferece uma ferramenta poderosa que, de outra forma, poderia ser cara ou inacessível para muitos estudantes, promovendo maior igualdade de oportunidades na preparação para o ENEM.

**Funcionalidades Futuras:**

  * **Módulo de Conteúdo do ENEM:** Inclusão de resumos e questões com acompanhamento de progresso por matéria.
  * **Simulados Semanais Adaptativos:** Geração de simulados com base no progresso do aluno, com feedback detalhado que será utilizado pela IA para refinar ainda mais os planos de estudo.
  * **Integrar o Crono ENEM diretamente com a API do Google Agenda para criar eventos automaticamente na agenda do usuário ou gerar um Arquivo .ics (iCalendar):

**Autor:** 
Daniel Valentim
