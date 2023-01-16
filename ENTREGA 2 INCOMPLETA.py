class Consultor():
    def __init__(self,ID,user,password):
        self.ID=ID
        self.__user=user
        self.__password=password
        #Consultores.append([ID,user,password])
        #print(Consultores)
        #print('Criando Objeto...')  

    @property
    def ver_dados(self):
        return {self.ID:{'user':self.__user,'senha':self.__password}}

    #Nao usei propriedades do setter porque precisaria de um getter de cada um
    #e como já havia um getter para todos os dados achei melhor ficar assim.
    def set_user(self,new_user):
        self.__user=new_user

    def set_password(self,new_password):
        self.__password=new_password
        
class Gerente(Consultor):
    def teste(self):
        pass
class Projeto():
    def __init__(self,nome,gerente,consultores=[],etapa='Desenvolvimento %d'%1):
        pass

class Sistema():
    def __init__(self):
        pass
    def criar_projeto(self):
        nome=input('Digite o Nome do Projeto: ')
        gerente=int(input('Digite o ID do Gerente: '))
        projeto=Projeto(nome,gerente)
        return projeto
    def rem_projeto(self):
        pass

    def criar_consultor(self):
        ID=verificarID()
        user=input('Digite um usuario valido: ')
        password=input('Digite uma senha: ')
        return Consultor(ID,user,password)
    def rem_consultor(self):
        pass

    def criar_gerente(self):
        ID=verificarID()
        user=input('Digite um usuario valido: ')
        password=input('Digite uma senha: ')
        return Gerente(ID,user,password)

    def rem_gerente(self):
        pass

    def listarGCP(self):
        pass

    def login(self):
        pass

def verificarID():
    x=1
    while x==1:
        Id=int(input('Digite um ID valido: '))
        if Id in Gerentes or Id in Consultores:
            print('O ID Já está sendo utilizado...')
        else:
            x=2
            return Id
def verificarUser():
    pass

def imprimirMenu():
#-----------------------------------
#FUNCAO QUE INTERAGE COM O USUARIO E
#RETORNA A OPCAO ESCOLHIDA
#-----------------------------------
    print('Opcoes:')
    print('1 - Criar Projeto.')
    print('2 - Remover Projeto.')
    print('3 - Criar Consultor.')
    print('4 - Remover Consultor.')
    print('5 - Criar Gerente.')
    print('6 - Remover Gerente.')
    print('7 - Listagem de Gerentes Consultores e Projetos.')
    print('8 - Fazer Login.')
    print('0 - Sair.')
    
    op = input('Digite uma das opcoes acima: ')
    return op
def menuConsultor():
    print('Opcoes de Consultor:')
    print('1 - Ver seus dados.')
    print('2 - Modificar seus dados.')
    print('3 - Verificar seus projetos.')
    print('4 - Avançar com um projeto.')
    print('5 - Pedir retirada do projeto.')

    op = input('Digite uma das opcoes acima: ')
    return op
def menuGerente():
    print('Opcoes de Gerente:')
    print('1 - Ver seus dados.')
    print('2 - Modificar seus dados.')
    print('3 - Verificar seus projetos.')
    print('4 - Avançar com um projeto.')
    print('5 - Aval de Retirada de Consultor.')
    print('6 - Transferir projeto.')
    print('7 - Entregar Projeto.')

    op = input('Digite uma das opcoes acima: ')
    return op
def main():
    
    NC=0
    NG=0
    NP=0
    while True:
        op=imprimirMenu()
        if op=='1':
            Projetos[NP]=sistem.criar_projeto()
            NP+=1
            print('Projeto Criado com sucesso!')
            print(Projetos)
        elif op=='2':
            print('Funcao nao definida')
            continue
        elif op=='3':
            Consultores[NC]=sistem.criar_consultor()
            NC+=1
            print('Consultor Criado com sucesso!')
            print(Consultores[NC-1].ver_dados)
        elif op=='4':
            print('Funcao nao definida')
            continue
        elif op=='5':
            Gerentes[NG]=sistem.criar_gerente()
            NG+=1
            print('Gerente Criado com Sucesso!')
            print(Gerentes)
        elif op=='6':
            print('Funcao nao definida')
            continue
        elif op=='7':
            print('Funcao nao definida')
            continue
        elif op=='8':
            login='Gerente'
            if login=='Consultor':
                menuConsultor()
            elif login=='Gerente':
                menuGerente()
                
            print('Funcao nao definida')
            continue
        elif op=='0':
            print('Programa Encerrado')
            break
        else:
            print('Opção Invalida')
            continue
Projetos=[[]*20]
Consultores=[[]*20]
Gerentes=[[]*20]
sistem=Sistema()
main()
        
        
