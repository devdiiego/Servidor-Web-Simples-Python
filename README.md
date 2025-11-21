🚀 Servidor Web Simples (HTTP 1.1) em Python

Este repositório contém a implementação de um servidor web básico em Python, desenvolvido para atividades da disciplina de Redes.
O objetivo principal é demonstrar o funcionamento do protocolo HTTP, utilizando sockets TCP para gerenciar a comunicação na camada de transporte.

✨ O que este servidor faz?

O servidor é capaz de:

Atender requisições HTTP GET

Gerenciar o fluxo de rede usando TCP

Enviar respostas formatadas corretamente

Servir arquivos estáticos como páginas HTML

Retornar erros adequados (ex: 404)

🧩 Funcionalidades Implementadas
🔌 Socket TCP

Uso de AF_INET (IPv4) e SOCK_STREAM (TCP)

Criação de um servidor de escuta confiável

🌐 Protocolo HTTP

Processamento de requisições GET

Geração de respostas com cabeçalhos HTTP válidos

Tratamento de exceções como arquivos inexistentes

🔢 Porta Não-Padrão

O servidor utiliza a porta 6789, evitando conflitos com portas padrão como 80
