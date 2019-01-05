# -*- coding: utf-8 -*-
"""
Docker settings file
"""

import os

# This file contains the default configuration values
# and configuration retrieval functions

import logging
import os

LOGGER = logging.getLogger("history." + __name__)
LOGGER.addHandler(logging.StreamHandler())
LOGGER.setLevel(logging.INFO)

# mongo related configuration
db_address = os.environ.get("HISTORY_DB_ADDRESS", "mongodb")
db_port = os.environ.get("HISTORY_DB_PORT", 27017)
db_host = "" + db_address + ":" + str(db_port)
db_replica_set = os.environ.get("HISTORY_DB_REPLICA_SET", None)
db_expiration = os.environ.get('HISTORY_DB_DATA_EXPIRATION', 604800)
db_shard = os.environ.get('MONGO_SHARD', False)

#
# Other dojot services
#
# device-manager URL
device_manager_url = os.environ.get('DEVICE_MANAGER_URL', "http://device-manager:5000")
