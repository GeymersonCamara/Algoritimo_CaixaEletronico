import json
import random
from datetime import datetime
from datetime import timedelta

class Pessoas:
    AGENCIA_FIXA = 1234  # Número fixo da agência

    def __init__(self):
        self.codigo = None
        self.nome = None
        self.cpf = None
        self.conta = None
        self.agencia = self.AGENCIA_FIXA  # Atribuindo agência fixa
        self.saldo = 0.0  # Saldo inicial padrão

    def detalhar(self):
        return self.__dict__

    def gerar_conta(self, lista):
        """
        Gera um número de conta único e aleatório de até 6 dígitos.
        """
        while True:
            numero_conta = random.randint(100000, 999999)  # Número de 6 dígitos
            if all(registro['conta'] != numero_conta for registro in lista):
                return numero_conta

    def inserir(self):
        try:
            with open('db/cadastros.json') as file:
                lista = json.load(file)
        except Exception:
            lista = []

        # Gerar código sequencial
        self.codigo = len(lista) + 1

        # Gerar conta única e aleatória
        self.conta = self.gerar_conta(lista)

        for registro in lista:
            if registro['cpf'] == self.cpf:
                print(f"Erro: Já existe um cadastro com o CPF {self.cpf}.")
                return

        lista.append(self.detalhar())

        with open('db/cadastros.json', 'w') as file:
            json.dump(lista, file, indent=4)

        print('Cadastro realizado com sucesso!')
        print(f"Código: {self.codigo}")
        print(f"Conta: {self.conta}")
        print(f"Agência: {self.agencia}")

    def fazer_cadastro(self):
        """
        Solicita os dados do usuário e realiza o cadastro.
        """
        print("Bem-vindo ao sistema de cadastro!")
        self.nome = input("Digite seu nome: ")
        while True:
            try:
                self.cpf = int(input("Digite seu CPF (apenas números): "))
                break
            except ValueError:
                print("Erro: Digite um CPF válido (apenas números).")
        self.inserir()

    @staticmethod
    def verificar_usuario(func):
        def dados(self, *args, **kwargs):
            print('Por favor, insira seus dados para acesso:')
            try:
                self.cpf2 = int(input('CPF: '))
                self.conta2 = int(input('Conta: '))
                self.agencia2 = int(input('Agência: '))
            except ValueError:
                print("Erro: Digite apenas números.")
                return

            try:
                with open('db/cadastros.json') as file:
                    lista = json.load(file)
            except FileNotFoundError:
                caractere = "="
                tamanho = 50
                linha = caractere * tamanho
                print(linha)
                print(' ')
                print('Erro: Nenhum cadastro encontrado.')
                print(' ')
                caractere = "="
                tamanho = 50
                linha = caractere * tamanho
                print(linha)
                return

            for registro in lista:
                if registro['cpf'] == self.cpf2 and registro['conta'] == self.conta2 and registro['agencia'] == self.agencia2:
                    # Permite a execução da função decorada
                    return func(self, registro, *args, **kwargs)

            print("Erro: Dados não encontrados ou incorretos.")
            return
        return dados

    @verificar_usuario
    def extrato(self, registro):
        """
        Exibe todas as movimentações realizadas no dia atual pelo usuário autenticado.
        """
        try:
            print("\n" + "Extrato - Movimentações do Dia".center(50, "=") + "\n")
    
            # Tenta carregar os registros de movimentações (saques e depósitos)
            try:
                with open('db/saque.json', 'r') as saque_file:
                    saques = json.load(saque_file)
            except (FileNotFoundError, json.JSONDecodeError):
                saques = []
    
            try:
                with open('db/deposito.json', 'r') as deposito_file:
                    depositos = json.load(deposito_file)
            except (FileNotFoundError, json.JSONDecodeError):
                depositos = []
    
            # Obter a data atual no formato "dd-mm-yyyy"
            data_atual = datetime.now().strftime("%d-%m-%Y")
    
            # Filtrar registros de saques e depósitos do dia atual
            movimentacoes_hoje = []
    
            for item in saques + depositos:
                if (
                    str(item.get("CPF")) == str(registro["cpf"]) and
                    str(item.get("Conta")) == str(registro["conta"]) and
                    str(item.get("Agencia")) == str(registro["agencia"]) and
                    item.get("data", "").startswith(data_atual)
                ):
                    # Extrair hora da data completa
                    hora = item["data"].split(" ")[1] if " " in item["data"] else "00:00:00"
                    movimentacoes_hoje.append(
                        {
                            "tipo": "Saque" if item in saques else "Depósito",
                            "hora": hora,
                            "valor": float(item["valor"]),
                        }
                    )
    
            # Verifica e exibe as movimentações do dia atual
            if movimentacoes_hoje:
                print(f"Movimentações realizadas em {data_atual}:")
                print("=" * 50)
                for mov in movimentacoes_hoje:
                    print(f"- Tipo: {mov['tipo']}")
                    print(f"  Hora: {mov['hora']}")
                    print(f"  Valor: R${mov['valor']:.2f}")
                    print("-" * 50)
            else:
                print(f"Nenhuma movimentação realizada em {data_atual}.")
    
            # Exibir saldo atual
            print(f"\nSeu saldo atual é: R${registro['saldo']:.2f}")
    
            # Rodapé
            print("=" * 50)
            print(datetime.now().strftime("%d-%m-%Y"))
    
        except Exception as e:
            print(f"Erro inesperado: {e}")


    @verificar_usuario
    def depositar(self, registro):
        """
        Realiza um depósito na conta do usuário autenticado e atualiza o saldo no JSON.
        """
        try:
            self.valor = float(input("Digite o valor do depósito: "))
            if self.valor <= 0:
                print("Erro: O valor do depósito deve ser maior que zero.")
                return
        except ValueError:
            print("Erro: Digite um valor numérico válido.")
            return

        # Atualizar o saldo do registro
        registro['saldo'] += self.valor
        
        print(" ")
        palavra = "Deposito"
        resultado = palavra.center(50, "=")
        print(resultado)
        print(" ")
        
        print(f"Depósito realizado com sucesso!\n \nNovo saldo: R${registro['saldo']:.2f}")
        
        print(" ")
        caractere = "="
        tamanho = 50
        linha = caractere * tamanho
        print(linha)
        
        hoje = datetime.now()
        print(hoje)
        print(" ")

        try:
            # Abrir o arquivo JSON para leitura
            with open('db/cadastros.json', 'r') as file:
                lista = json.load(file)

            # Atualizar o registro na lista
            for item in lista:
                if item['cpf'] == registro['cpf'] and item['conta'] == registro['conta'] and item['agencia'] == registro['agencia']:
                    item['saldo'] = registro['saldo']

            # Sobrescrever o arquivo JSON com a lista atualizada
            with open('db/cadastros.json', 'w') as file:
                json.dump(lista, file, indent=4)

        except FileNotFoundError:
            print("Erro: Arquivo de cadastro não encontrado.")
            return
        
    @verificar_usuario
    def sacar(self, registro):
        """
        Realiza um depósito na conta do usuário autenticado e atualiza o saldo no JSON.
        """
        try:
            self.valor = float(input("Digite o valor que deseja sacar: "))
            if self.valor <= 0:
                print("Erro: O valor de saque deve ser maior que zero.")
                return
            if self.valor > registro['saldo']:
                print("Valor indisponivel")
                return
        except ValueError:
            print("Erro: Digite um valor numérico válido.")
            return

        #Registro de saque
        def valordata():
            valor = self.valor
            data = datetime.now().strftime("%d-%m-%Y")
            print(f"Valor: {valor} \nData: {data}")
            return {"valor": valor, "data": data,
                    "CPF": self.cpf2, "Conta": self.conta2, "Agencia": self.agencia2}


        
        try:
            with open('db/saque.json', 'r') as file:
                lista = json.load(file)
        except Exception:
            lista = []
            
        lista.append(valordata())
        
        with open('db/saque.json', 'w') as file:
            json.dump(lista, file, indent=4)
            
        # Atualizar o saldo do registro
        registro['saldo'] -= self.valor
        
        palavra = "Saque"
        resultado = palavra.center(50, "=")
        print(" ")
        print(resultado)
        print(" ")

        print(f"Saque realizado com sucesso!\n \nNovo saldo: R${registro['saldo']:.2f}")
        
        print(" ")
        caractere = "="
        tamanho = 50
        linha = caractere * tamanho
        print(linha)
        
        hoje = datetime.now().strftime("%d-%m-%Y")
        print(hoje)
        print(" ")

        try:
            # Abrir o arquivo JSON para leitura
            with open('db/cadastros.json', 'r') as file:
                lista = json.load(file)

            # Atualizar o registro na lista
            for item in lista:
                if item['cpf'] == registro['cpf'] and item['conta'] == registro['conta'] and item['agencia'] == registro['agencia']:
                    item['saldo'] = registro['saldo']

            # Sobrescrever o arquivo JSON com a lista atualizada
            with open('db/cadastros.json', 'w') as file:
                json.dump(lista, file, indent=4)

        except FileNotFoundError:
            print("Erro: Arquivo de cadastro não encontrado.")
            return