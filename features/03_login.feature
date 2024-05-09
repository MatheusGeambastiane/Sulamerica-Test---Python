Feature: Login de usuário na API do Petstore
  Como um usuário da API
  Quero fazer login
  Para acessar minha conta

  Scenario: Usuário faz login com credenciais válidas
    Given que eu tenho um usuário registrado com email e senha válidos
    When eu faço login com essas credenciais
    Then o login deverá ser bem-sucedido
