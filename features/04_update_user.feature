Feature: Atualização de dados do usuário na API
  Como um cliente da API
  Eu quero fazer uma requisição de atualização
  Para alterar os dados do meu usuário

  Scenario: Atualizar o FirstName de um usuário cadastrado
    Given que existe um usuário cadastrado válido
    When o usuário enviar uma requisição de atualização do FirstName
    Then o FirstName do usuário deve ser atualizado com sucesso
    And o FirstName do usuário deverá ser diferente do anterior

    
