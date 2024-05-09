import json
import os
import logging

def save_evidence(filename, data):
    evidences_directory = "evidences"
    if not os.path.exists(evidences_directory):
        os.makedirs(evidences_directory)

    path = os.path.join(evidences_directory, filename)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    logging.info(f"Evidence saved in JSON format: {path}")
