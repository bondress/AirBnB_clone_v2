#!/usr/bin/python3
# This Fabric script generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Create a tar gzipped archive of the directory web_static.
    """
    curr_dt= datetime.now()
    archive = 'web_static_' + curr_dt.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None

