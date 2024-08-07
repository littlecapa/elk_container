import random
import time
import logging
from datetime import datetime
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

# Logstash endpoint
logstash_url = 'http://localhost:5000'

def generate_log(time=None):
    if time == None:
        execution_time = round(random.uniform(1.0, 2.0), 2)
    else:
        execution_time = time
    log_message = {
        'timestamp': datetime.now().isoformat(),
        'execution_time': execution_time
    }
    logger.info(f"Execution time: {execution_time} seconds")
    send_to_logstash(log_message)

def send_to_logstash(log_message):
    try:
        response = requests.post(logstash_url, json=log_message)
        if response.status_code != 200:
            logger.error(f"Failed to send log to Logstash: {response.text}")
    except Exception as e:
        logger.error(f"Error sending log to Logstash: {e}")

if __name__ == "__main__":
    for i in range(20):
        generate_log()
        time.sleep(100)
        i+=1
    generate_log(3.1)
