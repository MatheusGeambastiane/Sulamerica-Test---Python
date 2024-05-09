Feature: Criação de usuário na API do Petstore
  Como um cliente da API
  Eu quero criar um usuário
  Para gerenciar suas informações no sistema

  Scenario: Criar um novo usuário com dados válidos
    Given que tenho um novo usuário com nome, username e email válidos
    When eu envio a solicitação de criação de usuário
    Then a resposta deverá ser 200 OK
    And o schema da resposta deverá ser validado corretamente

