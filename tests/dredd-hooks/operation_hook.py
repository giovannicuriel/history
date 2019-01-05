import dredd_hooks as hooks
import json
from datetime import datetime

from dojot.history.models import HistoryUtil
import pymongo

@hooks.before_each
def create__device(transaction):

    _create_device = {
        'attr': "temperature",
        'value': "22.12",
        'device_id': "labtemp",
        'ts': datetime.utcnow()
    }
    db = HistoryUtil.get_db()
    db["admin_labtemp"].insert_one(_create_device)

    _update_data = {
        'attr': "temperature",
        'value': "23.12",
        'device_id': "labtemp",
        'ts': datetime.utcnow()
    }
    db["admin_labtemp"].insert_one(_update_data)

    _update_data = {
        'attr': "temperature",
        'value': "24.12",
        'device_id': "labtemp",
        'ts': datetime.utcnow()
    }
    db["admin_labtemp"].insert_one(_update_data)


