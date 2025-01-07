"""Exercício 06. Eliminação de Duplicatas."""

lista_com_duplicatas = [0, 0, 1, 3, 5, 6, 8, 8, 10, 1, 13, 13]

lista_sem_duplicatas = [*set(lista_com_duplicatas)]

# Outra forma de fazer a transformação do set em lista é usando list comprehension

print(f"A lista sem elementos duplicados é {lista_sem_duplicatas}")
