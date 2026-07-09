#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo: carregar_competencias.py
Objetivo: Carregar e validar os arquivos JSON de competências e configurações.
          Este é o primeiro passo do sistema de automação.
Autor: Seu nome
Data: Julho 2026
"""

# Importa os módulos necessários
import json          # Para trabalhar com JSON
import os            # Para lidar com caminhos de arquivos
import sys           # Para encerrar o programa se algo der errado
import logging       # Para exibir mensagens de forma organizada

# Configura o logging para mostrar informações e erros no terminal
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# =============================================================================
# 1. DEFINIÇÃO DOS CAMINHOS
# =============================================================================

# Obtém o caminho completo da pasta onde este script está localizado
# Exemplo: /home/user/jornada_profissional/03 - automacao/src/
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Sobe um nível para chegar na pasta '03 - automacao' (a raiz do módulo)
BASE_DIR = os.path.dirname(SCRIPT_DIR)

# Monta os caminhos absolutos para os arquivos JSON dentro da pasta 'config'
CAMINHO_COMPETENCIAS = os.path.join(BASE_DIR, 'config', 'competencias.json')
CAMINHO_CONFIG = os.path.join(BASE_DIR, 'config', 'config.json')


# =============================================================================
# 2. FUNÇÕES DE CARREGAMENTO E VALIDAÇÃO
# =============================================================================

def carregar_json(arquivo):
    """
    Carrega um arquivo JSON e retorna o conteúdo.
    Em caso de erro, interrompe a execução com mensagem adequada.
    """
    # Verifica se o arquivo existe no sistema
    if not os.path.exists(arquivo):
        logging.error(f"Arquivo não encontrado: {arquivo}")
        sys.exit(1)  # Encerra o programa com código de erro 1

    try:
        # Tenta abrir e ler o arquivo como UTF-8 (suporta acentos)
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)  # Converte o JSON para dicionário Python
        logging.info(f"Arquivo carregado: {arquivo}")
        return dados
    except json.JSONDecodeError as e:
        # Se o JSON estiver mal formatado, capturamos o erro
        logging.error(f"Erro ao decodificar JSON do arquivo {arquivo}: {e}")
        sys.exit(1)
    except Exception as e:
        # Qualquer outro erro inesperado (ex: permissão negada)
        logging.error(f"Erro inesperado ao ler {arquivo}: {e}")
        sys.exit(1)


def validar_competencias(competencias):
    """
    Valida a lista de competências.
    Retorna True se tudo estiver correto, False caso contrário.
    """
    # Verifica se o JSON tem a chave 'competencias'
    if 'competencias' not in competencias:
        logging.error("O arquivo competencias.json não contém a chave 'competencias'.")
        return False

    # Pega a lista de competências
    lista = competencias['competencias']
    # Confirma que é uma lista (e não um dicionário ou outro tipo)
    if not isinstance(lista, list):
        logging.error("O campo 'competencias' não é uma lista.")
        return False

    # Define os campos obrigatórios para cada competência
    campos_obrigatorios = {'id', 'nome', 'dominio', 'tipo', 'nivel', 'perfis'}
    erros = 0  # Contador de erros

    # Percorre cada item da lista, com índice para referência
    for idx, item in enumerate(lista):
        # Verifica se o item é um dicionário
        if not isinstance(item, dict):
            logging.error(f"Item {idx} não é um dicionário: {item}")
            erros += 1
            continue

        # Verifica se todos os campos obrigatórios estão presentes
        faltando = campos_obrigatorios - set(item.keys())
        if faltando:
            # Se faltar algum, exibe o ID da competência para facilitar a correção
            logging.error(f"Competência {idx} ('{item.get('id', 'desconhecido')}') "
                          f"faltando campos: {faltando}")
            erros += 1

        # Verifica se o 'tipo' é 'hard' ou 'soft'
        tipo = item.get('tipo')
        if tipo not in ['hard', 'soft']:
            logging.error(f"Competência {idx} tem tipo inválido: {tipo}. Deve ser 'hard' ou 'soft'.")
            erros += 1

        # O campo 'nivel' será validado depois, com os dados do config.json

    # Retorna True se não houve nenhum erro
    return erros == 0


def validar_config(config):
    """
    Valida o arquivo config.json.
    Retorna True se estiver correto, False caso contrário.
    """
    # Campos obrigatórios no config.json
    campos_obrigatorios = {'perfis', 'niveis', 'caminhos'}
    faltando = campos_obrigatorios - set(config.keys())
    if faltando:
        logging.error(f"Configuração faltando campos: {faltando}")
        return False

    # Verifica se 'perfis' é uma lista
    if not isinstance(config['perfis'], list):
        logging.error("O campo 'perfis' deve ser uma lista.")
        return False

    # Verifica se 'niveis' é uma lista
    if not isinstance(config['niveis'], list):
        logging.error("O campo 'niveis' deve ser uma lista.")
        return False

    # Verifica se 'caminhos' é um dicionário
    if not isinstance(config['caminhos'], dict):
        logging.error("O campo 'caminhos' deve ser um dicionário.")
        return False

    # (Aqui poderíamos verificar se os caminhos existem, mas deixamos para o futuro)
    return True


# =============================================================================
# 3. FUNÇÃO PRINCIPAL (ORQUESTRADORA)
# =============================================================================

def main():
    """
    Função principal: carrega os dois JSONs, valida e exibe um resumo.
    """
    logging.info("Iniciando carregamento do sistema...")

    # Carrega e valida competencias.json
    comp_data = carregar_json(CAMINHO_COMPETENCIAS)
    if not validar_competencias(comp_data):
        logging.error("Erros encontrados no arquivo competencias.json. Corrija e tente novamente.")
        sys.exit(1)

    # Carrega e valida config.json
    config_data = carregar_json(CAMINHO_CONFIG)
    if not validar_config(config_data):
        logging.error("Erros encontrados no arquivo config.json. Corrija e tente novamente.")
        sys.exit(1)

    # Validação cruzada: os níveis das competências devem estar na lista de níveis do config
    niveis_permitidos = set(config_data['niveis'])  # Converte lista para conjunto para busca rápida
    for item in comp_data['competencias']:
        nivel = item.get('nivel')
        if nivel not in niveis_permitidos:
            logging.error(f"Nível '{nivel}' não está na lista de níveis permitidos: {niveis_permitidos}")
            sys.exit(1)

    # Exibe um resumo do que foi carregado
    total = len(comp_data['competencias'])
    hard = sum(1 for c in comp_data['competencias'] if c.get('tipo') == 'hard')
    soft = sum(1 for c in comp_data['competencias'] if c.get('tipo') == 'soft')
    logging.info(f"Carregado com sucesso!")
    logging.info(f"Total de competências: {total} (Hard: {hard}, Soft: {soft})")
    logging.info(f"Perfis disponíveis: {config_data['perfis']}")
    logging.info(f"Sistema pronto para os próximos módulos.")


# =============================================================================
# 4. EXECUÇÃO DO SCRIPT
# =============================================================================

# Esta condição garante que o código só roda se o script for executado diretamente
if __name__ == "__main__":
    main()