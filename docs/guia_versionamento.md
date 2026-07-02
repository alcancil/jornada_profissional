# 📌 Guia de Versionamento Semântico

Este projeto utiliza [Versionamento Semântico](https://semver.org/lang/pt-BR/) (SemVer).

---

## 🎯 Formato da Versão

```text
MAJOR.MINOR.PATCH
↑ ↑ ↑
1 2 3
```

### **MAJOR** (primeiro número)

Incrementa quando ocorre uma **mudança estrutural incompatível** no repositório — algo que reorganiza completamente a forma como os dados ou o código são estruturados.

**Exemplos neste repositório:**

- 🏆 Lançamento da primeira versão funcional e estável do sistema (v1.0.0).
- 💥 Reestruturação completa do formato do JSON de dados dos currículos (quebra compatibilidade).
- 🔄 Mudança radical na arquitetura dos scripts de automação.

```bash
0.5.0 → 1.0.0  # Primeiro release estável do gerador de currículos
1.0.0 → 2.0.0  # Migração para novo sistema de templates (ex: Jinja2 para um motor diferente)
```

### **MINOR** (segundo número)

Incrementa quando um novo bloco de conteúdo ou funcionalidade é adicionado, mantendo compatibilidade com o que já existe.

**Exemplos neste repositório:**

- ✨ Adição de um novo módulo (ex: 03-dashboards ou 04-analise-llm).
- 🐍 Implementação de uma nova funcionalidade no script (ex: integração com Ollama).
- 📂 Criação de um novo modelo de currículo (ex: modelo-cybersecurity).
- 📊 Adição de um novo estudo de métricas no módulo de Valor de Mercado.

```bash
1.0.0 → 1.1.0  # Adiciona o módulo 03-dashboards
1.1.0 → 1.2.0  # Implementa a integração com Ollama local
```

### **PATCH** (terceiro número)

Incrementa quando há correções, ajustes ou adições pontuais que não representam a conclusão de um bloco completo.
  
**Exemplos neste repositório:**

- 🐛 Correção de link quebrado, typo ou bug em script.
- 📝 Atualização de documentação (README, CHANGELOG).
- 🔧 Ajuste de formatação ou padronização de nomes de arquivos.
- 📋 Pequena alteração em um modelo de currículo sem mudar sua estrutura.

```bash
1.0.0 → 1.0.1  # Corrige um bug no script de anonimização
1.0.1 → 1.0.2  # Atualiza o README com instruções de instalação
```

### 🚦 Regras de Decisão

```text

┌─────────────────────────────────────────────────────┐
│ Lançamento da primeira versão estável OU mudança    │
│ estrutural que quebra compatibilidade com dados?    │
└─────────────────────────┬───────────────────────────┘
                          │
                 ┌────────┴────────┐
                 │      SIM        │ → MAJOR++
                 └─────────────────┘
                          │
                 ┌────────┴────────┐
                 │      NÃO        │
                 └────────┬────────┘
                          │
┌─────────────────────────┴──────────────────────────┐
│ Adicionei um novo módulo, funcionalidade            │
│ ou um novo modelo de currículo?                     │
└─────────────────────────┬──────────────────────────┘
                          │
                 ┌────────┴────────┐
                 │      SIM        │ → MINOR++
                 └─────────────────┘
                          │
                 ┌────────┴────────┐
                 │      NÃO        │
                 └────────┬────────┘
                          │
┌─────────────────────────┴──────────────────────────┐
│ É uma correção, ajuste pontual ou documentação?     │
└─────────────────────────┬──────────────────────────┘
                          │
                 ┌────────┴────────┐
                 │      SIM        │ → PATCH++
                 └─────────────────┘
```

### 🏷️ Como Criar Tags no Git

1. Faça commit das mudanças

```bash
git add .
git commit -m "feat: adiciona módulo de dashboards com grafana"
```

2. Crie uma tag anotada  

```bash
git tag -a v1.1.0 -m "v1.1.0 - Módulo de dashboards adicionado"
```

3. Envie com as tags

```bash
git push origin main
git push origin v1.1.0
```

4. Veja todas as tags

```bash
git tag -l
```

5. Veja detalhes de uma tag

```bash
git show v1.1.0
```

### 📝 Padrão de Mensagens de Commit

Formato

```text
tipo(escopo): descrição curta

- Detalhe da mudança 1
- Detalhe da mudança 2

Refs: #issue
```

### Tipos e impacto na versão

| **Tipo**                 | **Quando usar**                               | **Impacto no SemVer**     |
| :---                     | :---                                          | :---                      |
| feat                     | Nova funcionalidade / novo módulo             | Incrementa MINOR          |
| fix                      | Correção de bug, link ou typo                 | Incrementa PATCH          |
| docs                     | Apenas documentação (README, CHANGELOG)       | Sem incremento            |
| style                    | Formatação, kebab-case, padronização          | Sem incremento            |
| refactor                 | Refatoração de script sem mudar comportamento | Sem incremento            |
| chore                    | Manutenção, .gitignore, dependências          | Sem incremento            |
| feat! ou BREAKING CHANGE | Mudança estrutural que quebra compatibilidade | Incrementa MAJOR          |
  
### Exemplos práticos

```bash

# PATCH — corrigiu um link no README
git commit -m "fix(docs): correct broken link to installation guide"

# PATCH — adicionou um modelo isolado
git commit -m "feat(curriculo): add cybersecurity model template"

# MINOR — adicionou um novo módulo
git commit -m "feat(mercado): add module 03-dashboards for KPI visualisation"

# MINOR — nova funcionalidade no script
git commit -m "feat(automation): add Ollama integration for job analysis"

# MAJOR — primeira versão estável
git commit -m "feat!: first stable release of CV generator

BREAKING CHANGE: System now uses JSON schema v2.0. All previous JSON files must be migrated.
Bump to v1.0.0."
```

### ✅ Checklist antes de Incrementar Versão

- Conteúdo testado e funcionando (scripts, modelos).
- Documentação atualizada (README, CHANGELOG).
- Commit com mensagem semântica descritiva.
- Tag criada no formato vX.Y.Z.
- Push da tag para o repositório remoto.

### 📌 Resumo Rápido

| **Mudança**                           | **Versão** | **Exemplo de commit**                            |
| :---                                  | :---       | :---                                             |
| 🐛 Correção / ajuste pontual          | X.Y.Z      | fix: corrige bug na anonimização → tag v1.0.1    |
| ✨ Novo módulo / funcionalidade       | X.Y.0      | feat: adiciona módulo 03-dashboards → tag v1.1.0 |
| 🏆 Primeira versão estável / breaking | X.0.0      | feat!: primeira versão funcional → tag v1.0.0    |
| 📝 Docs apenas                        |  —         | docs: ... (sem tag necessária)                   |

**Regra de Ouro:** Na dúvida durante a fase de desenvolvimento (0.x.x), use MINOR para entregas significativas e PATCH para correções pontuais.

### 🔗 Referências

- [Versionamento Semântico 2.0.0](https://semver.org/lang/pt-BR/)
  
- [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)
  
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/)

Última atualização: Julho de 2026
