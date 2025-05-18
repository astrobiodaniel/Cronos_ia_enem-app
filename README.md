# Cronos ENEM: Inteligência Artificial a Favor do Seu Futuro

Olá! Sou Daniel Valentim, Biólogo e Mestre em Biodiversidade Tropical, também um entusiasta da tecnologia que acredita no poder da inovação para transformar vidas. Desenvolvi o **_Cronos ENEM_** com um propósito muito especial: tornar a preparação para o ENEM acessível para *todos*, especialmente para quem não tem condições de investir em cursinhos caros.

## A Luta da Preparação e Nosso Propósito Social

Sabemos que estudar para o ENEM é um grande desafio. É preciso ter disciplina, material de qualidade e um plano de estudos que realmente funcione. Infelizmente, o acesso a tudo isso muitas vezes depende de quanto se pode pagar. **Muitos talentos ficam para trás não por falta de capacidade, mas por falta de oportunidade e ferramentas adequadas.**

O **_Cronos ENEM_** nasceu para mudar essa realidade. Ele é mais que um app; é um projeto com **impacto social**, feito para ser seu *aliado gratuito* nessa jornada.

## Como o **_Cronos ENEM_** Trabalha por Você? 

Vídeo explicando
(https://youtu.be/nLzlqno4Tuc)
 

Nosso app utiliza o que há de mais moderno em inteligência artificial, a **API Gemini do Google**, para oferecer um suporte de estudo *verdadeiramente personalizado e adaptativo*.

* **Seu Plano, Sua Medida:** Em vez de seguir um modelo pronto, o **_Cronos ENEM_** conversa com você, entende sua rotina, suas facilidades e, principalmente, suas dificuldades em cada matéria. Com base nisso, ele cria um **cronograma de estudos único e flexível**, que se encaixa perfeitamente no seu dia a dia.
* **Adaptação em Tempo Real:** A vida acontece, e imprevistos surgem. Se você ficou doente, teve um dia puxado ou sentiu que precisa revisar mais um tópico, o **_Cronos ENEM_** *ajusta seu plano automaticamente*. Ele te ajuda a manter o foco sem se sentir sobrecarregado.
* **Identificação de Pontos Fracos:** Nossa IA vai te ajudar a perceber onde você precisa dedicar mais tempo e esforço, sugerindo revisões e materiais específicos para **superar suas dificuldades** e fortalecer seu aprendizado.
* **Democratizando o Acesso:** Acreditamos que a educação de qualidade deve ser para todos. O **_Cronos ENEM_** oferece uma ferramenta poderosa de planejamento e acompanhamento de estudos, que antes seria cara, **agora disponível gratuitamente**, quebrando barreiras financeiras na busca pelo seu sonho de entrar na universidade.

## O Significado por Trás do Nome

Escolhemos **_Cronos_** (o deus do tempo na mitologia) porque gerenciar o tempo é fundamental na preparação para o ENEM. Nosso app te dá o *controle* sobre seu tempo de estudo, transformando essa preocupação em uma **estratégia vencedora**.

## Tecnologia por Trás da Inovação Social

Para construir o **_Cronos ENEM_**, utilizamos a **API Gemini do Google**, que é o coração da nossa inteligência adaptativa. A interface amigável e acessível que você vê e usa foi desenvolvida com a agilidade do **Streamlit**.

## Como Começar a Usar (Simulando a Experiência)

1.  Visite a página do [\[[**_Cronos ENEM_** ](https://astrobiodaniel-cronos-ia-enem-app-streamlit-app-guobpe.streamlit.app/)\]]
2.  Na primeira vez, o app fará algumas perguntas para entender seu perfil de estudante e sua rotina.
3.  Pronto! Seu primeiro plano de estudos personalizado será gerado.
4.  Use o app diariamente para registrar seu progresso, dar feedback sobre as aulas e exercícios, e ver seu plano se ajustar para te ajudar cada vez mais.

## Nosso Compromisso com o Futuro

Este é apenas o começo. Queremos continuar aprimorando o **_Cronos ENEM_**, adicionando novas funcionalidades e conteúdos para que ele seja a *ferramenta mais completa e acessível* para sua preparação.

## Uma Iniciativa Nascida para Impactar

Este projeto é fruto da **Imersão IA 2025 da Alura**, com o inestimável apoio do Google. Ele representa minha paixão por usar a tecnologia para construir um futuro mais justo e com mais oportunidades para todos. É minha contribuição inicial para o desenvolvimento de soluções que fazem a diferença na vida das pessoas.

---

## Referência Científica

Hwang, G.-J., & Xie, H. (2021). Applications and Trends of Artificial Intelligence in Education: a Review of Recent Studies. *Interactive Learning Environments*, *29*(6), 689-703. doi:10.1080/10494820.2019.1625891

---
--------------------------------- Texto resumido -----------------------
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
