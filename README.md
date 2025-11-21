🌐 Servidor Web Simples (HTTP 1.1) em Python (HTTP 1.1) em Python

Este repositório contém os arquivos desenvolvidos para a atividade da disciplina de Redes, cujo objetivo foi implementar um servidor Web simples utilizando Python e sockets.

O foco da atividade foi compreender o funcionamento básico do protocolo HTTP 1.1, incluindo:

Processamento de requisições GET;

Retorno do status 200 OK para arquivos existentes;

Retorno do status 404 Not Found para recursos inexistentes;

Tratamento de exceções com try...except;

Envio adequado de cabeçalhos HTTP, incluindo charset=utf-8;

Execução do servidor em porta não-padrão (6789) para evitar conflitos;

Testes de acesso tanto pelo localhost quanto pelo IP da rede local.

Além disso, foram realizadas validações exigidas na atividade, comprovando:

Funcionamento do servidor na porta configurada;

Retorno correto do código 200 OK ao acessar o arquivo disponível;

Funcionamento do tratamento de erro 404 Not Found;

Capacidade de acesso por outros hospedeiros dentro da rede local.

Este README resume as entregas realizadas na atividade. Os detalhes completos do código, estrutura e relatório técnico estão disponíveis na branch principal do repositório (main).
