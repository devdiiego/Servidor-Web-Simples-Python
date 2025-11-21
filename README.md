# 🌐 Servidor Web Simples (HTTP 1.1) em Python

Este repositório contém a implementação de um servidor web básico em Python, desenvolvido para atividades da disciplina de Redes.
O objetivo principal é demonstrar o funcionamento do protocolo HTTP, utilizando sockets TCP para gerenciar a comunicação na camada de transporte.

## ✨ O que este servidor faz?

O servidor é capaz de:

- **Atender requisições HTTP GET**

- **Gerenciar o fluxo de rede usando TCP**

- **Enviar respostas formatadas corretamente**

- **Servir arquivos estáticos como páginas HTML**

- **Retornar erros adequados (ex: 404)**

## 🧩 Funcionalidades Implementadas
## 🔌 Socket TCP

- **Uso de AF_INET (IPv4) e SOCK_STREAM (TCP)**

- **Criação de um servidor de escuta confiável**

## 🌐 Protocolo HTTP

**Processamento de requisições GET**

- **Geração de respostas com cabeçalhos HTTP válidos**

- **Tratamento de exceções como arquivos inexistentes**
  
## 🔢 Porta Não-Padrão

- **O servidor utiliza a porta 6789, evitando conflitos com portas padrão como 80**

## 📡 Análise de Protocolo e Documentação
Além da implementação do servidor, a atividade incluiu uma análise de protocolo utilizando o Wireshark para validar o comportamento do HTTP em cenários reais.

- Ferramenta Utilizada: Wireshark.

- Foco da Análise: Estudo detalhado da interação GET/Resposta, a versão do protocolo, o uso de cabeçalhos condicionais (If-Modified-Since), e a diferença entre as respostas 200 OK e 304 Not Modified.

## 🏁 Conclusão
Este projeto demonstra o domínio dos fundamentos de redes ao implementar um servidor TCP/HTTP funcional em Python.

O sucesso na gestão do protocolo HTTP (200 OK, 404 Not Found) e na vinculação do socket à porta 6789 prova a compreensão da arquitetura cliente-servidor. A superação dos desafios de Firewall e a validação em diferentes ambientes de rede confirmam a robustez da solução e a capacidade de análise de protocolo.

O repositório serve como prova de conceito para a comunicação de rede em nível de aplicação.
