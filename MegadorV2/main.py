import sys
import os
# Lista de bibliotecas necessárias

class INSTALARDOR_DO_SISTEMA:
    def __init__(self):
        self.LISTA_MENSAGEM = [
            "Erro: Algumas dependências necessárias não estão instaladas. Desaja instalar agora ? [S/N]: ",
            "Todas as dependências estão instaladas. O sistema está pronto para execução!"]
        self.LISTA_DE_BIBLIOTECAS_DEPENDENTE = [
        "os",
        "colorama",
        "time",
        "platform"]
        self.LISTA_DE_PIP_BIBLIOTECAS_DEPENDENTE = {
            'os':'install os',
            'colorama':'install colorama',
            'time':'install time',
            'platform':'install platform'
        }

    def VERIFICAR_BIBLIOTECAS_NECESSARIAS(self):
        dependencias = []
        for biblioteca in self.LISTA_DE_BIBLIOTECAS_DEPENDENTE:
            try:
                __import__(biblioteca)
            except ImportError:
                dependencias.append(biblioteca)
            
                if dependencias:
                    resposta = input(self.LISTA_MENSAGEM[0])
                    if resposta.lower() == 's':
                        match self.sistema_operacional:
                            case 'Windows':
                                for item in dependencias:
                                    os.system('pip ' + self.LISTA_DE_PIP_BIBLIOTECAS_DEPENDENTE[item])
                            case 'Linux':
                                for item in dependencias:
                                    os.system('pip3 ' + self.LISTA_DE_PIP_BIBLIOTECAS_DEPENDENTE[item])
                    else:
                        os.system("cls")
                        sys.exit()
                        
            
                else:
                    print(self.LISTA_MENSAGEM[1])
                    
    
    def VERIFICAR_TIPO_DE_SISTEMA_OPERACIAL(self):
        import os
        import platform
        self.sistema_operacional = platform.system()

    
    def INICIAR_VERSAO_CORRESPONDENTE(self):
        match self.sistema_operacional:
            case 'Windows':
                from versoes.windows import Megador
                windows = Megador()
                windows.Update()
            case 'Linux':
                from versoes.linux import Megador
                linux = Megador()
                linux.Update()
    
    def INICIAR_INSTALADOR(self):
        self.VERIFICAR_TIPO_DE_SISTEMA_OPERACIAL()
        self.VERIFICAR_BIBLIOTECAS_NECESSARIAS()
        self.INICIAR_VERSAO_CORRESPONDENTE()

instalador = INSTALARDOR_DO_SISTEMA()
instalador.INICIAR_INSTALADOR()