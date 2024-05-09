from behave import given, when, then
import logging
from jsonschema import validate, ValidationError


from services.load_schema import load_schema
from services.save_evidence import save_evidence
from services.logging_config import setup_logging

log_file = setup_logging()

user_schema_response = load_schema('schemas/user_created_response.json')
user_schema = load_schema('schemas/user_schema.json')


@given('que tenho um novo usuário com nome, username e email válidos')
def step_impl(context):
    user_data = context.user_data

    
    try:
        validate(instance=user_data, schema=user_schema)
        
        logging.info(f"User generated successfully: {user_data}")
    except ValidationError as e:
        raise AssertionError(f"The generated data does not comply with the schema: {e.message}")
    

@when('eu envio a solicitação de criação de usuário')
def step_impl(context):
    context.response = context.api_service.create_user(context.user_data)

@then('a resposta deverá ser 200 OK')
def step_impl(context):
    assert context.response.status_code == 200
    response_data = context.response.json()
    save_evidence("response_user_creation.json", response_data)
    



@then('o schema da resposta deverá ser validado corretamente')
def step_impl(context):
    try:
        validate(instance=context.response.json(), schema=user_schema_response)
        logging.info("Response validation successful and saved as JSON evidence.")
    except ValidationError as ve:
        assert False, f"Schema validation failed: {ve}"