from behave import given, when, then
import requests
from jsonschema import validate, ValidationError
import json
import logging


from services.load_schema import load_schema
from services.save_evidence import save_evidence



user_schema = load_schema('schemas/user_schema.json')

@given('que o haja um usuário cadastrado válido')
def step_impl(context):
    user_data = context.user_data

    try:
        validate(instance=user_data, schema=user_schema)
    
        logging.info(f"User validated successfully: {user_data}")
    except ValidationError as e:
        raise AssertionError(f"The generated data does not comply with the schema: {e.message}")




@when('eu fizer uma requisição ao endpoint passando seu username')
def step_impl(context):
    
    context.response = context.api_service.get_user(context.username)
    context.response_data = context.response.json()

    


@then('os dados deverão ser identicos aos cadastrados')
def step_impl(context):
    assert context.response.status_code == 200, "A resposta não foi 200 OK"
    try:
        validate(instance=context.response_data, schema=user_schema)
        logging.info(f"User data validated according to the created user : {context.response_data}")
        logging.info(f"User data saved")
        save_evidence("user_data.json", context.response_data)
        assert context.response_data == context.user_data, "Os dados recebidos não são idênticos aos cadastrados"
    except ValidationError as e:
        assert False, f"Validação do schema falhou: {e.message}"
    
