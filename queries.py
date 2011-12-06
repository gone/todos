import pymongo
from brubeck.models import User

COLLECTION = 'todos'


def init_db_conn(**kwargs):
    dbc = pymongo.Connection(**kwargs)
    db_conn = dbc[COLLECTION]
    return db_conn


def apply_all_indexes(db, indexes, collection):
    """ Takes a list of indexes and applies them to a collection
    Intended for use after functions that create/update/delete entire documents
    """
    for index in indexes:
        db[collection].ensure_index(index)
    return True


def load_user(db, username=None, email=None):
    query_dict = {}
    if username:
        query_dict['username'] = str(username).lower()
    else:
        return ValueError('username required')

