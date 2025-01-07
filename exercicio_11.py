"""Exercício 11. Atualização de Dados."""

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300},
]

ATUALIZAR_PRODUTO = "Monitor"

ATUALIZAR_VALOR = 400

# Caso em que é necessário gerar uma nova lista
produtos_atualizados = []
for produto in produtos:
    if produto["nome"] == ATUALIZAR_PRODUTO:
        produtos_atualizados.append(
            {"id": produto["id"], "nome": produto["nome"], "preço": ATUALIZAR_VALOR}
        )
    else:
        produtos_atualizados.append(produto)

print(f"Produtos antigos: {produtos}")
print(f"Produtos atualizados: {produtos_atualizados}")

# Caso em que se pode alterar a própria lista
for produto in produtos:
    if produto["nome"] == ATUALIZAR_PRODUTO:
        produto["preço"] = ATUALIZAR_VALOR

print(f"Lista de produtos atualizada: {produtos}")
