R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
code_info    = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result  = C + '[' + G + '+' + C + '] '
code_error   = C + '[' + R + '!' + C + '] '
from logging import exception
from random import randint
from conta import Conta



contas  = {}
contas2 = {}
valor   = 0
saldo   = 0
numero  = ''
lista = []
soma = 0









def menu():
    global op
    op = input(f'\n\t{code_result}O que deseja fazer:')


def CriarConta():
    global c
    global Nome
    global numero

    Nome          = input(f'\n\t{code_result}{B}Digite seu nome:{C}') #nome
    if Nome == '':
        print('\tNenhum nome digitado')
    else:
        print(f'\n\t{G}Conta criada com sucesso!{C}')
        numero_gerado = randint(10,99)
        numString     = str(numero_gerado)
        zeroString    = '0'
        numero        = zeroString + numString  #numero da conta 
        contas        = {numero:[Nome, saldo]}
        contas2.update(contas)
        c = Conta(titular = Nome,numero = numero,saldo = 0)
        

def ListarContas():
    if contas2 == {}:
        print((f'\t{code_info}Crie sua conta primeiro'))
    else:
        c.extrato()





def SacarValor():
    if contas2 == {}:
        print((f'\t{code_info}Crie sua conta primeiro'))
    else:
      c.extrato()

      print(f'\t{G}[Área de Saque]{B}')
      numconta = (input(f'\t{code_result}{B}Digite o numero da conta:{C}'))
      if numconta in contas2:
        numero = numconta
        valor1 = int(input(f'\t{code_result}{B}Quanto deseja sacar:{C}'))
        contas2[numero][1]-=valor1
        c.sacar(valor = valor1, numeroc=numconta)
        if valor <= contas2[numero][1]:
            print(f'\t{G}Saque realizado com sucesso!{C}')
        else:
            print('\tSaldo Insuficiente!')
    if numconta not in contas2:
       print(f'\t{code_error}Numero da conta errado')







def DepositarValor():
    global valor1
    if contas2 == {}:
       print(f'\t{code_info}Crie sua conta primeiro')
    else:
      c.extrato()

      print(f'\t{G}[Área de Depósito]{C}') 
      numconta = input(f'\t{code_result}{B}Digite o numero da conta:{C}') 
      if numconta in contas2:
         valor1  = int(input(f'\t{code_result}{B}Quanto deseja depositar:{C}'))
         contas2[numero][1]+=valor1 
         print(f'\t{G}Deposito realizado com sucessso!{C}')
         c.depositar(valor = valor1, numeroc=numconta)

    if numconta not in contas2:
       print(f'\t{code_error}Numero da conta errado')




def ExcluirConta():
    if contas2 == {}:
        print(f'\t{code_info}Você ainda não criou nenhuma conta')
    else:
      remover = input(f'\t{B}Numero da conta que deseja excluir:{C}')
      if remover in contas2 and contas2[numero][1] == 0:
         contas2.pop(remover)
         print(f'\t{G}conta excluida com sucesso!{C}') 
         s = input(f'\t{code_result}{B}Voçê deseja continuar com os testes no MINI SISTEMA S/N ?{C}')
         if s.lower() == 'n':
           exit()

         else:
           print(f'\t{code_error}Numero da conta errado') 





def transfere():
   print('\t[Área de Transferência]')
   env  = input('\tDigite o numero da conta que vai enviar:') 
   dest = input('\tDigite o numero da conta que vai receber:') 

   if env in contas2 and dest in contas2:
     numero = dest
     contas[numero][1] +=valor
     numero = env
     contas[numero][1] -= valor
     valor1 = int(input(f'\t{code_result}{B}Quanto deseja transferir{C}'))
     c.transfere(destino=dest,valor= valor1,num = env)
     print('\tValor transferido com sucesso!')
   else:
       print(f'\t{code_error}Numero da conta errado')





print(f'\n\t{B}[MINI SISTEMA BANCÁRIO]{C}')
print(f'\n\t[{G}1{C}] - {Y}Criar Conta{C}\n\t[{G}2{C}] - {Y}Listar Contas/Extrato{C}\n\t[{G}3{C}] - {Y}Sacar Valor{C}\n\t[{G}4{C}] - {Y}Depositar Valor{C}\n\t[{G}5{C}] - {Y}Excluir Conta{C}\n\t[{G}6{C}] - {Y}Fazer Transferência{C}')    
def Loop():
    while True:

        menu()

        #criar Conta
        if op == '1':
         CriarConta()

        #Listar Contas
        elif op == '2':
            ListarContas()

        #Sacar Valor
        elif op == '3':
            SacarValor()

        #Depositar valor
        elif op == '4':
            DepositarValor()

        #Excluir Conta
        elif op == '5':
         ExcluirConta()

        elif op =='6':
          transfere()

        else:
         print(f'\t{code_error}{B}Opção Invalida!{C}')


Loop()
