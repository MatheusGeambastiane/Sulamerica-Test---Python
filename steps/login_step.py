from behave import given, when, then
from jsonschema import validate, ValidationError

from services.save_evidence import save_evidence
from services.load_schema import load_schema

import logging


user_schema_response = load_schema('schemas/user_created_response.json')
user_schema = load_schema('schemas/user_schema.json')

@given('que eu tenho um usuário registrado com email e senha válidos')
def step_impl(context):
    user_data = context.user_data

    try:
        validate(instance=user_data, schema=user_schema)
    
        logging.info(f"User validated successfully: {user_data}")
    except ValidationError as e:
        raise AssertionError(f"The generated data does not comply with the schema: {e.message}")

    
    logging.info(f"User credentials set in context: {context.username}, {context.user_password}")

@when('eu faço login com essas credenciais')
def step_impl(context):
    response = context.api_service.login(context.username, context.user_password)
    context.login_response = response
    logging.info("Login attempted with provided credentials.")

@then('o login deverá ser bem-sucedido')
def step_impl(context):
    assert context.login_response.status_code == 200
    response_data = context.login_response.json()
    save_evidence("response_user_login.json", response_data)
    logging.info("Login successful and user is authenticated.")
