#!/usr/bin/python3
# This Fabric script generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    curr_dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(curr_dt.year,
                                                         curr_dt.month,
                                                         curr_dt.day,
                                                         curr_dt.hour,
                                                         curr_dt.minute,
                                                         curr_dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
