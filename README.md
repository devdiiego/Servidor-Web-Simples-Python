🚀 Servidor Web Simples (HTTP 1.1) em Python
Este repositório contém os arquivos desenvolvidos para a atividade da disciplina de Redes. O objetivo principal foi implementar um servidor Web básico em Python, utilizando a biblioteca socket para gerenciar a comunicação na Camada de Transporte (TCP) e o Protocolo de Aplicação (HTTP).

✨ O que este Servidor Faz
O servidor demonstra a capacidade de:

Processar Requisições HTTP: Recebe e analisa requisições do tipo GET.

Gerenciamento de Socket: Cria, vincula e escuta em um socket TCP na porta 6789 (uma porta não-padrão).

Respostas de Status: Retorna o status 200 OK para o arquivo HelloWorld.html encontrado e 404 Not Found para recursos inexistentes.

Controle de Fluxo: Utiliza try...except IOError para tratar erros de arquivo e inclui a lógica \r\n para separar cabeçalhos e o corpo da mensagem.

Compatibilidade de Rede: Vincula-se a todas as interfaces (0.0.0.0), permitindo o acesso via localhost e IP de rede local.
