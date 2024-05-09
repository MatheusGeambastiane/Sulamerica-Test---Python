import json

def load_schema(file_path):
    """Carrega um arquivo JSON e retorna como um dicionário."""
    with open(file_path, 'r') as file:
        schema = json.load(file)
    return schema
