from classes.cadastro import Pessoas

conta1 = Pessoas()



print('Olá, Seja bem vindo ao nosso sistema.')
escolha = int(input('Escolha a opção desejada: \n 1 - Cadastrar \n 2 - Deposito \n 3 - Extrato \n 4 - Saque \n'))

match escolha:
    case 1:
        print(conta1.fazer_cadastro())
    case 2:
        print(conta1.depositar())
    case 3:
        print(conta1.extrato())
    case 4:
        print(conta1.sacar())