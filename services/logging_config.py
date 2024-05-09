import logging
import os
from datetime import datetime

def setup_logging():
    logs_directory = "logs"
    if not os.path.exists(logs_directory):
        os.makedirs(logs_directory)

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"{logs_directory}/test_log_{current_time}.log"

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(log_filename, 'w', 'utf-8'),
            
        ]
    )

    logging.info("Logging setup complete. Log file created at: {}".format(log_filename))
    return log_filename
