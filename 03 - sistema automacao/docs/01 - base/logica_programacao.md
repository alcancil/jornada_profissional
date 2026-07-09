
# Lógica de Programação do Módulo de Base (carregar_competencias.py)

## 1. Importação de Módulos

```python
import json          # Para ler e escrever arquivos JSON
import os            # Para manipular caminhos de diretórios
import sys           # Para encerrar o programa com erro
import logging       # Para exibir mensagens de status e erro
```

**Por que esses módulos?**

- **json:** é a forma mais direta de transformar texto estruturado em dicionários Python.
- **os:** usado para construir caminhos absolutos, independente do sistema operacional.
- **sys:** necessário para parar a execução se algo falhar.
- **logging:** mais profissional que print(), porque permite níveis de severidade (INFO, ERROR) e facilita futura expansão.

## 2. Configuração do Logging

```python
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
```

O que faz:

- Define que todas as mensagens de nível INFO ou superior serão exibidas no terminal, com um formato limpo ([INFO] Mensagem). Isso ajuda a saber o que está acontecendo sem precisar ler o código.

## 3. Definição dos Caminhos Absolutos

```python
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
CAMINHO_COMPETENCIAS = os.path.join(BASE_DIR, 'config', 'competencias.json')
CAMINHO_CONFIG = os.path.join(BASE_DIR, 'config', 'config.json')
```

**Lógica:**

- **os.path.abspath(__file__)** retorna o caminho completo do próprio script.
- **os.path.dirname()** sobe um nível na árvore de diretórios.

> Isso garante que, não importa onde o script seja executado, ele sempre encontrará os arquivos JSON na pasta config/ ao lado da pasta src/. Sem isso, se você rodar o script de outro diretório, ele não acharia os arquivos.

## 4. Função carregar_json()

```python

def carregar_json(arquivo):
    if not os.path.exists(arquivo):
        logging.error(f"Arquivo não encontrado: {arquivo}")
        sys.exit(1)
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        logging.info(f"Arquivo carregado: {arquivo}")
        return dados
    except json.JSONDecodeError as e:
        logging.error(f"Erro ao decodificar JSON: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        sys.exit(1)
```

Por que assim:

- Verificação de existência: evita que o programa tente abrir um arquivo que não existe.
- **try/except:** captura erros de leitura ou JSON malformado, exibe uma mensagem clara e encerra o programa com sys.exit(1) (código de erro). Isso impede que o sistema continue com dados corrompidos.
- **encoding='utf-8':** garante que acentos e caracteres especiais sejam lidos corretamente (importante para competências em português).
- **json.load():** converte o conteúdo do JSON diretamente para um dicionário Python, pronto para uso.

## 5. Função validar_competencias()

```python

def validar_competencias(competencias):
    if 'competencias' not in competencias:
        logging.error("Chave 'competencias' ausente.")
        return False
    lista = competencias['competencias']
    if not isinstance(lista, list):
        logging.error("'competencias' não é uma lista.")
        return False

    campos_obrigatorios = {'id', 'nome', 'dominio', 'tipo', 'nivel', 'perfis'}
    erros = 0
    for idx, item in enumerate(lista):
        if not isinstance(item, dict):
            logging.error(f"Item {idx} não é um dicionário.")
            erros += 1
            continue

        faltando = campos_obrigatorios - set(item.keys())
        if faltando:
            logging.error(f"Competência {idx} faltando: {faltando}")
            erros += 1

        tipo = item.get('tipo')
        if tipo not in ['hard', 'soft']:
            logging.error(f"Competência {idx} com tipo inválido: {tipo}")
            erros += 1

    return erros == 0
```

Lógica de validação:

- Primeiro verifica se a estrutura raiz está correta.
- Depois percorre a lista de competências e confirma que cada uma tem todos os campos obrigatórios.
- Também verifica se o campo tipo é 'hard' ou 'soft', porque esses são os únicos aceitos.
- Acumula erros em vez de parar no primeiro erro, para que o usuário possa corrigir tudo de uma vez.
- Retorna True se nenhum erro foi encontrado.

## 6. Função validar_config()

```python

def validar_config(config):
    campos_obrigatorios = {'perfis', 'niveis', 'caminhos'}
    faltando = campos_obrigatorios - set(config.keys())
    if faltando:
        logging.error(f"Configuração faltando: {faltando}")
        return False
    if not isinstance(config['perfis'], list):
        logging.error("'perfis' não é lista.")
        return False
    if not isinstance(config['niveis'], list):
        logging.error("'niveis' não é lista.")
        return False
    if not isinstance(config['caminhos'], dict):
        logging.error("'caminhos' não é dicionário.")
        return False
    return True
```

Lógica:

- Os campos perfis, niveis e caminhos são obrigatórios para que o sistema funcione.
- Eles devem ter os tipos esperados (lista, lista, dicionário) para que o resto do código não quebre quando acessá-los.

## 7. Função main() (Orquestradora)

```python

def main():
    comp_data = carregar_json(CAMINHO_COMPETENCIAS)
    if not validar_competencias(comp_data):
        sys.exit(1)

    config_data = carregar_json(CAMINHO_CONFIG)
    if not validar_config(config_data):
        sys.exit(1)

    niveis_permitidos = set(config_data['niveis'])
    for item in comp_data['competencias']:
        nivel = item.get('nivel')
        if nivel not in niveis_permitidos:
            logging.error(f"Nível '{nivel}' não permitido.")
            sys.exit(1)

    total = len(comp_data['competencias'])
    hard = sum(1 for c in comp_data['competencias'] if c.get('tipo') == 'hard')
    soft = sum(1 for c in comp_data['competencias'] if c.get('tipo') == 'soft')
    logging.info(f"Carregado: {total} competências (Hard: {hard}, Soft: {soft})")
    logging.info(f"Perfis: {config_data['perfis']}")
    logging.info("Sistema pronto.")
```

Lógica de orquestração:

- Carrega e valida as competências. Se falhar, para.
- Carrega e valida a configuração. Se falhar, para.
- Validação cruzada: todos os níveis definidos nas competências devem estar na lista de níveis do config.json. Isso evita que, por exemplo, uma competência tenha nível "Expert" enquanto o sistema só aceita "Básico", "Intermediário", "Avançado".

Se tudo passar, exibe um resumo e termina com sucesso.

## 8. Execução Condicional (if __name__ == "__main__")

```python

if __name__ == "__main__":
    main()
```

**Por que isso é necessário?**  

Em Python, __name__ é uma variável especial. Quando o script é executado diretamente (via terminal), seu valor é "__main__". Quando o script é importado por outro arquivo (import carregar_competencias), o valor é o nome do módulo. Com essa condição, garantimos que main() só rode se o script for executado diretamente. Isso permite que futuramente você reutilize as funções de validação em outros scripts sem que o programa comece a rodar automaticamente.

## 9. Boas Práticas Utilizadas

| **Prática**                    | **Por que foi aplicada**                                                                                                         |
| :---                           | :---                                                                                                                             |
| Caminhos absolutos             | Garante que o script funcione independentemente do diretório de execução.                                                        |
| Validação de entrada           | Impede que dados corrompidos causem erros imprevisíveis mais adiante.                                                            |
| Tratamento de erros explícito  | Usa try/except e sys.exit() para falhar de forma controlada, exibindo mensagens claras.                                          |
| Logging em vez de print        | Permite expandir o sistema sem precisar reescrever as mensagens.                                                                 |
| Separação de responsabilidades | Cada função tem uma tarefa única (carregar, validar competências, validar config), o que facilita testes e modificações futuras. |
| Validação cruzada              | Garante que os dados em diferentes arquivos sejam consistentes entre si.                                                         |
