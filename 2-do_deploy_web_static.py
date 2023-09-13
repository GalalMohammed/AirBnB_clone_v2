#!/usr/bin/python3
"""This module distributes an archive to your web servers."""


from pathlib import Path
from fabric.api import run, put, env
from fabric.context_managers import cd
from fabric.operations import sudo

env.hosts = ["54.208.56.50", "54.90.5.188"]


def do_deploy(archive_path: str) -> bool:
    """Distributes an archive to your web servers.

    Args:
        archive_path (str): path to archive.

    Returns:
        True if all operations have been done correctly,
        otherwise returns False.

    """
    path = Path(archive_path)
    if not path.exists():
        return False
    # Get the base filename of the atchive (without extension)
    archive_filename = path.name
    archive_basename = path.stem

    # Upload the archive to the /tmp/ directory of the web server
    result = put(archive_path, "/tmp/" + archive_filename)

    if result.succeeded:
        # Create the target directory for the release
        result = sudo("mkdir -p /data/web_static/releases/" + archive_basename)

    if result.succeeded:
        # Uncopmress the archive into the target directory
        with cd("/data/web_static/releases/" + archive_basename):
            result = sudo("tar -xzf /tmp/" + archive_filename)

    if result.succeeded:
        # Remove the uploaded archive
        result = sudo("rm /tmp/" + archive_filename)

    if result.succeeded:
        # Move the contents to the current directory
        result = sudo("mv /data/web_static/releases/" + archive_basename +
                      "/web_static/* /data/web_static/releases/" +
                      archive_basename)

    if result.succeeded:
        # Remove the empty web_static directory
        result = sudo("rm -rf /data/web_static/releases/" + archive_basename +
                      "/web_static")

    if result.succeeded:
        # Update the symbolic link tests
        sudo("rm -rf /data/web_static/current")
        result = sudo("ln -s /data/web_static/releases/" + archive_basename +
                      " /data/web_static/current")
    return result.succeeded
