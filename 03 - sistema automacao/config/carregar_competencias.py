#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Módulo: carregar_competencias.py
Objetivo: Carregar e validar os arquivos JSON de competências e configurações.
          Este é o primeiro passo do sistema de automação.
Autor: Seu nome
Data: Julho 2026
"""

import json
import os
import sys
import logging

# Configuração básica de logging (exibe mensagens no terminal)
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# =============================================================================
# 1. DEFINIÇÃO DOS CAMINHOS
# =============================================================================

# Obtém o diretório onde este script está localizado (ex: .../03 - automacao/src/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Sobe um nível para chegar na pasta '03 - automacao'
BASE_DIR = os.path.dirname(SCRIPT_DIR)

# Caminhos absolutos para os arquivos JSON
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
    if not os.path.exists(arquivo):
        logging.error(f"Arquivo não encontrado: {arquivo}")
        sys.exit(1)

    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        logging.info(f"Arquivo carregado: {arquivo}")
        return dados
    except json.JSONDecodeError as e:
        logging.error(f"Erro ao decodificar JSON do arquivo {arquivo}: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Erro inesperado ao ler {arquivo}: {e}")
        sys.exit(1)


def validar_competencias(competencias):
    """
    Valida a lista de competências.
    Retorna True se tudo estiver correto, False caso contrário.
    """
    # Verifica se o campo 'competencias' existe e é uma lista
    if 'competencias' not in competencias:
        logging.error("O arquivo competencias.json não contém a chave 'competencias'.")
        return False

    lista = competencias['competencias']
    if not isinstance(lista, list):
        logging.error("O campo 'competencias' não é uma lista.")
        return False

    # Verifica cada competência
    campos_obrigatorios = {'id', 'nome', 'dominio', 'tipo', 'nivel', 'perfis'}
    erros = 0
    for idx, item in enumerate(lista):
        # Cada item deve ser um dicionário
        if not isinstance(item, dict):
            logging.error(f"Item {idx} não é um dicionário: {item}")
            erros += 1
            continue

        # Verifica se todos os campos obrigatórios estão presentes
        faltando = campos_obrigatorios - set(item.keys())
        if faltando:
            logging.error(f"Competência {idx} ('{item.get('id', 'desconhecido')}') "
                          f"faltando campos: {faltando}")
            erros += 1

        # Verifica se o campo 'tipo' é válido (hard ou soft)
        tipo = item.get('tipo')
        if tipo not in ['hard', 'soft']:
            logging.error(f"Competência {idx} tem tipo inválido: {tipo}. Deve ser 'hard' ou 'soft'.")
            erros += 1

        # Verifica se o campo 'nivel' está na lista de níveis permitidos
        # (iremos carregar os níveis do config.json depois)
        # Esta validação será feita na função principal, pois depende do config.

    return erros == 0


def validar_config(config):
    """
    Valida o arquivo config.json.
    Retorna True se estiver correto, False caso contrário.
    """
    campos_obrigatorios = {'perfis', 'niveis', 'caminhos'}
    faltando = campos_obrigatorios - set(config.keys())
    if faltando:
        logging.error(f"Configuração faltando campos: {faltando}")
        return False

    # Verifica se 'perfis' e 'niveis' são listas
    if not isinstance(config['perfis'], list):
        logging.error("O campo 'perfis' deve ser uma lista.")
        return False
    if not isinstance(config['niveis'], list):
        logging.error("O campo 'niveis' deve ser uma lista.")
        return False

    # Verifica se 'caminhos' é um dicionário
    if not isinstance(config['caminhos'], dict):
        logging.error("O campo 'caminhos' deve ser um dicionário.")
        return False

    # (Opcional) Pode-se verificar se os caminhos existem, mas não faremos agora.
    return True


# =============================================================================
# 3. FUNÇÃO PRINCIPAL (ORQUESTRADORA)
# =============================================================================

def main():
    """
    Função principal: carrega os dois JSONs, valida e exibe um resumo.
    """
    logging.info("Iniciando carregamento do sistema...")

    # Carrega competencias.json
    comp_data = carregar_json(CAMINHO_COMPETENCIAS)
    if not validar_competencias(comp_data):
        logging.error("Erros encontrados no arquivo competencias.json. Corrija e tente novamente.")
        sys.exit(1)

    # Carrega config.json
    config_data = carregar_json(CAMINHO_CONFIG)
    if not validar_config(config_data):
        logging.error("Erros encontrados no arquivo config.json. Corrija e tente novamente.")
        sys.exit(1)

    # Validação cruzada: níveis das competências devem estar na lista de níveis do config
    niveis_permitidos = set(config_data['niveis'])
    for item in comp_data['competencias']:
        nivel = item.get('nivel')
        if nivel not in niveis_permitidos:
            logging.error(f"Nível '{nivel}' não está na lista de níveis permitidos: {niveis_permitidos}")
            sys.exit(1)

    # Exibe resumo
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

if __name__ == "__main__":
    main()