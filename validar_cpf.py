def verificar_se_todos_sao_iguais(cpf):
    lista_digitos = [str(digito) for digito in range(0, 10)]
    repitidos = 0
    for digito in lista_digitos:
        repitidos = cpf.count(digito)
        if repitidos == 11:
            return False
    return cpf


def tratar_entrada(cpf):
    invalidos_para_calculo = (' ', '-', '.')
    digitos_cpf = ''
    for digito in cpf:
        if digito not in invalidos_para_calculo:
            digitos_cpf += digito
    
    if len(digitos_cpf) < 11 or len(digitos_cpf) > 11:
        return False
    digitos_cpf = verificar_se_todos_sao_iguais(digitos_cpf)
    return digitos_cpf


def calcular_digitos(cpf, fatores):
    sequencia_fatores = tuple(range(fatores, 1, -1))
    cont = resultado = 0
    for digito in cpf:
        if cont == len(sequencia_fatores):
            return resultado
        resultado += (int(digito) * sequencia_fatores[cont])
        cont += 1


def verificar_digitos(resultado):
    digito = (resultado * 10) % 11
    if digito == 10:
        digito = 0
    return digito


def validar_cpf():
    try:
        cpf = input('Informe o CPF: ').strip()
        cpf = tratar_entrada(cpf)
        if cpf:
            primeiro_digito =  str(verificar_digitos(calcular_digitos(cpf, 10)))
            segundo_digito = str(verificar_digitos(calcular_digitos(cpf, 11)))
            if primeiro_digito == cpf[-2] and segundo_digito == cpf[-1]:
                return True
        return False  
    except Exception as erro:
        print(f'\nErro: {erro}')
        return erro

print(validar_cpf())
