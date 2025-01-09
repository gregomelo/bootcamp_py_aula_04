"""Desafio. Refatorar código da aula anterior."""

"""
O código deverá ser refatorado para incluir o usuário de dicionários, type hint e funções.

Código original
---------------

nome_do_usario_invalidado = True

while nome_do_usario_invalidado:
    # Coletando nome do usuário
    nome_do_usuario = input("Digite o nome do usuário (ou para sair, digite sair): ")

    # Validando nome do usuário
    if len(nome_do_usuario) == 0:
        print("O nome não pode estar vazio. Tente novamente.")
    elif nome_do_usuario.isspace():
        print("Nome inválido contendo somente caracteres espaço. Tente novamente.")
    elif any(letra.isdigit() for letra in nome_do_usuario):
        print("Nome inválido contendo um ou mais números. Tente novamente.")
    elif nome_do_usuario.lower() == "sair":
        print("Obrigado por sua visita!")
        exit()
    else:
        nome_do_usario_invalidado = False


valor_salario_invalido = True

while valor_salario_invalido:
    try:
        # Coletando o valor do salário
        valor_salario = float(input("Digite o valor do salário: "))

        if valor_salario <= 0:
            print("Salário negativo ou zero. Tente novamente.")
        else:
            valor_salario_invalido = False

    except ValueError:
        print("Salário inválido. Tente novamente.")

# Calculando o bônus do usuário
valor_bonus = 1000 + valor_salario * 1.5

# Retornando o resultado
print(f"Olá {nome_do_usuario}, o seu bônus foi de {valor_bonus}.")

"""


def coleta_nome_usuario() -> str:
    """
    Coleta e valida o nome do usuário.

    O método solicita que o usuário insira um nome e verifica se:
    - O nome não está vazio.
    - O nome não contém apenas espaços.
    - O nome não contém números.

    Retorna
    -------
    str
        Nome do usuário validado.
    """
    nome_usario_invalidado = True
    while nome_usario_invalidado:
        # Coletando nome do usuário
        nome_usuario = input("Digite o nome do usuário (ou para sair, digite sair): ")

        # Validando nome do usuário
        if len(nome_usuario) == 0:
            print("O nome não pode estar vazio. Tente novamente.")
        elif nome_usuario.isspace():
            print("Nome inválido contendo somente caracteres espaço. Tente novamente.")
        elif any(letra.isdigit() for letra in nome_usuario):
            print("Nome inválido contendo um ou mais números. Tente novamente.")
        else:
            nome_usario_invalidado = False

    return nome_usuario


def coletar_salario_usuario() -> float:
    """
    Coleta e valida o salário do usuário.

    O método solicita que o usuário insira um valor numérico para o salário
    e verifica se:
    - O valor é um número válido.
    - O valor é maior que zero.

    Retorna
    -------
    float
        Valor do salário validado.
    """
    valor_salario_invalido = True
    while valor_salario_invalido:
        try:
            # Coletando o valor do salário
            valor_salario = float(input("Digite o valor do salário: "))

            if valor_salario <= 0:
                print("Salário negativo ou zero. Tente novamente.")
            else:
                valor_salario_invalido = False

            return valor_salario

        except ValueError:
            print("Salário inválido. Tente novamente.")


def calcular_bonus(valor_salario: float, taxa_bonus: float = 1.5) -> float:
    """
    Calcula o bônus do usuário com base no salário e na taxa de bônus.

    O cálculo considera um valor base fixo de 1000 e um multiplicador
    aplicado ao salário informado.

    Parâmetros
    ----------
    valor_salario : float
        Salário do usuário.
    taxa_bonus : float, opcional
        Taxa de bônus a ser aplicada sobre o salário. O valor padrão é 1.5.

    Retorna
    -------
    float
        Valor do bônus calculado, arredondado para duas casas decimais.
    """
    valor_bonus = round(1000 + valor_salario * taxa_bonus, 2)
    return valor_bonus


dados_usuarios = []
while True:
    nome_usuario = coleta_nome_usuario()
    if nome_usuario.lower() != "sair":
        salario_usuario = coletar_salario_usuario()
        bonus_usuario = calcular_bonus(valor_salario=salario_usuario)

        dado_usuario = {
            "nome_usuario": nome_usuario,
            "salario_usuario": salario_usuario,
            "bonus_usuario": bonus_usuario,
        }

        dados_usuarios.append(dado_usuario)

        # Retornando o resultado
        print(f"O {nome_usuario}, o seu bônus foi de {bonus_usuario}.")
    else:
        print(f"Foram gravados os seguintes dados: {dados_usuarios}")
        exit()
