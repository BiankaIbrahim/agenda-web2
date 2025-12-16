## Tecnologias Utilizadas

*  HTML \+ CSS — para a interface web  
*  Python — para a lógica de backend com Django  
* Uso da estrutura MVC (Model, View, Template)  
* SQLite para salvar os dados

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
