
def is_cpf_or_cns(cpf_or_cns):
    if len(cpf_or_cns) == 15:
        return 'cns'
    elif len(cpf_or_cns) == 11:
        return 'cpf'
    else:
        raise Exception('Deve ter 15 (cns) ou 11 (cpf) digitos')
