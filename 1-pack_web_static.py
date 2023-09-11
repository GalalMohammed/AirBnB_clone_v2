#!/usr/bin/python3
"""This module generates a .tgz archive from the contents of the web_static.

Example:
    $ fab -f 1-pack_web_static.py do_pack

"""


from datetime import datetime

from fabric.api import local


def do_pack() -> object:
    """Generate a .tgz archive from the contents of the web_static.

    Returns:
        archive path.

    """
    local("mkdir -p versions")
    archive_path = f"versions/web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
    result = local("tar -cvf " + archive_path + " web_static")
    if result.succeeded:
        return archive_path
    return None
