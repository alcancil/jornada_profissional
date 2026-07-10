#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
CAMINHO_COMPETENCIAS = os.path.join(BASE_DIR, 'config', 'competencias.json')
CAMINHO_PERFIL = os.path.join(BASE_DIR, 'dados', 'meu_perfil.json')

def carregar_json(arquivo):
    if not os.path.exists(arquivo):
        print(f"ERRO: Arquivo não encontrado: {arquivo}")
        sys.exit(1)
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"ERRO: Falha ao ler {arquivo}: {e}")
        sys.exit(1)

def salvar_json(arquivo, dados):
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Perfil salvo com sucesso em: {arquivo}")
    except Exception as e:
        print(f"ERRO: Falha ao salvar {arquivo}: {e}")
        sys.exit(1)

def carregar_perfil_existente():
    if os.path.exists(CAMINHO_PERFIL):
        return carregar_json(CAMINHO_PERFIL)
    return {"usuario": "", "hard_skills": {}, "soft_skills": {}}

def obter_nivel(niveis_permitidos):
    while True:
        nivel = input(f"Níveis disponíveis: {', '.join(niveis_permitidos)}. Digite um nível: ").strip()
        if nivel in niveis_permitidos:
            return nivel
        print(f"Nível inválido. Use um dos seguintes: {', '.join(niveis_permitidos)}.")

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

    # Configuração dos níveis permitidos (definidos no config.json, mas aqui usamos padrão)
    niveis_permitidos = ['Básico', 'Intermediário', 'Avançado']

    for comp in lista_competencias:
        id_comp = comp['id']
        nome = comp['nome']
        dominio = comp.get('dominio', 'Geral')
        tipo = comp.get('tipo', 'hard')

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

    # Remove domínios vazios
    for secao in ['hard_skills', 'soft_skills']:
        for dom in list(perfil[secao].keys()):
            if not perfil[secao][dom]:
                del perfil[secao][dom]

    salvar_json(CAMINHO_PERFIL, perfil)
    print("Marcação concluída!")

if __name__ == "__main__":
    main()