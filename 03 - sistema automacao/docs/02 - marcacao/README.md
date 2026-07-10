# Módulo 02 – Marcação de Competências

## 📌 Visão Geral

Este módulo fornece uma interface interativa para que o usuário possa marcar quais competências do inventário ele possui e em que nível de proficiência (Básico, Intermediário, Avançado). Ele lê o arquivo `config/competencias.json`, pergunta sobre cada competência e gera/atualiza o arquivo `dados/meu_perfil.json`.

**O que ele faz:**

- Carrega a lista completa de competências (hard e soft) do inventário.
- Para cada competência, pergunta ao usuário se ele a possui e, em caso positivo, solicita o nível.
- Armazena as respostas em um arquivo estruturado, separando hard skills por domínio e soft skills por domínio.
- Remove competências que o usuário não possui (ou que foram desmarcadas).

---

## 📁 Onde os arquivos estão localizados

Todos os arquivos estão dentro da pasta `03 - sistema automacao/`.

```bash
03 - sistema automacao/
├── config/
│ └── competencias.json # Inventário de competências (fonte de verdade)
├── dados/
│ └── meu_perfil.json # Perfil do usuário (gerado/atualizado por este módulo)
├── src/
│ └── marcar_competencias.py # Script interativo de marcação
└── docs/
└── 02 - marcacao/
├── README.md # Este arquivo
└── LOGICA_PROGRAMACAO.md # Lógica detalhada do código
```


---

## 📂 Arquivos criados e seus conteúdos

### `dados/meu_perfil.json`

Este arquivo contém o perfil do usuário com todas as competências marcadas. Sua estrutura é:

```json
{
  "usuario": "Seu Nome",
  "hard_skills": {
    "Redes": {
      "vlan": "Avançado",
      "ospf": "Intermediário"
    },
    "Automação": {
      "python_netmiko": "Intermediário"
    }
  },
  "soft_skills": {
    "Comportamental": {
      "comunicacao": "Avançado"
    }
  }
}
```

- **usuario:** Nome do usuário.
- **hard_skills:** Dicionário onde as chaves são os domínios (ex: "Redes", "Automação") e os valores são dicionários com as competências e seus níveis.
- **soft_skills:** Estrutura análoga para as soft skills.

O arquivo é gerado ou atualizado pelo script marcar_competencias.py.

## src/marcar_competencias.py

Script responsável pela interação com o usuário. Ele:

- Carrega o inventário de competências.
- Carrega o perfil existente (se houver).
- Para cada competência, pergunta se o usuário a possui e, em caso afirmativo, o nível.
- Atualiza o perfil e salva as alterações.

## 🚀 Como executar

Abra um terminal na pasta 03 - sistema automacao/.

Execute:

```bash
python src/marcar_competencias.py
```

Siga as instruções interativas:

- Digite seu nome (se não estiver preenchido).
- Para cada competência, responda s (sim) ou n (não).
- Se responder s, escolha um dos níveis disponíveis (Básico, Intermediário, Avançado).
- Ao final, o arquivo dados/meu_perfil.json será criado ou atualizado.

Exemplo de saída:

```Markdown

=== Marcação de Competências ===

Digite seu nome: Alexandre

Você possui 'VLAN' (Redes)? Atual: Não marcado (s/n): s
Níveis disponíveis: Básico, Intermediário, Avançado. Digite um nível: Avançado
Você possui 'OSPF' (Redes)? Atual: Não marcado (s/n): s
Níveis disponíveis: Básico, Intermediário, Avançado. Digite um nível: Intermediário
...

✅ Perfil salvo com sucesso em: ...\dados\meu_perfil.json
Marcação concluída!
```

## 🔍 Lógica do script (resumo)

- **Carregamento dos dados** – O script carrega o inventário (competencias.json) e o perfil existente (meu_perfil.json), se houver.
- **Perguntas interativas** – Para cada competência, o script pergunta se o usuário a possui e, se sim, solicita o nível. O nível atual (se já marcado) é mostrado para referência.
- **Organização por domínio** – Hard skills são armazenadas em hard_skills agrupadas por domínio; soft skills em soft_skills, também agrupadas.
- **Limpeza automática** – Domínios que ficam vazios são removidos para manter o JSON limpo.
- **Salvamento** – O perfil atualizado é salvo no arquivo meu_perfil.json com formatação legível.

> 📘 Documentação complementar: Para uma explicação linha a linha da lógica de programação, incluindo justificativas para cada bloco de código e boas práticas adotadas, consulte o arquivo [logica_programacao.md](/03%20-%20sistema%20automacao/docs/02%20-%20marcacao/logica_programacao.md) disponível nesta mesma pasta.

## ✅ Status atual do módulo

- Script interativo funcional.
- Gera/atualiza o perfil do usuário com hard e soft skills.
- Interface simples baseada em terminal.
- Nenhuma dependência externa (apenas módulos nativos do Python).
- Próximo passo: integrar o perfil gerado com o sistema de extração de termos.