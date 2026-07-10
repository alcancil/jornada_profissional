# Lógica de Programação do Módulo de Marcação (`marcar_competencias.py`)

## 1. Importação de Módulos

```python
import json
import os
import sys
```

Por que esses módulos?

- **json:** para ler e escrever arquivos JSON.
- **os:** para manipular caminhos de diretórios de forma independente do sistema operacional.
- **sys:** para encerrar a execução com código de erro em caso de falhas.

## 2. Definição dos Caminhos Absolutos

```python

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
CAMINHO_COMPETENCIAS = os.path.join(BASE_DIR, 'config', 'competencias.json')
CAMINHO_PERFIL = os.path.join(BASE_DIR, 'dados', 'meu_perfil.json')

    os.path.abspath(__file__) retorna o caminho completo do script atual.

    os.path.dirname() sobe um nível na estrutura de pastas, garantindo que os caminhos sejam sempre relativos à raiz do módulo, independentemente de onde o script for executado.

    os.path.join() monta os caminhos de forma compatível com Windows/Linux.
```

## 3. Função carregar_json()

```python

def carregar_json(arquivo):
    if not os.path.exists(arquivo):
        print(f"ERRO: Arquivo não encontrado: {arquivo}")
        sys.exit(1)
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERRO: JSON inválido em {arquivo}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERRO: Falha ao ler {arquivo}: {e}")
        sys.exit(1)
```

Lógica:

- Verifica se o arquivo existe. Se não, exibe erro e para.
- Tenta abrir o arquivo com encoding='utf-8' para suportar caracteres acentuados.
- Converte o conteúdo JSON para um dicionário Python com json.load().
- Se houver erro de JSON malformado (json.JSONDecodeError), captura e exibe uma mensagem clara.
- Qualquer outro erro é capturado com Exception genérico para garantir que o programa não continue com dados corrompidos.

## 4. Função salvar_json()

```python

def salvar_json(arquivo, dados):
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Perfil salvo com sucesso em: {arquivo}")
    except Exception as e:
        print(f"ERRO: Falha ao salvar {arquivo}: {e}")
        sys.exit(1)

Por que indent=2 e ensure_ascii=False?

    indent=2: formata o JSON com indentação de 2 espaços, tornando-o legível para humanos.

    ensure_ascii=False: permite que caracteres acentuados (como "Básico", "Intermediário") sejam salvos como texto normal, sem escapes como \u00E1.
```

## 5. Função carregar_perfil_existente()

```python

def carregar_perfil_existente():
    if os.path.exists(CAMINHO_PERFIL):
        return carregar_json(CAMINHO_PERFIL)
    else:
        return {
            "usuario": "",
            "hard_skills": {},
            "soft_skills": {}
        }

    Se o arquivo de perfil já existir, ele é carregado.

    Caso contrário, retorna um dicionário vazio com a estrutura correta, evitando que o script quebre ao tentar acessar chaves que não existem.
```

## 6. Função obter_nivel()

```python

def obter_nivel(niveis_permitidos):
    while True:
        nivel = input(f"Níveis disponíveis: {', '.join(niveis_permitidos)}. Digite um nível: ").strip()
        if nivel in niveis_permitidos:
            return nivel
        print(f"Nível inválido. Use um dos seguintes: {', '.join(niveis_permitidos)}.")

    Loop infinito até que o usuário forneça um nível válido.

    join() exibe os níveis separados por vírgula para melhor legibilidade.

    strip() remove espaços extras digitados pelo usuário.
```

## 7. Função main() (Orquestradora)

```python

def main():
    print("\n=== Marcação de Competências ===\n")
    competencias_data = carregar_json(CAMINHO_COMPETENCIAS)
    lista_competencias = competencias_data['competencias']
    perfil = carregar_perfil_existente()

    if not perfil.get('usuario'):
        perfil['usuario'] = input("Digite seu nome: ").strip()
        print()

    if 'hard_skills' not in perfil:
        perfil['hard_skills'] = {}
    if 'soft_skills' not in perfil:
        perfil['soft_skills'] = {}

    niveis_permitidos = ['Básico', 'Intermediário', 'Avançado']

    for competencia in lista_competencias:
        id_comp = competencia['id']
        nome = competencia['nome']
        dominio = competencia.get('dominio', 'Geral')
        tipo = competencia.get('tipo', 'hard')

        if tipo == 'hard':
            if dominio not in perfil['hard_skills']:
                perfil['hard_skills'][dominio] = {}
            local = perfil['hard_skills'][dominio]
        else:
            if dominio not in perfil['soft_skills']:
                perfil['soft_skills'][dominio] = {}
            local = perfil['soft_skills'][dominio]

        nivel_atual = local.get(id_comp, 'Não marcado')
        resposta = input(f"Você possui '{nome}' ({dominio})? Atual: {nivel_atual} (s/n): ").strip().lower()
        if resposta == 's':
            nivel = obter_nivel(niveis_permitidos)
            local[id_comp] = nivel
        else:
            if id_comp in local:
                del local[id_comp]

    for secao in ['hard_skills', 'soft_skills']:
        for dom in list(perfil[secao].keys()):
            if not perfil[secao][dom]:
                del perfil[secao][dom]

    salvar_json(CAMINHO_PERFIL, perfil)
    print("Marcação concluída!")
```

Explicação passo a passo:

- **Cabeçalho** – Exibe um título para orientar o usuário.
- **Carregamento** – Carrega o inventário e o perfil existente.
- **Nome do usuário** – Se não estiver definido, pergunta e salva.
- **Inicialização de estruturas** – Garante que as chaves hard_skills e soft_skills existam no perfil, mesmo que vazias.
- **Definição dos níveis** – Define os níveis aceitos. Futuramente poderia vir do config.json.
- **Loop sobre competências** – Para cada competência:
  - Determina onde armazenar (hard ou soft e domínio).
  - Pergunta se o usuário possui e, se sim, solicita o nível.
  - Remove a competência se o usuário responder não.
- Limpeza de domínios vazios – Remove domínios que ficaram sem competências.
- Salvamento – Salva o perfil atualizado e informa o usuário.

## 8. Execução Condicional

```python

if __name__ == "__main__":
    main()
```

Garante que o script só execute quando chamado diretamente, e não se for importado por outro módulo. Isso permite reutilizar as funções em outros scripts sem executar acidentalmente a interação.

## 9. Boas Práticas Utilizadas

| **Prática**             | **Por que foi aplicada**                                                              |
| :--                     | :--                                                                                   |
| Caminhos absolutos      | O script funciona independentemente do diretório de execução.                         |
| Tratamento de erros     | try/except captura erros de arquivo e JSON, exibindo mensagens claras.                |
| Validação de entrada    | A função obter_nivel() só aceita valores válidos, evitando dados inconsistentes.      |
| Estrutura modular       | Cada função tem uma responsabilidade única, facilitando testes e manutenção.          |
| Formatação JSON legível | indent=2 e ensure_ascii=False tornam o arquivo de perfil amigável para edição manual. |
