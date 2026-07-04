# 🎯 Capítulo 5 — Inventário de Competências e Matriz de Mapeamento para Vagas

---

## 📌 Sumário

- [🎯 Capítulo 5 — Inventário de Competências e Matriz de Mapeamento para Vagas](#-capítulo-5--inventário-de-competências-e-matriz-de-mapeamento-para-vagas)
  - [📌 Sumário](#-sumário)
  - [🎯 Objetivo deste Capítulo](#-objetivo-deste-capítulo)
  - [🧠 O que é um Inventário de Competências?](#-o-que-é-um-inventário-de-competências)
    - [Diferença entre currículo e inventário](#diferença-entre-currículo-e-inventário)
  - [📂 Domínios de Competências em TI e Redes](#-domínios-de-competências-em-ti-e-redes)
  - [📝 Como preencher seu próprio inventário](#-como-preencher-seu-próprio-inventário)
    - [Exemplo de inventário preenchido (parcial)](#exemplo-de-inventário-preenchido-parcial)
  - [🗺️ Matriz de Mapeamento: Competência × Perfil de Vaga](#️-matriz-de-mapeamento-competência--perfil-de-vaga)
    - [Exemplo da matriz (recorte)](#exemplo-da-matriz-recorte)
  - [🔍 Como extrair competências de um plano de estudos (CCNA/CCNP)](#-como-extrair-competências-de-um-plano-de-estudos-ccnaccnp)
    - [Exemplo: do tópico STP para competências profissionais](#exemplo-do-tópico-stp-para-competências-profissionais)
    - [Exemplo: do tópico Python para competências profissionais](#exemplo-do-tópico-python-para-competências-profissionais)
  - [📝 Exercício Prático: Construa seu Inventário e Matriz](#-exercício-prático-construa-seu-inventário-e-matriz)
  - [✅ Checklist de Validação do Inventário](#-checklist-de-validação-do-inventário)
  - [🔗 Próximo passo (Capítulo 6)](#-próximo-passo-capítulo-6)

---

## 🎯 Objetivo deste Capítulo

Até aqui, você aprendeu a estruturar um currículo, contar histórias com método S.T.A.R., extrair métricas e encaixar realizações em modelos. Porém, **falta a peça fundamental**: saber exatamente **o que você sabe** e **para que serve**.

Este capítulo resolve isso. Você aprenderá a:

- Construir um **Inventário de Competências** organizado por domínios técnicos.
- Mapear cada competência para os **perfis de vaga** mais relevantes (NOC, ISP, SOC, Enterprise, Cloud, Automação, etc.).
- Extrair competências profissionais a partir de certificações e planos de estudo (CCNA, CCNP, Python, etc.).
- Criar sua própria matriz de mapeamento, que servirá como base para gerar currículos direcionados e, futuramente, automatizar a seleção de conteúdo.

---

## 🧠 O que é um Inventário de Competências?

Inventário de competências é um **registro estruturado** de tudo o que você sabe fazer, organizado de forma que possa ser consultado rapidamente. Ele não é um currículo; é uma **base de dados interna**.

### Diferença entre currículo e inventário

| **Currículo**                                  | **Inventário de Competências**              |
|:---                                            |:---                                         |
| É uma **saída** (um resumo para o recrutador). | É uma **entrada** (seu conhecimento bruto). |
| Tem limite de espaço (1–2 páginas).            | Pode ser extenso e detalhado.               |
| Focado na vaga específica.                     | Focado em tudo o que você sabe.             |
| Usa palavras‑chave da vaga.                    | Usa a terminologia técnica real.            |

O inventário é o seu **"armazém"**. O currículo é apenas a **"vitrine"** que você monta a partir dele.

---

## 📂 Domínios de Competências em TI e Redes

Para organizar seu inventário, divida seu conhecimento em domínios. Os principais para um profissional de redes e infraestrutura são:

| **Domínio**                         | **Exemplos de competências**                                                                                              |
|:---                                 |:---                                                                                                                       |
| **Redes (L2/L3)**                   | VLAN, Trunk, EtherChannel, STP/RSTP/MSTP, OSPF, BGP, EIGRP, MPLS, VXLAN, QoS, HSRP, VRRP, ACL, NAT, DHCP, DNS.            |
| **Sistemas e Infra**                | Windows Server, Linux (Ubuntu, Debian, CentOS), Active Directory, SMB, SSH, RDP, Backup, Virtualização (VMware, Hyper‑V). |
| **Automação e Programabilidade**    | Python (Netmiko, Nornir, pyATS), Ansible, Git, GitHub, JSON, YAML, XML, RESTCONF, NETCONF, Jinja2, Docker.                |
| **Monitoramento e Observabilidade** | Zabbix, Grafana, Graylog, Syslog, SNMP, NetFlow, Wazuh, Prometheus.                                                       |
| **Segurança**                       | Firewalls (Palo Alto, Fortinet, Cisco ASA), IPS/IDS, VPN, Zero Trust, ACLs, Wazuh, SIEM básico.                           |
| **Cloud e Virtualização**           | AWS (VPC, IAM, EC2), Azure, GCP, VMware, Hyper‑V.                                                                         |

**Dica:** Você pode incluir também **soft skills** (comunicação, liderança, resolução de problemas) em um domínio separado, se quiser.

---

## 📝 Como preencher seu próprio inventário

O inventário pode ser feito em uma planilha, uma tabela Markdown, ou até mesmo um arquivo YAML/JSON. O importante é manter a estrutura.

**Modelo de tabela para seu inventário:**

| **Competência**  | **Domínio** | **Nível**     | **Onde aprendi/usei**                | **Última vez que usei** |
| :---             | :---        |:---           |:---                                  | :---                    |
| BGP              | Redes       | Intermediário | CCNP ENCOR, laboratórios             | 2025                    |
| Python           | Automação   | Intermediário | Estudos autodidatas, scripts Netmiko | 2026                    |
| Active Directory | Sistemas    | Avançado      | Universidade, suporte de TI          | 2023                    |
| ...                            | ...           | ...                                  | ...                     |

### Exemplo de inventário preenchido (parcial)

| Competência      | Domínio       | Nível         | Onde aprendi/usei            | Última vez |
|:---              |:---           |:---           |:---                          |:---        |
| VLAN / Trunk     | Redes         | Avançado      | Laboratórios CCNA, CCNP      | 2026       |
| STP/RSTP/MSTP    | Redes         | Avançado      | Laboratórios CCNA, CCNP      | 2026       |
| OSPF             | Redes         | Intermediário | Laboratórios CCNP            | 2026       |
| Python (Netmiko) | Automação     | Intermediário | Estudos de automação, GitHub | 2026       |
| Git              | Automação     | Intermediário | GitHub, projetos pessoais    | 2026       |
| Linux (Debian)   | Sistemas      | Intermediário | Laboratórios, servidores     | 2025       |
| Zabbix           | Monitoramento | Básico        | Estudos, laboratórios        | 2025       |

---

## 🗺️ Matriz de Mapeamento: Competência × Perfil de Vaga

Depois de listar suas competências, o próximo passo é saber **onde elas são úteis**. Crie uma matriz onde as linhas são suas competências e as colunas são os perfis de vaga.

**Perfis de vaga comuns:**

- **NOC** (Centro de Operações de Rede) – foco em monitoramento, incidentes, disponibilidade.
- **SOC** (Centro de Operações de Segurança) – foco em análise de logs, incidentes de segurança.
- **ISP** (Provedor de Internet) – foco em BGP, roteamento, enlaces.
- **Enterprise** (Redes Corporativas) – foco em switching, STP, VLAN, QoS, infra geral.
- **Cloud** (AWS/Azure) – foco em VPC, IAM, redes em nuvem, automação.
- **Automação / NetDevOps** – foco em Python, Ansible, APIs, pipelines.
- **Infraestrutura** (Servidores e Sistemas) – foco em AD, Linux, backup, virtualização.

### Exemplo da matriz (recorte)

| **Competência**      | **NOC** | **SOC** | **ISP** | **Enterprise** | **Cloud** | **Automação** | **Infra** |
|:---                  |:---:    | :---:   | :---:   | :---:          | :---:     | :---:         | :---:     |
| **VLAN**             | ✔       |         | ✔      | ✔              | ✔        |               | ✔         |
| **STP**              | ✔       |         |        | ✔               |          |               | ✔         |
| **OSPF**             | ✔       |         | ✔      | ✔               | ✔       |               | ✔         |
| **BGP**              |         |         | ✔      | ✔               | ✔       |               |            |
| **Python**           |         | ✔       |        | ✔               | ✔       | ✔             | ✔         |
| **Ansible**          |         |         |        | ✔               | ✔       | ✔             |            |
| **Linux**            | ✔      | ✔       | ✔      | ✔              | ✔        | ✔             | ✔         |
| **Active Directory** |         |         |        |                 |          |                | ✔         |
| **Wazuh**            |         | ✔       |        |                 |          |                |           |
| **AWS VPC**          |         |         |         |                | ✔        | ✔              |           |

**Como usar essa matriz:**

- Quando você for candidatar a uma vaga, consulte a matriz para saber **quais competências destacar**.
- Se a vaga é para **NOC**, você vai colocar no currículo: VLAN, STP, OSPF, Linux, monitoramento.
- Se a vaga é para **Automação**, você vai colocar: Python, Ansible, Git, Cloud, RESTCONF.

---

## 🔍 Como extrair competências de um plano de estudos (CCNA/CCNP)

A conversa que você teve com a colega trouxe um insight importante: **um plano de estudos pode virar um inventário de competências profissionais**. A maioria dos engenheiros estuda tópicos e não percebe que aquilo são competências que podem ir para o currículo.

### Exemplo: do tópico STP para competências profissionais

Você estuda **STP** no CCNA/CCNP. O que isso significa em termos de competências?

| **Tópico estudado**     | **Competências profissionais adquiridas**                                              |
|:---                     |:---                                                                                    |
| STP clássico (802.1D)   | Entendimento de prevenção de loops, eleição de Root Bridge, custos, portas bloqueadas. |
| PVST+                   | Capacidade de fazer balanceamento de carga por VLAN.                                   |
| RSTP                    | Conhecimento de convergência rápida (substitui 50s por 2s).                            |
| MSTP                    | Habilidade de agrupar VLANs em instâncias, redução de CPU.                             |
| BPDU Guard / Root Guard | Capacidade de proteger a topologia contra ataques.                                     |
| UDLD                    | Diagnóstico de links unidirecionais.                                                   |
| EtherChannel            | Agregação de links e comportamento do STP em bundles.                                  |

**Resultado:** Você não aprendeu apenas "STP". Você aprendeu **troubleshooting L2, design de redundância, segurança de camada 2, escalabilidade e otimização de convergência**. Tudo isso pode ser escrito em frases de impacto.

### Exemplo: do tópico Python para competências profissionais

| **Tópico estudado**      | **Competências profissionais adquiridas**     |
|:---                      |:---                                           |
| Sintaxe básica de Python | Capacidade de ler e modificar scripts.        |
| Netmiko                  | Automação de acesso SSH a equipamentos Cisco. |
| Ansible                  | Orquestração de configurações em massa.       |
| RESTCONF / NETCONF       | Interação com dispositivos via APIs.          |
| Git / GitHub             | Controle de versão de scripts e colaboração.  |
| YAML / JSON              | Estruturação de dados para automação.         |

**Resultado:** Você não aprendeu apenas "Python". Você aprendeu **automação de redes, integração de sistemas, gestão de código e cultura DevOps**.

---

## 📝 Exercício Prático: Construa seu Inventário e Matriz

**Parte 1 – Seu inventário pessoal:**

1. Pegue uma folha ou um arquivo Markdown.
2. Liste **todas as competências** que você tem, mesmo que sejam apenas teóricas (ex: estudou, mas nunca usou em produção).
3. Organize por domínios.
4. Atribua um nível (Básico, Intermediário, Avançado).

**Parte 2 – Sua matriz de mapeamento:**

1. Escolha 5 perfis de vaga que te interessam (ex: NOC, Enterprise, Automação, Cloud, Segurança).
2. Para cada competência do seu inventário, marque quais perfis ela atende.
3. O resultado será um mapa visual que mostra **onde você é forte** e **para quais vagas você deve mirar**.

---

## ✅ Checklist de Validação do Inventário

- [ ] Todas as competências estão organizadas por domínio?  
- [ ] Cada competência tem um nível de conhecimento associado?  
- [ ] A matriz indica claramente quais competências são relevantes para cada perfil de vaga?  
- [ ] O inventário é sincero (não inclui coisas que você não sabe)?  
- [ ] O inventário pode ser expandido facilmente (novos estudos, novas certificações)?  

Se você respondeu **sim** a todas, seu inventário está pronto para ser usado como base para os próximos capítulos.

---

## 🔗 Próximo passo (Capítulo 6)

Agora que você já construiu seu **Inventário de Competências** e sua **Matriz de Mapeamento**, o próximo passo (Capítulo 6) vai explorar um tema que muitos profissionais negligenciam: a diferença entre **Hard Skills e Soft Skills**. Você aprenderá a identificar quais habilidades comportamentais são mais valorizadas em cada perfil de vaga (NOC, SOC, Enterprise, Automação, Cloud, etc.) e como descrevê-las de forma autêntica e impactante no currículo, sem cair em clichês. Esse capítulo será a ponte entre o inventário técnico e a comunicação profissional completa, preparando o terreno para a geração de currículos verdadeiramente direcionados.

---

*Última atualização: Julho de 2026*
