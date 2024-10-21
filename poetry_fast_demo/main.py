import os
import logging.config

import yaml

log_conf_path = os.environ.get("LOG_CONFIG")
with open(log_conf_path, 'r', encoding="utf-8") as f:
    dict_conf = yaml.safe_load(f)
logging.config.dictConfig(dict_conf)

from module1.calc import do_something

do_something()
