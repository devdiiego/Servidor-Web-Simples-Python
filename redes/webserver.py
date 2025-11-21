#http://127.0.0.1:6789/HelloWorld.html

#Inicialização

# Importa o módulo socket
from socket import *
import sys # Necessário para encerrar o programa

# Porta definida
serverPort = 6789 

# Cria o socket TCP - Conexão
serverSocket = socket(AF_INET, SOCK_STREAM)

# Configuração do Socket para escuta
serverSocket.bind(('', serverPort))
serverSocket.listen(1) 

#Fim do Primeiro bloco

while True:
    # Estabelece a conexão
    print('Ready to serve...')
    # Aguarda e aceita uma nova conexão
    connectionSocket, addr = serverSocket.accept()
    
    try: 
        # Recebe a mensagem do cliente (requisição HTTP)
        message = connectionSocket.recv(1024).decode()
        # Analisa a requisição para obter o nome do arquivo
        filename = message.split()[1] 
        
        # Abre o arquivo local
        f = open(filename[1:], encoding='utf-8') 
        outputdata = f.read()
        
        # Envia a linha de status HTTP 200 OK
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        # Envia o cabeçalho Content-Type
        connectionSocket.send("Content-Type: text/html; charset=utf-8\r\n".encode())
        connectionSocket.send("\r\n".encode()) 
        
        # Envia o conteúdo / mensagem http do arquivo
        connectionSocket.send(outputdata.encode('utf-8'))
        
        connectionSocket.send("\r\n".encode())
        
        # Fecha a conexão após o envio bem-sucedido
        connectionSocket.close()

    except IOError: 
        # Tratamento de erro: Envia a linha de status 404 Not Found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        # Envia o conteudo da mensagem de erro
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        
        # Fecha a conexão após o envio do erro
        connectionSocket.close()

serverSocket.close()
sys.exit()