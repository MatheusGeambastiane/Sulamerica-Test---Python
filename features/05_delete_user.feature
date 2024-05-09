Feature: Deleção de usuário na API
  Como um cliente da API
  Eu quero fazer uma requisição de deleção
  Para remover um usuário cadastrado

  Scenario: Deletar um usuário cadastrado
    Given que existe um usuário cadastrado válido
    When o usuário enviar uma requisição de deleção
    Then o usuário deve ser removido com sucesso
