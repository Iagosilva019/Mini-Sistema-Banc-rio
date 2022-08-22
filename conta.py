
class Conta:
    def __init__(self, numero, saldo):
        self.numero         = numero
        self.saldo          = saldo
        contas[self.numero] = [cliente,self.saldo]



    def sacar(self, valor, numeroc):
        if valor<= contas[self.numero][1]and numeroc in contas:
            self.numero = numeroc
            contas[self.numero][1]-=valor
            print(f'\t{bgreen}Saque realizado com sucesso!')
            return True
        elif contas[self.numero][1] == 0:
            print(f'\t{code_error}{red}Saldo Insuficiente!')
        else:
            print(f'\t{code_error}{red}Saldo Insuficiente!')




    def depositar(self, valor,numeroc):
        if numeroc in contas:
            self.numero = numeroc
            contas[self.numero][1]+=valor
            return True
        else:
            print(f'\t{code_error}{red}Numero da conta errado')
            return False




    def extrato(self):
        for key,value in contas.items():
            #print(f'\t\t{red}[EXTRATO]{C}')
            print(f'\t\t{bcyan}TITULAR DA CONTA:{white}{value[0][0]}',f'\n\t\t{bcyan}CPF:{white}{value[0][1]}',f'\n\t\t{bcyan}NUMERO DA CONTA:{white}{key}',f'\n\t\t{bcyan}SALDO:{white}{value[1]:.2f}')
            print('\n')
          



    def transfere(self,destino,valor,num):
        self.numero = num
        if valor<= contas[self.numero][1]:
            self.numero =destino
            contas[self.numero][1] +=valor
            self.numero =num
            contas[self.numero][1] -= valor
            print(f'\t{bgreen}Valor transferido com sucesso!{C}')
            return True
        else:
            print(f'\t{code_error}{red}Saldo Insuficiente!')
            return False     
             
             
             
    def excluir(self, remov):
        if remov in contas and contas[self.numero][1] == 0:
           contas.pop(remov)
           print(f'\t{bgreen}Conta removida com sucesso!')
           return True
        else:
           print(f'\t{code_error}{red}Numero da conta errado ou Você ainda possui saldo')
           return False
               
    
    
    
    def cliente(self,titular,cpf):
        cliente = [titular, cpf]
        contas[self.numero] = [cliente,self.saldo]
        
        
        
        
#---------------------------------------------------------------------------------------------------
cliente = []
contas= {}
print('Bem Vindo :)')




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
