from behave import given, when, then
import logging
from services.load_schema import load_schema
from services.save_evidence import save_evidence

user_schema = load_schema('schemas/user_schema.json')

@given('que existe um usuário cadastrado válido para o delete')
def step_impl(context):
    context.username = context.user_data['username']
    context.response = context.api_service.get_user(context.username)
    context.response_data = context.response.json()
    assert context.response.status_code == 200, "User not found, or not valid."
    logging.info("User validated successfully with initial data to delete.")

@when('o usuário enviar uma requisição de deleção')
def step_impl(context):
    context.response = context.api_service.delete_user(context.username)
    logging.info(f"User delete request log: {context.response}")

@then('o usuário deve ser removido com sucesso')
def step_impl(context):
    assert context.response.status_code == 200, "Failed to delete user."
    response = context.api_service.get_user(context.username)
    assert response.status_code == 404, "User still exists after delete request."
    logging.info(f"User {context.username} successfully deleted.")
    save_evidence("delete_user_evidence.json", context.response.json())
    save_evidence("delete_user_get_evidence.json", response.json())
