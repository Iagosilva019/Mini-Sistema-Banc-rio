
R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'
code_info    = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result  = C + '[' + G + '+' + C + '] '
code_error   = C + '[' + R + '!' + C + '] '

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
#---------------------------------------------------------------------------------------------------
#logo
logop =f'''{red}╭━╮╭━╮╭━━╮╭━╮╱╭╮╭━━╮   ╭━━━╮╭━━╮╭━━━╮╭━━━━╮╭━━━╮╭━╮╭━╮╭━━━╮   ╭━━╮╱╭━━━╮╭━╮╱╭╮╭━━━╮╭━━━╮╭━━━╮╭━━╮╭━━━╮
{cyan}┃┃╰╯┃┃╰┫┣╯┃┃╰╮┃┃╰┫┣╯   ┃╭━╮┃╰┫┣╯┃╭━╮┃┃╭╮╭╮┃┃╭━━╯┃┃╰╯┃┃┃╭━╮┃   ┃╭╮┃╱┃╭━╮┃┃┃╰╮┃┃┃╭━╮┃┃╭━╮┃┃╭━╮┃╰┫┣╯┃╭━╮┃
{yellow}┃╭╮╭╮┃╱┃┃╱┃╭╮╰╯┃╱┃┃╱   ┃╰━━╮╱┃┃╱┃╰━━╮╰╯┃┃╰╯┃╰━━╮┃╭╮╭╮┃┃┃╱┃┃   ┃╰╯╰╮┃┃╱┃┃┃╭╮╰╯┃┃┃╱╰╯┃┃╱┃┃┃╰━╯┃╱┃┃╱┃┃╱┃┃
{blue}┃┃┃┃┃┃╱┃┃╱┃┃╰╮┃┃╱┃┃╱   ╰━━╮┃╱┃┃╱╰━━╮┃╱╱┃┃╱╱┃╭━━╯┃┃┃┃┃┃┃╰━╯┃   ┃╭━╮┃┃╰━╯┃┃┃╰╮┃┃┃┃╱╭╮┃╰━╯┃┃╭╮╭╯╱┃┃╱┃┃╱┃┃
{red}┃┃┃┃┃┃╭┫┣╮┃┃╱┃┃┃╭┫┣╮   ┃╰━╯┃╭┫┣╮┃╰━╯┃╱╱┃┃╱╱┃╰━━╮┃┃┃┃┃┃┃╭━╮┃   ┃╰━╯┃┃╭━╮┃┃┃╱┃┃┃┃╰━╯┃┃╭━╮┃┃┃┃╰╮╭┫┣╮┃╰━╯┃
{yellow}╰╯╰╯╰╯╰━━╯╰╯╱╰━╯╰━━╯   ╰━━━╯╰━━╯╰━━━╯╱╱╰╯╱╱╰━━━╯╰╯╰╯╰╯╰╯╱╰╯   ╰━━━╯╰╯╱╰╯╰╯╱╰━╯╰━━━╯╰╯╱╰╯╰╯╰━╯╰━━╯╰━━━╯
{green}╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
{cyan}╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
                                                                                     {bblue}Iago_Linux'''
#---------------------------------------------------------------------------------------------------

#Bibliotecas
from random import randint
from time import sleep
from conta import Conta
import sys, os
#---------------------------------------------------------------------------------------------------

#variaveis globais
contas  = {}
contas2 = {}
valor   = 0
saldo   = 0
numero  = ''
lista = []
soma = 0
Nome = ''

#---------------------------------------------------------------------------------------------------

#Limpa a Tela
def clear():
    if os == "Windons":
        os.system('cls')
    elif os == "Linux":
        os.system('clear')
    else:
        os.system('clear')  #mac
        
        
def sprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        sleep(0.01)
#------------------------------------------------------------------------------------------------


def menu():
    global op
    print(f'\n\t{G}[1{C}] - {Y}Criar Conta{C}\n\t[{G}2{C}] - {Y}Listar Contas/Extrato{C}\n\t[{G}3{C}] - {Y}Sacar Valor{C}\n\t[{G}4{C}] - {Y}Depositar Valor{C}\n\t[{G}5{C}] - {Y}Excluir Conta{C}\n\t[{G}6{C}] - {Y}Fazer Transferência{C}')    
    op = input(f'\n\t{code_result}{bblue}O que deseja fazer:{C}')
    if op == 'exit':
        exit()
    elif op == 'clear':
        clear()
#---------------------------------------------------------------------------------------------------



def CriarConta():
    global c
    global Nome
    global numero
  
    
    Nome = input(f'\n\t{code_result}{B}Digite seu nome:{C}') #nome
    if Nome == '':
        print(f'\t{code_error}{red}Nenhum nome digitado')
        sleep(2.0)
        clear()
    else:
        logo =f'\t{bgreen}[{red}||||||||||||||||||||||||{bgreen}]100%'
        sprint(logo)
        
        print(f'\n\t{bgreen}Conta criada com sucesso!{C}')
        sleep(2.5)
        clear()
        numero_gerado = randint(10,99)
        numString     = str(numero_gerado)
        zeroString    = '0'
        numero        = zeroString + numString  #numero da conta 
        contas        = {numero:[Nome, saldo]}
        contas2.update(contas)
       
        c = Conta(numero = numero,saldo = 0)
        ret =  c.cliente(titular = Nome,cpf = '000.000.000-00') # titular e gerando um cpf
        #print(type(ret)) >> NoneType: é um tipo de um objeto None 
    

#---------------------------------------------------------------------------------------------------


def ListarContas():
    if contas2 == {}:
        print((f'\t{code_info}{red}Crie sua conta primeiro{C}'))
        sleep(2.0)
        clear()
    else:
        c.extrato()


#---------------------------------------------------------------------------------------------------



def SacarValor():
    if contas2 == {}:
        print((f'\t{code_info}{red}Crie sua conta primeiro{C}'))
        sleep(2.0)
        clear()
    else:
        c.extrato()
       
        print(f'''\t{bgreen}[ÁREA DE SAQUE]{C}''')
        numconta = (input(f'\t{code_result}{B}Digite o numero da conta:{C}'))
        if numconta in contas2:
            strvalor1 = input(f'\t{code_result}{B}Quanto deseja sacar:{C}')
            
            if not  strvalor1.isdigit():
                print(f'\t{code_error}{red}Informe Somente Numeros')
                sleep(2.0)
                clear()
            else:
              valor1 = int(strvalor1)
              contas2[numero][1] -=valor1
              c.sacar(valor = valor1, numeroc=numconta)
              sleep(2.0)
              clear()
        elif numconta not in contas2:
           print(f'\t{code_error}{red}Numero da conta errado')
           sleep(2.0)
           clear()
        else:
           print( f'\t{code_error}{red}Saldo Insuficiente!')
           sleep(2.0)
           clear()

#---------------------------------------------------------------------------------------------------




def DepositarValor():
    if contas2 == {}:
       print(f'\t{code_info}{red}Crie sua conta primeiro')
       sleep(2.0)
       clear()
    else:
        c.extrato()
        print(f'\t{bgreen}[ÁREA DE DEPÓSITO]') 
        numconta = input(f'\t{code_result}{B}Digite o numero da conta:{C}') 
        if numconta in contas2:
            strvalor1  = input(f'\t{code_result}{B}Quanto deseja depositar:{C}')
            
            if not  strvalor1.isdigit():
                print(f'\t{code_error}{red}Informe Somente Numeros')
                sleep(2.0)
                clear()
            else:
               valor1 = int(strvalor1)
               contas2[numero][1] +=valor1
               print(f'\t{bgreen}Deposito realizado com sucessso!{C}')
               sleep(2.0)
               clear()
               c.depositar(valor = valor1, numeroc=numconta)
      
        else:
           print(f'\t{code_error}{red}Numero da conta errado')
           sleep(2.0)
           clear()
  
#---------------------------------------------------------------------------------------------------

def ExcluirConta():
    if contas2 == {}:
        print(f'\t{code_info}{red}Você ainda não criou nenhuma conta')
        sleep(2.0)
        clear()
    else:
        remover = input(f'\t{B}Numero da conta que deseja excluir:{C}')
        c.excluir(remov = remover)
        numero = remover
        if contas2[numero][1] == 0:
           contas2.pop(remover)
        else:
           s = input(f'\t{code_result}{B}Voçê deseja continuar com os testes no MINI SISTEMA S/N ?{C}')
           if s.lower() == 'n':
            exit()
           sleep(2.0)
           clear()
      
#---------------------------------------------------------------------------------------------------


def transfere():
    if contas2 == {}:
        print(f'\t{code_info}{red}Você ainda não criou nenhuma conta')
        sleep(2.0)
        clear()
    else:
        c.extrato()
        print(f'\t{bgreen}[ÁREA DE TRANSFERÊNCIA]')
        env  = input(f'\t{code_result}{bblue}Digite o numero da conta que vai enviar:{C}') 
        dest = input(f'\t{code_result}{bblue}Digite o numero da conta que vai receber:{C}') 

        if env in contas2 and dest in contas2:
            strvalor1 = input(f'\t{code_result}{B}Quanto deseja transferir:{C}')
            numero = dest
            aux = int(strvalor1)
            numero = env
            if aux <= contas2[numero][1]:
               contas2[numero][1] +=aux
               numero = env
               contas2[numero][1]-=aux
            if not  strvalor1.isdigit():
                print(f'\t{code_error}{red}Informe Somente Numeros')
                sleep(2.0)
                clear()
            else:
              valor1 = int(strvalor1)
              c.transfere(destino=dest,valor= valor1,num = env)
              sleep(2.0)
              clear()
        elif  env not in contas2 or dest not in contas2:
           print(f'\t{code_error}{red}Numero da conta errado')
           sleep(2.0)
           clear()
         
        else:
           return False
      

#---------------------------------------------------------------------------------------------------

    #menu
                                                                                    
sprint(logop)

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

        elif op != 'clear':
         invalid = f'\t{code_error}{B}Opção Invalida!{C}'
         sprint(invalid)
         sleep(2.0)
         clear()
         
         
        
Loop()
