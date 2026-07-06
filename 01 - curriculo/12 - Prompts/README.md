# 🎯 Capítulo 12 — Criando Prompts Personalizados para Currículos

---

## 📌 Sumário

- [🎯 Capítulo 12 — Criando Prompts Personalizados para Currículos](#-capítulo-12--criando-prompts-personalizados-para-currículos)
  - [📌 Sumário](#-sumário)
  - [🎯 Objetivo deste Capítulo](#-objetivo-deste-capítulo)
  - [🧠 Por que prompts personalizados?](#-por-que-prompts-personalizados)
  - [🛠️ Estrutura de um prompt eficaz](#️-estrutura-de-um-prompt-eficaz)
  - [⚠️ Exemplos de prompts ruins (e por que falham)](#️-exemplos-de-prompts-ruins-e-por-que-falham)
  - [📝 Exemplo de prompt com contexto bem fornecido](#-exemplo-de-prompt-com-contexto-bem-fornecido)
  - [🎭 Adaptando o prompt para diferentes papéis e audiências](#-adaptando-o-prompt-para-diferentes-papéis-e-audiências)
  - [✍️ Como adaptar o texto ao seu estilo de escrita](#️-como-adaptar-o-texto-ao-seu-estilo-de-escrita)
    - [Passos práticos:](#passos-práticos)
  - [✅ O que manter, o que evitar e o que melhorar nos prompts](#-o-que-manter-o-que-evitar-e-o-que-melhorar-nos-prompts)
    - [✅ O que manter (essencial)](#-o-que-manter-essencial)
    - [❌ O que evitar](#-o-que-evitar)
    - [🔧 O que melhorar](#-o-que-melhorar)
  - [📊 Sistema de pontuação para avaliar seus prompts](#-sistema-de-pontuação-para-avaliar-seus-prompts)
    - [Como funciona:](#como-funciona)
    - [Exemplo de tabela de avaliação:](#exemplo-de-tabela-de-avaliação)
    - [Como usar:](#como-usar)
  - [🧪 Exercício prático: crie e avalie seu próprio prompt](#-exercício-prático-crie-e-avalie-seu-próprio-prompt)
  - [🔗 Próximo passo (Capítulo 13)](#-próximo-passo-capítulo-13)

---

## 🎯 Objetivo deste Capítulo

No capítulo anterior, você aprendeu a usar IA de forma consciente. Agora, vamos dominar a ferramenta mais importante para extrair o melhor da IA: o **prompt**.

Um prompt bem construído é a diferença entre uma resposta genérica e uma frase pronta para o currículo, que soa como você e atende ao que o mercado espera.

Neste capítulo, você aprenderá a:

- Estruturar prompts eficazes com contexto, exemplos e restrições.
- Identificar e corrigir prompts ruins.
- Adaptar o prompt para diferentes perfis de recrutador e papéis profissionais.
- Ajustar o resultado ao seu estilo de escrita e voz.
- Avaliar seus próprios prompts com um sistema de pontuação prático.

---

## 🧠 Por que prompts personalizados?

Um mesmo pedido, com prompts diferentes, gera resultados completamente distintos:

| **Prompt ruim** | **Resultado** |
|:---|:---|
| "Crie frases STAR para meu currículo." | "Gerenciei redes com eficiência e melhorei a conectividade." (genérico, sem contexto, inútil). |

| **Prompt bom** | **Resultado** |
|:---|:---|
| (com contexto, exemplo e restrições) | "Implementei a segmentação de VLANs para 5 novos departamentos, reduzindo a latência em 20%." (específico, com métrica e ação). |

**O prompt é a chave para transformar o que você sabe em uma frase que o recrutador valoriza.**

---

## 🛠️ Estrutura de um prompt eficaz

Um bom prompt deve conter:

1. **Contexto:** a situação, seu papel, o ambiente.
2. **Objetivo:** o que você quer que a IA faça (ex: gerar frases STAR, resumir, adaptar).
3. **Restrições:** o que evitar (ex: não use clichês, seja técnico, limite de linhas).
4. **Exemplo:** um modelo do que você considera uma boa resposta.
5. **Tom e estilo:** como você quer que soe (ex: formal, técnico, direto).

**Exemplo de estrutura:**
  
- **Contexto:** [descreva sua experiência de forma breve]
- **Objetivo:** [transforme isso em X frases STAR para meu currículo]
- **Restrições:** [evite clichês, use números, seja específico]
- **Exemplo:** [uma frase que você gostaria que fosse parecida]
- **Tom:** [direto, técnico, com verbos de ação]

---

## ⚠️ Exemplos de prompts ruins (e por que falham)

| **Prompt ruim**                    | **O que falta**                 | **Resultado típico**                  |
|:---                                |:---                             |:---                                   |
| "Crie frases STAR para redes."     | Contexto, exemplo, restrições.  | "Melhorei a rede da empresa."         |
| "Ajude a escrever meu currículo."  | Objetivo claro, especificidade. | "Sou proativo e aprendo rápido."      |
| "Gere frases para Analista de TI." | Sem dados reais, sem métricas.  | "Atendi usuários com eficiência."     |
| "Faça um resumo profissional."     | Sem quem sou, sem foco.         | "Profissional dedicado e experiente." |

**Por que falham:** falta de direção, ausência de contexto real, excesso de generalidade, nenhum exemplo de saída esperada.

---

## 📝 Exemplo de prompt com contexto bem fornecido

- **Contexto:** Trabalhei como analista de redes em uma empresa de médio porte com 15 switches e 200 usuários. Durante uma expansão, precisei reorganizar as VLANs para acomodar novos departamentos. O projeto exigiu análise de tráfego, planejamento de novos segmentos e implantação sem interrupção.
- **Objetivo:** Gere 3 frases STAR para meu currículo, cada uma com verbo de ação, desafio, ação e resultado (com métricas).
- **Restrições:** Evite clichês como "proativo" ou "melhorei". Use linguagem técnica mas compreensível. Não invente números.
- **Exemplo:** "Implementei a segmentação de VLANs para 5 departamentos, reduzindo a latência em 20%."
- **Tom:** Direto, profissional, com ênfase no impacto.

**Por que funciona:** contexto rico, objetivo claro, restrições específicas, exemplo de referência, tom definido.
  
---

## 🎭 Adaptando o prompt para diferentes papéis e audiências

Cada tipo de leitor valoriza aspectos diferentes. Adapte o prompt para priorizar o que mais interessa.

| **Papel / Audiência**             | **Foco do prompt**                            | **Exemplo de restrição/adicionar**                                  |
|:---                               |:---                                           |:---                                                                 |
| **Recrutador de RH (ATS)**        | Palavras‑chave, habilidades, certificações.   | "Use termos como VLAN, OSPF, Python, Git."                          |
| **Recrutador Técnico**            | Protocolos, arquiteturas, soluções, métricas. | "Detalhe a solução técnica, mencione protocolos, use números."      |
| **Gestor / Líder de equipe**      | Liderança, coordenação, tomada de decisão.    | "Destaque ações que demonstrem liderança e coordenação de equipes." |
| **Analista de TI (par)**          | Ferramentas, metodologias, troubleshooting.   | "Foque em ferramentas, scripts, diagnósticos e tempo de resposta."  |
| **Analista de Redes Sênior**      | Arquitetura, redundância, escalabilidade.     | "Use termos como BGP, STP, MPLS, SD‑WAN, redundância."              |
| **Recrutador de mercado global**  | Impacto em negócios, adaptabilidade cultural. | "Traduza o impacto em termos de negócio, mostre adaptabilidade."    |
| **Você mesmo (autoconhecimento)** | Sua voz, seu estilo, sua verdade.             | "Mantenha sua voz, evite palavras que você não usaria."             |

**Exemplo de prompt adaptado para Recrutador Técnico:**
  
- **Contexto:** [mesmo contexto anterior]
- **Objetivo:** Gere frases STAR com foco técnico, mencionando protocolos e soluções.
- **Restrições:** Use termos como VLAN, OSPF, EtherChannel. Inclua números.
- **Exemplo:** "Implementei VLANs e EtherChannel para 4 setores, eliminando loops e melhorando a redundância."
- **Tom:** Técnico, objetivo.


---

## ✍️ Como adaptar o texto ao seu estilo de escrita

A IA não conhece você. O texto gerado precisa ser ajustado para soar como se você tivesse escrito.

### Passos práticos:

1. **Leia em voz alta:** Se a frase não soa natural para você, mude.
2. **Troque palavras muito formais:** Substitua por expressões que você usa normalmente.
3. **Adicione detalhes reais:** Insira o nome do protocolo, o número de equipamentos, o problema específico.
4. **Corte adjetivos genéricos:** "excelente", "eficiente", "dedicado" – mostre, não fale.
5. **Simplifique frases longas:** Divida em duas ou três mais curtas.
6. **Use seu vocabulário:** Se você não usa "otimizei", não use. Use "melhorei", "ajustei", "configurei".

**Exemplo de adaptação:**

| **Gerado pela IA** | **Adaptado por você** |
|:---|:---|
| "Implementei a segmentação de VLANs, otimizando a performance da rede." | "Configurei VLANs para separar o tráfego entre departamentos, o que reduziu a lentidão que os usuários reclamavam." |
| "Desenvolvi um script em Python para automação de backups." | "Criei um script Python que faz o backup automático das configurações – agora qualquer colega pode usar." |

---

## ✅ O que manter, o que evitar e o que melhorar nos prompts

### ✅ O que manter (essencial)

- Contexto claro (seu papel, o ambiente).
- Objetivo específico (o que você quer que a IA faça).
- Restrições (o que evitar ou priorizar).
- Exemplo (uma frase que você gostaria de receber).
- Tom e estilo (formal, técnico, direto).

### ❌ O que evitar

- Prompts genéricos sem contexto ("faça um currículo").
- Pedidos vagos sem especificar o que você quer.
- Esquecer de dar um exemplo de saída esperada.
- Usar jargão sem necessidade (a IA pode se perder).
- Pedir para a IA "inventar" números ou fatos.

### 🔧 O que melhorar

- Adicione **quem você é**: cargo, anos de experiência, setor.
- Adicione **o que você fez**: descreva a ação, não só o cargo.
- Adicione **para quem**: era para um time, para clientes, para alunos?
- Adicione **resultados esperados**: redução de tempo, aumento de disponibilidade.
- Peça **variações**: "Me dê 3 versões diferentes da mesma frase."

---

## 📊 Sistema de pontuação para avaliar seus prompts

Você pode avaliar seus prompts com uma nota de 0 a 10 para cada um dos papéis que a IA deve assumir. Isso ajuda a identificar qual prompt funciona melhor para cada situação.

### Como funciona:

- Defina os papéis que você quer testar (ex: Recrutador Técnico, Gestor, Analista de Redes Sênior).
- Crie um prompt para cada papel.
- Peça para a IA gerar as frases.
- Avalie cada frase com uma nota de 0 a 10 com base em:
  - **Relevância:** atende ao que o papel valoriza?
  - **Especificidade:** é concreta, com detalhes?
  - **Impacto:** mostra resultado?
  - **Autenticidade:** parece com você?

### Exemplo de tabela de avaliação:

| **Papel**                | **Frase gerada**                                  | **Relevância** | **Especificidade** | **Impacto** | **Autenticidade** | **Nota final (0‑10)** |
|:---                      |:---                                                                                             |:---|:---|:---|:---|:---|
| Recrutador Técnico       | "Implementei OSPF em uma rede com 20 roteadores, reduzindo o tempo de convergência."            | 9 | 8 | 9 | 7 | 8,3 |
| Gestor                   | "Coordenei a migração de 5 switches, alinhando prazos com a equipe e garantindo zero downtime." | 10 | 9 | 10 | 8 | 9,3 |
| Analista de Redes Sênior | "Projetei uma topologia com BGP e MPLS para garantir redundância e escalabilidade."             | 10 | 10 | 9 | 7 | 9,0 |

### Como usar:

- A nota mais alta indica qual prompt gerou a melhor frase para aquele público.
- A partir daí, você pode refinar o prompt para melhorar as notas mais baixas.

---

## 🧪 Exercício prático: crie e avalie seu próprio prompt

1. Escolha uma experiência real (ex: trabalhou na universidade, em um escritório, ou um projeto pessoal).
2. Escreva um prompt seguindo a estrutura que aprendemos.
3. Adapte o prompt para 3 papéis diferentes (ex: RH, Técnico, Gestor).
4. Gere as frases usando a IA.
5. Avalie cada frase com notas de 0 a 10 usando a tabela acima.
6. Refine o prompt e repita.

**Dica:** Esse exercício vai te ajudar a entender como pequenas mudanças no prompt mudam completamente o resultado.

---

## 🔗 Próximo passo (Capítulo 13)

Agora que você já sabe criar prompts personalizados e avaliá-los para diferentes públicos, o **Capítulo 13** vai aplicar tudo isso ao contexto internacional: **inglês técnico para TI e adaptação de currículos para o mercado global**. Você aprenderá o vocabulário essencial, como descrever suas experiências em inglês e como ajustar seu currículo para oportunidades fora do Brasil, mantendo a autenticidade e o profissionalismo que já construímos.

---

*Última atualização: Julho de 2026*