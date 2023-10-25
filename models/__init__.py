#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv

<<<<<<< HEAD

storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
=======
storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

>>>>>>> 7caf28ff500a1e9b848553ea807079ad29041485
storage.reload()
