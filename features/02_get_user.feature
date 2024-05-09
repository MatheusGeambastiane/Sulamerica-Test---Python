
Feature: Obter dados do usuário na API
  Como um cliente da API
  Eu quero fazer uma requisição
  Para obter dados do meu usuário

  Scenario: Obter dados do usuário pelo atributo username
    Given que o haja um usuário cadastrado válido
    When eu fizer uma requisição ao endpoint passando seu username
    Then os dados deverão ser identicos aos cadastrados
    

