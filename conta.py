


class Conta:

    def __init__(self, titular,  numero, saldo):

        self.titular        = titular
        self.numero         = numero
        self.saldo          = saldo
        contas[self.numero] = [self.titular,self.saldo]

    def sacar(self, valor, numeroc):
        if valor<= contas[self.numero][1]and numeroc in contas:
            self.numero = numeroc
            contas[self.numero][1]-=valor
            msg = 'Saque realizado com sucesso!'
            return True, msg
        else:
            return False, 'Saldo Insuficiente!'

    def depositar(self, valor,numeroc):
        if numeroc in contas:
            self.numero = numeroc
            contas[self.numero][1]+=valor
        return True

    def extrato(self):
        for key,value in contas.items():
            print('\t\tTitular da Conta:',value[0],'\n\t\tNumero da Conta:',key,f'\n\t\tSaldo:{value[1]:.2f}')
            print('\n')

    def transfere(self,destino,valor,num):
             self.numero =destino
             contas[self.numero][1] +=valor
             self.numero =num
             contas[self.numero][1] -= valor


contas= {}
print('classe executando...')
