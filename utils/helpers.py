import logging
import yaml
import logging.config

def setup_logger(name):
    with open("config/logging_config.yaml", "r") as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    return logging.getLogger(name)

def save_to_file(data, filename):
    with open(filename, "w") as f:
        f.write(data)