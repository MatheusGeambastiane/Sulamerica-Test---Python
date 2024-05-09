import logging

from services.data_generator import DataGenerator
from services.api_service import ApiService
from services.logging_config import setup_logging

api_service = ApiService()
log_file = setup_logging()


def before_all(context):
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting test suite")
    context.api_service = api_service

    user = DataGenerator.generate_user(valid=True)
    user_data = user.to_dict()
    context.user_data = user_data
    context.username = user_data['username']
    context.user_password = user_data['password']


def after_all(context):
    logging.info("Finished test suite")

def before_feature(context, feature):
    logging.info(f"Starting feature: {feature.name}")
  

def after_feature(context, feature):
    logging.info(f"Completed feature: {feature.name}")

def before_scenario(context, scenario):
    
    logging.info(f"Running a {scenario.name} scenario")


def after_scenario(context, scenario):
    logging.info(f"Scenario completed: {scenario.name}")

def before_step(context, step):
    logging.debug(f"About to execute step: {step.name}")

def after_step(context, step):
    if step.status == "failed":
        logging.error(f"Step failed: {step.name}")
