# 📒 Agenda de Contatos – Django

## 📌 Sobre o Projeto

Este projeto consiste em uma **aplicação web de Agenda de Contatos**, desenvolvida com o framework **Django**, com o objetivo de permitir o gerenciamento seguro de informações pessoais, como criação, visualização, edição e exclusão de contatos.

A aplicação foi estruturada seguindo o padrão **MVC (Model, View, Template)**, garantindo melhor organização do código, facilidade de manutenção e maior escalabilidade do sistema.

## 🔐 Segurança da Aplicação

A segurança é um dos pontos centrais do projeto. O sistema conta com **autenticação de usuários**, garantindo que cada usuário tenha acesso apenas aos seus próprios contatos. O gerenciamento de sessões é realizado utilizando os mecanismos nativos do Django, que oferecem proteção contra acessos não autorizados.

Entre as principais medidas de segurança adotadas, destacam-se:

- Autenticação e controle de sessão de usuários;
- Proteção contra ataques CSRF (Cross-Site Request Forgery);
- Validação de dados no backend;
- Separação adequada entre as camadas da aplicação;
- Restrição de acesso a rotas sensíveis.

## 🗂️ Armazenamento de Dados

Os dados da aplicação são armazenados em um banco de dados **SQLite**, adequado para fins educacionais e ambientes de desenvolvimento, garantindo persistência e integridade das informações.

## 🎯 Objetivo do Projeto

O principal objetivo deste projeto é consolidar conhecimentos em **desenvolvimento web com Django**, **arquitetura de software** e **boas práticas de segurança em aplicações web**.


## Tecnologias Utilizadas

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)

![MVC](https://img.shields.io/badge/MVC-Architecture-blue)

![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)



## Funcionalidades Principais

### CRUD de Usuário

✔️ Cadastrar no sistema  
✔️ Realizar login  
✔️ Visualizar  
✔️ Editar Perfil  
✔️ Deslogar da conta

##  Autenticação

obs: sessão, feita no próprio app, não usando Django Auth padrão.

✔️ Cadastro de usuários com senha criptografada  
✔️ Login com verificação de hash  
✔️ Sessão para manter usuário autenticado  
✔️ Logout  
✔️ Proteção de rotas com decorator personalizado

### CRUD de Contatos

Para um usuário autenticado, é possível:  
✔️ Listar contatos  
✔️ Criar novo contato  
✔️ Editar um contato  
✔️ Deletar um contato  

## Diagrama 
```mermaid
flowchart TD
    U["Usuário no Navegador"]

    U -->|"HTTP Requests"| D["Django URL Dispatcher"]

    D --> V1["Views - Contatos"]
    D --> V2["Views - Usuário"]

    %% Views de Contatos
    V1 --> CRUD["CRUD"]
    V1 --> CACHE["Cache"]
    CRUD --> M1["Model Contato"]

    %% Views de Usuário
    V2 --> AUTH["Autenticação"]
    V2 --> SESSION["Sessão"]
    AUTH --> M2["Model Usuário"]

    %% Banco de Dados
    M1 --> DB[("Banco de Dados")]
    M2 --> DB

