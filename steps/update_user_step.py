from behave import given, when, then
import requests
from jsonschema import validate, ValidationError
import json
import logging

from faker import Faker

from services.load_schema import load_schema
from services.save_evidence import save_evidence




fake = Faker()
user_schema = load_schema('schemas/user_schema.json')

@given('que existe um usuário cadastrado válido')
def step_impl(context):
    context.response = context.api_service.get_user(context.username)
    context.response_data = context.response.json()
    assert context.response.status_code == 200
    
  
    
    logging.info("User validated successfully with initial data.")

@when('o usuário enviar uma requisição de atualização do FirstName')
def step_impl(context):
    context.new_first_name = fake.first_name()
    new_first_name = context.new_first_name
    updated_data = {'firstName': context.new_first_name}
    context.user_data.update(updated_data)
    response = context.api_service.update_user(context.user_data['username'], context.user_data)


    context.response = response
    context.response_data = response.json()
    
@then(f'o FirstName do usuário deve ser atualizado com sucesso')
def step_impl(context):

    assert context.response.status_code == 200, "Failed to update user."


@then(f'o FirstName do usuário deverá ser diferente do anterior')
def step_impl(context):

    
    user_verify = context.api_service.get_user(context.username)
    context.response_data = user_verify.json()
    

    assert context.response_data['firstName'] == context.new_first_name, f"FirstName was not updated as expected. Expected: {context.new_first_name}, Got: {context.response_data['firstName']}"
    logging.info(f"FirstName updated successfully to: {context.new_first_name}. New user data {context.user_data}")
    save_evidence("updated_user_data.json", context.response_data)
