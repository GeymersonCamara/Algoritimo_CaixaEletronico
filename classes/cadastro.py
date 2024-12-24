import json
import random

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

    def gerar_conta(self, lista):import json
import random
from datetime import datetime

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
                cpf = int(input('CPF: '))
                conta = int(input('Conta: '))
                agencia = int(input('Agência: '))
            except ValueError:
                print("Erro: Digite apenas números.")
                return

            try:
                with open('db/cadastros.json') as file:
                    lista = json.load(file)
            except FileNotFoundError:
                print('################################')
                print(' ')
                print('Erro: Nenhum cadastro encontrado.')
                print(' ')
                print('################################')
                return

            for registro in lista:
                if registro['cpf'] == cpf and registro['conta'] == conta and registro['agencia'] == agencia:
                    # Permite a execução da função decorada
                    return func(self, registro, *args, **kwargs)

            print("Erro: Dados não encontrados ou incorretos.")
            return
        return dados

    @verificar_usuario
    def extrato(self, registro):
        """
        Exibe o saldo do usuário autenticado.
        """
        print(f"Seu saldo é: {registro['saldo']}")
        
        hoje = datetime.now()
        print(hoje)
        
    @verificar_usuario
    def depositar(self, registro):
        """
        Realiza um depósito na conta do usuário autenticado e atualiza o saldo no JSON.
        """
        try:
            valor = float(input("Digite o valor do depósito: "))
            if valor <= 0:
                print("Erro: O valor do depósito deve ser maior que zero.")
                return
        except ValueError:
            print("Erro: Digite um valor numérico válido.")
            return

        # Atualizar o saldo do registro
        registro['saldo'] += valor

        print("Depósito realizado com sucesso!")
        print(f"Novo saldo: R${registro['saldo']:.2f}")
        
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
        
        hoje = datetime.now()
        print(hoje)
        
    @verificar_usuario
    def sacar(self, registro):
        """
        Realiza um depósito na conta do usuário autenticado e atualiza o saldo no JSON.
        """
        try:
            valor = float(input("Digite o valor que deseja sacar: "))
            if valor <= 0:
                print("Erro: O valor de saque deve ser maior que zero.")
                return
        except ValueError:
            print("Erro: Digite um valor numérico válido.")
            return

        # Atualizar o saldo do registro
        registro['saldo'] -= valor
        print(f"Saque realizado com sucesso! Novo saldo: R${registro['saldo']:.2f}")

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
        
        hoje = datetime.now()
        print(hoje)
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
                cpf = int(input('CPF: '))
                conta = int(input('Conta: '))
                agencia = int(input('Agência: '))
            except ValueError:
                print("Erro: Digite apenas números.")
                return

            try:
                with open('db/cadastros.json') as file:
                    lista = json.load(file)
            except FileNotFoundError:
                print('################################')
                print(' ')
                print('Erro: Nenhum cadastro encontrado.')
                print(' ')
                print('################################')
                return

            for registro in lista:
                if registro['cpf'] == cpf and registro['conta'] == conta and registro['agencia'] == agencia:
                    # Permite a execução da função decorada
                    return func(self, registro, *args, **kwargs)

            print("Erro: Dados não encontrados ou incorretos.")
            return
        return dados

    @verificar_usuario
    def extrato(self, registro):
        """
        Exibe o saldo do usuário autenticado.
        """
        print(f"Seu saldo é: {registro['saldo']}")
        
    @verificar_usuario
    def depositar(self, registro):
        """
        Realiza um depósito na conta do usuário autenticado e atualiza o saldo no JSON.
        """
        try:
            valor = float(input("Digite o valor do depósito: "))
            if valor <= 0:
                print("Erro: O valor do depósito deve ser maior que zero.")
                return
        except ValueError:
            print("Erro: Digite um valor numérico válido.")
            return

        # Atualizar o saldo do registro
        registro['saldo'] += valor
        print(f"Depósito realizado com sucesso! Novo saldo: R${registro['saldo']:.2f}")

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
            valor = float(input("Digite o valor que deseja sacar: "))
            if valor <= 0:
                print("Erro: O valor de saque deve ser maior que zero.")
                return
        except ValueError:
            print("Erro: Digite um valor numérico válido.")
            return

        # Atualizar o saldo do registro
        registro['saldo'] -= valor
        print(f"Saque realizado com sucesso! Novo saldo: R${registro['saldo']:.2f}")

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