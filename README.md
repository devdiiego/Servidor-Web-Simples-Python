🚀 Servidor Web Simples (HTTP 1.1) em Python
Este repositório contém os arquivos desenvolvidos para a atividade de Redes, cujo objetivo principal foi implementar um servidor Web básico em Python, utilizando a biblioteca socket para gerenciar a comunicação na Camada de Transporte (TCP) e o Protocolo de Aplicação (HTTP).

✨ O que este Servidor Faz
O servidor demonstra a capacidade de atender a requisições HTTP e gerenciar o fluxo de rede de forma eficiente.

🛠️ Funcionalidades Implementadas
Socket TCP: Utiliza AF_INET e SOCK_STREAM para criar um socket de escuta TCP.

Protocolo HTTP: Processa requisições GET e retorna respostas formatadas para o cliente.

Porta Não-Padrão: Executa na porta 6789, conforme exigido, evitando conflitos com a porta 80 padrão.

Respostas de Status:

200 OK: Retorno para o arquivo HelloWorld.html encontrado.

404 Not Found: Retorno para recursos inexistentes, tratado via except IOError.

Controle de Fluxo: Utiliza a lógica \r\n para delimitar cabeçalhos e o corpo da mensagem.

📶 Compatibilidade e Testes de Rede
O servidor foi projetado para ser robusto em diferentes ambientes de rede:

Vinculação Ampla: Está vinculado a todas as interfaces (0.0.0.0), garantindo acesso via localhost e IP de rede local (ex: 192.168.225.82).

Hospedeiros Diferentes: Foi comprovada a capacidade de acesso por outros dispositivos dentro da rede, confirmando a correta configuração do bind e superando bloqueios de Firewall com sucesso.
