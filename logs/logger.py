import logging
import json
from datetime import datetime

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(message)s"
)

def log_prediction(data, prediction):
    log_data = {
        "timestamp": str(datetime.now()),
        "input": data,
        "prediction": prediction
    }
    logging.info(json.dumps(log_data))