# 📈 Carreira & Mercado — Automação, Estratégia e Inteligência de Dados

Bem-vindo ao meu repositório de **Inteligência de Carreira e Automação de Processos**. 
Este espaço é um reflexo da minha transição estratégica da engenharia de redes para a **automação (NetDevOps)**, aplicando conceitos de programação, governança de dados e análise de métricas para otimizar a forma como profissionais se apresentam ao mercado.

---

## 📋 Índice

- [📈 Carreira \& Mercado — Automação, Estratégia e Inteligência de Dados](#-carreira--mercado--automação-estratégia-e-inteligência-de-dados)
  - [📋 Índice](#-índice)
  - [🎯 Propósito do Repositório](#-propósito-do-repositório)
  - [🚀 Produtos e Projetos do Portfólio](#-produtos-e-projetos-do-portfólio)
  - [⚙️ Padrões de Engenharia](#️-padrões-de-engenharia)
    - [Dicionário Semântico](#dicionário-semântico)
    - [Workflow de Commits Semânticos](#workflow-de-commits-semânticos)
    - [Versionamento Semântico (SemVer)](#versionamento-semântico-semver)
  - [🛠️ Ecossistema de Ferramentas](#️-ecossistema-de-ferramentas)
  - [🗺️ Roadmap de Desenvolvimento](#️-roadmap-de-desenvolvimento)
  - [💡 Guia de Navegação](#-guia-de-navegação)
  - [📚 Base de Conhecimento e Padrões](#-base-de-conhecimento-e-padrões)
  - [🔒 Conformidade e Governança de Dados (LGPD/PII)](#-conformidade-e-governança-de-dados-lgpdpii)
  - [✉️ Contato](#️-contato)

---

## 🎯 Propósito do Repositório

Este repositório serve como um **portfólio técnico e estratégico** que une **engenharia de software** à **gestão de carreira**. O objetivo é demonstrar como problemas cotidianos (como adaptar um currículo para uma vaga ou calcular o valor de mercado) podem ser resolvidos com automação, boas práticas de dados e programabilidade.

Aqui, você encontrará:

- **Teoria e Cartilhas:** Boas práticas para construção de currículos técnicos, anonimização de dados (LGPD) e métricas de ROI profissional.
- **Modelos e Templates:** Estruturas de currículo em Markdown para diferentes nichos (Redes, Automação, TI Geral).
- **Automação (Python):** Scripts que analisam descrições de vagas, escolhem o modelo ideal, preenchem com dados pessoais (JSON) e geram versões anônimas e diffs de validação.
- **Inteligência de Mercado:** Estudos sobre métricas (ROI, PME, PII), indicadores de desempenho e fontes de dados para tomada de decisão profissional.

---

## 🚀 Produtos e Projetos do Portfólio

Este repositório é dividido em módulos independentes, permitindo que o projeto cresça sem perder a organização:

| Pasta | Descrição | Status |
| :--- | :--- | :--- |
| **`01-curriculo-automation/`** | Cartilha de boas práticas, modelos de currículos e scripts de geração/análise. | ✅ Em andamento |
| **`02-valor-mercado/`** | Estudo teórico sobre métricas de mercado, ROI, PME, coleta de dados e governança. | 📖 Em estudo |
| **`docs/`** | Documentação de padrões e guias do repositório. | ✅ Ativo |

---

## ⚙️ Padrões de Engenharia

Para garantir um histórico limpo, rastreável e profissional, adoto as mesmas práticas do meu projeto de estudos Cisco:

### Dicionário Semântico

Utilizo o padrão **kebab-case** e prefixos funcionais para organizar arquivos e pastas, garantindo compatibilidade com ambientes Linux e scripts de automação. Para detalhes das normas, consulte o [Dicionário Semântico](./docs/dicionario_semantico.md).

### Workflow de Commits Semânticos

Adoto a convenção de **Commits Semânticos** para padronizar o histórico de alterações. Isso permite uma leitura clara da evolução do projeto e facilita a geração automática de logs. Veja o [Guia de Commits Profissionais](./docs/git_commit_guide.md).

### Versionamento Semântico (SemVer)

Este repositório segue o modelo `MAJOR.MINOR.PATCH` para controle de progresso.

- **MAJOR:** Lançamento de um novo "Produto" (ex: integração com Ollama).
- **MINOR:** Adição de novos modelos, scripts ou seções.
- **PATCH:** Correções de bugs, atualizações de documentação ou ajustes menores.

Todo o histórico é detalhado no [CHANGELOG.md](./CHANGELOG.md).

---

**Estrutura de Pastas (Arquitetura):**

```bash
./
├── 01-curriculo-automation/                # Módulo de Geração de Currículos
│   ├── modelos/                            # Templates Markdown (Redes, TI, Automação)
│   ├── scripts/                            # Scripts Python de geração e anonimização
│   └── README.md                           # README específico do módulo
├── 02-valor-mercado/                       # Módulo de Inteligência de Mercado
│   ├── metricas/                           # ROI, PME, PII, indicadores
│   ├── analises/                           # Estudos de caso e fontes de dados
│   └── README.md                           # README específico do módulo
├── docs/                                   # Documentação geral do repositório
│   ├── git_commit_guide.md
│   ├── dicionario_semantico.md
│   └── guia_versionamento.md
├── CHANGELOG.md                            # Histórico de versões
├── .gitignore                              # Arquivos e pastas ignorados pelo Git
└── README.md                               # Este arquivo: Visão geral do projeto
```

## 🛠️ Ecossistema de Ferramentas

- **Git & GitHub**: Para controle de versão e hospedagem do portfólio.
- **Python:** Linguagem principal para automação (Netmiko para redes, Pandas para análise, Regex para anonimização).
- **Markdown & YAML:** Para os modelos de currículo e arquivos de configuração.
- **Ollama (Futuro):** Para análise local e inteligente de descrições de vagas com LLMs, mantendo a privacidade dos dados.
- **VS Code:** Ambiente de desenvolvimento e edição de texto.

## 🗺️ Roadmap de Desenvolvimento

Minha jornada de construção deste projeto segue este cronograma:

- Definição da estrutura do repositório (Cópia do padrão Cisco).
- Criação da Cartilha Teórica (Guia de Boas Práticas de Currículo).
- Criação dos 4 modelos de currículo (Genérico, TI, Redes, Automação).
- Desenvolvimento do script de Seleção de Modelo (baseado em palavras-chave da vaga).
- Desenvolvimento do script de Preenchimento (Leitura de JSON + Template).
- Implementação do Módulo de Anonimização (Regex + placeholders).
- Implementação do Gerador de Diff (Validação de alterações).
- Integração com Ollama para análise de vagas com IA local.
- Criação do módulo de Valor de Mercado (Métricas e Dashboards).

## 💡 Guia de Navegação

Para explorar o conteúdo deste repositório:

- Visão Geral: Este README.md fornece a introdução e os padrões.
- Módulo de Currículos: Navegue até 01-curriculo-automation/ para ver os modelos e scripts.
- Módulo de Mercado: Navegue até 02-valor-mercado/ para os estudos de métricas e ROI.
- Histórico: Verifique o progresso detalhado no CHANGELOG.md.

## 📚 Base de Conhecimento e Padrões

A pasta docs/ centraliza guias e documentações detalhadas que regem a organização deste projeto:

- Guia de Commits Profissionais: Detalhes sobre a convenção de mensagens de commit adotada.
- Guia de Versionamento Semântico: Explicação de como o versionamento é aplicado.
- Dicionário Semântico: Definição de termos e padrões de nomenclatura.

## 🔒 Conformidade e Governança de Dados (LGPD/PII)

Este projeto lida com informações pessoais (PII). Por isso, todos os scripts de anonimização são prioridade, e o uso de modelos locais (Ollama) garante que nenhum dado sensível seja enviado para servidores externos. A transparência sobre o tratamento de dados é um pilar fundamental deste portfólio.

## ✉️ Contato

Conecte-se comigo para discutir redes, automação, estratégias de carreira ou este projeto:

- Nome: **Alexandre Lavorenti Cancilieri**
- LinkedIn: **alexandre-analista-de-ti**
- GitHub: **@alcancil**
