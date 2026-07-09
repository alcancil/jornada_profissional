# Changelog

Todos os marcos notáveis deste projeto serão documentados neste arquivo. O formato é baseado no [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/) e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.19.0] - 2026-07-09

### Added

- **Módulo de Automação (Base e Validação):** Criação da estrutura inicial do sistema de automação na pasta `03 - sistema automacao/` com os seguintes arquivos:

  - `config/competencias.json`: Inventário de competências (hard e soft) com campos de identificação, domínio, nível e perfis de vaga.
  - `config/config.json`: Configurações gerais (perfis, níveis, caminhos) para o sistema.
  - `src/carregar_competencias.py`: Script em Python para carregar e validar os arquivos JSON e realizar a validação cruzada entre eles.

- **Documentação do Módulo de Automação:** Criação da documentação do primeiro módulo na pasta `docs/01 - base/`:

  - `README.md`: Visão geral, estrutura de pastas, arquivos criados, como executar e lógica resumida do script.
  - `LOGICA_PROGRAMACAO.md`: Explicação linha a linha da lógica de programação, justificativas para cada bloco e boas práticas adotadas.

### Changed

- N/A

### Impact

- Estabelece a base técnica e documental do sistema de automação, permitindo que os próximos módulos (extração, match, ranqueamento, geração) sejam construídos sobre uma fundação validada e bem documentada.
- A documentação criada garante que o sistema seja compreensível e reproduzível, tanto para o autor quanto para futuros usuários ou colaboradores.

## [1.18.0] - 2026-07-09

### Added

- **Módulo de Currículo (Teoria - Capítulo 17):** Adição do guia "Fechamento da Jornada Teórica e Caminho para a Automação" na pasta `01 - curriculo/01 - Teoria/17 - fechamento/`.
  - Realiza uma síntese de todos os capítulos anteriores.
  - Apresenta a transição da teoria para a prática.
  - Mapeia como os conceitos aprendidos serão aplicados na automação.

- **Estrutura do Projeto:** Definição dos 3 pilares do framework:
  - `01 - curriculo/` → Teoria e boas práticas para construção de currículos.
  - `02 - valor de mercado/` → Estudos sobre métricas, indicadores (ROI, KPI, etc.) e linguagem de mercado.
  - `03 - automacao/` → Sistema de automação de currículos com Python, integração com Ollama e dashboard de análise.

- **Módulo de Automação:** Criação da estrutura inicial da pasta `03 - automacao/` com:
  - Subpastas organizadas para scripts, modelos, dados e dashboard.
  - README.md específico para guiar a instalação e execução da ferramenta.
  - Preparação para futura implementação do gerador de currículos e sistema de ranqueamento.

### Changed

- **Estrutura do repositório:** O projeto agora está organizado de forma modular, permitindo crescimento independente de cada área.

### Impact

- Consolida a parte teórica do projeto e inaugura a fase prática.
- Cria uma base sólida para o desenvolvimento da automação, com separação clara entre conhecimento, métricas e implementação.

## [1.17.0] - 2026-07-07

### Added

- **Módulo de Currículo (Teoria - Capítulo 16):** Adição do guia "Como Escrever uma Carta de Apresentação (Cover Letter) Eficaz" na pasta `16 - cover-letter`.
  - Explica a importância da carta de apresentação como complemento ao currículo.
  - Apresenta a estrutura básica (cabeçalho, saudação, corpo, fechamento).
  - Fornece exemplos práticos em português e inglês.
  - Ensina a adaptar a carta para diferentes perfis de vaga e culturas.
  - Inclui um checklist de validação e comparação com o currículo.
  - Ajusta o gancho final para direcionar ao Capítulo 17 (visão geral da automação).

### Changed

- N/A

### Impact

- Capacita o leitor a escrever cartas de apresentação personalizadas e profissionais, tanto para o mercado nacional quanto internacional.
- Prepara o terreno para o último capítulo teórico, que fará a ponte para a automação.

## [1.16.0] - 2026-07-07

### Added

- **Módulo de Currículo (Teoria - Capítulo 15):** Adição do guia "Como Narrar uma Transição de Carreira de Forma Convincente" na pasta `15 - transicao-carreira`.
  - Apresenta o método dos 3 Pilares (ponto de partida, virada e chegada) para estruturar a narrativa.
  - Ensina a escrever sobre transição no currículo (resumo, experiências e projetos).
  - Oferece estratégias para responder a perguntas sobre transição em entrevistas.
  - Inclui exercício prático para construir sua própria narrativa.
  - Ajusta o gancho final para direcionar ao Capítulo 16 (carta de apresentação).

### Changed

- N/A

### Impact

- Capacita o leitor a comunicar mudanças de carreira de forma estratégica, transformando a transição em um ponto forte.
- Prepara o terreno para o próximo capítulo sobre cover letters.

## [1.15.0] - 2026-07-07

### Added

- **Módulo de Currículo (Teoria - Capítulo 14):** Adição do guia "Como Lidar com Lacunas no Currículo (Gaps)" na pasta `14 - gaps`.
  - Explica os diferentes tipos de lacunas (estudos, cuidados familiares, saúde, transição, freelance).
  - Apresenta estratégias para abordar cada tipo de gap no currículo e na entrevista.
  - Oferece exemplos práticos de frases para currículo e respostas para entrevistas.
  - Inclui exercício para transformar o próprio gap em uma narrativa positiva.
  - Ajusta o gancho final para redirecionar o próximo passo (Capítulo 15) ao tema "Transição de carreira (de TI geral para redes/automação)".

### Changed

- N/A

### Impact

- Capacita o leitor a lidar com períodos sem emprego formal de forma honesta, estratégica e profissional.
- Prepara o terreno para o Capítulo 15, que abordará como narrar transições de carreira.

## [1.14.0] - 2026-07-07

### Added

- **Módulo de Currículo (Teoria - Capítulo 13):** Adição do guia "Inglês Técnico para TI e Adaptação para o Mercado Global" na pasta `01 - curriculo/01 - Teoria/13 - ingles-tecnico/`.
  - Apresenta vocabulário essencial de redes, infraestrutura, automação e segurança em inglês.
  - Ensina a escrever realizações STAR em inglês, com exemplos práticos.
  - Compara as diferenças entre currículos brasileiros e internacionais (EUA, Reino Unido, Europa).
  - Orienta sobre adaptação para diferentes mercados e como usar IA como assistente.
  - Inclui checklist de validação para currículos em inglês.
  - Ajusta o gancho final para redirecionar o próximo passo (Capítulo 14) ao tema "Como lidar com lacunas no currículo (gaps)".

### Changed

- **Capítulo 13:** Ajuste do gancho final para redirecionar o próximo passo (Capítulo 14) ao tema "Como lidar com lacunas no currículo (gaps)", em vez de automação com Python.

### Impact

- Prepara o terreno para o Capítulo 14, que abordará a gestão de lacunas e transições de carreira antes de avançar para a automação.

## [1.13.0] - 2026-07-05

### Added

- **Módulo de Currículo (Teoria - Capítulo 12):** Adição do guia "Criando Prompts Personalizados para Currículos" na pasta `01 - curriculo/01 - Teoria/12 - prompts-personalizados/`.
  - Ensina a estruturar prompts eficazes com contexto, objetivo, restrições, exemplos e tom.
  - Apresenta exemplos de prompts ruins e por que falham.
  - Demonstra como adaptar prompts para diferentes papéis e audiências (RH, recrutador técnico, gestor, analista sênior, etc.).
  - Oferece técnicas para adaptar o texto gerado ao seu próprio estilo de escrita.
  - Lista o que manter, evitar e melhorar nos prompts.
  - Inclui um sistema de pontuação (0 a 10) para avaliar prompts por papel, com tabela prática.
  - Fornece um exercício para o leitor criar e avaliar seus próprios prompts.
  - Ajusta o gancho final para direcionar ao Capítulo 13 (inglês técnico e mercado global).

### Changed

- N/A

### Impact

- Capacita o leitor a dominar a arte de criar prompts personalizados, garantindo respostas mais relevantes e autênticas.
- Prepara o terreno para o próximo capítulo, sobre inglês técnico e adaptação internacional.

## [1.12.0] - 2026-07-05

### Added

- **Módulo de Currículo (Teoria - Capítulo 11):** Adição do guia "Uso Consciente de IAs na Redação de Currículos" na pasta `01 - curriculo/01 - Teoria/11 - uso-consciente-ia/`.
  - Explica os benefícios e riscos do uso de IA na redação de currículos.
  - Ensina a criar prompts eficazes para gerar frases STAR personalizadas.
  - Apresenta um fluxo de trabalho: esboço → prompt → geração → revisão → adaptação.
  - Fornece exemplos práticos de prompts bons e ruins, com análise do resultado.
  - Lista as armadilhas comuns e um checklist de validação pós‑IA.
  - Ajusta o gancho final para direcionar ao Capítulo 12 (prompts personalizados e estilo).

### Changed

- N/A

### Impact

- Capacita o leitor a utilizar IA como assistente estratégico, não como substituto.
- Prepara o terreno para o próximo capítulo sobre prompts personalizados e adaptação ao estilo de escrita.

## [1.11.0] - 2026-07-05

### Changed

- **Capítulo 10:** Ajuste do gancho final para redirecionar o próximo passo (Capítulo 11) ao tema "Uso consciente de IAs na redação de currículos", em vez de organização de repositório.

### Impact

- Realinha o fluxo do projeto para incluir um capítulo dedicado ao uso estratégico de IAs (como ChatGPT) na construção de currículos, com ênfase em revisão humana e autenticidade.

## [1.10.0] - 2026-07-05

### Added

- **Módulo de Currículo (Teoria - Capítulo 10):** Adição do guia "Exemplos Práticos de Currículos Anonimizados" na pasta `01 - curriculo/01 - Teoria/10 - exemplos-anonimizados/`.
  - Apresenta três currículos completos (Analista de TI, Analista de Redes, Automação/NetDevOps) com suas respectivas versões anônimas.
  - Para cada exemplo, mostra uma tabela comparativa do que foi removido, substituído e mantido.
  - Inclui uma análise geral das anonimizações e lições aprendidas.
  - Ajusta o gancho final para apontar para o Capítulo 11 (gerenciamento de repositório e documentação do processo).

### Changed

- N/A

### Impact

- Consolida o conhecimento prático de anonimização com exemplos reais e comparativos.
- Prepara o terreno para o Capítulo 11, que organizará o repositório e documentará o processo de forma estruturada.

## [1.9.0] - 2026-07-05

### Added

- **Módulo de Currículo (Teoria - Capítulo 9):** Adição do guia "Anonimização de Currículos: Proteção de Dados e Conformidade com LGPD" na pasta `01 - curriculo/01 - Teoria/09 - anonimizacao/`.
  - Explica os motivos legais e práticos para anonimizar currículos (LGPD, PII, redução de viés, segurança digital).
  - Define quando anonimizar (recrutador, plataformas, LLMs, ambientes públicos).
  - Apresenta tabela clara do que remover/substituir e o que manter.
  - Ensina o processo manual passo a passo, com exemplos práticos de antes e depois.
  - Orienta sobre como armazenar versões anônimas e proteger dados pessoais.
  - Inclui checklist de validação para garantir a anonimização completa.
  - Ajusta o gancho final para direcionar ao Capítulo 10 (exemplos de currículos anonimizados).

### Changed

- N/A

### Impact

- Estabelece a base de privacidade e conformidade legal para todos os currículos gerados no projeto.
- Prepara o terreno para o Capítulo 10, que apresentará exemplos práticos de anonimização aplicada a diferentes perfis.

## [1.8.1] - 2026-07-04

### Added

- **Capítulo 8:** Adição de uma seção "Versão em PDF do Modelo" com um link para download do currículo exemplo em PDF, facilitando a visualização do resultado final.

### Changed

- N/A

### Impact

- Melhora a experiência do leitor, oferecendo o currículo exemplo em um formato pronto para uso imediato.

## [1.8.0] - 2026-07-04

### Added

- **Módulo de Currículo (Teoria - Capítulo 8):** Adição do guia "Preenchendo um Modelo de Currículo: Da Teoria à Prática" na pasta `08 - Estrutura`.
  - Apresenta um passo a passo prático para preencher o modelo de Analista de Redes, integrando todos os conceitos dos capítulos anteriores.
  - Inclui seções sobre:
    - Escolha do modelo certo com base na matriz de mapeamento.
    - Ordem recomendada dos campos e suas justificativas.
    - Uso de foto (apenas se solicitado).
    - Idiomas (quando e como incluir).
    - Tamanho do currículo (1 página vs 2 páginas, e como encurtar).
    - Ícones (recomendação para evitar em currículos para ATS).
  - Fornece um exemplo completo de currículo em Markdown, com métricas estimadas, STAR, soft skills e idiomas.
  - Ajusta o gancho final para redirecionar o próximo passo (Capítulo 9) para o tema "Anonimização de Dados (LGPD/PII)".

### Changed

- N/A

### Impact

- Completa a parte prática do projeto, mostrando como aplicar todo o conhecimento teórico na construção de um currículo real.
- Prepara o terreno para o Capítulo 9, que abordará a anonimização de currículos para conformidade com LGPD e proteção de PII.

## [1.7.0] - 2026-07-04

### Added

- **Módulo de Currículo (Teoria - Capítulo 7):** Adição do guia "Soft Skills Observáveis: Como Demonstrar Seu Valor Comportamental com Evidências" na pasta `07 - soft skills observaveis`.
  - Apresenta o conceito de soft skills como comportamentos observáveis, não adjetivos.
  - Fornece uma tabela de mapeamento entre soft skills, comportamentos observáveis e frases de currículo.
  - Ensina a transformar comportamentos em evidências concretas.
  - Demonstra como laboratórios de rede e projetos pessoais evidenciam múltiplas soft skills.
  - Inclui exercício prático para o leitor mapear suas próprias evidências.

### Changed

- **Capítulo 6:** Ajuste do gancho final para redirecionar o próximo passo ao Capítulo 7, em vez de "montagem de currículo direcionado".

### Impact

- Completa a base teórica sobre competências, abrangendo hard skills, soft skills e sua demonstração prática por meio de comportamentos observáveis.
- Prepara o terreno para o Capítulo 8, onde todos os conceitos serão integrados para a geração de currículos direcionados.

## [1.6.1] - 2026-07-04

### Changed

- **Capítulo 6:** Ajuste do gancho final para redirecionar o próximo passo (Capítulo 7) ao tema "Soft Skills Observáveis", em vez de "montar currículo direcionado".

### Impact

- Realinha o fluxo do projeto para incluir um capítulo dedicado a soft skills observáveis, complementando o conteúdo sobre hard skills.

## [1.5.0] - 2026-07-03

### Added

- **Módulo de Currículo (Teoria - Capítulo 6):** Adição do guia "Hard Skills vs Soft Skills: Como Descrever Seu Valor Comportamental" na pasta `06 - skills`.
  - Explica a diferença entre hard skills e soft skills com exemplos práticos.
  - Apresenta uma tabela de mapeamento de soft skills mais valorizadas por perfil de vaga (NOC, SOC, ISP, Enterprise, Cloud, Automação, Infra).
  - Ensina como descrever soft skills no currículo sem usar clichês, transformando frases genéricas em evidências concretas.
  - Inclui exercício prático para o leitor transformar seus próprios clichês em frases de impacto.
  - Fornece um checklist de validação para garantir que as soft skills escolhidas sejam autênticas e defensáveis.

### Changed

- N/A

### Impact

- Completa a base teórica do projeto, cobrindo tanto competências técnicas quanto comportamentais.
- Prepara o terreno para o Capítulo 7, onde o inventário e as soft skills serão integrados para gerar currículos direcionados.

## [1.4.0] - 2026-07-03

### Added

- **Módulo de Currículo (Teoria - Capítulo 5):** Adição do guia "Inventário de Competências e Matriz de Mapeamento para Vagas" na pasta `05 - Matriz de Competencias`.
  - Ensina a construir um inventário organizado por domínios técnicos (Redes, Sistemas, Automação, Monitoramento, Segurança, Cloud).
  - Apresenta uma matriz de mapeamento entre competências e perfis de vaga (NOC, SOC, ISP, Enterprise, Cloud, Automação, Infra).
  - Demonstra como extrair competências profissionais a partir de planos de estudo (CCNA/CCNP).
  - Inclui exercício prático para o leitor construir seu próprio inventário e matriz.
  - Ajusta o gancho final para redirecionar o próximo passo (Capítulo 6) ao tema "Hard Skills vs Soft Skills".

### Changed

- N/A

### Impact

- Consolida a transição entre o mapeamento técnico e a comunicação profissional.
- Prepara o terreno para o Capítulo 6, que abordará soft skills e diferenciais comportamentais.
- Mantém o repositório alinhado com o novo fluxo estratégico definido pelo usuário.

## [1.3.0] - 2026-07-03

### Added

- **Módulo de Currículo (Teoria - Capítulo 4):** Adição do guia: "Encaixando Realizações nos Modelos de Currículo" na pasta `04 - realizacoes`
  - Apresenta as diferenças de ênfase entre os modelos Genérico, Analista de TI, Analista de Redes e Automação.
  - Fornece exemplos práticos de como adaptar a mesma realização para cada modelo.
  - Inclui um exercício prático para o leitor adaptar suas próprias experiências aos 4 modelos.
  - Disponibiliza um checklist de validação para garantir que a realização esteja adequada ao modelo escolhido.
  - Atualiza o gancho final para redirecionar o próximo passo (Capítulo 5) para a construção de um Inventário de Competências.

### Change

- N/A

### Impact

- Consolida a transição entre a teoria de realizações (Capítulos 2 e 3) e a aplicação prática nos modelos de currículo.
- Prepara o terreno para o Capítulo 5, que abordará o inventário de competências e o mapeamento para perfis de vaga (NOC, ISP, SOC, etc.).

## [1.2.0] - 2026-07-03

### Added

- **Módulo de Currículo (Teoria - Capítulo 3):** Adição do guia "Como Extrair Métricas e Realizações da Experiência Passada" na pasta `03 - metricas`.
  - Aborda técnicas de inferência baseada no porte da empresa para estimar números sem relatórios oficiais.
  - Ensina a comparar experiências com padrões de mercado (SLA, disponibilidade, tempo de resposta).
  - Apresenta métodos para traduzir observações cotidianas em frases de impacto.
  - Inclui exercício prático de "Antes e Depois" para transformar tarefas em realizações.
  - Fornece um checklist de validação para garantir que as estimativas sejam honestas e defensáveis.

### Changed

- N/A

### Impact

- Expande a base teórica do projeto, resolvendo o maior gargalo dos profissionais de TI: a falta de métricas documentadas.
- Prepara o terreno para o próximo capítulo, onde essas métricas serão aplicadas nos modelos de currículo.

## [1.1.0] - 2026-07-03

### Added

- **Módulo de Currículo (Teoria - Capítulo 2):** Adição do guia "Storytelling Técnico e Descrição de Realizações" na pasta `02 - storytelling`.
  - Aborda a importância do storytelling e do método S.T.A.R. para construção de realizações impactantes.
  - Inclui exemplos práticos de transformação de tarefas em realizações, mesmo sem métricas exatas.
  - Apresenta técnicas para estimar e inferir métricas usando o porte da empresa e observações cotidianas.
  - Prepara o terreno para a automação futura, ensinando como extrair valor da experiência passada.

### Changed

- N/A

### Impact

- Expande a base teórica do projeto, fornecendo ferramentas práticas para que profissionais de TI possam construir currículos mais assertivos.
- Cria uma ponte entre a teoria geral e a aplicação prática nos modelos de currículo (próximo capítulo).

## [1.0.0] - 2026-07-01

### Added

- **Módulo de Currículo (Teoria - Capítulo 1):** Adição do guia "Currículo Profissional para TI e Redes — Guia Prático" na pasta `01 - curriculo`.
  - Apresenta o objetivo do guia: fornecer um roteiro prático para construção de currículos eficazes para profissionais de TI, com ênfase em redes, infraestrutura e automação.
  - Explica por que criar currículos direcionados é crucial, abordando filtros ATS, recorte por vaga, tempo de leitura do recrutador e a necessidade de adaptação.
  - Detalha estratégias práticas: estrutura recomendada (cabeçalho, resumo, competências, experiência, certificações, formação, projetos), dicas de redação com verbos de ação e resultados, e adaptação para vagas específicas.
  - Inclui um checklist completo com seções obrigatórias e opcionais, além do que NÃO deve constar no currículo.
  - Apresenta exemplos de currículos antigos (a evitar) e modernos (a fazer), incluindo modelos orientados a resultados para Analista de Redes e para Automação/NetDevOps.
  - Finaliza com reflexões e lições aprendidas sobre a construção de um currículo profissional.

### Changed

- N/A

### Impact

- Estabelece a base teórica fundamental para o projeto, introduzindo os conceitos essenciais para a elaboração de currículos direcionados.
- Prepara o terreno para os capítulos subsequentes, que aprofundarão em storytelling, métricas, inventário de competências e automação.
- Posiciona o repositório como uma referência prática e estruturada para profissionais de TI que desejam melhorar sua apresentação no mercado.

## [1.0.1] - 2026-07-01

### Added

- **Documentação de Governança:** Adição dos guias de padronização do repositório na pasta `docs/`:
  - `dicionario_semantico.md`: Padrões de nomenclatura de pastas e arquivos (kebab-case, snake_case).
  - `guia_versionamento.md`: Regras para versionamento semântico (SemVer) aplicadas ao projeto.
  - `git_commit_guide.md`: Guia de commits profissionais com tipos, escopos e exemplos práticos.
- **README:** Atualização da seção "Base de Conhecimento" com links ativos para os novos documentos.

### Changed

- N/A

### Impact

- Estabelece a governança completa do repositório, garantindo escalabilidade e profissionalismo na gestão do projeto.

## [1.0.0] - 2026-07-01

### Added

- **Estrutura Inicial do Repositório:** Criação da estrutura de pastas modular para organizar a jornada profissional.
  - Definição dos diretórios raiz: `01 - curriculo/` e `02 - valor de mercado/`.
- **Documentação Geral:** Criação do `README.md` raiz para apresentar o escopo do projeto, seus padrões de governança e guia de navegação.
- **Módulo de Currículo (Parte Teórica):** 
  - Criação da subestrutura `01 - curriculo/01 - Teoria/`.
  - Adição do guia "Currículo Profissional para TI e Redes — Guia Prático", contendo fundamentos, estratégias e boas práticas para elaboração de currículos direcionados.
- **Preparação para Modelos:** Criação da pasta `01 - curriculo/modelos/` para armazenar futuramente os templates de currículo em Markdown.
- **Versionamento:** Criação do arquivo `CHANGELOG.md` para registro do progresso, adotando o padrão Keep a Changelog e SemVer.

### Impact

- Estabelece a base física e documental do projeto como um portfólio profissional.
- Define a estrutura de pastas que permite crescimento futuro (novos módulos) sem desorganização.
- Posiciona o projeto dentro dos mesmos padrões de engenharia e governança já utilizados nos estudos de certificação Cisco, demonstrando consistência metodológica.
  