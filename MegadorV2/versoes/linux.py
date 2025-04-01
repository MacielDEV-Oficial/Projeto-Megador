from colorama import Style,Fore
import time
import os

class Megador:
    def __init__(self):

        self.iniciar_loop = True
    
    def Cor(texto,Id):
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
    
    def Instalar_dependencias(self):
        print(self.Cor("Verificando os arquivos...",1))

        
    def sistema_de_comandos(self):
        match self.comando:
            case 'start server':
                print(self.Cor("Iniciando Servidor na porta: 789", 1))
                               #os.system('nc -nvlp 789')
            case 'exit':
                print(self.Cor("Encerrando o sistema...\n",3))
                time.sleep(5)
                os.system("clear")
                self.iniciar_loop = False
                
    def criar_pyload(self):
        pass

    def carregar_logo_megador(self):
        os.system("clear")
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
        try:
            self.carregar_logo_megador()
            while self.iniciar_loop:
                self.comando = input(self.Cor("|MegadorV2> ",1))
                self.sistema_de_comandos()
        except:
            pass
    def Update(self):
        self.mainloop()

if __name__=="__main__":
    mg = Megador()
    mg.Update()