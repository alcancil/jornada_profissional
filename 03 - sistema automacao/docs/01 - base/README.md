# Módulo 00 – Base e Validação de Dados

## 📌 Visão Geral

Este é o primeiro módulo do sistema de automação. Ele cria a base de dados de competências e configurações, além de validar a integridade desses arquivos antes de qualquer processamento.

**O que ele faz:**

- Carrega o inventário de competências (hard e soft) a partir de um arquivo JSON.
- Carrega as configurações gerais do sistema a partir de outro arquivo JSON.
- Valida a estrutura e os campos obrigatórios de ambos os arquivos.
- Exibe um resumo do que foi carregado, indicando que o sistema está pronto.

---

## 📁 Onde cada arquivo foi gravado (caminhos)

Todos os arquivos foram criados dentro da pasta `03 - sistema automacao/`.

```Markdown
03 - sistema automacao/
├── config/
│ ├── competencias.json # Lista de competências (hard e soft)
│ └── config.json # Configurações gerais
├── src/
│ └── carregar_competencias.py # Script responsável por carregar e validar
├── docs/ # (aqui você está lendo)
└── README.md # (será um índice, futuramente)
```

---


---

## 📂 Arquivos criados e seus conteúdos

### `config/competencias.json`

Este arquivo contém o **inventário de competências**. Cada competência possui os seguintes campos:

| Campo        | Descrição                                                                          | Exemplo                                     |
|:---          |:---                                                                                |:---                                         |
| `id`         | Identificador único (sem espaços)                                                  | `vlan`                                      |
| `nome`       | Nome legível para humanos                                                          | `VLAN`                                      |
| `dominio`    | Área técnica (Redes, Sistemas, Automação, etc.)                                    | `Redes`                                     |
| `tipo`       | `hard` ou `soft`                                                                   | `hard`                                      |
| `nivel`      | Nível de proficiência (Básico, Intermediário, Avançado)                            | `Avançado`                                  |
| `perfis`     | Lista de perfis de vaga que essa competência atende                                | `["NOC", "Enterprise"]`                     |
| `evidencias` | (opcional, para soft skills) Exemplos de comportamentos que comprovam a habilidade | `["Apresentei arquitetura para diretoria"]` |

**Exemplo de entrada:**

```json
{
  "id": "python_netmiko",
  "nome": "Python (Netmiko)",
  "dominio": "Automação",
  "tipo": "hard",
  "nivel": "Intermediário",
  "perfis": ["Automação", "DevNet", "Cloud"]
}
```

---

## `config/config.json`  

Este arquivo contém as configurações gerais do sistema:

| Campo    | Descrição                                     | Exemplo                                 |
| :---     | :---                                          | :---                                    |
| perfis   | Lista de perfis de vaga disponíveis           | ["NOC", "SOC", "ISP", ...]              |
| niveis   | Níveis de proficiência aceitos                | ["Básico", "Intermediário", "Avançado"] |
| caminhos | Diretórios onde estão modelos, saídas e dados | { "modelos": "../modelos/", ... }       |

## `src/carregar_competencias.py`  

Este é o script principal do módulo. Ele:

- Localiza os arquivos JSON (usando caminhos absolutos).
- Carrega e valida cada arquivo.
- Realiza uma validação cruzada entre os dois arquivos.
- Exibe um resumo do que foi carregado.

## 🚀 Como executar o script (passo a passo)

- Abra um terminal (PowerShell, CMD ou Git Bash).
- Navegue até a pasta 03 - sistema automacao/:

```bash
cd caminho/para/jornada_profissional/03\ -\ sistema\ automacao/
```

 Execute o comando:

```bash
python src/carregar_competencias.py
```

Se tudo estiver correto, você verá uma saída como esta:

```markdown

    [INFO] Iniciando carregamento do sistema...
    [INFO] Arquivo carregado: ...\config\competencias.json
    [INFO] Arquivo carregado: ...\config\config.json
    [INFO] Carregado com sucesso!
    [INFO] Total de competências: 20 (Hard: 15, Soft: 5)
    [INFO] Perfis disponíveis: ['NOC', 'SOC', 'ISP', 'Enterprise', 'Cloud', 'Automação', 'Infra']
    [INFO] Sistema pronto para os próximos módulos.
```

### 🔍 Lógica do script (explicação detalhada)

1. Definição dos caminhos absolutos

O script utiliza os.path.abspath(__file__) para descobrir sua própria localização. A partir disso, ele sobe um nível (os.path.dirname) para chegar na pasta raiz do módulo (03 - sistema automacao/). Isso garante que o script funcione independentemente do diretório de onde for executado.

2. Função carregar_json()

- Recebe o caminho de um arquivo JSON.
- Verifica se o arquivo existe com os.path.exists().
- Tenta abrir o arquivo com encoding='utf-8' e usar json.load() para convertê-lo em um dicionário Python.
- Se algo der errado (arquivo não encontrado, JSON malformado, etc.), exibe uma mensagem de erro e encerra o programa com sys.exit(1).

3. Função validar_competencias()

- Verifica se o JSON tem a chave competencias e se seu valor é uma lista.
- Para cada competência, valida:
  - Campos obrigatórios: id, nome, dominio, tipo, nivel, perfis.
  - Tipo: deve ser 'hard' ou 'soft'.
  - Conta quantos erros encontra. Se houver pelo menos um, retorna False.

4. Função validar_config()

- Verifica se o JSON tem os campos perfis, niveis, caminhos.
- Confirma que perfis e niveis são listas e caminhos é um dicionário.
- Se tudo estiver certo, retorna True.

5. Função main() (orquestradora)

- Carrega e valida competencias.json e config.json.
- Realiza uma validação cruzada: todos os níveis definidos em competencias.json devem estar presentes na lista niveis do config.json.
- Se a validação for bem-sucedida, exibe um resumo com:
  - Total de competências.
  - Quantidade de hard e soft skills.
  - Perfis disponíveis.
  - Mensagem de que o sistema está pronto.

6. Execução condicional (if __name__ == "__main__")

Essa linha garante que o script só execute a função main() quando for executado diretamente, e não se for importado por outro módulo.

>📘 **Documentação complementar:** Para uma explicação linha a linha da lógica de programação, incluindo justificativas para cada bloco de código e boas práticas adotadas, consulte o arquivo [LOGICA_PROGRAMACAO.md](LOGICA_PROGRAMACAO.md) disponível nesta mesma pasta.

### ✅ Status atual do módulo

- Arquivos JSON criados e preenchidos.
- Script de carregamento e validação funcionando.
- Nenhuma dependência externa necessária (apenas módulos nativos do Python).
- Sistema pronto para os próximos módulos.

### 🔜 Próximos passos (dentro da automação)

- **Módulo 1** – Extração de termos da vaga – ler um arquivo .txt com a descrição da vaga e extrair as competências relevantes.
- **Módulo 2** – Match e Ranqueamento – comparar as competências extraídas com o inventário e calcular uma nota de aderência.
- **Módulo 3** – Seleção do modelo e geração do currículo (com preenchimento e anonimização).
