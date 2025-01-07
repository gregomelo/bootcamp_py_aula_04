"""Exercício 06. Ordenação Personalizada."""

pessoa_01 = {"nome": "Greg", "idade": 36, "empregado": True}

pessoa_02 = {"nome": "Gregory", "idade": 37, "empregado": False}

pessoa_03 = {"nome": "Oliveira", "idade": 60, "empregado": False}

pessoas = [pessoa_01, pessoa_02, pessoa_03]

pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)
